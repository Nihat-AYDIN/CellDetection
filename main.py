# I.png görseli RGB bir görüntüdür. 
# Üzerinde koyu tonda hücreler bulunmaktadır.

# >> Görüntüdeki hücreleri  sayınız.
# >> Her hücrenin merkezini gösteren bir nokta (istediğiniz bir renkte) koyunuz. 
# >> bu işlem için regionprop->center özelliğini kullanabilirsiniz. 
# >> Hücrelerin tüm görsele olan oranını bulunuz.

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure, color
from skimage.measure import regionprops, label

# Resmi okuyalım
image = cv2.imread('I.png')

# Görüntünün yüklenip yüklenmediğini kontrol edelim
if image is None:
    raise ValueError(f"Görüntü dosyası açılamadı. Lütfen dosya yolunu kontrol edin!")

# Gri Formata dönüştürelim
# Gri formata dönüştürdüğümüz resim üzerinden hücrelerin pixel değerlerini inceleyelim
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# İnceledğimiz gri formattaki resimde 127 eşik değerinin uygun olduğuna karar verildi.
_, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 2*2 lik 1 lerden oluşan matris oluşuralım
kernel = np.ones((2, 2), np.uint8)

# 1 lerden oluşan matris erozyon işleminde siyahları belirginleştirecektir.
# İterasyon sayısının az olmasının sebebi merkezlere konulacak noktalar sapmamalıdır.
eroded_image = cv2.erode(binary_image, kernel, iterations=3)

# Merkezleri işaretlemek için kenarları tespit edelim
edges = cv2.Canny(eroded_image, 30, 140)

# Birleşik olan kontorler bulunur etiketlenir
labeled_image = label(edges)

# Region prop ile merkezleri bulalım
props = regionprops(labeled_image)

# Hücre sayısını 0 dan başlatalım
i=0

# merkezleri gezelim ve noktaları koyalım
for prop in props:
    # Hücreleri sayalım
    i+=1
    center_y, center_x = prop.centroid
    cv2.circle(image, (int(center_x), int(center_y)), 3, (0, 0, 255), -1)

# Hücrelerin tüm resme oranını bulalım öncelikle hücrelerin bulunduğu pixelleri sayalım
black_pixels = sum(1 for pixel in binary_image.flatten() if pixel == 0)
print(f"Hücrelerin bulunduğu pixel sayısı {black_pixels}")

# Toplam piksel sayısını bulalım
total_pixels = binary_image.size
print(f"Resimde bulunan pixel sayısı: {total_pixels}")    
# Siyah piksellerin tüm resme oranını hesaplayalım
black_ratio = (black_pixels / total_pixels) * 100
print(f"Hücrelerin tüm resme oranı : %{black_ratio}") 
print(f"Hücre Sayısı: {i} ")


# Resimleri göstermek için subplotlar oluşturalım
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Her bir subplota resmi ekleyelim
axes[0, 0].imshow(gray, cmap='gray')
axes[0, 0].set_title('Gray Image')

axes[0, 1].imshow(binary_image, cmap='gray')
axes[0, 1].set_title('Binary Image')

axes[0, 2].imshow(eroded_image, cmap='gray')
axes[0, 2].set_title('Eroded Image')

axes[1, 0].imshow(edges, cmap='gray')
axes[1, 0].set_title('Edges')

axes[1, 1].imshow(labeled_image, cmap='jet')  # cmap='jet' burası tam olmadı
axes[1, 1].set_title('Labeled Image')

axes[1, 2].imshow(image)
axes[1, 2].set_title('Original Image')

# Boşlukları ve ekseni kapatalım
for ax in axes.flat:
    ax.axis('off')

# Ekranda gösterelim
plt.tight_layout()
plt.show()

