#!/usr/bin/env python3
"""
Job Description Fit Analyzer
Analyzes how well your background matches a job description using Claude API.
"""

import anthropic
import os
import sys
import json
from pathlib import Path

# Your experience summary (condensed from resume)
# TODO: Replace this with your own background
CANDIDATE_PROFILE = """
YOUR_NAME - YOUR_TITLE

CORE STRENGTHS:
- [Years] of experience in [your field]
- [Key achievement with metrics]
- [Quota/performance metrics]
- [Deal sizes, sales cycles, or relevant metrics]
- [Territory/account building experience]
- [Key skill or approach]
- [Awards or recognition]

EXPERIENCE HIGHLIGHTS:
- Company 1 ([tenure]): [Key outcomes and responsibilities]
  - [Specific achievement]
  - [Specific achievement]

- Company 2 ([tenure]): [Key outcomes]
- Company 3 ([tenure]): [Key outcomes]

TECHNICAL SKILLS:
- [Relevant technical skills]
- [Tools and platforms]
- [Cross-functional experience]

BUYER PERSONAS:
- [Executive level buyers you've sold to]
- [Functional leaders]
- [Technical buyers]

VERTICALS:
- [Industries you have experience in]

IDEAL ROLES:
- [Target role 1]
- [Target role 2]
- [Target role 3]
- [Key requirements you're looking for]

NOT A FIT FOR:
- [Role type to avoid]
- [Motion that doesn't match your style]
- [Other exclusions]
"""

ANALYSIS_PROMPT = """You are a senior GTM recruiter evaluating candidate fit for enterprise SaaS sales roles.

Analyze this job description against the candidate's background and provide:

1. **FIT SCORE** (0-100%): Overall match quality
   - 90-100%: Exceptional fit, apply immediately
   - 75-89%: Strong fit, high priority
   - 60-74%: Good fit, worth applying
   - 40-59%: Moderate fit, apply if passionate about company
   - Below 40%: Poor fit, likely waste of time

2. **STRENGTHS** (3-5 bullet points): What makes this candidate compelling for THIS specific role

3. **GAPS** (2-4 bullet points): What's missing or might raise concerns

4. **POSITIONING STRATEGY**: 
   - How to frame experience in application/interview
   - What to emphasize from background
   - How to address gaps proactively
   - Red flags to watch for in company/role

5. **RECRUITER OBJECTIONS**: Anticipate 2-3 specific objections a recruiter might raise and provide rebuttals

6. **APPLICATION PRIORITY**: Should candidate apply? (YES / MAYBE / NO) with reasoning

Be direct and pragmatic. Focus on what hiring managers actually care about for enterprise SaaS roles.

CANDIDATE BACKGROUND:
{candidate_profile}

JOB DESCRIPTION:
{job_description}
"""


def analyze_job_fit(job_description: str, api_key: str = None) -> dict:
    """
    Analyze job description fit using Claude API.
    
    Args:
        job_description: Full text of the job posting
        api_key: Anthropic API key (or set ANTHROPIC_API_KEY env var)
    
    Returns:
        Dictionary with analysis results
    """
    if not api_key:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
    
    if not api_key:
        raise ValueError("API key required. Set ANTHROPIC_API_KEY env var or pass api_key parameter")
    
    client = anthropic.Anthropic(api_key=api_key)
    
    # Call Claude API
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": ANALYSIS_PROMPT.format(
                    candidate_profile=CANDIDATE_PROFILE,
                    job_description=job_description
                )
            }
        ]
    )
    
    # Extract response
    analysis_text = message.content[0].text
    
    return {
        "analysis": analysis_text,
        "model": message.model,
        "usage": {
            "input_tokens": message.usage.input_tokens,
            "output_tokens": message.usage.output_tokens
        }
    }


def main():
    """CLI interface for job description analysis."""
    
    if len(sys.argv) < 2:
        print("Usage: python analyze_jd.py <job_description_file.txt>")
        print("\nOr pipe job description:")
        print("  cat job.txt | python analyze_jd.py")
        print("\nSet ANTHROPIC_API_KEY environment variable before running")
        sys.exit(1)
    
    # Read job description from file or stdin
    if sys.argv[1] == "-":
        job_description = sys.stdin.read()
    else:
        jd_file = Path(sys.argv[1])
        if not jd_file.exists():
            print(f"Error: File not found: {jd_file}")
            sys.exit(1)
        job_description = jd_file.read_text()
    
    print("=" * 80)
    print("JOB DESCRIPTION FIT ANALYZER")
    print("=" * 80)
    print()
    
    # Analyze
    try:
        result = analyze_job_fit(job_description)
        print(result["analysis"])
        print()
        print("-" * 80)
        print(f"Model: {result['model']}")
        print(f"Tokens: {result['usage']['input_tokens']} in, {result['usage']['output_tokens']} out")
        print("-" * 80)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
