import socket
import requests
from colorama import init, Fore, Style

# Colorama'yı başlatıyoruz (otomatik reset sayesinde stil sonrasında sıfırlanır)
init(autoreset=True)

def get_domain_info(domain):
    """
    Belirtilen domain'in IP adresini çözümler ve ip-api.com üzerinden detaylı bilgiler alır.
    """
    try:
        ip_address = socket.gethostbyname(domain)
    except Exception as e:
        print(f"{Fore.RED}'{domain}' domain adresi çözümlenemedi: {Style.RESET_ALL}{e}")
        return None

    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(f"{Fore.RED}IP bilgileri alınırken hata oluştu: {Style.RESET_ALL}{e}")
        data = None

    return ip_address, data

def get_ip_info(ip):
    """
    Belirtilen IP adresi için ip-api.com üzerinden detaylı bilgi sorgular.
    """
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(f"{Fore.RED}IP bilgileri alınırken hata oluştu: {Style.RESET_ALL}{e}")
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
        print(f"{Fore.RED}Kendi IP adresiniz alınırken hata oluştu: {Style.RESET_ALL}{e}")
        data = None

    return data

def print_geo_info(data):
    """
    ip-api.com tarafından dönen veriden coğrafi konum bilgilerini özenli bir şekilde yazdırır.
    """
    if data:
        print(f"\n{Fore.MAGENTA}Coğrafi Konum Bilgileri:{Style.RESET_ALL}")
        print(f"  {Fore.WHITE}Ülke: {data.get('country', 'Bilinmiyor')}{Style.RESET_ALL}")
        print(f"  {Fore.WHITE}Bölge: {data.get('regionName', 'Bilinmiyor')}{Style.RESET_ALL}")
        print(f"  {Fore.WHITE}Şehir: {data.get('city', 'Bilinmiyor')}{Style.RESET_ALL}")
        print(f"  {Fore.WHITE}Koordinatlar: {data.get('lat', 'Bilinmiyor')}, {data.get('lon', 'Bilinmiyor')}{Style.RESET_ALL}")
        print(f"  {Fore.WHITE}Zaman Dilimi: {data.get('timezone', 'Bilinmiyor')}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Coğrafi konum bilgileri alınamadı.{Style.RESET_ALL}")

def main():
    print(f"{Fore.CYAN}{Style.BRIGHT}===== ipTracer ====={Style.RESET_ALL}")
    while True:
        print(f"\n{Fore.YELLOW}Lütfen aşağıdaki seçeneklerden birini seçin:")
        print("1. Bir sitenin IP adresi, ekstra bilgileri ve coğrafi konumunu al")
        print("2. Belirli bir IP adresi hakkında bilgi ve coğrafi konum bilgisi al")
        print("3. Kendi genel IP adresinizi ve coğrafi konum bilgilerinizi öğren")
        print("4. Çıkış" + Style.RESET_ALL)
        
        choice = input(f"{Fore.GREEN}Seçiminiz (1-4): {Style.RESET_ALL}").strip()

        if choice == '1':
            domain = input(f"{Fore.GREEN}Bilgilerini almak istediğiniz sitenin domain'ini girin (örnek: google.com): {Style.RESET_ALL}").strip()
            result = get_domain_info(domain)
            if result:
                ip, info = result
                print(f"\n{Fore.CYAN}Domain: {domain}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}IP Adresi: {ip}{Style.RESET_ALL}")
                if info:
                    print_geo_info(info)
                    print(f"\n{Fore.MAGENTA}Ek Bilgiler:{Style.RESET_ALL}")
                    for key, value in info.items():
                        print(f"  {Fore.WHITE}{key}: {value}{Style.RESET_ALL}")

        elif choice == '2':
            ip = input(f"{Fore.GREEN}Bilgilerini almak istediğiniz IP adresini girin: {Style.RESET_ALL}").strip()
            info = get_ip_info(ip)
            if info:
                print(f"\n{Fore.CYAN}IP: {ip} bilgileri:{Style.RESET_ALL}")
                print_geo_info(info)
                print(f"\n{Fore.MAGENTA}Ek Bilgiler:{Style.RESET_ALL}")
                for key, value in info.items():
                    print(f"  {Fore.WHITE}{key}: {value}{Style.RESET_ALL}")

        elif choice == '3':
            my_ip_data = get_my_ip()
            if my_ip_data and "ip" in my_ip_data:
                print(f"\n{Fore.CYAN}Kendi Genel IP Adresiniz: {my_ip_data['ip']}{Style.RESET_ALL}")
                info = get_ip_info(my_ip_data['ip'])
                if info:
                    print_geo_info(info)
                    print(f"\n{Fore.MAGENTA}Ek Bilgiler:{Style.RESET_ALL}")
                    for key, value in info.items():
                        print(f"  {Fore.WHITE}{key}: {value}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Kendi IP adresiniz alınamadı.{Style.RESET_ALL}")

        elif choice == '4':
            print(f"{Fore.YELLOW}Program kapatılıyor. İyi günler!{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}Geçersiz seçim! Lütfen tekrar deneyin.{Style.RESET_ALL}")

if __name__ == '__main__':
    main()
