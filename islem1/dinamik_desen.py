import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Görsel boyutları ve grid oluştur
width, height = 512, 512
x = np.linspace(-8, 8, width)
y = np.linspace(-8, 8, height)
X, Y = np.meshgrid(x, y)

# 🔮 Zaman parametresi alan fonksiyon
def generate_chaotic_image(t):
    # Kırmızı kanal: Trigonometrik karışım + zamanla kayma
    R_channel = (np.sin(X * np.cos(t * 0.1) + Y * np.sin(t * 0.1)) * 
                 np.cos(X**2 - Y**2 + t * 0.2) + 1) / 2

    # Yeşil kanal: Spiral dalgalar (polar koordinatlarla)
    R = np.sqrt(X**2 + Y**2)
    Theta = np.arctan2(Y, X)
    G_channel = (np.sin(R * 3 + Theta * 6 + t * 0.3) + 1) / 2

    # Mavi kanal: Modüler desen + parabolik + zamanla frekans titreşimi
    mod_component = ((X**2 + Y**2 + t) % 5) / 5
    wave = np.abs(np.cos(0.1 * X * Y + t * 0.5))
    B_channel = (mod_component * wave + 0.1) % 1.0

    # RGB görüntü oluştur
    image = np.zeros((height, width, 3), dtype=np.uint8)
    image[:, :, 0] = (R_channel * 255).astype(np.uint8)
    image[:, :, 1] = (G_channel * 255).astype(np.uint8)
    image[:, :, 2] = (B_channel * 255).astype(np.uint8)

    return image

# 🎨 Statik görüntü oluştur (örnek: t=10)
def show_static_image(t=10):
    img = generate_chaotic_image(t)
    plt.figure(figsize=(8, 8))
    plt.imshow(img)
    plt.title(f"Kaotik Dinamik Görüntü (t = {t})")
    plt.axis('off')
    plt.show()

# 🎞️ Animasyon başlat
def run_animation():
    fig, ax = plt.subplots()
    im = ax.imshow(generate_chaotic_image(0))
    ax.axis('off')
    plt.title("Kaotik Desen Animasyonu")

    def update(frame):
        im.set_array(generate_chaotic_image(frame))
        return [im]

    ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
    plt.show()

# 🚀 Çalıştırmak için:
if __name__ == "__main__":
    show_static_image(t=20)  # Yalnızca tek bir kare görüntülemek istersen
    run_animation()          # Animasyonu başlatmak istersen
