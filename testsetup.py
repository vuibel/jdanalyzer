#!/usr/bin/env python3
"""
Test script to validate setup without making API calls.
Run this to verify your installation before using the analyzer.
"""

import sys
from pathlib import Path

def test_imports():
    """Test that required libraries are installed."""
    print("Testing imports...")
    try:
        import anthropic
        print("  ✓ anthropic library installed")
        return True
    except ImportError:
        print("  ✗ anthropic library not found")
        print("    Run: pip install -r requirements.txt")
        return False

def test_example_files():
    """Test that example files exist."""
    print("\nTesting example files...")
    examples = [
        "examples/anthropic_founding_ae.txt",
        "examples/liveramp_account_director.txt",
        "examples/snowflake_healthcare_ae.txt"
    ]
    
    all_exist = True
    for example in examples:
        path = Path(example)
        if path.exists():
            print(f"  ✓ {example}")
        else:
            print(f"  ✗ {example} not found")
            all_exist = False
    
    return all_exist

def test_main_script():
    """Test that main script can be imported."""
    print("\nTesting main script...")
    try:
        # Add current directory to path
        sys.path.insert(0, str(Path(__file__).parent))
        import analyze_jd
        print("  ✓ analyze_jd.py can be imported")
        
        # Check that key functions exist
        if hasattr(analyze_jd, 'analyze_job_fit'):
            print("  ✓ analyze_job_fit function exists")
        else:
            print("  ✗ analyze_job_fit function not found")
            return False
            
        if hasattr(analyze_jd, 'CANDIDATE_PROFILE'):
            print("  ✓ CANDIDATE_PROFILE constant exists")
        else:
            print("  ✗ CANDIDATE_PROFILE constant not found")
            return False
            
        return True
    except Exception as e:
        print(f"  ✗ Error importing analyze_jd.py: {e}")
        return False

def test_readme():
    """Test that README exists."""
    print("\nTesting documentation...")
    readme = Path("README.md")
    if readme.exists():
        print("  ✓ README.md exists")
        return True
    else:
        print("  ✗ README.md not found")
        return False

def main():
    print("=" * 60)
    print("JD FIT ANALYZER - Setup Validation")
    print("=" * 60)
    print()
    
    results = []
    results.append(("Import Test", test_imports()))
    results.append(("Example Files", test_example_files()))
    results.append(("Main Script", test_main_script()))
    results.append(("Documentation", test_readme()))
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    for test_name, passed in results:
        status = "PASS" if passed else "FAIL"
        symbol = "✓" if passed else "✗"
        print(f"{symbol} {test_name}: {status}")
    
    all_passed = all(result[1] for result in results)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ All tests passed!")
        print("\nNext steps:")
        print("1. Set your ANTHROPIC_API_KEY environment variable")
        print("2. Run: python analyze_jd.py examples/anthropic_founding_ae.txt")
        print("\nSee SETUP.md for detailed instructions.")
    else:
        print("✗ Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("- Run: pip install -r requirements.txt")
        print("- Make sure you're in the jd-fit-analyzer directory")
    print("=" * 60)
    
    sys.exit(0 if all_passed else 1)

if __name__ == "__main__":
    main()
