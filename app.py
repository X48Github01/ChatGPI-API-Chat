import random
from configparser import ConfigParser

import colorama
import openai
from colorama import Back, Fore, Style, init
from rich.console import Console

init()

console = Console()

dbconf = ConfigParser()
dbconf.read_file(open("config.ini"))

# Set the OpenAI API key
openai.api_key = dbconf.get("SETTING", "API_KEY")
print("\n")


def main():
    # Set the prompt that the ChatGPT model will use to generate responses
    prompt = console.input(
        "\n[bold white3]Enter TEXT Prompt (use '\ n' for other prompt) : \n"
    )

    # Use the OpenAI `Completion` API to generate responses to the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
    )

    # Print the generated responses
    for i, response in enumerate(response.choices[0].text.split("\n")):
        print(Fore.LIGHTGREEN_EX, Style.BRIGHT, f"{response}", Style.RESET_ALL)


if __name__ == "__main__":
    while True:
        main()
        continue
