import os

class Market:
    def __init__(self):
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_name = os.path.join(current_dir, "product.txt")

        if not os.path.exists(self.file_name):
            with open(self.file_name, "w") as file:
                pass
        
        self.file = open(self.file_name, "r+")
        print(f"{self.file_name} dosyası açıldı.")


    def __del__(self):
        if hasattr(self, 'file') and not self.file.closed:
            self.file.close()
            print(f"{self.file_name} dosyası kapatıldı.")

    def list_product(self):
        try: 
            with open(self.file_name, "r", encoding="utf-8") as file:
                lines = file.read().splitlines()
                if not lines:
                    print("Ürün listesi boş.")
                    return
                print("Ürün Listesi: ")
                for i, line in enumerate(lines):
                    name, category, price, stock = line.split(",")
                    print(f"{i+1}. Ürün Adı: {name}, Kategori: {category}, Fiyat: {price}, Stok: {stock}")
        except Exception as e:
            print("Ürünler listelenirken bir hata oluştu: ", e)
    
    def add_product(self):
        try:
            name= input("Ürün adı: ")
            category = input ("Kategori: ")
            price = input("Fiyat: ")
            stock = input("Stok miktarı: ")

            with open(self.file_name, "a", encoding="utf-8") as file:
                file.write(f"{name}, {category}, {price}, {stock}\n")
            print("Ürün başarıyla eklendi.")
        except Exception as e:
            print("Ürün eklenirken bir hata oluştu.")
    
    def delete_product(self):
        try: 
            with open(self.file_name, "r", encoding="utf-8") as file:
                lines = file.read().splitlines()
            
            if not lines:
                print("Silinecek ürün yok. Ürün listesi boş.")
                return
            
            print("Ürün Listesi:")
            for i, line in enumerate(lines):
                name, category, price, stock = line.split(",")
                print(f"{i+1}. Ürün Adı: {name}, Kategori: {category}, Fiyat: {price}, Stok: {stock}")
            
            product_number = int(input("Silmek istediğiniz ürünün numarasını girin: "))
            if 1 <= product_number <= len(lines):
                deleted_product = lines.pop(product_number-1)
                with open(self.file_name, "w") as file:
                    file.write("\n".join(lines) + "\n")
                print(f"{deleted_product.split(',')[0]} adlı ürün başarıyla silindi.")
            else:
                print("Geçersiz ürün numarası.")
            
        except Exception as e:
            print("Ürün silinirken bir hata oluştu: ", e)


if __name__ == "__main__":
    market = Market()
    
    while True:  
        print("\n*** ÇEVRİMİÇİ MARKET ALIŞVERİŞ SEPETİ ***")
        print("1) Ürünleri Listele")
        print("2) Ürün Ekle")
        print("3) Ürün Sil")
        print("4) Çıkış")
        print("***************************************")
        
        choice = input("Bir işlem seçiniz (1-4): ")
        
        if choice == "1":
            print("\n--- ÜRÜNLERİ LİSTELE ---")
            market.list_product()
        elif choice == "2":
            print("\n--- YENİ ÜRÜN EKLE ---")
            market.add_product()
        elif choice == "3":
            print("\n--- ÜRÜN SİL ---")
            market.delete_product()
        elif choice == "4":
            print("\nProgramdan çıkılıyor...")
            del market
            break
        else:
            print("\nGeçersiz seçim! Lütfen 1-4 arasında bir değer girin.")

        continue_choice = input("\nBaşka bir işlem yapmak istiyor musunuz? (E/H): ").strip().lower()
        if continue_choice == 'h':
            print("\nProgramdan çıkılıyor...")
            del market
            break
        elif continue_choice == 'e':
            print("\nMenüye dönülüyor...")
            continue
        else:
            print("\nGeçersiz seçim! Programdan çıkılıyor...")
            del market
            break
