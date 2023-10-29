label start:

    "Oyunun dilini seçin."
    menu:
        "Türkçe":
            $ renpy.config.language = "turkisgscript.rpy"
    play music "music/background_music.ogg"  # Müziği başlat
    scene bg_room  # Arka planı değiştir
    "Bir şifreli kapı önündesiniz. Kapıyı açmak için bir şifre gerekiyor."
    $ _input = renpy.input("Şifreyi girin:")
    
    if _input == "1234":
        "Doğru şifre! Kapıyı açtınız."
    else:
        "Yanlış şifre. Tekrar deneyin."
        jump start

