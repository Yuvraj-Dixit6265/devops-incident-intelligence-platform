import os
import re
import sys

SECRET_PATTERNS = [
    r'AKIA[0-9A-Z]{16}',          # AWS key example
    r'password\s*=\s*["\'].*["\']',
    r'api_key\s*=\s*["\'].*["\']'
]

def scan_file(file_path):
    with open(file_path, 'r', errors='ignore') as f:
        content = f.read()
        for pattern in SECRET_PATTERNS:
            if re.search(pattern, content, re.IGNORECASE):
                print(f"❌ Secret detected in {file_path}")
                return True
    return False

def scan_repo():
    found = False
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                if scan_file(os.path.join(root, file)):
                    found = True
    if found:
        print("🚨 Security scan failed")
        sys.exit(1)
    else:
        print("✅ No secrets found")

if __name__ == "__main__":
    scan_repo()
