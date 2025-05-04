import socket
import requests
from colorama import init, Fore, Style
from pyfiglet import Figlet

def display_banner():
    """
    Pyfiglet ile "ipTracer" metnini büyük harflerle banner şeklinde yazdırır.
    """
    fig = Figlet(font="slant")  # Farklı fontları da deneyebilirsiniz.
    banner = fig.renderText("ipTracer")
    print(Fore.CYAN + banner + Style.RESET_ALL)

def get_domain_info(domain):
    """
    Verilen domain'in IP adresini çözümler ve ip-api.com üzerinden detaylı bilgileri sorgular.
    """
    try:
        ip_address = socket.gethostbyname(domain)
    except Exception as e:
        print(f"{Fore.RED}'{domain}' domain çözümlenemedi: {e}{Style.RESET_ALL}")
        return None

    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(f"{Fore.RED}IP bilgileri alınırken hata oluştu: {e}{Style.RESET_ALL}")
        data = None

    return ip_address, data

def get_ip_info(ip):
    """
    Belirtilen IP adresi için ip-api üzerinden detaylı bilgileri sorgular.
    """
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(f"{Fore.RED}IP bilgileri alınırken hata oluştu: {e}{Style.RESET_ALL}")
        data = None
    return data

def get_my_ip():
    """
    Kendi genel IP adresinizi ipify servisi üzerinden elde eder.
    """
    url = "https://api.ipify.org?format=json"
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(f"{Fore.RED}Kendi IP adresiniz alınırken hata oluştu: {e}{Style.RESET_ALL}")
        data = None
    return data

def main():
    # Colorama'yı başlatıyoruz (autoreset sayesinde stil her print sonrasında sıfırlanır)
    init(autoreset=True)
    
    display_banner()
    print(Fore.YELLOW + "ipTracer'a hoşgeldiniz!" + Style.RESET_ALL)
    
    while True:
        print(f"\n{Fore.BLUE}Aşağıdaki seçeneklerden birini seçin:{Style.RESET_ALL}")
        print("1. Bir sitenin IP ve ek bilgilerini al")
        print("2. Belirli bir IP hakkında bilgi al")
        print("3. Kendi genel IP'nizi öğren")
        print("4. Çıkış")
        
        choice = input(Fore.GREEN + "Seçiminiz (1-4): " + Style.RESET_ALL).strip()
        
        if choice == '1':
            domain = input(Fore.GREEN + "Domain giriniz (örnek: google.com): " + Style.RESET_ALL).strip()
            result = get_domain_info(domain)
            if result:
                ip, info = result
                print(f"\n{Fore.CYAN}Domain: {domain}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}IP Adresi: {ip}{Style.RESET_ALL}")
                if info:
                    print(Fore.MAGENTA + "Ek Bilgiler:" + Style.RESET_ALL)
                    for key, value in info.items():
                        print(f"{Fore.WHITE}{key}: {value}{Style.RESET_ALL}")
        elif choice == '2':
            ip = input(Fore.GREEN + "IP giriniz: " + Style.RESET_ALL).strip()
            info = get_ip_info(ip)
            if info:
                print(f"\n{Fore.CYAN}IP: {ip} bilgileri:{Style.RESET_ALL}")
                for key, value in info.items():
                    print(f"{Fore.WHITE}{key}: {value}{Style.RESET_ALL}")
        elif choice == '3':
            info = get_my_ip()
            if info:
                print(f"\n{Fore.CYAN}Kendi Genel IP Adresiniz:{Style.RESET_ALL}")
                for key, value in info.items():
                    print(f"{Fore.WHITE}{key}: {value}{Style.RESET_ALL}")
        elif choice == '4':
            print(Fore.YELLOW + "Çıkılıyor. İyi günler!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Geçersiz seçim, lütfen tekrar deneyin." + Style.RESET_ALL)

if __name__ == '__main__':
    main()
