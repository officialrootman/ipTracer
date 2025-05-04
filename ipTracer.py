import socket
import requests

def get_domain_info(domain):
    """
    Belirtilen domain'in IP adresini çözümler ve ip-api.com üzerinden detaylı bilgiler alır.
    """
    try:
        # Domain adresini IP'ye çeviriyoruz.
        ip_address = socket.gethostbyname(domain)
    except Exception as e:
        print(f"'{domain}' domain adresi çözümlenemedi: {e}")
        return None

    # Çözümlenen IP adresi için ip-api üzerinden sorgulama yapıyoruz.
    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(f"IP bilgileri alınırken hata oluştu: {e}")
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
        print(f"IP bilgileri alınırken hata oluştu: {e}")
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
        print(f"Kendi IP adresiniz alınırken hata oluştu: {e}")
        data = None

    return data

def main():
    print("===== Python Multi-tool: Site & IP Bilgi Aracı =====")
    while True:
        print("\nLütfen aşağıdaki seçeneklerden birini seçin:")
        print("1. Bir sitenin IP adresi ve ekstra bilgilerini al")
        print("2. Belirli bir IP adresi hakkında bilgi al")
        print("3. Kendi genel IP adresini öğren")
        print("4. Çıkış")
        
        choice = input("Seçiminiz (1-4): ").strip()

        if choice == '1':
            domain = input("IP bilgilerini almak istediğiniz sitenin domain'ini girin (örnek: google.com): ").strip()
            result = get_domain_info(domain)
            if result:
                ip, info = result
                print(f"\nDomain: {domain}")
                print(f"IP Adresi: {ip}")
                if info:
                    print("Ek Bilgiler:")
                    # JSON datasını okunabilir biçimde yazdırıyoruz.
                    for key, value in info.items():
                        print(f"  {key}: {value}")

        elif choice == '2':
            ip = input("Bilgilerini almak istediğiniz IP adresini girin: ").strip()
            info = get_ip_info(ip)
            if info:
                print(f"\nIP: {ip} bilgileri:")
                for key, value in info.items():
                    print(f"  {key}: {value}")

        elif choice == '3':
            my_ip = get_my_ip()
            if my_ip:
                print("\nKendi Genel IP Adresiniz:")
                for key, value in my_ip.items():
                    print(f"  {key}: {value}")

        elif choice == '4':
            print("Program kapatılıyor. İyi günler!")
            break

        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

if __name__ == '__main__':
    main()
