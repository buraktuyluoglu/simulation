import random
import numpy as np

matris = np.zeros((500, 500), dtype=int)

class Creature:
    def __init__(self, creature_type, gender, x, y):
        self.creature_type = creature_type  # Tür (koyun, inek, tavuk, kurt, aslan, avcı)
        self.gender = gender  # Cinsiyet (erkek veya dişi)
        self.x = x  # X koordinatı
        self.y = y  # Y koordinatı

    def getVolume(self):
        if self.creature_type == "tavuk" or self.creature_type == "avci":
            return 1
        elif self.creature_type == "koyun" or self.creature_type == "inek":
            return 2
        elif self.creature_type == "kurt":
            return 3
        elif self.creature_type == "aslan":
            return 4
        
    def move(self):
        volume = self.getVolume()
        directions = [(0, volume), (0, -volume), (volume, 0), (-volume, 0)]
        random.shuffle(directions)  # Yönleri karıştırma
        for direction in directions:
            new_x = self.x + direction[0]
            new_y = self.y + direction[1]
            # Yeni konumun matris sınırları içinde ve boş olup olmadığını kontrol et
            if 0 <= new_x < 500 and 0 <= new_y < 500 and matris[new_x][new_y] == 0:
                # Eski konumu boşalt
                matris[self.x][self.y] = 0
                # Yeni konuma taşı
                self.x = new_x
                self.y = new_y
                # Matristeki yeni konumu işaretle
                matris[self.x][self.y] = 1
                break  # Hareket başarılı olduysa döngüden çık

    def interact(self, other, hayvanlar):
        if self != other:  # Kendi kendisi hariç
            if (self.creature_type == "avci" and abs(self.x - other.x) + abs(self.y - other.y) < 8) or (self.creature_type == "aslan" and (other.creature_type == "inek" or other.creature_type == "koyun") and abs(self.x - other.x) + abs(self.y - other.y) < 5) or (self.creature_type == "kurt" and (other.creature_type == "tavuk" or other.creature_type == "koyun") and abs(self.x - other.x) + abs(self.y - other.y) < 4):
                print(f"{self.creature_type} killed {other.creature_type}.")
                matris[other.x][other.y] = 0       
                hayvanlar.remove(other)
            elif self.creature_type == other.creature_type and self.gender != other.gender and abs(self.x - other.x) + abs(self.y - other.y) < 3:
                max_attempts = 100  # Maksimum deneme sayısı
                for _ in range(max_attempts):
                    x = random.randint(0, 499)
                    y = random.randint(0, 499)
                    if matris[x][y] == 0:
                        hayvan = Creature(self.creature_type, random.choice(["erkek", "dişi"]), x, y)
                        matris[x][y] = 1  # hayvanların konumunu matriste işaretleme
                        hayvanlar.append(hayvan)
                        print(f"{self.creature_type} and {other.creature_type} merged.")
                        break


def create_animals(creature_type, gender, count):
    animals = []
    for _ in range(count):
        while True:
            x = random.randint(0, 499)
            y = random.randint(0, 499)
            if matris[x][y] == 0:
                hayvan = Creature(creature_type, gender, x, y)
                matris[x][y] = 1  # hayvanların konumunu matriste işaretleme
                animals.append(hayvan)
                break           
    return animals

    
def main():
    hayvanlar = []
    hayvanlar.extend(create_animals("koyun", "dişi", 15))
    hayvanlar.extend(create_animals("koyun", "erkek", 15))
    hayvanlar.extend(create_animals("inek", "dişi", 5))
    hayvanlar.extend(create_animals("inek", "erkek", 5))
    hayvanlar.extend(create_animals("kurt", "dişi", 5))
    hayvanlar.extend(create_animals("kurt", "erkek", 5))
    hayvanlar.extend(create_animals("aslan", "dişi", 5))
    hayvanlar.extend(create_animals("aslan", "erkek", 5))
    hayvanlar.extend(create_animals("tavuk", "dişi", 10))
    hayvanlar.extend(create_animals("tavuk", "erkek", 10))
    hayvanlar.extend(create_animals("avci", "dişi", 1))

    print("Başlangıçta hayvanlar listesi uzunluğu:", len(hayvanlar))

    # hayvanların hareket etmesi ve son konumlarını yazdırma
    for _ in range(1000):
        #print(f"{i + 1}. Hamle:")
        for hayvan in hayvanlar:
            hayvan.move()
            others = [other for other in hayvanlar if other != hayvan and abs(hayvan.x - other.x) + abs(hayvan.y - other.y) < 15]
            if others:  # Check if the list is not empty
                other = random.choice(others)
                hayvan.interact(other, hayvanlar)
                   
    # Her türden kaçar hayvan kaldığını hesaplayıp yazdıralım
    koyun_sayisi = sum(1 for hayvan in hayvanlar if hayvan.creature_type == "koyun")
    inek_sayisi = sum(1 for hayvan in hayvanlar if hayvan.creature_type == "inek")
    kurt_sayisi = sum(1 for hayvan in hayvanlar if hayvan.creature_type == "kurt")
    aslan_sayisi = sum(1 for hayvan in hayvanlar if hayvan.creature_type == "aslan")
    tavuk_sayisi = sum(1 for hayvan in hayvanlar if hayvan.creature_type == "tavuk")
    avci_sayisi = sum(1 for hayvan in hayvanlar if hayvan.creature_type == "avci")
    print("Hayvanlar listesi uzunluğu:", len(hayvanlar))
    print(f"Kalan koyun sayısı: {koyun_sayisi}")
    print(f"Kalan inek sayısı: {inek_sayisi}")
    print(f"Kalan kurt sayısı: {kurt_sayisi}")
    print(f"Kalan aslan sayısı: {aslan_sayisi}")
    print(f"Kalan tavuk sayısı: {tavuk_sayisi}")
    print(f"Kalan avci sayısı: {avci_sayisi}")

main()

