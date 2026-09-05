# HACKNUT - OSINT Reconnaissance Tool 🌰

**HACKNUT** is a Python-based OSINT tool developed for educational purposes. 
It helps in gathering public information about Usernames, Domains, IP Addresses, and Websites.

Developed by: **[Hacknut988]**    
Date: **September 2026**

---

## 📌 About The Project

In Cyber Security, OSINT means "Open Source Intelligence". Doing it manually takes a lot of time. 
HACKNUT automates this process and collects public data in one place.

This project is made for educational purposes only.

---

## ⚡ Features

HACKNUT v1.0 has 9 main modules:

1.  Username Scanner
2.  Domain OSINT - Whois + IP 
3.  IP Geolocation
4.  Email Scraper
5.  Port Scanner - Nmap
6.  Subdomain Finder
7.  Server Detector
8.  DNS Records - A, MX, NS, TXT
9.  Social Post Finder

## 🛠️ Tech Stack & Requirements

- **Language**: Python 3
- **Libraries**: 
    - `requests`
    - `python-whois` 
    - `beautifulsoup4`
    - `colorama`
    - `nmap`
- **OS**: Works on Windows, Linux, and Kali Linux

---

## 🚀 How to Install & Run

```bash
git clone https://github.com/Hacknut988/HACKNUT-OSINT.git
cd HACKNUT-OSINT
pip install -r requirements.txt
sudo apt install nmap
python3 hacknut.py
