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

HACKNUT v1.1 has 7 main modules:

1.  **Username Recon**  
    Checks if a username exists on GitHub, Instagram, Twitter/X, and Reddit.

2.  **Domain OSINT**  
    Performs WHOIS lookup, gets Registrar, Creation Date, and resolves IP Address.

3.  **IP OSINT**  
    Finds Geolocation, Country, City, Region, and ISP of any IP Address.

4.  **Email Scraper**  
    Extracts all public email addresses from any given website.

5.  **Auto Report Generation**  
    Saves all results in a `.txt` file like `HACKNUT_Report_target.txt`

6.  **Facebook Recon**: Check username on Facebook

7.  **Server Detection**: Detect server, CMS, CDN
---

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

### Step 1: Clone or Download
```bash
git clone https://github.com/Hacknut988/HACKNUT-OSINT.git
cd HACKNUT-OSINT
