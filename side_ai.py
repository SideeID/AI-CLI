import click
from prompt_toolkit import PromptSession
from prompt_toolkit.validation import ValidationError
from colorama import Fore, Style, init
from api_service import process_request

init(autoreset=True)

@click.command(help="CLI sederhana untuk mengakses LLM. Gunakan --help untuk melihat opsi.")
@click.option('--loop', is_flag=True, help="Aktifkan mode percakapan terus-menerus.")
@click.option('--mode', type=click.Choice(['default', 'translate', 'summarize', 'code', 'tsundere'], case_sensitive=False), default='default', help="Pilih mode kerja.")
def sendRequest(loop, mode):
    def get_multiline_input():
        session = PromptSession()
        try:
            prompt = session.prompt("Apa yang bisa saya bantu tuan?\n")
            return prompt
        except ValidationError:
            print(f"{Fore.YELLOW}Masukan tidak valid. Silakan coba lagi.{Style.RESET_ALL}")
            return get_multiline_input()

    if loop:
        print(f"{Fore.GREEN}Mode loop diaktifkan. Ketik 'exit' untuk keluar.{Style.RESET_ALL}\n")
        while True:
            prompt = get_multiline_input()
            if prompt.lower() in ['exit', 'keluar']:
                print(f"{Fore.GREEN}Terima kasih! Sampai jumpa!{Style.RESET_ALL}")
                break
            process_request(prompt, mode)
    else:
        prompt = get_multiline_input()
        process_request(prompt, mode)

if __name__ == '__main__':
    sendRequest()
