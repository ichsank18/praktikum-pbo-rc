import random

class Character:
  def __init__(self, name, hp, attack, accuracy, regen):
    self.name = name
    self.hp = hp
    self.max_hp = hp
    self.attack = attack #Damage Maksimal
    self.accuracy = accuracy
    self.regen = regen #Regen Maksimal
    
  #Fungsi Menyerang Robot lainnya
  def take_damage(self, damage):
    self.hp -= damage

  #Fungsi Me-Regen HP
  def regens(self):
    heal_amount = random.randint(7, self.regen)
    self.hp = min(self.hp + heal_amount, self.max_hp)
    print(f"{self.name} regens for {heal_amount} HP.")

  #Untuk mengetahui apakah robot sudah mati atau belum
  def is_alive(self):
    return self.hp > 0

  #Fungsi untuk besarnya serangan dan akurasi serangan
  def attack_enemy(self, enemy):
    if random.random() < self.accuracy:
      damage = random.randint(10, self.attack)
      enemy.take_damage(damage)
      print(f"{self.name} attacks {enemy.name} for {damage} damage.")
    else:
      print(f"{self.name} MISSES the attack on {enemy.name}!")

#Membuat 2 robot
#100 HP, 20 maks damage, 70% akurasi menyerang, regen hp maks: 15
character1 = Character("Gurren", 100, 20, 0.7, 15)  
#90 HP, 25 maks damage, 75% akurasi menyerang, regen hp maks: 15
character2 = Character("Lagann", 90, 25, 0.75, 15)


#Memulai permainan
print("Welcome to the Robot Battle!")
print(f"{character1.name} (HP: {character1.hp}) vs {character2.name}(HP: {character2.hp})")
print("Get ready to fight!\n")
turn = 1
#Perulangan Battle
while character1.is_alive() and character2.is_alive():
  print(f"~TURN {turn}~")
  print(f"{character1.name}'s turn!")
  print("Choose your move:")
  print("1. Attack")
  print("2. Regen")
  choice = input("Enter your choice (1 or 2): ")
  if choice == '1':
    character1.attack_enemy(character2)
  elif choice == '2':
    character1.regens()
  else:
    print("Invalid choice. Please choose 1 for Attack or 2 for Regen.")
  print("--------------------------------------")
  print(f"{character1.name} HP: {character1.hp}")
  print(f"{character2.name} HP: {character2.hp}")
  print("______________________________________")
  if character2.is_alive():
    print(f"{character2.name}'s turn!")
    print("Choose your move:")
    print("1. Attack")
    print("2. Regen")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
      character2.attack_enemy(character1)
    elif choice == '2' and character2.is_alive():
      character2.regens()
    else:
      print("Invalid choice. Please choose 1 for Attack or 2 for Regen.")
  print("--------------------------------------")
  print(f"{character1.name} HP: {character1.hp}")
  print(f"{character2.name} HP: {character2.hp}")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  turn=turn+1
  print("\n")
  
#Penentuan Pemenang
if character1.is_alive():
  print(f"{character1.name} wins! on turn {turn}!")
else:
  print(f"{character2.name} wins! on turn {turn}!")

#Basically, Game gacha damage hoki-hokian LMAO