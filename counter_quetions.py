import re
import random
import json

class CounterQuetions():
    def __init__(self):
        with open("./counter_quetion.json", "r") as fp:
            self.main_dict = json.load(fp) 
        self.caller = { 
                    "set_appName": self.set_appName,
                    "set_scheduleDate": self.set_scheduleDate,
                    "set_measure": self.set_measure,
                    "set_scheduleTime": self.set_scheduleTime,
                    }

    def set_appName(self, str, required):
        app_name = str
        required.remove('Application')
        #self.stored_data["app_name"] = app_name
        return {"app_name" : app_name}
    
    def set_measure(self, str, required):
        measure = str
        required.remove('Measures')
        #self.stored_data["measures"] = measure
        return {"measures" : measure}
    
    def set_scheduleDate(self, str, required):
        schedule_date = str
        required.remove('Schedule_date')
        #self.stored_data["schedule_date"] = schedule_date
        return {"schedule_date" : schedule_date}    
    
    def set_scheduleTime(self, str, required):
        days = []
        schedule_time = str
        required.remove('Schedule_time')
        num_of_days = input("On how many days do you want this alert?")
        if(num_of_days.lower() == 'everyday'):
            days = self.main_dict['prompt']['everyday']
        else:
            for i in range(int(num_of_days)):
                day = input("Enter Day for alert:")
                days.append(day)
        #self.stored_data["schedule_time"] = schedule_time
        #self.stored_data["days"] = days
        return{"schedule_time" :schedule_time, "days": days}

    def main(self):
        try:
            stored_data = {}
            name = 'Akash'
            # print(people[1]['name'])
            # import pdb;pdb.set_trace()
            task = input("Welcome %s, What can I do for you today?" % (name))
            required = ""
            for val in self.main_dict["possible_tasks"]:
                if(val in task.lower()):
                    required = (self.main_dict['followup'][val])
            
            if required:
                for count in range(len(required)):
                    item = random.choice(required)
                    input1 = input("Please enter your %s: " % (item))
                    call_func = self.identifier(input1)
                    if call_func in self.caller:
                        extracted_data = self.caller[call_func](input1, required)
                        stored_data.update(extracted_data)
                        
            else:
                print("Please Provide appropriate data")
        except Exception as e:
            print("Exception in main function:", e)       
        print("All collected data is", stored_data)
        return stored_data

    def identifier(self, input1):
        if re.match("^([A-Z][a-zA-Z]*\s*)+$", input1):
            call_func = "set_appName"
        elif re.match("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$", input1):
            call_func = "set_scheduleDate"
        elif re.match("^[A-Za-z]+$", input1):
            call_func = "set_measure"
        elif re.match("^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$", input1):
            call_func = "set_scheduleTime"
        else:
            print(random.choice(self.main_dict["fallback"]))    
                
        return call_func
    

if __name__ == "__main__":
    counter_quetion = CounterQuetions()
    counter_quetion.main()     
    
        
# print("")        
# print("Alert Information")        
# print("Application Name: ",App_Name)
# print("Measures: ",Measures)
# print("Schedule:",Schedule_Date)
# print("Time:", Schedule_Time)
# print("Days:", days1)