import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Resim boyutları
width, height = 512, 512

# Koordinat grid'i
x = np.linspace(-50, 50, width)
y = np.linspace(-50, 50, height)
X, Y = np.meshgrid(x, y)

# RGB kanalları için ifadeler
R_channel = (np.sin(0.1 * X)**2 + np.cos(0.1 * Y)**2) / 2
G_channel = (np.sin(0.15 * (X + Y)) + 1) / 2
B_channel = (np.cos(0.1 * X) * np.sin(0.1 * Y) + 1) / 2

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
plt.title("Kafes Deseni")
plt.axis('off')

# Mavi kanal için 3D yüzey
ax = fig.add_subplot(2, 2, 2, projection='3d')
ax.plot_surface(X, Y, B_channel, cmap='Blues')
ax.set_title("Mavi Kanal 3D Yüzey")

# Kırmızı kanal için imshow
plt.subplot(2, 2, 3)
plt.imshow(R_channel, cmap='Reds')
plt.title("Kırmızı Kanal")
plt.axis('off')

# Yeşil kanal için imshow
plt.subplot(2, 2, 4)
plt.imshow(G_channel, cmap='Greens')
plt.title("Yeşil Kanal")
plt.axis('off')

plt.tight_layout()
plt.show()