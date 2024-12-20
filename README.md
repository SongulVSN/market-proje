# Çevrimiçi Market Alışveriş Sepeti

Bu proje, nesne yönelimli programlama (OOP) tekniklerini kullanarak bir "Çevrimiçi Market Alışveriş Sepeti" sistemi geliştirmeyi amaçlamaktadır. Python programlama dili ile oluşturulan bu sistem, ürünleri yönetmek ve kullanıcılarla etkileşim kurmak için tasarlanmıştır.

---

## Özellikler

1. **Ürün Listeleme**:
   - `product.txt` dosyasındaki ürünleri listeler.
   - Ürün adı, kategori, fiyat ve stok bilgileri gösterilir.

2. **Ürün Ekleme**:
   - Kullanıcıdan yeni bir ürün bilgisi alır.
   - Ürün adı, kategori, fiyat ve stok miktarı `product.txt` dosyasına kaydedilir.

3. **Ürün Silme**:
   - Kullanıcıdan silmek istediği ürünün numarasını alır.
   - Ürün `product.txt` dosyasından kaldırılır.

4. **Çıkış**:
   - Programdan çıkış yapar ve dosya işlemlerini güvenli bir şekilde sonlandırır.

---

## Dosya Yapısı

- **market.py**: Projenin ana Python kodları.
- **product.txt**: Ürün verilerinin saklandığı dosya. Her satır bir ürün bilgisi içerir:
