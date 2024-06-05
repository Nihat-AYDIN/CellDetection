import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure, color
from skimage.measure import regionprops, label

# Streamlit başlığı
st.title("Görüntü İşleme Parametre Ayarlamaları")

# Resmi yükleme
uploaded_file = st.file_uploader("Bir görüntü yükleyin", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Görüntüyü okuyalım
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Görüntünün yüklenip yüklenmediğini kontrol edelim
    if image is None:
        st.error("Görüntü dosyası açılamadı. Lütfen dosya yolunu kontrol edin!")
    else:
        # Gri Formata dönüştürelim
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Kullanıcıdan parametreleri alalım
        threshold_value = st.slider("Eşik Değeri", 0, 255, 127)
        erosion_kernel_size = st.slider("Erozyon Kernel Boyutu", 1, 10, 2)
        erosion_iterations = st.slider("Erozyon İterasyon Sayısı", 1, 10, 3)
        canny_threshold1 = st.slider("Canny Threshold1", 0, 255, 30)
        canny_threshold2 = st.slider("Canny Threshold2", 0, 255, 140)

        # Eşikleme işlemi
        _, binary_image = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

        # Kernel oluşturma
        kernel = np.ones((erosion_kernel_size, erosion_kernel_size), np.uint8)

        # Erozyon işlemi
        eroded_image = cv2.erode(binary_image, kernel, iterations=erosion_iterations)

        # Kenar tespiti
        edges = cv2.Canny(eroded_image, canny_threshold1, canny_threshold2)

        # Birleşik olan kontorler bulunur etiketlenir
        labeled_image = label(edges)

        # Region prop ile merkezleri bulalım
        props = regionprops(labeled_image)

        # Hücre sayısını 0 dan başlatalım
        i = 0

        # Merkezleri gezelim ve noktaları koyalım
        for prop in props:
            i += 1
            center_y, center_x = prop.centroid
            cv2.circle(image, (int(center_x), int(center_y)), 3, (0, 0, 255), -1)

        # Hücrelerin tüm resme oranını bulalım
        black_pixels = sum(1 for pixel in binary_image.flatten() if pixel == 0)
        total_pixels = binary_image.size
        black_ratio = (black_pixels / total_pixels) * 100

        # Sonuçları gösterelim
        st.write(f"Hücrelerin bulunduğu pixel sayısı: {black_pixels}")
        st.write(f"Resimde bulunan pixel sayısı: {total_pixels}")
        st.write(f"Hücrelerin tüm resme oranı: %{black_ratio:.2f}")
        st.write(f"Hücre Sayısı: {i}")

        # Resimleri göstermek için subplotlar oluşturalım
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))

        axes[0, 0].imshow(gray, cmap='gray')
        axes[0, 0].set_title('Gray Image')

        axes[0, 1].imshow(binary_image, cmap='gray')
        axes[0, 1].set_title('Binary Image')

        axes[0, 2].imshow(eroded_image, cmap='gray')
        axes[0, 2].set_title('Eroded Image')

        axes[1, 0].imshow(edges, cmap='gray')
        axes[1, 0].set_title('Edges')

        axes[1, 1].imshow(labeled_image, cmap='jet')
        axes[1, 1].set_title('Labeled Image')

        axes[1, 2].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        axes[1, 2].set_title('Original Image with Centers')

        for ax in axes.flat:
            ax.axis('off')

        st.pyplot(fig)
