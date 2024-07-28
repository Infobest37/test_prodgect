#homework5.py
immutable_var = ([1,2,4,5,6], 1, [7,8,9,10,11],2, "python", True)
print( immutable_var)
#Картеж не я вляется списком, в списке можно изменить объект, в картеже так делать нельзя, картедж так делать не может.
#immutable_var("python")= "filipinu" - будет ошибка.
immutable_var[2][0]=3 #в картеже можно создавать списки и в этих списках можно производить изменения присваевая каждому списку свой индекс
print( immutable_var)
mutable_lis = [1,2,3,4,5, "Python", "Juice", True]
mutable_lis[0]=6
print(mutable_lis)
mutable_lis[6] = "apel"
print(mutable_lis)


