## 👋🏾**DESCRIPTION**
This is my first official project as I begin my career in cybersecurity.

Something I have encountered in my personal and work life is phishing attacks. We've all receieved an email telling us to click a link for some too-good-to-be-true reason or another and instantly felt that moment of regret when we realise, in real time.... we messed up.

In a perfect world, the emails we recieve would all be legitimate, honest and **harmless** but unfortunately the _"Perfect World" patch_ has not been released yet....

...so in the meantime we all need to learn how to identify suspicious emails and know the necessary steps to take to avoid being the next victim of a malware attack.


## Purpose
My aim is to identify a threat (email with a link to a malicious website) and analyse it before safely removing it.


## 🛠️ Lab Environment
To ensure safe execution and analysis of potentially malicious indicators, all triage actions were contained within a virtualized sandbox.

* **Hypervisor:** VMware Workstation Pro (Windows 11 Host)
* **Guest Operating System:** REMnux v7 (Linux-based Malware Analysis Toolkit)
* **Network Profile:** NAT Configuration (Restricted outbound API access; isolated from local LAN)
* **Defensive Controls:** Baseline snapshots utilized to guarantee a pristine state between analysis iterations.
