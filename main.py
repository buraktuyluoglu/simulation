import random
import numpy as np

matris = np.zeros((5, 5), dtype=int)

class Creature:
    def __init__(self, creature_type, gender, x, y):
        self.creature_type = creature_type  # Tür (koyun, inek, tavuk, kurt, aslan, avcı)
        self.gender = gender  # Cinsiyet (erkek veya dişi)
        self.x = x  # X koordinatı
        self.y = y  # Y koordinatı

    def getVolume(self):
        if self.creature_type == "tavuk" or self.creature_type == "avci":
            return 1
        elif self.creature_type == "koyun":
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
            if 0 <= new_x < 5 and 0 <= new_y < 5 and matris[new_x][new_y] == 0:
                # Eski konumu boşalt
                matris[self.x][self.y] = 0
                # Yeni konuma taşı
                self.x = new_x
                self.y = new_y
                # Matristeki yeni konumu işaretle
                matris[self.x][self.y] = 1
                break  # Hareket başarılı olduysa döngüden çık

    def interact(self, other):
        if self.creature_type == other.creature_type and self.gender != other.gender and abs(self.x - other.x) + abs(self.y - other.y) < 3:
            print(f"{self.creature_type} ile {other.creature_type} çiftleşti.")

            # Yeni hayvanın cinsiyetini belirle
            new_gender = random.choice(["erkek", "dişi"])

            # Yeni hayvanın konumunu belirle
            while True:
                i, j = random.randint(self.x - 1 , other.x + 1), random.randint(self.y - 1, other.y + 1)
                if matris[i][j] == 0:
                    matris[i][j] = 1
                    break
                # Yeni hayvanı oluştur ve konumunu güncelle
                new_creature = Creature(self.creature_type, new_gender, i, j)
                print(f"Yeni {new_creature.creature_type} oluşturuldu: ({new_creature.x}, {new_creature.y})")
            
        else:
            if self.creature_type == "avci" and abs(self.x - other.x) + abs(self.y - other.y) < 0:
                print(f"{self.creature_type} killed {other.creature_type}.")
                matris[other.x][other.y] = 0


def isreachable(Creature):
    if matris[Creature.x][Creature.y] == 0:
        return True
    else:
        return False
def test():
    # 3 koyun oluşturma
    hayvanlar = []
    for _ in range(3):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        hayvanlar.append(Creature("koyun", "dişi", x, y))
        matris[x][y] = 1  # hayvanların konumunu matriste işaretleme

    x = random.randint(0, 4)
    y = random.randint(0, 4)
    avci = Creature("avci", "dişi", x, y)
    hayvanlar.append(avci)
    matris[x][y] = 1  # Avcının konumunu matriste işaretleme
    
    # hayvanların hareket etmesi ve son konumlarını yazdırma
    for i in range(4):
        print(f"{i + 1}. Hamle:")
        for hayvan in hayvanlar:
            hayvan.move()
            for other_hayvan in hayvanlar:
                if hayvan != other_hayvan:  # Kendi kendisi hariç diğer hayvanlarla etkileşime gir
                    hayvan.interact(other_hayvan)
            print(f"({hayvan.creature_type}): ({hayvan.x}, {hayvan.y})")
        print(matris)


test()