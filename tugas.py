import requests
from bs4 import BeautifulSoup
import json

# URL Target
url = "https://informatika.umsida.ac.id/pembekalan-calon-asisten-laboratorium-teknik-informatika-umsida-perkuat-pemahaman-dasar-jaringan/"

# Headers agar tidak diblokir
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Cek jika koneksi gagal
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # 1. Ambil Judul (Gunakan pencarian yang lebih umum)
    judul_tag = soup.find('h1')
    judul = judul_tag.get_text(strip=True) if judul_tag else "Judul tidak ditemukan"

    # 2. Ambil Isi Konten (Gunakan selector yang lebih luas jika class spesifik gagal)
    # Kita coba cari di 'article' atau 'div' yang umum digunakan WordPress
    konten_div = soup.find('div', class_='entry-content') or soup.find('article') or soup.find('main')

    if konten_div:
        isi_teks = konten_div.get_text(separator=" ", strip=True)
    else:
        isi_teks = "Konten berita tidak ditemukan"

    # 3. Susun Data
    data_hasil = {
        "sumber": url,
        "judul_artikel": judul,
        "isi_konten": isi_teks
    }

    # 4. Simpan ke JSON
    with open('hasil_scraping.json', 'w', encoding='utf-8') as f:
        json.dump(data_hasil, f, indent=4, ensure_ascii=False)

    print("✅ Berhasil! Cek file hasil_scraping.json di folder C:\latihan")

except Exception as e:
    print(f"❌ Terjadi kesalahan: {e}")