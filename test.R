#!/usr/bin/env Rscript
#-------------------------------------------------------------------------------
# Name:     
# Purpose:      
# Version:      1.0
# Licence:      MIT Licence
# Author:       Jack Simpson
# Email:        jack.simpson@jacksimpson.co
# Created:      2015-02-12
#-------------------------------------------------------------------------------

rm(list=ls())                                   # clear workspace variables
setwd("")                                       # set working directory

packages <- c("", "")                           # packages to install and load
install.packages(packages)
lapply(packages, library, character.only = T)   # load all packages

data_file_name <- ""
csv_file <- read.table(data_file_name, sep = ",", head = F, skip = 0, stringsAsFactors = F)


