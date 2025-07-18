import requests
import re
from urllib.parse import urljoin

BASE_URL = "https://www.temu.com/"

def get_js_files():
    print("[*] Obteniendo archivos JS desde el HTML principal...")
    res = requests.get(BASE_URL)
    scripts = re.findall(r'src="(.*?\.js)"', res.text)
    js_urls = [urljoin(BASE_URL, s) for s in scripts if "http" not in s]
    return js_urls

def scan_for_leaks(js_urls):
    print("[*] Buscando patrones sensibles en JS...")
    patterns = ["token", "auth", "redirect", "session", "api_key", "jwt"]
    for url in js_urls:
        try:
            r = requests.get(url, timeout=10)
            for p in patterns:
                if p in r.text:
                    print(f"[!] Posible fuga encontrada en {url} → patrón: {p}")
        except Exception as e:
            print(f"[x] Error al escanear {url}: {e}")

if __name__ == "__main__":
    js_files = get_js_files()
    scan_for_leaks(js_files)


