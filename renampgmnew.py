# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:11:50 2020

@author: DJML
"""

import os
def main():
   i = 0
   path="E:/VTU_database/ripeness/Aug_ripe/ripe/"
   for filename in os.listdir(path):
       if i<10:
          my_dest ="IP_RIP_00" + str(i) + ".jpg"
          my_source =path + filename
          my_dest =path + my_dest
          os.rename(my_source, my_dest)
          i += 1
       elif i<100:
          my_dest ="IP_RIP_0" + str(i) + ".jpg"
          my_source =path + filename
          my_dest =path + my_dest
          os.rename(my_source, my_dest)
          i += 1
       else:
          my_dest ="IP_" + str(i) + ".jpg"
          my_source =path + filename
          my_dest =path + my_dest
          os.rename(my_source, my_dest)
          i += 1
          
main()