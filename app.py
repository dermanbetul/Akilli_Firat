import random

# -------------------------------------------------------------
# Akıllı Nesne Tahminleyici
# -------------------------------------------------------------

OBJECTS = [
    {
        "name": "telefon",
        "features": {
            "elektronik": True,
            "tasinabilir": True,
            "canli": False,
            "ev_icinde": True,
            "giyilebilir": False,
            "iletişim": True,
            "ucabilir": False,
            "oyuncak": False,
            "sivi": False,
            "hareket_eder": False,
        },
    },
    {
        "name": "bilgisayar",
        "features": {
            "elektronik": True,
            "tasinabilir": True,
            "canli": False,
            "ev_icinde": True,
            "giyilebilir": False,
            "iletişim": False,
            "ucabilir": False,
            "oyuncak": False,
            "sivi": False,
            "hareket_eder": False,
        },
    },
    {
        "name": "kitap",
        "features": {
            "elektronik": False,
            "tasinabilir": True,
            "canli": False,
            "ev_icinde": True,
            "giyilebilir": False,
            "iletişim": False,
            "ucabilir": False,
            "oyuncak": False,
            "sivi": False,
            "hareket_eder": False,
        },
    },
    {
        "name": "kalem",
        "features": {
            "elektronik": False,
            "tasinabilir": True,
            "canli": False,
            "ev_icinde": True,
            "giyilebilir": False,
            "iletişim": False,
            "ucabilir": False,
            "oyuncak": False,
            "sivi": False,
            "hareket_eder": False,
        },
    },
    {
        "name": "anahtar",
        "features": {
            "elektronik": False,
            "tasinabilir": True,
            "canli": False,
            "ev_icinde": True,
            "giyilebilir": False,
            "iletişim": False,
            "ucabilir": False,
            "oyuncak": False,
            "sivi": False,
            "hareket_eder": False,
        },
    },
    {
        "name": "kedi",
        "features": {
            "elektronik": False,
            "tasinabilir": False,
            "canli": True,
            "ev_icinde": True,
            "giyilebilir": False,
            "iletişim": False,
            "ucabilir": False,
            "oyuncak": False,
            "sivi": False,
            "hareket_eder": True,
        },
    },
    {
        "name": "köpek",
        "features": {
            "elektronik": False,
            "tasinabilir": False,
            "canli": True,
            "ev_icinde": True,
            "giyilebilir": False,
            "iletişim": False,
            "ucabilir": False,
            "oyuncak": False,
            "sivi": False,
            "hareket_eder": True,
        },
    },
    {
        "name": "uçak",
        "features": {
            "elektronik": True,
            "tasinabilir": False,
            "canli": False,
            "ev_icinde": False,
            "giyilebilir": False,
            "iletişim": False,
            "ucabilir": True,
            "oyuncak": False,
            "sivi": False,
            "hareket_eder": True,
        },
    },
    {
        "name": "araba",
        "features": {
            "elektronik": True,
            "tasinabilir": False,
            "canli": False,
            "ev_icinde": False,
            "giyilebilir": False,
            "iletişim": False,
            "ucabilir": False,
            "oyuncak": False,
            "sivi": False,
            "hareket_eder": True,
        },
    },
    {
        "name": "top",
        "features": {
            "elektronik": False,
            "tasinabilir": True,
            "canli": False,
            "ev_icinde": True,
            "giyilebilir": False,
            "iletişim": False,
            "ucabilir": False,
            "oyuncak": True,
            "sivi": False,
            "hareket_eder": False,
        },
    },
    {
        "name": "bardak",
        "features": {
            "elektronik": False,
            "tasinabilir": True,
            "canli": False,
            "ev_icinde": True,
            "giyilebilir": False,
            "iletişim": False,
            "ucabilir": False,
            "oyuncak": False,
            "sivi": True,
            "hareket_eder": False,
        },
    },
    {
        "name": "elbise",
        "features": {
            "elektronik": False,
            "tasinabilir": True,
            "canli": False,
            "ev_icinde": True,
            "giyilebilir": True,
            "iletişim": False,
            "ucabilir": False,
            "oyuncak": False,
            "sivi": False,
            "hareket_eder": False,
        },
    },
    {
        "name": "saat",
        "features": {
            "elektronik": True,
            "tasinabilir": True,
            "canli": False,
            "ev_icinde": True,
            "giyilebilir": False,
            "iletişim": False,
            "ucabilir": False,
            "oyuncak": False,
            "sivi": False,
            "hareket_eder": False,
        },
    },
    {
        "name": "fincan",
        "features": {
            "elektronik": False,
            "tasinabilir": True,
            "canli": False,
            "ev_icinde": True,
            "giyilebilir": False,
            "iletişim": False,
            "ucabilir": False,
            "oyuncak": False,
            "sivi": True,
            "hareket_eder": False,
        },
    },
    {
        "name": "masa",
        "features": {
            "elektronik": False,
            "tasinabilir": False,
            "canli": False,
            "ev_icinde": True,
            "giyilebilir": False,
            "iletişim": False,
            "ucabilir": False,
            "oyuncak": False,
            "sivi": False,
            "hareket_eder": False,
        },
    },
]

