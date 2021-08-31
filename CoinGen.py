#Just learning how to modify xml files with a py script
import xml.dom.minidom as md

def main():

    #Get the file name
    inp = input('Enter save data file name with .xml extension: ')
    
    file = md.parse(inp)
    file.getElementsByTagName( "coins" )[ 0 ].childNodes[ 0 ].nodeValue = "6969" 

    with open( inp, "w" ) as fs: 
  
        fs.write( file.toxml() )
        fs.close() 

if __name__ == '__main__':
    main()