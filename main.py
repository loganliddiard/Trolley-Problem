import KNN
import sys
import csv
import time
import analysis
from survey import Survey
import os

def usage():
    print("Here are your options:")
    print("train    -   train KNN model")
    print("predict  -   see what the KNN model would do in a random situation")
    print("analysis -   run trained model through a bunch of simulations and get report for results")
    print("survey   -   decide what you would do in a random trolly problem and give it to the model")
    print("exit     -   exit program\n\n")



if __name__ == "__main__":

    model = None
    
    
    #data = "trolley.csv"
    data = "dummy_data.csv"
    survey = "survey.csv"

    if data != "trolley.csv":
        print(f"Warning! You are working with {data} for you dataset!")

    while True:
        # Clearing the Screen
        os.system('cls')
        
        print("What would you like to do?\n")
        usage()
        action = input()
        wait = False
        match action.lower():

            case "exit":
                print("Goodbye!")
                sys.exit()
            case "train":
                print("Creating KNN model...")
                model = KNN.KNN(data)
                model.visualize()
                print("KNN model created!")
            
            case "predict":
                wait = True
                if model == None:
                    print("No current model!")
                else:
                    Survey(1,'c',model)
            case "survey":

                print("\nWhat would you do in the following scenarios...\n\n\n")
                survey = Survey(3)
                print(survey.info)

                # Open the CSV file in write mode
                with open(data, "a", newline="") as file:

                    # Create a CSV writer object
                    writer = csv.writer(file)


                    # Write the data rows
                    writer.writerows(survey.info)
            case "analysis":

                data = []
                wait = True
                if model == None:
                    print("No current model!")
                    break

                analysis.run_analysis(model)



            case _:
                usage()
        if wait: 
            time.sleep(2)
        

