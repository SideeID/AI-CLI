import requests
from colorama import Fore, Style, init

init(autoreset=True)

def process_request(prompt, mode):
    if mode == 'translate':
        prompt = f"Terjemahkan teks berikut ke Bahasa Inggris tetapi jika sudah dalam Bahasa Inggris, terjemahkan ke Bahasa Indonesia: {prompt}"
    elif mode == 'summarize':
        prompt = f"Ringkas teks berikut: {prompt}"
    elif mode == 'code':
        prompt = f"Tulis kode untuk permintaan berikut: {prompt}"
    elif mode == 'tsundere':
        prompt = f"Jangan lupa untuk meminta dengan sopan: {prompt}"

    payload = {
        "messages": [
            {"role": "system", "content": "Nama Anda adalah Dimas AI dan Anda adalah asisten virtual saya."},
            {"role": "user", "content": prompt}
        ]
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(
            "https://api.zpi.my.id/v1/ai/gpt-4-turbo", 
            json=payload, 
            headers=headers
        )
        if response.status_code == 200:
            result = response.json()
            ai_response = result['data']['choices']['content']
            print(f"\n{Fore.CYAN}{ai_response}{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.RED}Kesalahan API: {response.status_code}\n{response.text}{Style.RESET_ALL}")
    except requests.RequestException as e:
        print(f"{Fore.RED}Kesalahan dalam mengirim permintaan: {e}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Kesalahan tidak terduga: {e}{Style.RESET_ALL}")