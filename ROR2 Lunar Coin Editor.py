#Just learning how to modify xml files with a py script
import os
from os import walk
import xml.dom.minidom as md
import xml.etree.ElementTree as ET


def main():

    #Declarations
    fullpath = []
    profiles = []
    count = 0

    #find dir
    path_parent = 'C:/Program Files (x86)/Steam/userdata/'
    itr = iter(os.walk(path_parent))
    root, dirs, files = next(itr)

    for next_root, next_dirs, next_files in itr:  #This just gets opens the file that contains your steam profile number since its unique
        root = next_root
        break

    path = root + '/632360/remote/UserProfiles/'

    for filename in os.listdir(path):
        if not filename.endswith('.xml'): continue
        file = md.parse(path + filename)
        fullpath.append(path + filename)
        profiles.append(file.getElementsByTagName('name')[ 0 ].childNodes[ 0 ].nodeValue)
    
    #Input time :-)
    print('Choose profile to edit:\n')

    for number, letter in enumerate(profiles):
        print(number, letter)
    print()
    
    #Get the file name
    profInp = input('Enter a number: ')
    while int(profInp) < 0 or int(profInp) >= len(profiles):
        print('Invalid')
        print('Choose profile to edit:\n')
        for number, letter in enumerate(profiles):
            print(number, letter)
        print()
        profInp = input('Enter a number: ')

    #Parse selected profile
    file = md.parse(fullpath[int(profInp)])
    
    #Ask coins
    coinsIn = input('Enter coin amount: ')
    while int(coinsIn) < 0:
        print("Please do 0 or more :-):")
        coinsIn = input('Enter coin amount: ')
    
    #Edit
    file.getElementsByTagName( "coins" )[ 0 ].childNodes[ 0 ].nodeValue = str(coinsIn)

    with open( fullpath[int(profInp)], "w" ) as fs: 
  
        fs.write( file.toxml() )
        fs.close() 

    print("Enjoy your coins. Thanks for using :-). - Decoyroid")
    os.system('pause')
    #Goodbye

if __name__ == '__main__':
    main()
