#Just learning how to modify xml files with a py script
import os
import xml.dom.minidom as md
import glob

def main():

    #Declarations
    fullpath = []
    profiles = []
    count = 0
    drives = ['C:\\','E:\\','F:\\','D:\\']

    for rootPath in drives:
        print("Now searching in: ", rootPath)
        if rootPath == drives[0]:
            for filePath in glob.iglob(rootPath + '\\Program Files (x86)\\Steam\\userdata\\**\\632360\\remote\\UserProfiles\\'):
                print(filePath)
        for filePath in glob.iglob(rootPath + 'Steam\\userdata\\**\\632360\\remote\\UserProfiles\\'):
            print(filePath)


    for saveData in os.listdir(filePath):
        if not saveData.endswith('.xml'): continue
        file = md.parse(filePath + saveData)
        fullpath.append(filePath + saveData)
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
