import email
from email import policy
import hashlib
import re
import os
import requests
import base64

VT_API_KEY = os.getenv("VT_API_KEY")
eml_file_path = input("Enter the path to the .eml file to analyze: ")

try:
    with open(eml_file_path, 'rb') as f:
        msg = email.message_from_binary_file(f, policy=policy.default)

    print("\n" + "="*40)
    print("      SOC EMAIL ANALYSIS REPORT")
    print("="*40)
    print(f"[+] From:    {msg['from']}")
    print(f"[+] To:      {msg['to']}")
    print(f"[+] Subject: {msg['subject']}")
    print("-" * 40)

    email_body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() in ["text/plain", "text/html"]:
                email_body += part.get_payload(decode=True).decode(errors='ignore')
    else:
        email_body = msg.get_payload(decode=True).decode(errors='ignore')

    url_pattern = r'https?://[^\s<>"]+'
    urls = re.findall(url_pattern, email_body)
    unique_urls = list(set(urls))

    print(f"[!] Found {len(unique_urls)} URLs inside the email:")
    
    if not VT_API_KEY:
        print("[-] Warning: VT_API_KEY environment variable not set. Skipping API checks.")
        for url in unique_urls:
            print(f"    -> {url}")
    else:
        for url in unique_urls:
            print(f"    -> Analyzing: {url}")
            
            url_bytes = url.encode('utf-8')
            base64_bytes = base64.urlsafe_b64encode(url_bytes)
            url_id = base64_bytes.decode('utf-8').rstrip('=')
            
            # Formulate components array to bypass VMware clipboard translation blocks
            domain_parts = ["https:", "", "www.virustotal.com", "api", "v3", "urls", url_id]
            vt_url = "/".join(domain_parts)
            
            headers = {
                "accept": "application/json",
                "x-apikey": VT_API_KEY
            }
            
            try:
                response = requests.get(vt_url, headers=headers)
                if response.status_code == 200:
                    stats = response.json()['data']['attributes']['last_analysis_stats']
                    print(f"       [!] VirusTotal Verdict: {stats['malicious']} engines flagged as Malicious.")
                elif response.status_code == 404:
                    print("       [-] VirusTotal Verdict: Clean (No history found for this URL).")
                else:
                    print(f"       [-] API Error: Status Code {response.status_code}")
            except Exception as api_err:
                print(f"       [-] Failed to query API: {api_err}")

    print("-" * 40)
    print("[!] Checking Attachments:")
    attachments_found = False
    for part in msg.walk():
        if part.get_content_disposition() == 'attachment':
            attachments_found = True
            filename = part.get_filename()
            file_data = part.get_payload(decode=True)
            sha256_hash = hashlib.sha256(file_data).hexdigest()
            print(f"    -> Filename: {filename}\n       SHA-256:  {sha256_hash}")
    if not attachments_found:
        print("    -> No attachments found in this email.")
    print("="*40)

except FileNotFoundError:
    print(f"[-] Error: File '{eml_file_path}' not found.")
except Exception as e:
    print(f"[-] Error: {e}")
