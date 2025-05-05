import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Resim boyutları
width, height = 512, 512

# Koordinat grid'i (polar için kartezyen başlangıç)
x = np.linspace(-15, 15, width)
y = np.linspace(-15, 15, height)
X, Y = np.meshgrid(x, y)

# Polar koordinatlar
R = np.sqrt(X**2 + Y**2)  # Radyus
Theta = np.arctan2(Y, X)  # Açı

# RGB kanalları için ifadeler
R_channel = (np.sin(4 * Theta) * np.cos(0.1 * R) + 1) / 2  # Kırmızı
G_channel = (np.cos(6 * Theta) + 1) / 2                   # Yeşil
B_channel = (np.sin(0.2 * R) + 1) / 2                     # Mavi

# RGB resmi oluşturma
image = np.zeros((height, width, 3), dtype=np.uint8)
image[:, :, 0] = R_channel * 255
image[:, :, 1] = G_channel * 255
image[:, :, 2] = B_channel * 255

# Görselleştirme
fig = plt.figure(figsize=(15, 10))

# Nihai RGB Resim
plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title("Dairesel Dalga Deseni")
plt.axis('off')

# Kırmızı kanal için 3D yüzey
ax = fig.add_subplot(2, 2, 2, projection='3d')
ax.plot_surface(X, Y, R_channel, cmap='Reds')
ax.set_title("Kırmızı Kanal 3D Yüzey")

# Yeşil kanal için 2D imshow
plt.subplot(2, 2, 3)
plt.imshow(G_channel, cmap='Greens')
plt.title("Yeşil Kanal")
plt.axis('off')

# Mavi kanal için kontur grafiği
plt.subplot(2, 2, 4)
plt.contourf(X, Y, B_channel, cmap='Blues')
plt.title("Mavi Kanal Kontur")
plt.axis('off')

plt.tight_layout()
plt.show()