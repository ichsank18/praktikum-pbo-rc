import random
class Father:
  def __init__(self, blood_type):
    self.blood_type = blood_type

  def get_allele(self):
    if self.blood_type == 'A':
      return "A"
    elif self.blood_type == 'B':
      return "B"
    elif self.blood_type == 'O':
      return "O"
    elif self.blood_type == "AA":
      return "A"
    elif self.blood_type == "AB":
      return ["A", "B"]
    elif self.blood_type == "AO":
      return ["A", "O"]
    elif self.blood_type == "BA":
      return ["B", "A"]
    elif self.blood_type == "BB":
      return "B"
    elif self.blood_type == "BO":
      return ["B", "O"]
    elif self.blood_type == "OA":
      return ["O", "A"]
    elif self.blood_type == "OB":
      return ["O", "B"]
    elif self.blood_type == "OO":
      return ["O", "O"]
      
class Mother:
  def __init__(self, blood_type):
    self.blood_type = blood_type

  def get_allele(self):
    if self.blood_type == 'A':
      return "A"
    elif self.blood_type == 'B':
      return "B"
    elif self.blood_type == 'O':
      return "O"
    elif self.blood_type == "AA":
      return "A"
    elif self.blood_type == "AB":
      return ["A", "B"]
    elif self.blood_type == "AO":
      return ["A", "O"]
    elif self.blood_type == "BA":
      return ["B", "A"]
    elif self.blood_type == "BB":
      return "B"
    elif self.blood_type == "BO":
      return ["B", "O"]
    elif self.blood_type == "OA":
      return ["O", "A"]
    elif self.blood_type == "OB":
      return ["O", "B"]
    elif self.blood_type == "OO":
      return ["O", "O"]

class Child:
  def __init__(self, father, mother):
    self.father = ayah
    self.mother = ibu
    self.allele = []

  def get_allele(self):
    allele_father = self.father.get_allele()
    allele_mother = self.mother.get_allele()
    self.allele.append(random.choice(allele_father))
    self.allele.append(random.choice(allele_mother))
    return "".join(self.allele)

  def tampil_get_allele(self):
    return self.get_allele()

  def get_blood_type(self):
    if self.allele[0] == "A" and self.allele[1] == "A":
      return "A"
    elif self.allele[0] == "A" and self.allele[1] == "O":
      return "A"
    elif self.allele[0] == "A" and self.allele[1] == "B":
      return "AB"
    elif self.allele[0] == "B" and self.allele[1] == "A":
      return "AB"
    elif self.allele[0] == "B" and self.allele[1] == "B":
      return "B"
    elif self.allele[0] == "B" and self.allele[1] == "O":
      return "B"
    elif self.allele[0] == "O" and self.allele[1] == "O":
      return "O"
    elif self.allele[0] == "O" and self.allele[1] == "B":
      return "B"
    elif self.allele[0] == "O" and self.allele[1] == "A":
      return "A"
    else:
      return "Golongan darah tidak valid"
      
father = Father(input("Enter the father's allele :"))
mother = Mother(input("Enter the mother's allele : "))
child = Child(father, mother)
print(f"Child's allele : {child.tampil_get_allele()}")
blood_type = child.get_blood_type()
print(f"Child's blood type : {blood_type}")