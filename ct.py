#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:         Code Template
# Purpose:      Creates a template for Python, R, C and C++ Programs.
#               Will add Makefile, and HTML/CSS support later
# Version:      1.0
# Licence:      MIT License
# Author:       Jack Simpson
# Email:        jack.simpson@jacksimpson.co
# Created:      2015-02-06
#-------------------------------------------------------------------------------
# These modules are available in the Standard Library of Python 2.7 and 3.4
import sys
import os
import datetime

AUTHOR =    'Jack Simpson'
EMAIL =     'jack@jacksimpson.co'
DATE =      datetime.date.today()
LICENCE =   'MIT Licence'

def create_cpp_project():
    '''Generates a c++ template'''
    contents = '''/*******************************************************************************
* Name:         
* Purpose:      
* Version:      1.0
* Licence:      %s
* Author:       %s
* Email:        %s 
* Created:      %s
*******************************************************************************/

#include <iostream>
#include <string>
#include <vector>

int main (int argc, char *argv[])
{
    
    return 0;
}


''' % (LICENCE, AUTHOR, EMAIL, DATE)
    return contents

def create_python_project():
    '''Generates a Python project'''
    contents = '''#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:     
# Purpose:  
# Version:      1.0
# Licence:      %s
# Author:       %s
# Email:        %s
# Created:      %s
#-------------------------------------------------------------------------------
# These modules are available in the Standard Library of Python

# These modules come from third party libraries


def main():
    

if __name__ == "__main__":
    main()
        
''' % (LICENCE, AUTHOR, EMAIL, DATE)
    return contents 

def create_r_project():
    '''Generates an R program template'''
    contents = '''#!/usr/bin/env Rscript
#-------------------------------------------------------------------------------
# Name:         
# Purpose:      
# Version:      1.0
# Licence:      %s
# Author:       %s
# Email:        %s
# Created:      %s
#-------------------------------------------------------------------------------

rm(list=ls())                                   # clear workspace variables
setwd("")                                       # set working directory

packages <- c("", "")                           # packages to install and load
install.packages(packages)
lapply(packages, library, character.only = T)   # load all packages

data_file_name <- ""
csv_file <- read.table(data_file_name, sep = ",", head = F, skip = 0, stringsAsFactors = F)


''' % (LICENCE, AUTHOR, EMAIL, DATE)
    return contents



def create_c_project():
    '''Generates a C template'''
    contents = '''/*******************************************************************************
* Name:         
* Purpose:      
* Version:      1.0
* Licence:      %s
* Author:       %s
* Email:        %s 
* Created:      %s
*******************************************************************************/

#include <stdio.h>

int main (int argc, char *argv[])
{
    
    return 0;
}


''' % (LICENCE, AUTHOR, EMAIL, DATE)
    return contents

def create_makefile_project():
    '''Generates a makefile template'''
    pass

def create_web_project():
    '''Generates a web project in a folder with HTML, CSS and JS'''
    pass

def main():
    if len(sys.argv) == 1:
        sys.exit("Please specify the name of at least one program: e.g. test.py")    
    
    for each_file in sys.argv[1:]:
        directories = os.path.dirname(each_file)
        if directories:
            if not os.path.exists(directories):
                os.makedirs(directories)
        
        filename, extension = os.path.splitext(each_file)
    
        if extension  == '.py':
            file_contents = create_python_project()

        elif extension == '.cpp':
            file_contents = create_cpp_project()

        elif extension == '.c' or extension == '.cc':
            file_contents = create_c_project()

        elif extension == '.R' or extension == '.r':
            file_contents = create_r_project()

        else:
            print('Could not recognise file ' + each_file)
            continue

        open_file = open(each_file, 'w')
        open_file.write(file_contents)
        open_file.close()

if __name__ == "__main__":
    main()
