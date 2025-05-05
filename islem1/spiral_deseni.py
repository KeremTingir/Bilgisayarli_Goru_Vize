import numpy as np
import matplotlib.pyplot as plt

# Resim boyutları
width, height = 512, 512

# Koordinat grid'i
x = np.linspace(-20, 20, width)
y = np.linspace(-20, 20, height)
X, Y = np.meshgrid(x, y)

# RGB kanalları için ifadeler
R_channel = (np.sin(np.sqrt(X**2 + Y**2) + np.arctan2(Y, X)) + 1) / 2
G_channel = (np.cos(0.05 * (X**2 + Y**2)) + 1) / 2
B_channel = (np.sin(0.1 * X) * np.cos(0.1 * Y) + 1) / 2

# RGB resmi oluşturma
image = np.zeros((height, width, 3), dtype=np.uint8)
image[:, :, 0] = R_channel * 255
image[:, :, 1] = G_channel * 255
image[:, :, 2] = B_channel * 255

# Görselleştirme
fig = plt.figure(figsize=(15, 5))

# Nihai RGB Resim
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Spiral ve Vorteks Deseni")
plt.axis('off')

# Kırmızı kanal için imshow
plt.subplot(1, 3, 2)
plt.imshow(R_channel, cmap='Reds')
plt.title("Kırmızı Kanal")
plt.axis('off')

# Yeşil kanal için kesit grafiği (y=0 boyunca)
plt.subplot(1, 3, 3)
plt.plot(x, G_channel[height//2, :], color='green')
plt.title("Yeşil Kanal (y=0 Kesiti)")
plt.xlabel("x")
plt.ylabel("Değer")

plt.tight_layout()
plt.show()