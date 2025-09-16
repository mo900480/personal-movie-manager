 # save my movies in list
movies_list = ["the dark knight","fast and furious","dhoom" ]
# add details to each movie and save in dictionary
movie_dic = {
    movies_list[0] : {
        "Name":"the dark knight",
        "Year of product" : 2020,
        "Actors":["ahmed ezz","ahmed saqqa","nelly karim","hend sabry"],
    },
    movies_list[1]:{
        "Name":"fast and furious",
        "Year of product":2021,
        "Actors":["van diessel","statham","tom cruse"]
    },
    movies_list[2]:{
        "Name":"dhoom",
        "Year of product":2013,
        "Actors":["Amir khan","karina kapoor","akshay komar"]
    }
}
print(f"details about all movies : {movie_dic}")
print("=" * 60) # simple separator
# list of choises and user choise one from it to make a changes based on his choise
print("List of choises : ")
choise = input("choise one from this please : [delete , uptade , add] ").strip().lower()

# if he choised delete or d the both its same thing
if choise == 'delete' or choise == 'd' :
     delete_choise = input("enter name of movie you want to delete it : ").strip().lower()
     if delete_choise == movies_list[0]:
        movies_list.remove(movies_list[0])
        print("Your movies : " , movies_list)
     elif delete_choise == movies_list[1]:
        movies_list.remove(movies_list[1])
        print("Your movies : ", movies_list)
     elif delete_choise == movies_list[2] :
        movies_list.remove(movies_list[2])
        print("Your movies : ", movies_list)
     else:
        print("movie not found !!")

# if he choise uptade 
elif choise == 'uptade' or choise == 'u' :
    uptaded_choise = input("enter name of movie to replace another movie : ").strip().lower()
    uptade_new = input(f"enter name the movie you want to add replace of {uptaded_choise} : ").strip().lower()
    if uptaded_choise == movies_list[0] :
        movies_list[0] = uptade_new
        print("Your movies : ", movies_list)
    elif uptaded_choise == movies_list[1] :
        movies_list[1] = uptade_new
        print("Your movies : ", movies_list)
    elif uptaded_choise == movies_list[2] : 
        movies_list[2] = uptade_new
        print("Your movies : ", movies_list)
    else:
        print("wrong input !!")

# if he choise add to add new movie to the list
elif choise == 'add' or choise == 'a' :
    added_movie = input("enter your new movie to add it : ").strip().lower()
    movies_list.append(added_movie)
    print("Your movie : ", movies_list)
else : 
    print("wrong choise!!")
    print("the project is well done now you can using it easily")
