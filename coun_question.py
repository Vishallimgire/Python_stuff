import re
import random


def set_appName(str):
    app_name = str
    required.remove('Application')
    return(app_name)
    
def set_measure(str):
    measure = str
    required.remove('Measures')
    return(measure)
    
def set_scheduleDate(str):
    schedule_date = str
    required.remove('Schedule_date')
    return(schedule_date)    
    
def set_scheduleTime(str):
    days = []
    Schedule_time = str
    required.remove('Schedule_time')
    i = 0

    num_of_days = input("On how many days do you want this alert?")
    if(num_of_days.lower() == 'everyday'):
        days = main_dict['prompt']['everyday']
    while (i<int(num_of_days)):
        day = input("Enter Day for alert:")
        days.append(day)
        i = i + 1
    return(Schedule_time,days)


Name = 'Akash'
main_dict = {
"possible_tasks" : ['alert','Applications'],
"followup" : {'alert':['Application','Measures','Schedule_time','Schedule_date']},
"foll_back": ['Sorry, But I didnt understand yur selection','Please enter once again','Invalid option, enter again'],
"prompt":  {'everyday':['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']}
}

caller = {
    "set_appName": set_appName,
    "set_scheduleDate": set_scheduleDate,
    "set_measure": set_measure,
    "set_scheduleTime": set_scheduleTime,
}

# print(people[1]['name'])
import pdb;pdb.set_trace()
task = input("Welcome %s, What can I do for you today?" % (Name))

for val in main_dict["possible_tasks"]:
    if(val in task.lower()):
        required = (main_dict['followup'][val])
        
count = 0

def identifier(input):
    if re.match("^([A-Z][a-zA-Z]*\s*)+$", Input1):
        call_func = "set_appName"
    elif re.match("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$", Input1):
        call_func = "set_scheduleDate"
    elif re.match("^[A-Za-z]+$", Input1):
        call_func = "set_measure"
    elif re.match("^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$", Input1):
        call_func = "set_scheduleTime"
    else:
        print(random.choice(main_dict["foll_back"]))    
            
    return call_func
    
Iterations = len(required)
while (count < Iterations):
    item = random.choice(required)
    Input1 = input("Please enter your %s: " % (item))
    
    call_func = identifier(Input1)
    
    if call_func in caller:
        extracted_data = caller[call_func](Input1)
        print(extracted_data)
        count = count + 1
        
    
        
# print("")        
# print("Alert Information ")        
# print("Application Name: ",App_Name)
# print("Measures: ",Measures)
# print("Schedule:",Schedule_Date)
# print("Time:", Schedule_Time)
# print("Days:", days1)