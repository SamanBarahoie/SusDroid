import os
import re
import argparse
from colorama import Fore, Style
from report_generator import generate_report

SUSPICIOUS_PATTERNS = {
    "Send SMS": r'Landroid\/telephony\/SmsManager;->sendTextMessage',
    "Access Location": r'Landroid\/location\/LocationManager;->getLastKnownLocation',
    "Dynamic Code Execution": r'Ldalvik\/system\/DexClassLoader;',
    "Call Phone": r'android.intent.action.CALL',
    "Load URL": r'Landroid\/webkit\/WebView;->loadUrl',
    "Sensitive Permissions": r'android\.permission\.(SEND_SMS|READ_SMS|CALL_PHONE|ACCESS_FINE_LOCATION|INTERNET)'
}

def scan_file(filepath):
    findings = []
    try:
        with open(filepath, 'r', errors='ignore') as f:
            content = f.read()
            for label, pattern in SUSPICIOUS_PATTERNS.items():
                if re.search(pattern, content):
                    findings.append(label)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return findings

def walk_directory(directory):
    results = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.smali') or file == 'AndroidManifest.xml':
                full_path = os.path.join(root, file)
                matches = scan_file(full_path)
                if matches:
                    results[full_path] = matches
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SusDroid - APK Static Behavior Analyzer")
    parser.add_argument('--path', required=True, help='Path to decompiled APK (smali + manifest)')
    parser.add_argument('--report', required=False, help='Path to save HTML report')
    args = parser.parse_args()

    print(Fore.CYAN + "[*] Scanning for suspicious behavior..." + Style.RESET_ALL)
    results = walk_directory(args.path)

    for file, matches in results.items():
        print(Fore.YELLOW + f"\n[+] {file}" + Style.RESET_ALL)
        for match in matches:
            print(Fore.RED + f"  ↳ {match}" + Style.RESET_ALL)

    if args.report:
        generate_report(results, args.report)
        print(Fore.GREEN + f"\n[✓] Report saved to {args.report}" + Style.RESET_ALL)