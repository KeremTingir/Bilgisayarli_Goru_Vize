import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import random

class PuzzleGUI:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("3x3 Jigsaw Bulmacası")

        # Resmi yükle
        self.original_image = cv2.imread(image_path)
        if self.original_image is None:
            messagebox.showerror("Hata", f"Resim yüklenemedi: {image_path}. Lütfen geçerli bir resim dosyası seçin.")
            root.destroy()
            return
        self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)

        # Resmi 3x3 parçaya böl
        self.tile_size = self.original_image.shape[0] // 3  # Resim boyutuna göre
        self.tiles = []
        for i in range(3):
            for j in range(3):
                tile = self.original_image[i*self.tile_size:(i+1)*self.tile_size,
                                          j*self.tile_size:(j+1)*self.tile_size]
                self.tiles.append(tile)

        # 4 farklı varyasyon oluştur
        self.variations = []
        for _ in range(4):
            indices = list(range(9))
            random.shuffle(indices)
            self.variations.append(indices.copy())

        # GUI elemanları
        self.current_variation = 0
        self.current_indices = self.variations[self.current_variation].copy()
        self.selected_tile = None

        # Sol frame: Orijinal resim
        self.left_frame = tk.Frame(root)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.original_canvas = tk.Canvas(self.left_frame, width=self.original_image.shape[1], height=self.original_image.shape[0])
        self.original_canvas.pack()
        self.original_photo = ImageTk.PhotoImage(Image.fromarray(self.original_image))
        self.original_canvas.create_image(0, 0, anchor='nw', image=self.original_photo)

        # Sağ frame: Bulmaca ve kontroller
        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # Bulmaca canvas'ı
        self.puzzle_canvas = tk.Canvas(self.right_frame, width=self.original_image.shape[1], height=self.original_image.shape[0], bg='black')
        self.puzzle_canvas.pack()

        # Kontrol düğmeleri
        self.button_frame = tk.Frame(self.right_frame)
        self.button_frame.pack(pady=10)
        
        tk.Button(self.button_frame, text="Önceki Varyasyon", command=self.prev_variation).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Sonraki Varyasyon", command=self.next_variation).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Yeni Karışım", command=self.new_shuffle).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Kontrol Et", command=self.check_solution).pack(side=tk.LEFT, padx=5)

        # Varyasyon etiketi
        self.variation_label = tk.Label(self.right_frame, text=f"Varyasyon {self.current_variation + 1}/4")
        self.variation_label.pack(pady=5)

        # Bulmacayı çiz
        self.draw_puzzle()

        # Fare olayları
        self.puzzle_canvas.bind("<Button-1>", self.click_tile)

    def draw_puzzle(self):
        self.puzzle_canvas.delete("all")
        self.photos = []  # Referansları tut
        for idx, tile_idx in enumerate(self.current_indices):
            row = idx // 3
            col = idx % 3
            tile = self.tiles[tile_idx]
            img = Image.fromarray(tile)
            photo = ImageTk.PhotoImage(img)
            self.photos.append(photo)
            self.puzzle_canvas.create_image(col * self.tile_size, row * self.tile_size,
                                           anchor='nw', image=photo, tags=f"tile_{idx}")

    def click_tile(self, event):
        # Tıklanan karenin indeksini bul
        col = event.x // self.tile_size
        row = event.y // self.tile_size
        idx = row * 3 + col

        if self.selected_tile is None:
            # İlk seçilen kare
            self.selected_tile = idx
            self.puzzle_canvas.itemconfig(f"tile_{idx}", outline='yellow', width=3)
        else:
            # İkinci seçilen kare, takas yap
            other_idx = self.selected_tile
            self.current_indices[idx], self.current_indices[other_idx] = \
                self.current_indices[other_idx], self.current_indices[idx]
            self.selected_tile = None
            self.puzzle_canvas.itemconfig(f"tile_{other_idx}", outline='', width=0)
            self.draw_puzzle()

    def prev_variation(self):
        if self.current_variation > 0:
            self.current_variation -= 1
            self.current_indices = self.variations[self.current_variation].copy()
            self.variation_label.config(text=f"Varyasyon {self.current_variation + 1}/4")
            self.draw_puzzle()

    def next_variation(self):
        if self.current_variation < 3:
            self.current_variation += 1
            self.current_indices = self.variations[self.current_variation].copy()
            self.variation_label.config(text=f"Varyasyon {self.current_variation + 1}/4")
            self.draw_puzzle()

    def new_shuffle(self):
        self.current_indices = list(range(9))
        random.shuffle(self.current_indices)
        self.variations[self.current_variation] = self.current_indices.copy()
        self.draw_puzzle()

    def check_solution(self):
        if self.current_indices == list(range(9)):
            messagebox.showinfo("Tebrikler!", "Bulmaca doğru çözüldü!")
        else:
            messagebox.showwarning("Hata", "Bulmaca henüz çözülmedi.")

# GUI başlat
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Ana pencereyi gizle
    image_path = filedialog.askopenfilename(
        title="Resim Seç",
        filetypes=[("Resim Dosyaları", "*.png *.jpg *.jpeg")]
    )
    root.deiconify()  # Ana pencereyi geri göster
    if not image_path:
        messagebox.showerror("Hata", "Resim seçilmedi. Uygulama kapanıyor.")
        root.destroy()
    else:
        app = PuzzleGUI(root, image_path)
        root.mainloop()