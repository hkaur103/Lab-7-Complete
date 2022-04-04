

from typing import Tuple
from xml.etree.ElementTree import PI


def main():
 # Initialize the complex data structure
    Info_in_table = {
        'name': 'Harmanjot Kaur',
        'Student_id': '10264930',
        'Pizza_topings': [
            'corns',
            'peppers',
            'onions',  
        ],
        'Movies': [
            {'title': 'Qismat',
            'genre': 'Romantic',
            },
            {'title': 'The chronicles of Narnia',
            'genre': 'Fantasy Novels',
            }
        ]
    } 
    
    #Append new movie to movie list
    new_movie = {'title':'3 Idiot', 'genre':'Comedy'}
    Info_in_table['Movies'].append(new_movie)
    pass
    
   # adding new topping
    new_Pizza_topings = ('mozrella','mushroom')
    add_toping(Info_in_table, new_Pizza_topings)
    Info_in_table['Pizza_topings'].sort()
    
    Printing_info(Info_in_table)
    pass

def Printing_info(Info_in_table):
    first_line = "Hi Jeremy, my name is " + Info_in_table['name'], "and my student ID is " + Info_in_table['Student_id']
    print(first_line)

def Printing_info(Info_in_table):
    scnd_line = "My ideal pizza has " + Info_in_table['Pizza_topings'] 
    print(scnd_line)

#third_line = "I like to watch " Info_in_table['movies'] + " movies" +
#fourth-line = "some of my favourites are " Info_in_table['movies']

def add_toping(Info_in_table, new_Pizza_topings):
    for p in new_Pizza_topings:
        Info_in_table['Pizza_topings'].append(p)


main()