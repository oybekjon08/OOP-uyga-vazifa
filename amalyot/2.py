class Familiya:
    def __init__ (self, lst:list):
        self.list=lst
    def tayyorlangan(self):
        self.list.sort(key=lambda indeks: indeks.split()[1])
        print(self.list)




Names=[
    'Vivian Kidd','Bradyn Grant',
    'Alexis Strickland',    'Madeleine Dunn',
    'Emanuel Deleon',    'Charlotte Moody',
    'Ian Wells',    'Greyson Sellers',
    'Abril Cordova',    'Julissa Wolf',
    'Gabrielle Osborne',    'Brian Webster',
    'Ethen Charles',    'Ashtyn Cowan',
    'Brycen Benson',    'Thomas Sexton',
    'Brynlee Park',    'Keaton Pena',
    'Lily Ochoa',    'Jaycee Glass',
    'Anderson Stark',    'Alexandria Harper',
    'Derek Cooley',    'Savannah Coleman',
    'Chase Cantu',    'Maverick Gonzales',
    'Wyatt Browning',    'Brenden Walter',
    'Paula Bullock',    'Alisha Hicks',
    'Genevieve Petty',    'Reece Erickson',
    'Brice Pope',    'Maverick Hammond',
    'Giuliana Morris',    'Kaelyn Kelley',
    'Paisley French',    'Cassius Rogers',
    'Gloria French',    'Hugh Richardson',
    'Braiden Tate',    'Sophia Wang',
    'Cortez Kirby',    'Sebastian Wilkinson',
    'Joanna Shannon',    'Miracle Barrera',
    'Cali Kaiser',    'Bridget Leon',
    'Gillian Hall',    'Jade King',
    'Aydin Powell',    'Anthony Paul',
    'Brittany Rios',    'Arely Howe',
    'Trace Valenzuela',    'Aryanna Hicks',
    'Connor Nixon',    'Santiago Vargas',
    'Kirsten Monroe',    'Norah Schultz',
    'Danika Hudson',    'Makena Escobar',
    'Jayce Navarro',    'Thaddeus Strickland',
    'Michaela Robinson',    'Remington Hurley',
    'Jairo Sanders',    'Averie Huber',
    'Cody Jensen',    'Kennedy Wall',
    'Fiona Huynh',    'August Tapia',
    'Sarah Manning',    'Joselyn Allison',
    'Dayton Barnes',    'Santiago Glenn',
    'Rashad Cuevas',    'Bernard Nicholson',
    'Will Moyer',    'Aliza Frazier',
    'Abram Burch',    'Lilly Klein',
    'Carlee Montes',    'Madeleine Patton',
    'Brady Osborn',    'Ruth Monroe',
    'Celia Horn',    'Braylen Cabrera',
    'Jennifer Tanner',    'Kendra Cross',
    'Olive Sherman',    'Aiyana Wolfe',
    'Charlize Cervantes',    'Braydon Esparza',
    'Kash Osborne',    'Maximus Mathews',
    'Kamora Richardson',    'Tripp Sosa',
    'Kameron Taylor',    'Tyler Jackson']
a=Familiya(Names)
a.tayyorlangan()