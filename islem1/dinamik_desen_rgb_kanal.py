import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Resim boyutları
width, height = 512, 512

# Koordinat grid'i
x = np.linspace(-10, 10, width)
y = np.linspace(-10, 10, height)
X, Y = np.meshgrid(x, y)

# Kırmızı kanal: Kaotik trigonometri (sinüs-kosinüs karışımı)
R_channel = (np.sin(3 * X**2 - Y**2) * np.cos(2 * Y) + 1) / 2
R_channel = np.clip(R_channel, 0, 1)

# Yeşil kanal: Fraktal benzeri spiral izler (polar koordinatlara dayalı)
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)
G_channel = (np.sin(R * 3 + Theta * 5) + 1) / 2

# Mavi kanal: Modüler dalgalar (parabolik + modüler yapı)
mod_pattern = ((np.floor((X**2 + Y**2) % 8)) / 8.0)
wave = np.abs(np.sin(X * Y * 0.1))
B_channel = (mod_pattern * wave + 0.2) % 1.0

# RGB resmi oluşturma
image = np.zeros((height, width, 3), dtype=np.uint8)
image[:, :, 0] = (R_channel * 255).astype(np.uint8)
image[:, :, 1] = (G_channel * 255).astype(np.uint8)
image[:, :, 2] = (B_channel * 255).astype(np.uint8)

# Görselleştirme
fig = plt.figure(figsize=(18, 12))

# Nihai RGB Resim
plt.subplot(2, 3, 1)
plt.imshow(image)
plt.title("Kaotik Trigonometri ve Fraktal Spiral Haritalar")
plt.axis('off')

# Kırmızı kanal 2D imshow
plt.subplot(2, 3, 2)
plt.imshow(R_channel, cmap='Reds')
plt.title("Kırmızı Kanal (Kaotik Trigonometrik Alan)")
plt.axis('off')

# Yeşil kanal 3D spiral yüzey
ax = fig.add_subplot(2, 3, 3, projection='3d')
ax.plot_surface(X, Y, G_channel, cmap='Greens', linewidth=0, antialiased=False)
ax.set_title("Yeşil Kanal (Spiral Fraktal Yüzey)")

# Mavi kanal kontur
plt.subplot(2, 3, 4)
plt.contourf(X, Y, B_channel, levels=15, cmap='Blues')
plt.title("Mavi Kanal (Modüler Dalgalar)")
plt.axis('off')

# Kırmızı kanal kesit grafiği (x=0)
plt.subplot(2, 3, 5)
plt.plot(y, R_channel[:, width // 2], color='red')
plt.title("Kırmızı Kanal Kesiti (x=0)")
plt.xlabel("y")
plt.ylabel("Yoğunluk")

# Yeşil kanal kesit grafiği (y=0)
plt.subplot(2, 3, 6)
plt.plot(x, G_channel[height // 2, :], color='green')
plt.title("Yeşil Kanal Kesiti (y=0)")
plt.xlabel("x")
plt.ylabel("Yoğunluk")

plt.tight_layout()
plt.show()
