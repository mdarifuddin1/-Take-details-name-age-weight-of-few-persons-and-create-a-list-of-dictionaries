# code by Md Arif Uddin
# 193027042
persons = []
for i in range(3):
  name = input("Enter name:")
  weight = float(input("Enter weight : "))
  age = int(input("Enter age: "))
  person = {"name": name, "weight":weight, "age": age}
  persons.append(person)



def selectionSort(list1):
  list2 = []
  while len(list1)>0:
    max = list1[0]["weight"]
    idx = 0
    for j in range(len(list1)):
      if list1[j]["weight"] > max:
        max = list1[j]["weight"]
        idx = j
    list2.append(list1[idx])
    list1.pop(idx)
  return list2

sortedPersons = selectionSort(persons)
 
for person in sortedPersons:
  print(person)