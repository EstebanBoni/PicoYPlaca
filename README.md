# PicoYPlaca
This program is meant to be used a way to know if a car can drive during Pico y Placa restriction on the city of Quito.

## General Info

This application works based on the law that the city of Quito implemented on 2010 where vehicles couldnt be driving around the city in certain days and certain hours.
On pico y placa hours cars would be restricted to not drive between 7:00 to 9:30 and 16:00 to 19:30.
License plates with the last digit 1 and 2 had pico y placa on Monday.
License plates with the last digit 1 and 2 had pico y placa on Tuesday.
License plates with the last digit 1 and 2 had pico y placa on Wednesday.
License plates with the last digit 1 and 2 had pico y placa on Thuersday.
License plates with the last digit 1 and 2 had pico y placa on Friday.

## How to use 

This appplication runs on python 3.8 version 

Run the .py file on spider. A new window will open where information can be written. 
The format of the license plate must have 7 characters and must end in a number. If not it will trigger an error message.
The date and hour must be valid otherwise an error box will appear.
Finally the apropiate format for date is: dd-mm-yyyy. Any separation between day month or year is also valid.
An correct example would be 22/02/2021 or 2-02-2021
An incorrect example would be 02222021 or 2/22/2021

## Technologies
***
A list of technologies used within the project:

* [datetime ](https://docs.python.org/3/library/datetime.html)
* [tkinter] (https://docs.python.org/3.8/library/tkinter.html?highlight=tkinter#module-tkinter)

