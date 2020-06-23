#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# yay termcolor
#

import os
import subprocess
import getopt
from sys import *
from termcolor import colored, cprint

#############################################################################################################

banner = '''

OSINT USERNAMES

This tool create a login list potentially usable on an LDAP from a first name and a last name.

by g0h4n
https://github.com/g0h4n/

'''

#############################################################################################################

def usage():
    cprint(banner, 'cyan', attrs=['bold'], file=stderr)
    cprint("Usage   : osint-usernames.py -i <LIST_IN>\n", 'red', attrs=['bold'], file=stderr)
    cprint("Example : osint-usernames.py -i example.list\n", 'red', attrs=['bold'], file=stderr)
    cprint("Arguments:\n", 'red', attrs=['bold'], file=stderr)
    cprint("-h --help     -print this help", 'red', attrs=['bold'], file=stderr)
    cprint("-i --in       -Firstname Lastname list.", 'red', attrs=['bold'], file=stderr)
    cprint("")
    exit(0)
#Fin_de_def_usage

#############################################################################################################

def argscheck():
    #No args ? help
    if not len(argv[1:]):
        usage()

    #Check args
    try:
        opts, args = getopt.getopt(argv[1:],"-h-i:", ["help","in"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        exit(1)

    inputfile = ""

    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-i","--in"):
            inputfile = str(a)
        else:
            assert False, "unhandled option"
    return (inputfile)
#End_def_argscheck

#############################################################################################################

def formatname(fullname):
	#Fullname exemple : 'Jean Dupont'
	#Firstname exemlpe : 'Jean'
	#Lastname exemple : 'Dupont'
	fullname = fullname.replace('\n','')
	firstname = fullname.split(' ')[0]
	lastname = fullname.split(' ')[1]

	#Nospacename exemple : 'jeandupont'
	nospacename = firstname + lastname
	
	#Dotnamespace exemple :'jean.dupont'
	dotname = fullname.replace(' ','.')

	#format1 exemple : 'j.dupont'
	format1 = firstname[:1] + '.' + lastname

	#format2 exemple : 'jdupont'
	format2 = firstname[:1] + lastname

	#format3 exemple : 'dupont.j'
	format3 = lastname + '.' + firstname[:1]
	
	#format4 exemple : 'dupontj'
	format4 = lastname + firstname[:1]
	
	#format5 exemple : 'dupontje'
	format5 = lastname + firstname[:2]
	
	#format6 exemple : 'dupontjea'
	format6 = lastname + firstname[:3]

	#format7 exemple : 'jean.d'
	format7 = firstname + '.' + lastname[:1]
	
	#format8 exemple : 'jeand'
	format8 = firstname + lastname[:1]
	
	#format9 exemple : 'jeandu'
	format9 = firstname + lastname[:2]
	
	#format10 exemple : 'jeandup'
	format10 = firstname + lastname[:3]
	
	result = fullname + '\n' + nospacename + '\n' + dotname + '\n' + format1 + '\n' + format2 + '\n' + format3 + '\n' + format4 + '\n' + format5 + '\n' + format6 + '\n' + format7 + '\n' + format8 + '\n' + format9 + '\n' + format10
	
	print(result)
	print(result.lower())
#############################################################################################################

#Main script :
inputfile = argscheck()

with open(inputfile) as f:
	lines = f.readlines()
	for line in lines:
		formatname(line)
