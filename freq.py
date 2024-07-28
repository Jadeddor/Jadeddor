"""
File:    freq.py
Author:  Jade Dorsainvil
Date:    9/30/2022
Section: 21
E-mail:  jdorsai1L@umbc.edu
Description:
  find how many times a number occurs in a list
"""
size_of_data =6

def main():

  #my data list and variable 
  dataList= []
  counter =0
  #For loop to determine how many items enter a list 
  for i in range(size_of_data):
    print("Please enter value #",(i+1),"into the data list:", end='')
    value=(int(input("")))
    dataList.append(value)
  # input for the number you want to check for frequency 
  frequency = int(input("Please enter a number to check the frequency:"))
  # add to counter number of times that a number shows up in a list
  for i in range(size_of_data):
    value=dataList[i]
    if(frequency == value):
      counter += 1
      
  print("We found ", counter, "value(s) of", frequency,"within the data list given")
main()
