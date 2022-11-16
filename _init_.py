import logging
import json

import azure.functions as func


def main(req: func.HttpRequest , inputTable) -> func.HttpResponse:
    
   #Bring in data from table
   data = json.loads(inputTable)
   #Convert json to a string
   data2 = json.dumps(data)

   #Azure tables returns data as an array, we'll need to remove the brackets  
   data3 = data2.replace("[" , '')   
   data4 = data3.replace("]" , '')
 
   #Return the modified content
   return func.HttpResponse( f"{data4}")