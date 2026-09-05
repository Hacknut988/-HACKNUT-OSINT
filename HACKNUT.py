import requests, whois, socket, datetime, re, subprocess
from colorama import Fore, Style, init
init()

BANNER = f"""{Fore.RED}
██╗  ██╗ █████╗  ██████╗██╗  ██╗███╗   ██╗██╗   ██╗████████╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝████╗  ██║██║   ██║╚══██╔══╝
███████║███████║██║     █████╔╝ ██╔██╗ ██║██║   ██║   ██║   
██╔══██║██╔══██║██║     ██╔═██╗ ██║╚██╗██║██║   ██║   ██║   
██║  ██║██║  ██║╚██████╗██║  ██╗██║ ╚████║╚██████╔╝   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝   
        HACKNUT OSINT SUITE v1.0
        Developed by: [Hacknut988]
        For Educational Purpose Only
{Style.RESET_ALL}"""

SITES = {
    "GitHub": "https://github.com/{}", "Instagram": "https://www.instagram.com/{}/",
    "Twitter/X": "https://twitter.com/{}", "Reddit": "https://www.reddit.com/user/{}",
    "Facebook": "https://www.facebook.com/{}"
}

def check_username(username):
    print(f"\n{Fore.YELLOW}[+] Scanning Username: {username}{Style.RESET_ALL}")
    found = []
    for site, url in SITES.items():
        try:
            r = requests.get(url.format(username), timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
            if r.status_code == 200: 
                print(f"{Fore.GREEN}[FOUND]{Style.RESET_ALL} {site}: {url.format(username)}")
                found.append(f"{site}: {url.format(username)}")
            else:
                print(f"{Fore.RED}[NOT FOUND]{Style.RESET_ALL} {site}")
        except: pass
    return found

def domain_osint(domain):
    print(f"\n{Fore.YELLOW}[+] Scanning Domain: {domain}{Style.RESET_ALL}")
    report = []
    try:
        w = whois.whois(domain)
        report.append(f"Registrar: {w.registrar}")
        report.append(f"Creation Date: {w.creation_date}")
        print(f"    Registrar: {w.registrar}")
    except: pass
    try:
        ip = socket.gethostbyname(domain)
        report.append(f"IP Address: {ip}")
        print(f"    IP Address: {ip}")
    except: pass
    return report

def ip_osint(ip):
    print(f"\n{Fore.YELLOW}[+] Scanning IP: {ip}{Style.RESET_ALL}")
    report = []
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        if r['status'] == 'success':
            report.append(f"Location: {r['city']}, {r['country']} | ISP: {r['isp']}")
            print(f"    Location: {r['city']}, {r['country']} | ISP: {r['isp']}")
    except: 
        print(f"{Fore.RED}Error fetching IP data{Style.RESET_ALL}")
    return report

def email_scraper(url):
    print(f"\n{Fore.YELLOW}[+] Scraping Emails from: {url}{Style.RESET_ALL}")
    emails = set(); report = []
    
    if not url.startswith("http"): 
        url = "http://" + url
    
    urls_to_check = [url, url + "/contact", url + "/about"]
    
    for target_url in urls_to_check:
        try:
            print(f"    Checking: {target_url}")
            r = requests.get(target_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
            found_emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', r.text)
            
            for email in found_emails:
                if "png" not in email and "jpg" not in email and "css" not in email and "example" not in email:
                    emails.add(email)
                    
        except: 
            print(f"    {Fore.RED}Failed to connect to {target_url}{Style.RESET_ALL}")
    
    if emails:
        for email in emails: 
            print(f"{Fore.GREEN}[EMAIL FOUND]{Style.RESET_ALL} {email}")
            report.append(email)
    else:
        print(f"{Fore.RED}[!] No emails found{Style.RESET_ALL}")
        report.append("No emails found")
        
    return report

def port_scanner(target):
    target = target.replace("http://", "").replace("https://", "").replace("/", "")
    print(f"\n{Fore.YELLOW}[+] Running Nmap Port Scan on: {target}{Style.RESET_ALL}")
    report = []
    try:
        result = subprocess.run(['nmap', '-F', target], capture_output=True, text=True, timeout=120)
        print(result.stdout)
        report.append(result.stdout)
    except FileNotFoundError:
        print(f"{Fore.RED}Error: Nmap not installed. Run: sudo apt install nmap{Style.RESET_ALL}")
        report.append("Nmap not installed")
    except subprocess.TimeoutExpired:
        print(f"{Fore.RED}Error: Nmap scan timed out{Style.RESET_ALL}")
        report.append("Scan timed out")
    return report

def subdomain_finder(domain):
    print(f"\n{Fore.YELLOW}[+] Finding Subdomains for: {domain}{Style.RESET_ALL}")
    subdomains = ["www", "mail", "ftp", "admin", "test", "dev", "api", "blog"]
    report = []
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            r = requests.get(url, timeout=3)
            if r.status_code < 400:
                print(f"{Fore.GREEN}[FOUND]{Style.RESET_ALL} {url}")
                report.append(url)
        except: pass
    return report

def server_detector(url):
    print(f"\n{Fore.YELLOW}[+] Detecting Server & Tech for: {url}{Style.RESET_ALL}")
    report = []
    try:
        if not url.startswith("http"): url = "http://" + url
        r = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        server = r.headers.get('Server', 'Not Found')
        report.append(f"Server: {server}")
        print(f"    {Fore.GREEN}Server:{Style.RESET_ALL} {server}")
        
        # Check for common tech
        if 'wordpress' in r.text.lower(): 
            print(f"    {Fore.GREEN}CMS:{Style.RESET_ALL} WordPress")
            report.append("CMS: WordPress")
    except: print("Error")
    return report
    
def social_bio_email(username):
    print(f"\n{Fore.YELLOW}[+] Checking Public Bios for Email: {username}{Style.RESET_ALL}")
    report = []
    try:
        r = requests.get(f"https://api.github.com/users/{username}", timeout=5).json()
        email = r.get('email', '')
        if email:
            print(f"{Fore.GREEN}[GITHUB EMAIL]{Style.RESET_ALL} {email}")
            report.append(f"GitHub Email: {email}")
    except: pass
    return report

def dns_records(domain):
    print(f"\n{Fore.YELLOW}[+] Getting DNS Records for: {domain}{Style.RESET_ALL}")
    report = []
    types = ['A', 'MX', 'NS', 'TXT']
    
    try:
        import dns.resolver
    except:
        print(f"{Fore.RED}[!] Install karo: pip install dnspython{Style.RESET_ALL}")
        return ["dnspython not installed"]
    
    for record_type in types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            for rdata in answers:
                result = f"{record_type}: {rdata}"
                print(f"{Fore.GREEN}[{record_type}]{Style.RESET_ALL} {rdata}")
                report.append(result)
        except: 
            pass
    
    if not report: report.append("No DNS records found")
    return report

def social_post_finder(username):
    print(f"\n{Fore.YELLOW}[+] Finding Public Profiles for: {username}{Style.RESET_ALL}")
    report = []
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://reddit.com/user/{username}",
        "Pinterest": f"https://pinterest.com/{username}",
        "Medium": f"https://medium.com/@{username}"
    }
    
    for site, url in sites.items():
        try:
            r = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
            if r.status_code == 200:
                print(f"{Fore.GREEN}[FOUND]{Style.RESET_ALL} {site}: {url}")
                report.append(f"{site}: {url}")
            else:
                print(f"{Fore.RED}[NOT FOUND]{Style.RESET_ALL} {site}")
        except: 
            pass
    
    if not report: report.append("No public profiles found")
    return report

def save_report(target, data):
    safe_target = target.replace("http://", "").replace("https://", "").replace("/", "_").replace(":", "_")
    filename = f"HACKNUT_Report_{safe_target}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("HACKNUT v3.4 REPORT\n" + "="*40 + "\n")
        f.write(f"Target: {target}\nDate: {datetime.datetime.now()}\n\n")
        for d in data: f.write(str(d) + "\n")
    print(f"\n{Fore.GREEN}[+] Report saved: {filename}{Style.RESET_ALL}")

def main():
    print(BANNER)
    print(f"{Fore.CYAN}1. Username 2. Domain 3. IP 4. Email Scraper{Style.RESET_ALL}")
    print(f"{Fore.CYAN}5. Port Scan 6. Subdomain 7. Server Detector{Style.RESET_ALL}")
    print(f"{Fore.CYAN}8. DNS Records 9. Social Post Finder{Style.RESET_ALL}")
    
    choice = input(f"\n{Fore.RED}HACKNUT> {Style.RESET_ALL}")
    all_data = []; target_name = ""
    
    if choice == "1": target_name = input("Username: "); all_data = check_username(target_name)
    elif choice == "2": target_name = input("Domain: "); all_data = domain_osint(target_name)
    elif choice == "3": target_name = input("IP: "); all_data = ip_osint(target_name)
    elif choice == "4": target_name = input("URL: "); all_data = email_scraper(target_name)
    elif choice == "5": target_name = input("Target IP/Domain: "); all_data = port_scanner(target_name)
    elif choice == "6": target_name = input("Domain: "); all_data = subdomain_finder(target_name)
    elif choice == "7": target_name = input("Domain/URL: "); all_data = server_detector(target_name)
    elif choice == "8": target_name = input("Domain: "); all_data = dns_records(target_name)
    elif choice == "9": target_name = input("Username: "); all_data = social_post_finder(target_name)
    
    if all_data: save_report(target_name, all_data)

if __name__ == "__main__":
    main()
