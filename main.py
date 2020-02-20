f=open("C:/Users/Shizuka/Hashcode2020/a_example.txt", "r")
f1 = f.readlines()
libraries_param = []
libraries_books = []
 
B , L , D = map(int, f1[0].split())
books = list(map(int, f1[1].split()))
i = 2
while(i<len(f1)-1):
    libraries_param.append(list(map(int, f1[i].split())))
    libraries_books.append(list(map(int, f1[i+1].split())))
    i+=2
print(B,L,D)
print(books)
print(libraries_param)
print(libraries_books)
    


