#!/bin/bash

# Renkleri tanımlama
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
MAGENTA='\033[0;35m'
WHITE='\033[0;37m'
RESET='\033[0m'

get_domain_info() {
    domain=$1
    ip_address=$(getent hosts "$domain" | awk '{ print $1 }')

    if [[ -z "$ip_address" ]]; then
        echo -e "${RED}'$domain' domain adresi çözümlenemedi.${RESET}"
        return
    fi

    url="http://ip-api.com/json/$ip_address"
    response=$(curl -s "$url")

    echo -e "\n${CYAN}Domain: $domain${RESET}"
    echo -e "${CYAN}IP Adresi: $ip_address${RESET}"
    echo -e "${MAGENTA}Ek Bilgiler:${RESET}"
    echo "$response" | jq '.'
}

get_ip_info() {
    ip=$1
    url="http://ip-api.com/json/$ip"
    response=$(curl -s "$url")

    echo -e "\n${CYAN}IP: $ip bilgileri:${RESET}"
    echo "$response" | jq '.'
}

get_my_ip() {
    url="https://api.ipify.org?format=json"
    response=$(curl -s "$url")

    echo -e "\n${CYAN}Kendi Genel IP Adresiniz:${RESET}"
    echo "$response" | jq '.'
}

main() {
    echo -e "${CYAN}===== Bash Multi-tool: Site & IP Bilgi Aracı =====${RESET}"

    while true; do
        echo -e "\n${YELLOW}Lütfen aşağıdaki seçeneklerden birini seçin:${RESET}"
        echo "1. Bir sitenin IP adresi ve ekstra bilgilerini al"
        echo "2. Belirli bir IP adresi hakkında bilgi al"
        echo "3. Kendi genel IP adresini öğren"
        echo "4. Çıkış"

        read -rp "$(echo -e "${GREEN}Seçiminiz (1-4): ${RESET}")" choice

        case "$choice" in
            1)
                read -rp "$(echo -e "${GREEN}Domain girin (örnek: google.com): ${RESET}")" domain
                get_domain_info "$domain"
                ;;
            2)
                read -rp "$(echo -e "${GREEN}IP adresi girin: ${RESET}")" ip
                get_ip_info "$ip"
                ;;
            3)
                get_my_ip
                ;;
            4)
                echo -e "${YELLOW}Program kapatılıyor. İyi günler!${RESET}"
                break
                ;;
            *)
                echo -e "${RED}Geçersiz seçim! Lütfen tekrar deneyin.${RESET}"
                ;;
        esac
    done
}

# Ana fonksiyonu çalıştır
main
