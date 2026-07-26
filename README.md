# Phishing Email Investigation and Safe Triage

## Overview
This project documents the safe investigation of a suspicious email containing a malicious-looking link inside a controlled malware analysis lab. The objective was to identify phishing indicators, preserve evidence, analyze the email in an isolated environment, and record the findings in a format suitable for a cybersecurity portfolio.

## Project Objective
The purpose of this project was to investigate a suspicious email, determine whether it displayed phishing characteristics, and safely analyze its contents without exposing the host system to unnecessary risk. The project also demonstrates basic incident triage, evidence handling, and safe analysis workflows that are relevant to entry-level SOC and cybersecurity roles.

## Scenario
Phishing attacks are one of the most common ways attackers attempt to trick users into revealing information or visiting harmful websites. In this scenario, a suspicious email claimed that the recipient had won a cash prize and instructed them to click a link to claim the reward. Because the message used urgency, financial temptation, and an embedded hyperlink, it was treated as suspicious and investigated further.

## Lab Environment
To ensure safe execution and analysis of potentially malicious indicators, all triage actions were completed inside a virtualized sandbox.

- **Hypervisor:** VMware Workstation Pro on a Windows 11 host
- **Guest Operating System:** REMnux v7
- **Network Profile:** NAT configuration with restricted exposure to the local network
- **Defensive Controls:** Baseline snapshots used to restore a clean state between analysis attempts

## Tools Used
- VMware Workstation Pro
- Windows 11
- Microsoft Outlook
- REMnux
- Python 3
- Custom phishing analyzer script
- `.eml` email file for offline analysis
- Optional reputation checking through VirusTotal API integration

## Methodology
The investigation followed a simple and safe workflow:

1. Create or obtain the suspicious phishing email in a controlled environment.
2. Save the suspicious email as an `.eml` file to preserve the original message structure.
3. Transfer the file into the REMnux analysis environment.
4. Confirm Python 3 and required tooling are available.
5. Run the phishing analysis script against the `.eml` file.
6. Review the output for suspicious URLs, sender details, and attachment indicators.
7. Record the findings and determine whether the email should be treated as phishing.

## Evidence

### 1. Suspicious Email Received
The email used a prize-based lure and attempted to pressure the user into clicking a link before a deadline. Common phishing indicators visible in the message include emotional manipulation, a reward theme, urgency, and a clickable hyperlink.



**Figure 1.** Suspicious email claiming that the recipient has won £150,000 and must click a link to claim the prize.

### 2. Email Creation and Link Setup
The screenshot below shows the hyperlink configuration used in the phishing email. This demonstrates how attackers can hide a destination behind convincing anchor text to make a malicious or suspicious link appear harmless.



**Figure 2.** Hyperlink text configured as "Collect Winnings" while the destination is embedded separately.

### 3. Exporting the Email as an EML File
To preserve the email for safe offline inspection, the message was saved in `.eml` format. This allows analysis without interacting with the live email repeatedly and helps maintain evidence integrity.



**Figure 3.** Suspicious email saved as an `.eml` file before transfer to the REMnux investigation environment.

### 4. Preparing the REMnux Environment
Before analysis, Python 3 and supporting packages were verified in the REMnux virtual machine. This step ensured that the analysis tooling could run correctly in the isolated environment.



**Figure 4.** Python 3 and related packages being installed or updated inside the REMnux analysis VM.

### 5. Running the Analyzer
The `.eml` file was placed inside the phishing analysis workspace and processed with a Python-based analyzer. The script extracted the sender information, subject line, and URL contained in the message.



**Figure 5.** Analyzer output showing the email subject, sender, and a discovered URL inside the message body.

## Findings
The investigation identified several indicators commonly associated with phishing:

- The email promised a large financial reward.
- The language attempted to create urgency by giving a claim deadline.
- The message encouraged the user to click a link.
- The sender identity and message theme appeared suspicious.
- The analyzer detected a URL embedded in the email body.
- No file attachments were present, which suggests the main lure was the embedded link rather than a malicious document.

## Analysis Summary
The message exhibited classic phishing characteristics. Rather than delivering malware through an attachment, the email attempted to lure the victim into clicking a suspicious link related to a prize scam. The analyzer confirmed that the email contained a URL, which supports the conclusion that the message was intended to redirect the user to an external site.

In a real-world environment, the next defensive steps would normally include checking the sender domain, reviewing full email headers, validating SPF/DKIM/DMARC results, and submitting the extracted URL to a reputation platform such as VirusTotal or URLScan in accordance with organizational policy.

## Outcome
Based on the available evidence, the email should be classified as a phishing attempt and removed or reported according to incident response procedures. Because the investigation was conducted in a sandboxed lab, the suspicious content was reviewed safely without direct interaction from the host operating system.

## Lessons Learned
This project reinforced several important cybersecurity concepts:

- Suspicious emails often rely on urgency, emotion, or financial incentives.
- Embedded links should never be trusted based only on their display text.
- Saving a message as an `.eml` file helps preserve evidence for offline analysis.
- Malware and phishing triage should be performed in an isolated environment.
- Even simple scripts can quickly identify useful indicators such as URLs and attachment presence.

## Skills Demonstrated
- Email triage
- Phishing detection
- Safe malware analysis workflow
- Evidence preservation
- Virtual machine usage
- Basic Python tool execution
- Technical documentation

## GitHub Repository Structure
A simple project layout for this repository could look like this:

```text
phishing-email-investigation/
├── README.md
├── screenshots/
│   ├── phising-email-received.jpg
│   ├── phishing-email-setup-5.jpg
│   ├── remnux-transfer-email-3.jpg
│   ├── python-3-install-2.jpg
│   └── analyser-report-4.jpg
├── samples/
│   └── urgent.eml
└── tools/
    └── phishing_analyzer.py
```

## Suggested Screenshot Folder Update
If these images are added to a `screenshots/` folder in GitHub, update the image paths in this README to:

```markdown
![Suspicious phishing email received](screenshots/phising-email-received.jpg)
![Phishing email hyperlink setup](screenshots/phishing-email-setup-5.jpg)
![Saving phishing email as EML](screenshots/remnux-transfer-email-3.jpg)
![Python installation check in REMnux](screenshots/python-3-install-2.jpg)
![Analyzer report in REMnux](screenshots/analyser-report-4.jpg)
```

## Future Improvements
This project can be expanded in several ways:

- Add full email header analysis
- Include SPF, DKIM, and DMARC validation
- Integrate VirusTotal or URLScan results
- Defang URLs before documentation
- Add indicators of compromise in a separate section
- Include a short incident response playbook for phishing emails

## Conclusion
This project demonstrates a beginner-friendly but realistic phishing investigation workflow. It shows how a suspicious email can be preserved, transferred into a secure analysis environment, examined with basic tooling, and documented clearly as part of a cybersecurity portfolio.
