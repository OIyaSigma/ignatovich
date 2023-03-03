import datetime
import queue


my_data = ("Игнатович Ольга Дмитриевна", 21, 10, 2003)
disc_marks = {
    "русский": 4, 
    "литература": 5, 
    "алгебра": 5,
    "геометрия": 4,
    "история": 3,
    "география": 3,
    "биология": 4,
    "обществознание": 5,
    "музыка": 3,
    "физика": 4,
    "информатика": 5,
    "физкультура": 4,
    "ИЗО": 5,
    "ОБЖ": 5
    }
family_names = ["Ирина", "Дмитрий", "Алёна", "Татьяна", \
                "Алексей","Светлана","Сергей","Татьяна","Алексей"]

kiwa_name = "Брусничка"

#1

average_mark = sum(disc_marks.values()) / len(disc_marks.values())
print("Средние значение аттестата: ", average_mark)

#2

unique_names=set(family_names)
print("Уникальные имена: ", *unique_names, "Ольга")

#3

pred=[0]*len(disc_marks.values())
count=0
stroka_bykv=""
for i in disc_marks.keys():
    pred[count]=i
    stroka_bykv+=pred[count]
    count+=1
print("Число букв в предметах: ",len(stroka_bykv))

#4
lenght=sum(disc_marks.values())
print(lenght)
k = {}
for i in stroka_bykv:
    if i in k:
        k[i] += 1
    else:
        k[i]=1
print("Число уникальных букв: ",k)

#5

print("Бинарный код кивы: ",*bytearray(kiwa_name, 'utf-8'))

#6

alf=list(set(family_names))
alf.sort(reverse= True)
print("Обратный порядок имен: ", *alf)

#7

today = datetime.datetime.today()
my_bday = datetime.datetime(day=my_data[1],
                            month=my_data[2],
                            year=my_data[3])
print("Количество дней от дня рождения до текущей даты: ", (today-my_bday).days)

#8

q=queue.Queue()
for i in disc_marks.keys():
    q.put(i)
    
while True:
    slovo=input()
    if slovo=='':
        break
    else:
        q.put(slovo)
        
while True:
    print(q.get())
    if q.empty()==True:
        break

#9

i=int(input())
number_drevnii=(my_data[1]+my_data[2]**2+my_data[3])%21+1
drevnii="Чимальпопока"
alf[i]=drevnii
print("Замена на ацтекского правителя", *alf)
