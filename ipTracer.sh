#!/bin/sh

# API ile IP bilgilerini çekme
get_domain_info() {
    domain="$1"
    ip_address=$(busybox nslookup "$domain" 2>/dev/null | awk '/^Address/ { print $2 }' | tail -n1)

    if [ -z "$ip_address" ]; then
        echo "'$domain' domain adresi çözümlenemedi."
        return
    fi

    url="http://ip-api.com/json/$ip_address"
    response=$(curl -s "$url")

    echo "\nDomain: $domain"
    echo "IP Adresi: $ip_address"
    echo "Ek Bilgiler:"
    echo "$response"
}

get_ip_info() {
    ip="$1"
    url="http://ip-api.com/json/$ip"
    response=$(curl -s "$url")

    echo "\nIP: $ip bilgileri:"
    echo "$response"
}

get_my_ip() {
    url="https://api.ipify.org?format=json"
    response=$(curl -s "$url")

    echo "\nKendi Genel IP Adresiniz:"
    echo "$response"
}

main() {
    echo "===== Ish Shell Multi-tool: Site & IP Bilgi Aracı ====="

    while true; do
        echo "\nLütfen aşağıdaki seçeneklerden birini seçin:"
        echo "1. Bir sitenin IP adresi ve ekstra bilgilerini al"
        echo "2. Belirli bir IP adresi hakkında bilgi al"
        echo "3. Kendi genel IP adresini öğren"
        echo "4. Çıkış"

        read -r choice

        case "$choice" in
            1)
                echo "Domain girin (örnek: google.com):"
                read -r domain
                get_domain_info "$domain"
                ;;
            2)
                echo "IP adresi girin:"
                read -r ip
                get_ip_info "$ip"
                ;;
            3)
                get_my_ip
                ;;
            4)
                echo "Program kapatılıyor. İyi günler!"
                break
                ;;
            *)
                echo "Geçersiz seçim! Lütfen tekrar deneyin."
                ;;
        esac
    done
}

# Ana fonksiyonu çalıştır
main
