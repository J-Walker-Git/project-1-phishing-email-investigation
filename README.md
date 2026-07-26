# Phishing Email Investigation and Safe Triage

## Overview
This project documents the safe investigation of a suspicious email containing a malicious-looking link inside a controlled malware analysis lab..

## Project Objective
The purpose of this project was to investigate a suspicious email, determine whether it displayed phishing characteristics, and safely analyse its contents without exposing the host system to unnecessary risk. The project also demonstrates basic incident triage, evidence handling, and safe analysis workflows that are relevant to SOC L1 and cybersecurity roles.

## Scenario
In this scenario, a suspicious email claimed that the recipient had won a cash prize and instructed them to click a link to claim the reward. Because the message used urgency, financial temptation, and an embedded hyperlink, it was treated as suspicious and investigated further.

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
- Custom phishing analyser script
- `.eml` email file for offline analysis

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

### 1. Email Creation and Link Setup
The screenshot below shows the hyperlink configuration used in the phishing email. I hid the malicious destination behind a link that appeared harmless.



### 2. Suspicious Email Received
The email used a prize-based lure and attempted to pressure the user into clicking a link before a deadline. To preserve the email for safe offline inspection, the message was saved in `.eml` format.



### 3. Exporting the Email as an EML File
The eml file was drage and dropped from the host machine to the VM sandbox. This allows analysis without interacting with the live email repeatedly and helps maintain evidence integrity.



**Figure 3.** Suspicious email saved as an `.eml` file before transfer to the REMnux investigation environment.

### 4. Preparing the REMnux Environment
Before analysis, Python 3 and supporting packages were verified in the REMnux virtual machine. This step ensured that the analysis tooling could run correctly in the isolated environment.



**Figure 4.** Python 3 and related packages being installed or updated inside the REMnux analysis VM.

### 5. Running the Analyser
The `.eml` file was placed inside the phishing analysis workspace and processed with a Python-based analyser. The script extracted the sender information, subject line, and URL contained in the message.



![image alt](https://github.com/J-Walker-Git/project-1-phishing-email-investigation/blob/6a048a2f7a0e7848bc176568a9f008d32954e683/screenshots/analyser-report.png)

## Findings
The investigation identified several indicators commonly associated with phishing:

- The email promised a large financial reward.
- The language created urgency by giving a short window of time to claim the prize.
- The message encouraged the user to click a link.
- The analyser detected a URL embedded in the email body.
- No file attachments were present, which suggests the main lure was the embedded link rather than a malicious document.

## Analysis Summary
The email attempted to lure the victim into clicking a suspicious link related to a prize scam. The analyser confirmed that the email contained a URL, confirming that the message was intended to redirect the user to an external site.

In a real-world environment, the next defensive steps would be to check the sender domain, review full email headers to check for hidden message routing data and cryptographic signatures which verify the authenticity of the sender. The extracted URL would then be submitted a reputation platform (e.g. VirusTotal) in accordance with company policy.

## Outcome
True Positive - The evidence available concludes that the email was a phishing attempt. It was removed and logged according to incident response procedures. As this investigation was conducted in a sandboxed lab, the suspicious content was reviewed safely without direct interaction from the host operating system.

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

## Future Improvements
Ways I would expand on this project would be to provide the VirusTotal API key for further results and also include a short incident response playbook for phishing emails

## Conclusion
This project demonstrates a realistic phishing investigation workflow. It shows how a suspicious email can be preserved, transferred into a secure analysis environment, examined with basic tooling, and documented clearly as part of a cybersecurity portfolio.
