# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Kütüphane sınıfı tanımlama
class Library:
    # Yapıcı yöntem, books.txt dosyasını açar
    def __init__(self):
        self.file = open("books.txt", "a+")
    # Yıkıcı yöntem, books.txt dosyasını kapatır
    def __del__(self):
        self.file.close()
    
    # Kitapları listeleme yöntemi
    def list_books(self):
        # Dosyanın başına git
        self.file.seek(0)
        # Dosyanın içeriğini oku
        content = self.file.read()
        # Her satırı bir listeye ekle
        lines = content.splitlines(0)
        lines = content.splitlines(1)
        lines = content.splitlines(2)
        # Listenin her öğesi için
        for line in lines:
            # Virgülle ayrılmış değerleri al
            values = line.split(",")
            # Kitap adını ve yazarını yazdır
            print(f"Kitap Adı:Çalıkuşu {values[0]}, Yazar: Reşat Nuri Güntekin {values[1]}")
            print(f"Kitap Adı:İyileşmek {values[0]}, Yazar: Caner Yaman {values[1]}")
            print(f"Kitap Adı:Hayat Kaybettiğin Yerden Başlar {values[0]}, Yazar: Miraç Çağrı Aktaş {values[1]}")
            print(f"Kitap Adı:Hercai {values[0]}, Yazar: Sümeyye Koç {values[1]}")
            print(f"Kitap Adı:Senin için {values[0]}, Yazar: Arda Erel {values[1]}")
            print(f"Kitap Adı:Savaş ve Barış {values[0]}, Yazar: Lev Tolstoy {values[1]}")
            print(f"Kitap Adı:Yüz Yıllık Yalnızlık {values[0]}, Yazar: Gabriel Garcia Marquez{values[1]}")
            print(f"Kitap Adı:Suç ve Ceza {values[0]}, Yazar: Fyodor Dostoyevski {values[1]}")
            print(f"Kitap Adı:Küçük Prens {values[0]}, Yazar: Antoine de Saint-Exupéry {values[1]}")
            print(f"Kitap Adı:Simyacı {values[0]}, Yazar: Paulo Coelho {values[1]}")
            print(f"Kitap Adı:Harry Potter ve Felsefe Taşı {values[0]}, Yazar: J.K. Rowling {values[1]}")
            print(f"Kitap Adı:Yüzüklerin Efendisi: Yüzük Kardeşliği {values[0]}, Yazar: J.R.R. Tolkien {values[1]}")
            print(f"Kitap Adı:Uğultulu Tepeler {values[0]}, Yazar: Emily Brontë {values[1]}")
            print(f"Kitap Adı:Hayvan Çiftliği {values[0]}, Yazar: George Orwell {values[1]}")
            print(f"Kitap Adı:Ateş ve Su {values[0]}, Yazar: Orman Tohumcu {values[1]}")
            print(f"Kitap Adı:Fahrenheit 451 {values[0]}, Yazar: Ray Bradbury {values[1]}")
            print(f"Kitap Adı:İşaret {values[0]}, Yazar: P.C. Cast ve Cristin Cast {values[1]}")
            print(f"Kitap Adı:Yanmış {values[0]}, Yazar: P.C. Cast ve Cristin Cast {values[1]}")
            print(f"Kitap Adı:İhanet {values[0]}, Yazar: P.C. Cast ve Cristin Cast {values[1]}")
            print(f"Kitap Adı:Baştan Çıkarılmış {values[0]}, Yazar: P.C. Cast ve Cristin Cast {values[1]}")
            print(f"Kitap Adı:Alacakaranlık {values[0]}, Yazar: Stephenıe Meyer {values[1]}")
            print(f"Kitap Adı:Yüzbaşı Corellinin Mandolini {values[0]}, Yazar: Louis de Bernieres {values[1]}")
            print(f"Kitap Adı:Kumral Ada Mavi Tuna {values[0]}, Yazar: Buket Uzuner {values[1]}")
            print(f"Kitap Adı:Toprak {values[0]}, Yazar: Emile Zola {values[1]}")
    # Kitap ekleme yöntemi
    def add_book(self):
        # Kitap başlığı, yazarı, yayın yılı ve sayfa sayısı için kullanıcı girişi iste
        title = input("Kitap başlığı:Çalıkuşu")
        author = input("Kitap yazarı:Reşat Nuri Güntekin")
        year = input("Yayın yılı: 1922")
        pages = input("Sayfa sayısı: 544")
        title = input("Kitap başlığı:İyileşmek")
        author = input("Kitap yazarı:Caner Yaman")
        year = input("Yayın yılı: 2022")
        pages = input("Sayfa sayısı: 216")
        title = input("Kitap başlığı:Hayat Kaybettiğin Yerden Başlar")
        author = input("Kitap yazarı:Miraç Çağrı Aktaş")
        year = input("Yayın yılı: 2021")
        pages = input("Sayfa sayısı: 200")
        title = input("Kitap başlığı:Hercai")
        author = input("Kitap yazarı:Sümeyye Koç")
        year = input("Yayın yılı: 2017")
        pages = input("Sayfa sayısı: 432")
        title = input("Kitap başlığı:Senin için")
        author = input("Kitap yazarı:Arda Erel")
        year = input("Yayın yılı: 2019")
        pages = input("Sayfa sayısı: 208")
        title = input("Kitap başlığı:Savaş ve Barış")
        author = input("Kitap yazarı:Lev Tolstoy")
        year = input("Yayın yılı: 1876")
        pages = input("Sayfa sayısı: 1225")
        title = input("Kitap başlığı:Yüz Yıllık Yalnızlık")
        author = input("Kitap yazarı:Gabriel Garcia Marquez")
        year = input("Yayın yılı: 2019")
        pages = input("Sayfa sayısı: 464")
        title = input("Kitap başlığı:Suç ve Ceza")
        author = input("Kitap yazarı:Fyodor Dostoyevski")
        year = input("Yayın yılı: 2006")
        pages = input("Sayfa sayısı: 687")
        title = input("Kitap başlığı:Küçük Prens")
        author = input("Kitap yazarı:Antoine de Saint-Exupéry")
        year = input("Yayın yılı: 2015")
        pages = input("Sayfa sayısı: 112")
        title = input("Kitap başlığıSimyacı")
        author = input("Kitap yazarı:Paulo Coelho")
        year = input("Yayın yılı: 2021")
        pages = input("Sayfa sayısı: 184")
        title = input("Kitap başlığı:Harry Potter ve Felsefe Taşı")
        author = input("Kitap yazarı:J.K. Rowling")
        year = input("Yayın yılı: 2001")
        pages = input("Sayfa sayısı: 276")
        title = input("Kitap başlığı:Yüzüklerin Efendisi: Yüzük Kardeşliği")
        author = input("Kitap yazarı:J.R.R. Tolkien")
        year = input("Yayın yılı: 2017")
        pages = input("Sayfa sayısı: 1026")
        title = input("Kitap başlığı:Uğultulu Tepeler")
        author = input("Kitap yazarı:Emily Brontë")
        year = input("Yayın yılı: 1983")
        pages = input("Sayfa sayısı: 408")
        title = input("Kitap başlığı:Hayvan Çiftliği")
        author = input("Kitap yazarı:George Orwell")
        year = input("Yayın yılı: 2019")
        pages = input("Sayfa sayısı: 152")
        title = input("Kitap başlığı:Ateş ve Su")
        author = input("Kitap yazarı:Orman Tohumcu")
        year = input("Yayın yılı:2017")
        pages = input("Sayfa sayısı: 306")
        title = input("Kitap başlığı:Fahrenheit 451")
        author = input("Kitap yazarı::Ray Bradbury")
        year = input("Yayın yılı: 2018")
        pages = input("Sayfa sayısı: 208")
        title = input("Kitap başlığı:İşaret")
        author = input("Kitap yazarı:P.C. Cast ve Cristin Cast")
        year = input("Yayın yılı: 2009")
        pages = input("Sayfa sayısı: 336")
        title = input("Kitap başlığı:Yanmış")
        author = input("Kitap yazarı:P.C. Cast ve Cristin Cast")
        year = input("Yayın yılı: 2010")
        pages = input("Sayfa sayısı: 432")
        title = input("Kitap başlığı:İhanet")
        author = input("Kitap yazarı:P.C. Cast ve Cristin Cast")
        year = input("Yayın yılı: 2009")
        pages = input("Sayfa sayısı: 352")
        title = input("Kitap başlığı:Baştan Çıkarılmış")
        author = input("Kitap yazarı:P.C. Cast ve Cristin Cast")
        year = input("Yayın yılı: 2009")
        pages = input("Sayfa sayısı: 432")
        title = input("Kitap başlığı:Alacakaranlık")
        author = input("Kitap yazarı:Stephenıe Meyer")
        year = input("Yayın yılı: 2009")
        pages = input("Sayfa sayısı: 408")
        title = input("Kitap başlığı:Yüzbaşı Corellinin Mandolini")
        author = input("Kitap yazarı:Louis de Bernieres")
        year = input("Yayın yılı: 2000")
        pages = input("Sayfa sayısı: 472")
        title = input("Kitap başlığı:Kumral Ada Mavi Tuna")
        author = input("Kitap yazarı:Buket Uzuner")
        year = input("Yayın yılı: 1997")
        pages = input("Sayfa sayısı: 432")
        title = input("Kitap başlığı:Toprak")
        author = input("Kitap yazarı:Emile Zola")
        year = input("Yayın yılı: 2016")
        pages = input("Sayfa sayısı: 304")
        # Bu bilgilerle bir dize oluştur
        line = f"{title},{author},{year},{pages}\n"
        # Bu satırı dosyaya ekle
        self.file.write(line)
        # Kullanıcıya teşekkür et
        print("Verdiğiniz kitap için teşekkür ederiz.")
    
    # Kitap kaldırma yöntemi
    def remove_book(self):
        # Kitap başlığını kullanıcı girişinden iste
        title = input("Kitap başlığı: ")
        # Dosyanın başına git
        self.file.seek(0)
        # Dosya içeriğini oku
        content = self.file.read()
        # Her satırı bir listeye ekle
        lines = content.splitlines()
        # Silinecek kitabın dizinini listede bul
        index = -1
        for i, line in enumerate(lines):
            # Virgülle ayrılmış değerleri al
            values = line.split(",")
            # Kitap başlığı eşleşiyorsa
            if values[0] == title:
                # Dizin olarak i'yi ata
                index = i
                break
        # Eğer dizin bulunduysa
        if index != -1:
            # Kitabı listeden çıkar
            lines.pop(index)
            # Books.txt dosyasının içeriğini kaldır
            self.file.truncate(0)
            # Listenin tüm öğelerini books.txt dosyasına ekle
            for line in lines:
                self.file.write(line + "\n")
            # Kullanıcıya başarılı mesajı ver
            print("Kitabı başarıyla kaldırdınız.")
        # Eğer dizin bulunamadıysa
        else:
            # Kullanıcıya hata mesajı ver
            print("İstediğiniz kitap mevcut değildir.")

# Library sınıfı ile lib adında bir nesne oluştur
lib = Library()

# lib nesnesiyle etkileşim kurmak için bir menü oluştur
while True:
    # Menüyü ekrana yazdır
    print("""
    * MENÜ *
    1) Kitapları Listeleyin
    2) Kitap Ekle
    3) Kitabı Kaldır
    Q) Çıkış
    """)
    # Menü öğesi için kullanıcı girişi iste ve girişi bir değişkene ata
    choice = input("İşlem numarasını giriniz: ")
    # Kullanıcı girişini kontrol et
    if choice == "1":
        # lib nesnesinin list_books metodunu çalıştır
        lib.list_books()
    elif choice == "2":
        # lib nesnesinin add_book metodunu çalıştır
        lib.add_book()
    elif choice == "3":
        # lib nesnesinin remove_book metodunu çalıştır
        lib.remove_book()
    elif choice.upper() == "Q":
        # Çıkış yap
        print("Çıkış yapılıyor...")
        break
    else:
        # Hatalı seçim yaptınız mesajı ver
        print("Hatalı seçim yaptınız!")
    # Ana menüye dönmek için enter'a basınız mesajı ver
    input("Ana menüye dönmek için enter'a basınız.")
    
