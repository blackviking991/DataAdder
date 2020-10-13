#!/usr/bin/python3
import configparser

'''
	Path to Configuration File.
'''
CONFIGFILE_PATH = 'config.ini'

def read_config():
	arrFields = []
	returnAll = 0
	'''
		Default filename in case patToDataFile is not specified.
	'''
	pathToDataFile = "defaultfile.dat"

	config = configparser.ConfigParser()

	'''
		Read the configuration file.
	'''
	config.read(CONFIGFILE_PATH)

	if 'Fields' in config:
		arrFieldsTemp = config['Fields']
		for x in arrFieldsTemp:
			if arrFieldsTemp[x].casefold() == "yes".casefold():
				arrFields.append(x)

	if 'Search' in config and 'ReturnAll' in config['Search']:
		temp = config['Search']['ReturnAll']
		if temp.casefold() == "yes".casefold():
			returnAll = 1

	if 'Misc' in config and 'pathToDataFile' in config['Misc']:
		temp = config['Misc']['pathToDataFile']

		pathToDataFile = temp

	return (arrFields,returnAll,pathToDataFile)

'''
	If this file is executed, then read the configuration file.
'''
if __name__ == "__main__":
	arrFields,returnAll,pathToDataFile = read_config()
	