#!/usr/bin/python3

## Import configParser file. It handles the config File.
import configParser

'''
	Open the 
'''
from gui import make_gui

arrColumns,returnall,path = configParser.read_config()

print("Retun:" + str(returnall) )
make_gui(arrColumns,path,returnall)

