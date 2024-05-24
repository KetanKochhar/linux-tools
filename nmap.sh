#!/bin/bash

# Check if the script is running with sudo
if [[ $EUID -ne 0 ]]; then
    echo "This script needs to be run with sudo."
    exit 1
fi

#!/bin/bash

# Check if Nmap is installed
if ! command -v nmap &> /dev/null; then
    echo "Nmap is not installed. Please install Nmap before running this script."
    exit 1
fi

# Prompt the user for the target IP address or hostname
read -p "Enter the target IP address or hostname: " target

# Display options menu
echo "Select an option:"
echo "1. Basic scan"
echo "2. TCP scan"
echo "3. UDP scan"
echo "4. OS detection"
echo "5. Full port scan"
echo "6. Quick scan"
echo "7. Full scan"
echo "8. Custom port scan"
echo "9. Service version detection"
echo "10. Exit"

# Prompt the user for the desired scan type
read -p "Enter your choice (1-7): " option

# Perform the selected scan based on user input
case $option in
    1)
        nmap $target
        ;;
    2)
        nmap -sS $target
        ;;
    3)
        nmap -sU $target
        ;;
    4)
        nmap -O $target
        ;;
    5)
        nmap -p- $target
        ;;
    6)
        nmap -T4 -F $target
        ;;
    7)
         nmap -T4 -A $target
        ;;
    8)
        read -p "Enter the port(s) to scan: " ports
        nmap -p $ports $target
        ;;
    9)
        nmap -sV $target
        ;;
    10)
        echo "Exiting the script..."
        exit 0
        ;;
    *)
        echo "Invalid option. Exiting the script..."
        exit 1
        ;;
esac

