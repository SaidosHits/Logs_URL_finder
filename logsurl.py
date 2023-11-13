import os
from colorama import init, Fore, Back, Style
from time import sleep
# Initialize Colorama
init(autoreset=True)
print("")
print("")

print("Welcom to @SaidosHits Tools")
sleep(2)
print("")
print("")
print("")

# Define the text with multiple colors
text = """

██╗░░░░░░█████╗░░██████╗░░██████╗██╗░░░██╗██████╗░██╗░░░░░  ███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
██║░░░░░██╔══██╗██╔════╝░██╔════╝██║░░░██║██╔══██╗██║░░░░░  ██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
██║░░░░░██║░░██║██║░░██╗░╚█████╗░██║░░░██║██████╔╝██║░░░░░  █████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██║░░░░░██║░░██║██║░░╚██╗░╚═══██╗██║░░░██║██╔══██╗██║░░░░░  ██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
███████╗╚█████╔╝╚██████╔╝██████╔╝╚██████╔╝██║░░██║███████╗  ██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
╚══════╝░╚════╝░░╚═════╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
"""

# Define the colors
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

# Split the text into lines and print with alternating colors
lines = text.strip().split('\n')
for i, line in enumerate(lines):
    print(colors[i % len(colors)] + line)

sleep(1)
print("")
print("")
print("")

dromin = input("Write the Domin Search: ")


# Function to search for files and extract credentials
def search_and_extract_credentials(root_path, keyword, output_file):
    with open(output_file, 'w', encoding='utf-8') as result_file:
        for foldername, subfolders, filenames in os.walk(root_path):
            for filename in filenames:
                if filename == "Passwords.txt":
                    file_path = os.path.join(foldername, filename)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        lines = file.readlines()
                        found_facebook = False
                        for i, line in enumerate(lines):
                            if keyword in line:
                                url = line.strip()
                                if f"{dromin}" in url:
                                    found_facebook = True
                            elif found_facebook:
                                if "Username:" in line:
                                    username = line.strip()
                                if "Password:" in line:
                                    password = line.strip()
                                    result_file.write(f"{username}:{password}\n")
                                    found_facebook = False

# Main function
def main():
    root_path = input("Enter the root folder path: ")
    keyword = f"{dromin}"
    output_file = "result.txt"

    search_and_extract_credentials(root_path, keyword, output_file)
    print(f"Search completed. result saved in {output_file}")

if __name__ == "__main__":
    main()
