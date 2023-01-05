import openai
import random
from configparser import ConfigParser
from rich.console import Console
import colorama
from colorama import Fore, Back, Style, init
init()

console = Console()

dbconf = ConfigParser()
dbconf.read_file(open("config.ini"))

print("")
print(Fore.LIGHTGREEN_EX, Style.BRIGHT + "Welcome ChatGPT-OpenAI by X48-Python.EXE\n" + Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "This is a little program to help someone use ChatGPT without web browser\n" + Style.RESET_ALL)
promptpay_donate = 'Buy Me a Coffee : PromptPay : 095-518-8528'
print(Fore.LIGHTYELLOW_EX, Style.BRIGHT + promptpay_donate + Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX, Style.BRIGHT + 'Thanks For Support' + Style.RESET_ALL)
print('---------------------------------------------------------------------------------')
print('██   ██ ██   ██  █████   ██ ███████  ██  ██████  ██████  ██████  ██   ██ ██████ ')
print(' ██ ██  ██   ██ ██   ██ ███ ██      ███ ██            ██      ██ ██   ██      ██')
print('  ███   ███████  █████   ██ ███████  ██ ███████   █████   █████  ███████  █████ ')
print(' ██ ██       ██ ██   ██  ██      ██  ██ ██    ██ ██           ██      ██ ██     ')
print('██   ██      ██  █████   ██ ███████  ██  ██████  ███████ ██████       ██ ███████')
print('---------------------------------------------------------------------------------')
print(Fore.YELLOW + '')
print(" ██████╗██╗  ██╗ █████╗ ████████╗    ██████╗ ██████╗ ████████╗")
print("██╔════╝██║  ██║██╔══██╗╚══██╔══╝   ██╔════╝ ██╔══██╗╚══██╔══╝")
print("██║     ███████║███████║   ██║█████╗██║  ███╗██████╔╝   ██║   ")
print("██║     ██╔══██║██╔══██║   ██║╚════╝██║   ██║██╔═══╝    ██║   ")
print("╚██████╗██║  ██║██║  ██║   ██║      ╚██████╔╝██║        ██║   ")
print(" ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═════╝ ╚═╝        ╚═╝   ")
print(Style.RESET_ALL + '')
print('---------------------------------------------------------------------------------')
print(Fore.BLUE, Style.BRIGHT + 'If You Found Some Bug Please Contact My Developer Master >> Here Line ID : x4815x')
print(Style.RESET_ALL)

# Set the OpenAI API key
openai.api_key = dbconf.get("SETTING","API_KEY")
#print("\n")

def main():
    # Set the prompt that the ChatGPT model will use to generate responses
    prompt = console.input("\n[bold white3]>>> Enter TEXT Prompt or Some Question : \n")
    print(Fore.LIGHTBLUE_EX, Style.DIM + "\nPlease Wait The Anwser >>>")

    # Use the OpenAI `Completion` API to generate responses to the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
    )

    # Print the generated responses
    for i, response in enumerate(response.choices[0].text.split("\n")):
        print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "")
        print(f"{response}")
    #print

if __name__ == "__main__":
    while True:
        try:
            main()
            print(Style.RESET_ALL)
        except:
            print(Fore.YELLOW, Style.BRIGHT, Back.RED + "Master !!!!! Please Check API Form OpenAi Website and Try Again" + Style.RESET_ALL)
            print(Style.RESET_ALL)
        continue
