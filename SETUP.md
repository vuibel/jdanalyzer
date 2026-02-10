# Setup Guide

## Prerequisites

- Python 3.8 or higher
- Anthropic API key ([get one here](https://console.anthropic.com/))
- Basic command line familiarity

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/jdanalyzer.git
cd jdanalyzer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Or with virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up API Key

**Option A: Environment Variable (Recommended)**
```bash
export ANTHROPIC_API_KEY="sk-ant-api03-..."
```

Add to your `~/.bashrc` or `~/.zshrc` to make permanent:
```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-..."' >> ~/.zshrc
source ~/.zshrc
```

**Option B: Pass as Argument**
```bash
python analyze_jd.py examples/anthropic_founding_ae.txt --api-key "sk-ant-api03-..."
```

### 4. Test the Installation

Run the example:
```bash
python analyze_jd.py examples/anthropic_founding_ae.txt
```

Expected output: Detailed fit analysis with score, strengths, gaps, positioning strategy

## Customization

### Update Your Profile

Edit the `CANDIDATE_PROFILE` constant in `analyze_jd.py` (lines 15-70):

```python
CANDIDATE_PROFILE = """
YOUR NAME - YOUR TITLE

CORE STRENGTHS:
- Your key accomplishments
- Quota attainment %
- Deal sizes and cycles
- etc.

EXPERIENCE HIGHLIGHTS:
- Company 1: Key outcomes
- Company 2: Key outcomes

... (see current format for template)
"""
```

### Modify Analysis Prompt

Edit `ANALYSIS_PROMPT` in `analyze_jd.py` (lines 72-110) to:
- Change scoring criteria
- Adjust output format
- Add/remove analysis sections
- Modify focus areas

## Usage Examples

### Analyze a Job Posting
```bash
python analyze_jd.py path/to/job_description.txt
```

### From Clipboard (macOS)
```bash
pbpaste | python analyze_jd.py -
```

### From Clipboard (Linux)
```bash
xclip -o | python analyze_jd.py -
```

### Save Output
```bash
python analyze_jd.py job.txt > analysis_output.md
```

### Batch Processing
```bash
for file in jobs/*.txt; do
    echo "Analyzing: $file"
    python analyze_jd.py "$file" > "results/$(basename $file .txt)_analysis.md"
done
```

## Troubleshooting

### "API key required" Error
Make sure your API key is set:
```bash
echo $ANTHROPIC_API_KEY  # Should print your key
```

### "Module not found: anthropic"
Install dependencies:
```bash
pip install -r requirements.txt
```

### Rate Limiting
If you hit rate limits, add a delay between analyses:
```bash
for file in jobs/*.txt; do
    python analyze_jd.py "$file"
    sleep 2  # Wait 2 seconds between calls
done
```

## Cost Estimation

Each analysis uses approximately:
- **Input tokens**: ~1,500 (your profile + job description)
- **Output tokens**: ~1,000 (analysis)
- **Cost**: ~$0.02 per analysis (at Claude Sonnet 4 pricing)

**Monthly budget examples:**
- 25 analyses = ~$0.50
- 50 analyses = ~$1.00
- 100 analyses = ~$2.00

## Next Steps

1. Customize `CANDIDATE_PROFILE` with your background
2. Analyze a few real job postings you're considering
3. Compare fit scores to prioritize applications
4. Use positioning strategies in your actual applications
5. Track which approaches lead to interviews

## Support

Issues? Questions?
- GitHub Issues: [Create an issue](https://github.com/YOUR_USERNAME/jdanalyzer/issues)