QUESTIONS = [
    ("canli", "Canlı bir varlık mı?"),
    ("elektronik", "Elektronik bir nesne mi?"),
    ("tasinabilir", "Taşınabilir mi?"),
    ("ev_icinde", "Evde / çevrede daha çok kullanılır mı?"),
    ("giyilebilir", "Giyilebilir bir şey mi?"),
    ("sivi", "Sıvı taşıyan bir nesne mi?"),
    ("oyuncak", "Oyun amaçlı mı?"),
    ("ucabilir", "Uçabilir mi?"),
    ("hareket_eder", "Kendi hareketiyle yer değiştirebilir mi?"),
    ("iletişim", "İletişim / çağrı / mesaj için kullanılır mı?"),
]


def print_banner():
    print("\n" + "=" * 60)
    print("       🤔 AKILLI NESNE TAHMİNLEYİCİ 🧠")
    print("=" * 60)
    print("Aklında bir nesne tut. Ben sana birkaç soru sorup onu bulacağım!\n")


def ask_yes_no(question):
    while True:
        answer = input(f"{question} (e/h): ").strip().lower()
        if answer in {"e", "evet", "y", "yes"}:
            return True
        if answer in {"h", "hayır", "n", "no"}:
            return False
        print("Lütfen sadece 'e' veya 'h' yaz. 😊")


def pick_best_question(candidates):
    best = None
    best_score = -1
    for key, text in QUESTIONS:
        yes_count = sum(1 for obj in candidates if obj["features"].get(key, False))
        no_count = len(candidates) - yes_count
        score = abs(yes_count - no_count)
        if score > best_score:
            best_score = score
            best = (key, text)
    return best


def filter_candidates(candidates, key, answer):
    return [obj for obj in candidates if obj["features"].get(key, False) == answer]


def show_options(options):
    for idx, item in enumerate(options, start=1):
        print(f"  {idx}. {item['name']}")


def guess_final(candidates):
    if len(candidates) == 1:
        return candidates[0]["name"]
    if not candidates:
        return None

    print("\nŞu seçeneklerden biri olabilir: ")
    show_options(candidates)
    while True:
        try:
            choice = int(input("Hangisi senin aklındaki nesne? (numara yaz): ").strip())
            if 1 <= choice <= len(candidates):
                return candidates[choice - 1]["name"]
        except ValueError:
            pass
        print("Geçersiz numara, tekrar deneyin. 😅")


def game_loop():
    print_banner()
    print("İstersen başlatayım. Aklında bir nesne tut, ben sana birkaç soru soracağım.\n")

    while True:
        candidates = OBJECTS[:]
        print("1. Oyun başlasın")
        print("2. Neler olabilir, bir bak")
        print("3. Çıkış")
        mode = input("Seçimin: ").strip()

        if mode == "3":
            print("\nYine görüşürüz. Güzel düşüncelerle! 👋")
            return

        if mode == "2":
            print("\nBulabileceğim nesneler: ")
            show_options(OBJECTS)
            print()
            continue

        if mode not in {"1"}:
            print("Geçersiz seçenek. Tekrar dene. 😊")
            continue

        print("\nHarika! Aklında bir nesne tut, ben tahmin etmeye çalışayım.\n")

        while len(candidates) > 1:
            key, question = pick_best_question(candidates)
            answer = ask_yes_no(question)
            candidates = filter_candidates(candidates, key, answer)

            if not candidates:
                print("Hmm ... bazı bilgileri çelişiyor gibi görünüyor. 😮")
                break

            if len(candidates) == 1:
                break

            print(f"\nŞu an {len(candidates)} olasılık kaldı. Devam ediyorum...\n")

        guessed = guess_final(candidates)

        if guessed is None:
            print("\nAklındaki nesne listemde görünmüyor. Ama senin için bir tane ekleyeyim mi? 🧩")
            custom_name = input("Nesnenin adını yaz: ").strip().title()
            if custom_name:
                print(f"O zaman senin nesnen {custom_name} olmalı! Harika bir seçim. ✨")
            else:
                print("Bir isim yazmadın ama tahminim yine de çok eğlenceliydi. 😄")
        else:
            print(f"\nTahminim: {guessed.upper()}! Benim tahminim doğru mu? 😄")
            confirmation = input("(e/h): ").strip().lower()
            if confirmation in {"e", "evet", "y", "yes"}:
                print("Yuhuuu! Buldum! 🏆")
            else:
                print("Aman, bir dahaki sefere daha iyi tahmin edeceğim. 😎")
                print("Benim son tahminim: ", guessed)

        print("\nTekrar oynamak ister misin?")
        again = input("(e/h): ").strip().lower()
        if again not in {"e", "evet", "y", "yes"}:
            print("\nİyi oyunlar! Görüşmek üzere. 👋")
            return

        print("\nYeniden başlatıyorum...\n")


if __name__ == "__main__":
    random.seed()
    game_loop()
