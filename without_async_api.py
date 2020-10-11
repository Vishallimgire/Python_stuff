import requests
import asyncio
import time

class PingApi():
    def __init__(self):
        pass

    def create_alert(self, alert_id):
       
        starttime = time.time()
        print("In create alert", alert_id)
        alert_data = { "frmCntAlertID": alert_id,
                        "frmCntAlertName": "",
                        "frmCntDelivertTo": [ "Email", "MobileApp" ],
                        "frmCntRecipient": "vishal.limgire@roxai.com",
                        "frmCntMobileUser": { "Email": "vishal@roxai.com", "token": "" },
                        "frmCntDataSource": "QlikSenseApplication",
                        "frmCntApplication":
                        { 
                            "Appid":"003828ae-5a46-4433-83e5-895d582571da",
                            "AppName": "Consumer Goods Sales" 
                        },
                        "frmCntMeasures":
                        { "Appid":"003828ae-5a46-4433-83e5-895d582571da",
                            "pingMeasuresqLabel":"Northeast Revenue",
                            "pingMeasuresqDef": "Sum({$<[Region Name]={'Northeast'}>}   [Sales Quantity]*[Sales Price])" },
                        "frmCntCurrentValue": 17225219.810000027,
                        "frmCntCondition": "greaterthan",
                        "frmCntFunction": 12324,
                        "frmCntNumberformat": "",
                        "frmCntLoopDiamention": [],
                        "diamentionValue": "",
                        "filterValue": "",
                        "InsertBy": "m",
                        "frmCntFieldValue": { "Field": [], "Value": "" },
                        "frmCntTrigger": "Scheduled",
                        "UserID": "User8",
                        "frmGrpShedules":
                        { "SUN": "",
                            "MON": "",
                            "TUE": "",
                            "WED": "",
                            "THU": "",
                            "FRI": "",
                            "SAT": "",
                            "startTimeSchedule": "15:27",
                            "endTimeSchedule": "15:28",
                            "dateSchedule": "",
                            "repeatCounts": "",
                            "intervalTimeSchedule": "1"} 
                            }
        
        response = requests.post("http://localhost:4008/api",json = alert_data)
       
        print(response.json())
        print("Create_alert time",time.time()-starttime)

    def delete_alert(self,id):
        response = requests.delete("http://localhost:4008/api/{}".format(id))
        print(response.status_code)
   

if __name__ == "__main__":
    ping_api = PingApi()
    ping_api.create_alert('701')
    ping_api.create_alert('702')
   
    # ping_api.delete_alert("5b9f6adebadb9f27e957573f")
    

