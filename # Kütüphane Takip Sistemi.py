import json  # JSON işlemleri için kütüphane

# --- Kitapları Dosyadan Yükleme ---
def kitaplari_yukle():
    try:
        with open("kitaplar.json", "r", encoding="utf-8") as f:
            kitaplar = json.load(f)  # JSON dosyasını oku, Python listesine çevir
    except FileNotFoundError:
        kitaplar = []  # Dosya yoksa boş liste oluştur
    return kitaplar

# --- Kitapları Dosyaya Kaydetme ---
def kitaplari_kaydet(kitaplar):
    with open("kitaplar.json", "w", encoding="utf-8") as f:
        json.dump(kitaplar, f, ensure_ascii=False, indent=4)  # Listeyi JSON olarak yaz

# --- Kitapları Listeleme ---
def kitaplari_listele():
    kitaplar = kitaplari_yukle()
    if not kitaplar:
        print("📚 Kütüphane boş.")
    else:
        print("\n--- Kitap Listesi ---")
        for kitap in kitaplar:
            durum = "Mevcut" if kitap["mevcut"] else "Ödünçte"
            print(f'ID: {kitap["id"]} | İsim: {kitap["isim"]} | Yazar: {kitap["yazar"]} | Durum: {durum}')

# --- Kitap Ekleme ---
def kitap_ekle():
    kitaplar = kitaplari_yukle()

    isim = input("Kitap ismi: ")
    yazar = input("Yazar ismi: ")

    yeni_id = max([kitap["id"] for kitap in kitaplar]) + 1 if kitaplar else 1

    yeni_kitap = {
        "id": yeni_id,
        "isim": isim,
        "yazar": yazar,
        "mevcut": True
    }

    kitaplar.append(yeni_kitap)
    kitaplari_kaydet(kitaplar)

    print(f'✅ "{isim}" kitabı eklendi.')

# --- Ana Menü ---
def menu():
    while True:
        print("\n--- Kütüphane Sistemi ---")
        print("1. Kitapları Listele")
        print("2. Kitap Ekle")
        print("3. Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            kitaplari_listele()
        elif secim == "2":
            kitap_ekle()
        elif secim == "3":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")

# --- Program Başlatma ---
if __name__ == "__main__":
    menu()
