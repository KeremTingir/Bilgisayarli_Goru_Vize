# Bilgisayarlı Görü Ödevi

Bu repositori, **Ondokuz Mayıs Üniversitesi Bilgisayar Mühendisliği Bölümü** Bilgisayarlı Görü dersi kapsamında **2024-2025 Bahar Dönemi** için hazırlanan ödev projesini içermektedir.  
Proje, iki ana işlemden oluşmaktadır:

- **İşlem 1:** Matematiksel ifadelerle yapay RGB resimler oluşturma  
- **İşlem 2:** Bir RGB resmin 3x3 parçaya bölünerek interaktif bir jigsaw bulmacası haline getirilmesi

Tüm işlemler Python programlama dili ile **NumPy**, **Matplotlib**, **OpenCV**, **Tkinter** ve **Pillow** kütüphaneleri kullanılarak gerçekleştirilmiştir.

---

## 📁 Proje Yapısı

### `images/`

- **Üretilen resimler:** Dairesel dalga, spiral ve vorteks, kafes, kaotik fraktal ve dinamik desenlere ait görseller.
- **Dinamik desen videosu:** Zamanla evrilen kaotik desenin animasyonu (`Dinamik_desen_videosu.mp4` veya ilgili dosya adı).
- **Jigsaw bulmacası resmi:** İşlem 2’de kullanılan örnek RGB resim.

### `islem1/`

İşlem 1’e ait kaynak kodların bulunduğu klasördür. Beş farklı yapay RGB resmi üretmek için gerekli Python script’lerini içerir:

- `dairesel_dalga_deseni.py`: Dairesel dalga deseni oluşturur.
- `spiral_deseni.py`: Spiral ve vorteks deseni oluşturur.
- `kafes_deseni.py`: Kafes deseni oluşturur.
- `kilcal_desen.py`: Kaotik fraktal desen oluşturur.
- `dinamik_desen.py`: Zaman parametreli dinamik desen oluşturur.

### `islem2/`

İşlem 2’ye ait kaynak kodların bulunduğu klasördür. 3x3 jigsaw bulmacasını interaktif bir grafik arayüz (GUI) ile sunan Python script’ini içerir:

- `odev.py`: Jigsaw bulmacası GUI’sini ve etkileşim mekanizmalarını içerir.

---

## 🖼️ Görseller

- **Yapay RGB Resimler**: `images/` klasöründe her desene ait nihai RGB resimler ve kanal grafikleri (örneğin, 3D yüzey grafikleri, kontur grafikleri, kesit grafikleri) bulunmaktadır.
- **Dinamik Desen**: Animasyonlu desenin videosu `images/Dinamik_desen_videosu.mp4` olarak saklanmıştır.
- **Jigsaw Bulmacası**: `images/` klasöründeki puzzle.jpeg, İşlem 2’de bulmacada kullanılan varsayılan görüntüdür.
