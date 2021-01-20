import imdb

mov = imdb.IMDb()
print()
a=input("Enter Movie name: ")
movie = mov.search_movie(a)
id = movie[0].getID()
movies = mov.get_movie(id)
name = movies['title']
year = movies['year']
rate = movies['rating']
direct = movies['directors']
casting = movies['cast']

print('Movie Info:- ')
print()
print(f'{name} - {year}')
print(f'Rating: {rate}')
directStr = '\n'.join(map(str, direct))
print(f'Directors: {directStr}')
actors = '\n'.join(map(str, casting))
print(f'Actors: \n{actors}')