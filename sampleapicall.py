import requests
import asyncio
import concurrent.futures
import time
import random
class PingApi():
    def __init__(self):
        pass

    async def create_alert(self, alert_id):
        starttime = time.time()
        # with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        #         loop = asyncio.get_event_loop()
                
                
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
        
        future1 = loop.run_in_executor(None, requests.post, 'http://localhost:4008/api', None, alert_data)
        response1 = await future1
        print(response1.json())
        
        print("Create_alert time",time.time()-starttime)
    async def edit_alert(self):
        await asyncio.sleep(0.0000000001)
        print("In edit alert")

    async def update_alert(self):
        await asyncio.sleep(1)
        print("In update alert")




if __name__ == "__main__":
    ping_api = PingApi()
    # ping_api.insert_time_zone()
    loop = asyncio.get_event_loop()
    # for i in ["697", "698","699","700","701"]:
    #     count = random.uniform(0.01, 0.1)
    #     loop.run_until_complete(ping_api.create_alert(i, count))
    coroutine1 = ping_api.create_alert('697')
    coroutine2 = ping_api.create_alert('698')
    task1 = loop.create_task(coroutine1)
    task2 = loop.create_task(coroutine2)
    loop.run_until_complete(asyncio.wait([task1, task2]))
    loop.close()
    # loop.run_until_complete(ping_api.create_alert('697'))
    # loop.run_until_complete(ping_api.create_alert('698'))
    # loop.run_until_complete(ping_api.create_alert('699'))
    # loop.run_until_complete(ping_api.create_alert('700'))
    
    # loop.close()
    # loop.close()
    # loop.run_until_complete(ping_api.create_alert())
    # loop.run_until_complete(ping_api.create_alert())
    # loop.run_until_complete(
    #     asyncio.gather( ping_api.create_alert("513"),ping_api.create_alert("514"),ping_api.create_alert("515")))
    # loop.close()
    # ping_api.create_alert()
    # ping_api.create_alert()
    # ping_api.create_alert()

