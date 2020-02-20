import sys
sys.stdout = open("C:/Users/Shizuka/Hashcode2020/result2.txt", "w")
f=open("C:/Users/Shizuka/Hashcode2020/c_incunabula.txt", "r")
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
lib_sign_up = []
for i in range (L):
    lib_sign_up.append((i,libraries_param[i][1]))
lib_sign_up= sorted(lib_sign_up, key=lambda x: x[1])
s = 0
i = 0
lib_array = []
while(s<D and i<len(lib_sign_up)):
    s+= lib_sign_up[i][1]
    lib_array.append(lib_sign_up[i])
    i+=1
nb_libraries = i
print(nb_libraries)
accumulator = 0
for i in range(nb_libraries-1):
    lib_id = lib_array[i][0]
    accumulator += lib_array[i][1]
    print(str(lib_id) + " " + str(min(D-accumulator,len(libraries_books[lib_id]))))
    j = 0 
    while (j<D-accumulator and j<len(libraries_books[lib_id])):
        if (j == D-accumulator - 1 or j == len(libraries_books[lib_id])-1):
            print(libraries_books[lib_id][j])
        else : 
            print(libraries_books[lib_id][j], end=" ")
        j+=1

