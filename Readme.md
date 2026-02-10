# Job Description Fit Analyzer

**AI-powered tool to analyze job posting alignment with your background and generate positioning strategies.**

Built for job search optimization using Claude API.

## What It Does

Takes any job description and provides:
- **Fit Score** (0-100%): How well your background matches
- **Strengths**: What makes you compelling for this specific role
- **Gaps**: What's missing or might raise concerns
- **Positioning Strategy**: How to frame your experience in applications/interviews
- **Recruiter Objections**: Anticipated concerns and how to address them
- **Application Priority**: Should you apply? (YES/MAYBE/NO)

## Why This Tool

Enterprise AE job searching requires:
1. **Speed**: Evaluate dozens of postings quickly
2. **Strategy**: Understand positioning before applying
3. **Objectivity**: See gaps recruiters will see before they reject you

This tool was built during an active job search to:
- Filter out low-fit roles faster (saved ~10 hours/week)
- Craft better application materials (increased response rate from 8% → 23%)
- Prepare for objections before interviews started

## Installation

```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/jdanalyzer.git
cd jdanalyzer

# Install dependencies
pip install -r requirements.txt

# Set API key
export ANTHROPIC_API_KEY="your-api-key-here"
```

## Usage

### Basic Usage
```bash
python analyze_jd.py examples/anthropic_founding_ae.txt
```

### From Clipboard (macOS)
```bash
pbpaste | python analyze_jd.py -
```

### Save Output
```bash
python analyze_jd.py job_posting.txt > analysis.txt
```

## Example Output

**Input**: Anthropic Founding AE job posting (AI sales, technical buyers, $100K+ deals)

**Output**:
```
FIT SCORE: 87% - Strong fit, high priority

STRENGTHS:
• Enterprise deal execution matches perfectly: $1M+ contracts, 3-6 month cycles, proven at $1B+ accounts
• Technical selling experience: Sold data platforms and APIs to technical buyers (Product, Engineering, IT)
• Territory building from zero: $0→$750K ARR aligns with founding AE motion
• AI credibility: Building automation tools with Claude API demonstrates product knowledge beyond typical AE
• Winner's Circle 4x shows consistent performance in complex selling environments

GAPS:
• No direct "AI platform" selling experience (Gartner was data/research, not AI infrastructure)
• Chainalysis/Braintrust short tenures might raise "can he stick at early-stage?" concerns
• Limited startup experience outside 2 brief stints (Gartner was large enterprise)

POSITIONING STRATEGY:
Frame Gartner as "selling complex, non-obvious value to technical buyers" not "research sales"
Lead with AI tool building (shows you understand Anthropic's product viscerally)
Address startup tenure proactively: "Learned what I wanted, went back to Gartner to rebuild foundation, now ready for right founding role"
Emphasize cross-functional work with Product/Marketing (shows GTM thinking beyond quota)

RECRUITER OBJECTIONS:
1. "Gartner isn't SaaS" → "Sold $100K+ annual software subscriptions with data platforms embedded. Multi-year contracts, land-and-expand motion, 95% retention."
2. "No AI selling experience" → "Currently building with Claude API—understand LLM adoption challenges firsthand. Plus technical selling to Eng/Product leaders translates directly."
3. "Won't stick at startup" → "Left previous startups because I was learning category, not building long-term. Different now—looking for founding AE role specifically to define playbook, not execute someone else's."

APPLICATION PRIORITY: YES - Apply immediately
This role values territory building, technical selling, and GTM strategy input. Your background is differentiated enough (AI tools + enterprise chops) to stand out.
```

## How It Works

1. **Candidate Profile**: Pre-loaded with my resume highlights (edit `CANDIDATE_PROFILE` in `analyze_jd.py` for your background)
2. **AI Analysis**: Uses Claude Sonnet 4 to evaluate fit from recruiter/hiring manager perspective
3. **Strategic Output**: Generates actionable positioning, not generic feedback

## Customization

Edit `CANDIDATE_PROFILE` constant in `analyze_jd.py` to match your background:
- Replace experience highlights
- Update ideal role criteria
- Modify buyer personas and verticals

## Real-World Results

Used this tool for 40+ job applications:
- **Saved 10+ hours/week** by filtering low-fit roles before deep research
- **Increased response rate** from 8% → 23% by applying strategically to high-fit roles only
- **Better interview prep**: Objection handling section helped preempt concerns in 12+ interviews

## Tech Stack

- **Python 3.8+**
- **Anthropic Claude API** (Sonnet 4)
- **Dependencies**: `anthropic` library only

## Examples Included

- `examples/anthropic_founding_ae.txt` - AI sales role at Anthropic
- `examples/liveRamp_account_director.txt` - Data platform role
- `examples/stripe_enterprise_ae.txt` - Fintech role (poor fit example)

## Cost

~$0.02 per analysis (1500 input tokens, 1000 output tokens at Claude Sonnet 4 pricing)

Analyzing 50 job postings = ~$1.00

## Roadmap

- [ ] Add batch processing for multiple JDs
- [ ] Export to JSON for tracking
- [ ] Compare multiple JDs side-by-side
- [ ] Integration with job board scraping
- [ ] Fine-tune scoring based on actual application outcomes

## License

MIT License - Use freely, attribution appreciated

## Contributing

Issues and pull requests welcome on GitHub.
