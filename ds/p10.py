import csv
import sys
filename="movie.csv"
def display_menu():
    print("COMMAND MENU")
    print("list-List all movies")
    print("add-Add a movie")
    print("del-Delete a movie")
    print("exit-Exit a program")
    
def write_movies(movies):
   try: 
    with open(filename,"w",newline="")as file:
        writer=csv.writer(file)
        writer.writerows(movies) 
   except FileNotFoundError :
       print("File not found")
       exit_pgm()
   except Exception as e:
       print("an error occured"+e+type(e)) 
       exit_pgm()
       
         
def read_movies():
    try:
      movies=[] 
      with open(filename,"r",newline="")as file:
        # raise OSError("OSError")
        reader=csv.reader(file)
        for movie in reader:
            movies.append(movie)  
      return movies
    except FileNotFoundError:
        print("file not found"+filename)
        exit_pgm()
    except OSError:
        print("file found,error while reading")
    except Exception as e:
        print("an error occured",e,type(e))
        exit_pgm()
        
        
# def read_movies():
#     try:
#         file=file.open(filename,newline="")
#         try:
#             movies=[]
#             reader=csv.reader(file)
#             for row in reader:
#                 movies.append(row)
#             return movies
#         except Exception as e:
#             print(type(e),e)
#         finally:
#             file.close()
#     except FileNotFoundError as e:
#         print(e)
        
        
def add_movies(movies):
    name=input("Movie:")
    year=input("year:")
    movie=[]
    movie.append(name)
    movie.append(year)
    movies.append(movie)
    write_movies(movies)
    print(movie[0]+" was added")
    
def list_movies(movies):
    for i in range(len(movies)):
        movie=movies[i]
        print(str(i+1)+"."+movie[0]+"("+movie[1]+")")
        
def exit_pgm():
    print("coludn't find movies.csv file")
    print("terminating pgm")   
    sys.exit()    
def del_movies(movies):
    while True:
      try:
        n=int(input("Number:"))
      except ValueError:
          print("Invalid integer.")
          continue
      if n<1 or n>len(movies):
          print("there is no movies with that number")
      else:
          break
    movie=movies.pop(n-1)
    write_movies(movies)
    print(movie[0]+" was deleted")
    
    
def main():
    display_menu()
    movies=read_movies()
    while True:
        command=input("Command:")
        if command=="list":
            list_movies(movies)
        elif command=="add":
            add_movies(movies)
        elif command=="del":
            del_movies(movies)
        elif command=="exit":
            print("Bye")
            break
        else:
            print("Invalid command.")
if __name__=='__main__':
    main()