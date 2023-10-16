# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1 Write a function that takes a single movie and returns True if its IMDB score is above 5.5

def my_func1(movies, movie):
    for n in movies:
        if n["name"] == movie:
            if n["imdb"] > 5.5:
                return True
    return False

movie = input()
print(my_func1(movies, movie))

#2 Write a function that returns a sublist of movies with an IMDB score above 5.5.

def my_func2(movies):
    list = []
    for m in movies:
        if m["imdb"] > 5.5:
            list.append(m["name"])
    return list

print(my_func2(movies))

#3 Write a function that takes a category name and returns just those movies under that category.

def my_func3(movies, str):
    list = []
    for m in movies:
        if m["category"] == str:
            list.append(m["name"])
    return list

str = input()
print(my_func3(movies, str))

#4 Write a function that takes a list of movies and computes the average IMDB score.

def my_func4(movies, list):
    cnt = 0
    imdb_cnt = 0
    for i in list:
        for n in movies:
            if n["name"] == i:
                cnt += 1
                imdb_cnt += n["imdb"]
    print(imdb_cnt/cnt)

#5 Write a function that takes a category and computes the average IMDB score.

def my_func5(movies, str):
    cnt = 0
    imdb_cnt = 0
    for n in movies:
        if n["category"] == str:
            cnt += 1
            imdb_cnt += n["imdb"]
    print(imdb_cnt/cnt)

str = input()
my_func5(movies, str)