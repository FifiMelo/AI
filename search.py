import random
import time

n1 = 200000000
grow_factor = 10
value_to_find1 = int(n1*0.5)

start_time = time.time()
tab1 = [random.randint(1,grow_factor)]
for x in range(1,n1):
    tab1.append(tab1[x-1] + random.randint(1,grow_factor))
print("czas tworzenia tablicy to: " + str(time.time() - start_time))
print("\n\n")

#wyszukiwanie za pomocą wbudowanej opcji "if item in list"
start_time = time.time()
if value_to_find1 in tab1:
    print("znalazłem")
print("czas dla 'if item in list' to: " + str(time.time() - start_time))
print("\n\n")

#wyszukiwanie za pomocą zaglądania do każdej komórki po kolei
start_time = time.time()
for x in range(n1):
    if tab1[x] == value_to_find1:
        print("znalazłem")
        break
print("czas dla zwykłego zaglądania to: " + str(time.time() - start_time))
print("\n\n")

#wyszukiwanie binarne bez dzielenia tablicy
start_time = time.time()
min_index = 0
max_index = n1 - 1
while not max_index == min_index:
    if tab1[(max_index + min_index)//2] >= value_to_find1:
        max_index = (max_index + min_index)//2
    else:
        min_index = (max_index + min_index)//2 + 1
if tab1[max_index] == value_to_find1:
    print("znalazłem")
print("czas dla wyszukiwania binarnego to: " + str(time.time() - start_time))
print("\n\n")

#wyszukiwanie Benka
start_time = time.time()
while not len(tab1) == 1:
    if tab1[len(tab1)//2] > value_to_find1:
        tab1 = tab1[:len(tab1)//2]
    else:
        tab1 = tab1[len(tab1)//2:]
if tab1[0] == value_to_find1:
    print("znalazłem")
print("czas dla wyszukiwania Benka to: " + str(time.time() - start_time))
print("\n\n")




