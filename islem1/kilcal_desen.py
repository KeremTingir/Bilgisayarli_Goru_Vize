import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Resim boyutları
width, height = 512, 512

# Koordinat grid'i
x = np.linspace(-2, 2, width)
y = np.linspace(-2, 2, height)
X, Y = np.meshgrid(x, y)

# Kırmızı kanal: Fraktal benzeri iterasyon
def fractal_intensity(x, y, max_iter=20):
    c = x + 1j * y
    z = 0
    for i in range(max_iter):
        if abs(z) > 2:
            return i / max_iter
        z = z**2 + c
    return 1.0

R_channel = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        R_channel[i, j] = fractal_intensity(X[i, j], Y[i, j])

# Yeşil kanal: Kaotik dalga kombinasyonu
G_channel = (np.sin((X**2 / 100))**3 + np.cos((Y**2 / 100))**2 + np.sin(X * Y / 200) + 2) / 4
G_channel = np.clip(G_channel, 0, 1)  # [0, 1] aralığına sıkıştırma

# Mavi kanal: Geometrik kırılmalar ve modüler aritmetik
B_channel = np.zeros((height, width))
condition = ((X**2 + Y**2) % 100) < 50
B_channel[condition] = (np.sin(0.1 * X[condition]) + 1) / 2
B_channel[~condition] = (np.cos(0.1 * Y[~condition]) + 1) / 2

# RGB resmi oluşturma
image = np.zeros((height, width, 3), dtype=np.uint8)
image[:, :, 0] = R_channel * 255  # Kırmızı
image[:, :, 1] = G_channel * 255  # Yeşil
image[:, :, 2] = B_channel * 255  # Mavi

# Görselleştirme
fig = plt.figure(figsize=(18, 12))

# Nihai RGB Resim
plt.subplot(2, 3, 1)
plt.imshow(image)
plt.title("Kaotik Fraktal-Vari Desen")
plt.axis('off')

# Kırmızı kanal için 2D imshow
plt.subplot(2, 3, 2)
plt.imshow(R_channel, cmap='Reds')
plt.title("Kırmızı Kanal (Fraktal İterasyon)")
plt.axis('off')

# Yeşil kanal için 3D yüzey
ax = fig.add_subplot(2, 3, 3, projection='3d')
ax.plot_surface(X, Y, G_channel, cmap='Greens')
ax.set_title("Yeşil Kanal 3D Yüzey (Kaotik Dalgalar)")

# Mavi kanal için kontur grafiği
plt.subplot(2, 3, 4)
plt.contourf(X, Y, B_channel, cmap='Blues')
plt.title("Mavi Kanal Kontur (Geometrik Kırılmalar)")
plt.axis('off')

# Kırmızı kanal için kesit grafiği (y=0 boyunca)
plt.subplot(2, 3, 5)
plt.plot(x, R_channel[height//2, :], color='red')
plt.title("Kırmızı Kanal (y=0 Kesiti)")
plt.xlabel("x")
plt.ylabel("Yoğunluk")

# Yeşil kanal için kesit grafiği (x=0 boyunca)
plt.subplot(2, 3, 6)
plt.plot(y, G_channel[:, width//2], color='green')
plt.title("Yeşil Kanal (x=0 Kesiti)")
plt.xlabel("y")
plt.ylabel("Yoğunluk")

plt.tight_layout()
plt.show()