#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:     Project Creator
# Purpose:  Creates a template for Python, R and C++ Programs.
#           Will add Makefile, C, and HTML/CSS support later
# Version:  1.0
# Author:   Jack Simpson
# Email:    jack.simpson@anu.edu
# Created:  2015-02-06
#-------------------------------------------------------------------------------
# These modules are available in the Standard Library of Python 2.7 and 3.4
import sys
import os
import datetime

AUTHOR = 'Jack Simpson'
EMAIL = 'jack.simpson@anu.edu.au'
DATE = datetime.date.today()

def create_cpp_project():
    '''Generates a c++ template'''
    contents = '''/*******************************************************************************
* Name:     
* Purpose:  
* Version:  1.0
* Author:   %s
* Email:    %s 
* Created:  %s
*******************************************************************************/

#include <iostream>
#include <string>
#include <vector>

int main (int argc, char *argv[])
{
    
    return 0;
}


''' % (AUTHOR, EMAIL, DATE)
    return contents

def create_python_project():
    '''Generates a Python project'''
    contents = '''#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:     
# Purpose:  
# Version:  1.0
# Author:   %s
# Email:    %s
# Created:  %s
#-------------------------------------------------------------------------------
# These modules are available in the Standard Library of Python

# These modules come from third party libraries


def main():
    

if __name__ == "__main__":
    main()
        
''' % (AUTHOR, EMAIL, DATE)
    return contents 

def create_r_project():
    '''Generates an R program template'''
    contents = '''#!/usr/bin/env Rscript
#-------------------------------------------------------------------------------
# Name:     
# Purpose:  
# Version:  1.0
# Author:   %s
# Email:    %s
# Created:  %s
#-------------------------------------------------------------------------------

rm(list=ls())                                   # clear workspace variables
setwd("")                                       # set working directory

packages <- c("", "")                           # packages to install and load
install.packages(packages)
lapply(packages, library, character.only = T)   # load all packages

data_file_name <- ""
csv_file <- read.table(data_file_name, sep = ",", head = F, skip = 0, stringsAsFactors = F)


''' % (AUTHOR, EMAIL, DATE)
    return contents


def create_web_project():
    '''Generates a web project in a folder with HTML, CSS and JS'''
    pass

def create_c_project():
    '''Generates a C program template'''
    pass

def create_makefile_project():
    '''Generates a makefile template'''
    pass

def main():
    if len(sys.argv) != 2:
        sys.exit("Please supply the path to the file")    
    
    file_contents = ''
    filename, extension = os.path.splitext(sys.argv[1])
    
    if extension  == ".py":
        file_contents = create_python_project()

    elif extension == ".cpp":
        file_contents = create_cpp_project()

    elif extension == ".R":
        file_contents = create_r_project()

    else:
        sys.exit("Invalid file")

    open_file = open(sys.argv[1], 'w')
    open_file.write(file_contents)
    open_file.close()

if __name__ == "__main__":
    main()
