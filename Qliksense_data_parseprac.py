import requests
import json
import redis
from ast import literal_eval
import time

class QliksenseData():
    def __init__(self):
       #self.r = redis.StrictRedis(charset = "utf-8", decode_responses = True)
       self.redis_conn = redis.StrictRedis()


    def qlik_connct(self):
        try:
            r = requests.Session()
            passport_data ={"passport": { "user": {
                    "IsActive": True,
                    "_id": "5bc4329429b6312302423692",
                    "PingUserID": "User8",
                    "PingUserName": "testuser1",
                    "PingUserDirectory": "qlik-sense",
                    "PingUserAccess": "Manage in Ping",
                    "EmailID": "vishal.limgire@roxai.com",
                    "password": "$2a$10$lCrY1WFVu6m2/Kt1G7ynr.2AIvwPR/Ee88JzI5Lv6tdHPk7/etUBm",
                    "PingMemberID": "1",
                    "PingGroupID": "1",
                    "PingRole": "Administrator",
                    "InsertBy": "m",
                    "LoginUserID": "User5",
                    "InsertDate": "2018-10-15T06:24:20.000Z",
                    "UpdateDate": "2018-10-15T06:24:20.000Z",
                    "__v": 0
                }
                }
                }

            r.sessions = passport_data
            response = r.get("http://localhost:4009/QlikSense/" )
            qlik_all_data = json.loads(response.text)
            print(type(qlik_all_data))
            print(qlik_all_data)
            self.redis_conn.setex("qlik_all_data", 600, qlik_all_data)
            print("Data stored successfully")
        except Exception as e:
            print("Exception in qlik_connct:", e)

    def qlik_ticket_gen(self):
        requests.get("http://localhost:4009/QlikSense/")

    def app_list(self):
        #import pdb;pdb.set_trace()
        qlik_app_list = []
        try:
            qlik_all_data = self.redis_conn.get("qlik_all_data")

            if qlik_all_data:
                qlik_all_data = literal_eval(qlik_all_data.decode('utf8'))
                s = json.dumps(qlik_all_data)
                qlik_apps_data = json.loads(s)
                #print(qlik_apps_data)
                for qlik_app in qlik_apps_data:
                    qlik_app_list.extend(qlik_app["pingAppList"])
        except Exception as e:
            print("Exception in applist", e)
        print(qlik_app_list)
        return qlik_app_list

    def measure_list(self, app_name):
        qlik_measure_list = []
        qlik_mea_list = []
        try:
            qlik_all_data = self.redis_conn.get("qlik_all_data")
            #print(qlik_all_data)
            #import pdb;pdb.set_trace()
            if qlik_all_data:
                qlik_all_data = literal_eval(qlik_all_data.decode('utf8'))
                s = json.dumps(qlik_all_data)
                qlik_apps_data = json.loads(s)
                for qlik_app in qlik_apps_data:
                    if qlik_app["pingAppList"][0]['appName'] == app_name:
                        qlik_measure_list.extend(qlik_app["pingAppObjects"][0]["measures"])
                #print(qlik_measure_list)
                for id, qlik_measure in enumerate(qlik_measure_list):
                      qlik_mea_dict = {}

                      measure_id = str(int(time.time()))+ "M" + str(id)
                      qlik_mea_dict["Id"] = measure_id
                      qlik_mea_dict["Name"] = qlik_measure["pingMeasuresqLabel"]
                      qlik_mea_dict["Expression"] = qlik_measure["pingMeasuresqDef"]
                      qlik_mea_list.append(qlik_mea_dict)
                      #print(qlik_mea_list)

        except Exception as e:
            print("Exception in measure list", e)
        print(qlik_mea_list)
        return qlik_mea_list

    def dimension_list(self, app_name):
        qlik_dimension_list = []
        qlik_dim_list = []
        try:
            qlik_all_data = self.redis_conn.get("qlik_all_data")

            if qlik_all_data:
                qlik_all_data = literal_eval(qlik_all_data.decode('utf8'))
                s = json.dumps(qlik_all_data)
                qlik_apps_data = json.loads(s)
                for qlik_app in qlik_apps_data:
                    if qlik_app["pingAppList"][0]['appName'] == app_name:
                        qlik_dimension_list.extend(qlik_app["pingAppObjects"][0]["dimensions"])

                for id, qlik_dim in enumerate(qlik_dimension_list):
                      qlik_dim_dict = {}
                      dimension_id = str(int(time.time()))+ "D" + str(id)
                      qlik_dim_dict["DimensionID"] = dimension_id
                      qlik_dim_dict["DimensionName"] = qlik_dim["pingDiamentionTitle"]
                      qlik_dim_list.append(qlik_dim_dict)
                #print(qlik_dim_list)

        except Exception as e:
            print("Exception in measure list", e)
        print(qlik_dim_list)
        return qlik_dim_list

    def measure_value(self):
        data = ""
        try:

            # json_data = { "qdef": 'Count( {$<[Status]={\'New\'} >} Distinct %CaseId )',
            #             "appid": '57572144-cb68-4724-baf6-2eafe6e0aa23' }
            #json_data = { "qdef": "Sum([Sales Quantity])",
            #              "appid": "4e470736-ba3a-4490-981a-916cdc0d9fc9" }
            json_data = { "qdef": "Sum([Opportunity Amount]*[Opportunity Probability]*$(='ExRate_USD'))", "appid": "6a15cb1a-b285-4cbb-b38b-218adb494899" }
            requests.get("http://localhost:4009/QlikSenseMeasures/")
            response = requests.post("http://localhost:4009/QlikSenseMeasures/getMeasureValue", json=json_data)
            #print(response.json())
            data = response.json()
        except Exception as e:
            print("Exception in measure_value", e)
        print(data)
        return data

    def filter_by_dimension(self):
        data = ""
        try:
            json_data = {
                          "appid": '57572144-cb68-4724-baf6-2eafe6e0aa23',
                          "qdefD": 'Priority' }
            response = requests.post("http://localhost:4009/QlikSenseMeasures/getFielddValue", json=json_data)
            #print(response.json())
            data = response.json()
        except Exception as e:
            print("Exeception in filter_by_dimension", e)
        print(data)
        return data

    def get_filter_value(self):
        data = ""
        try:
            json_data = { "appid": '003828ae-5a46-4433-83e5-895d582571da',
                        "filter": [
                                    { "Field": 'State', "Value":  [ 'ME', 'MA']
                                    }
                                ]
                        }
            response = requests.post("http://localhost:4009/QlikSenseMeasures/getFilterValue", json=json_data)
            #print(response.json())
            data = response.json()
        except Exception as e:
            print("Exception in get_filter_value", e)
        print(data)
        return data

    def all_alertdata_userid(self, userid):
        all_alert_data = ""
        try:
            response = requests.get("http://localhost:4009/api/LoggedUserWiseAlertData/{}".format(userid))
            if response.status_code == 200:
                all_alert_data = response.json()
        except Exception as e:
            print("Exception in all_aletdata_userid:", e)
        print(all_alert_data)
        return all_alert_data

    def all_alertdata_isnotactive(self, userid):
        all_alert_data = ""
        try:
            response = requests.get("http://localhost:4009/api/LoggedUserWiseAlertData/Notactive/{}".format(userid))
            if response.status_code == 200:
                all_alert_data = response.json()
        except Exception as e:
            print("Exception in all_aletdata_userid:", e)
        print(all_alert_data)
        return all_alert_data

    def alert_by_alertid(self, alert_id):
        alert_data = {}
        try:
            alert_data = requests.get("http://localhost:4009/api/getdatabyalertid/{}".format(alert_id))
            if alert_data.status_code == 200:
                alert_data = alert_data.json()

        except Exception as e:
            print (e)
        print(alert_data)
        return alert_data

    def edit_alert(self, alert_id):
        try:
            edit_data = {
                    "frmCntAlertName": "",
                    "frmCntDelivertTo": [" Email,MobileApp" ],
                    "frmCntRecipient": "rohit@roxai.com",
                    "frmCntDataSource": "QlikSenseApplication",
                    "frmCntApplication":
                    {
                        "Appid": "87903735-db37-4206-b143-455f4d2d55b3",
                        "AppName": "Sales and Product Performance"
                    },
                    "frmCntMeasures":
                    {
                        "Appid": "87903735-db37-4206-b143-455f4d2d55b3",
                        "pingMeasuresqLabel": "Gross Sales Amount",
                        "pingMeasuresqDef": "sum(Quantity * UnitPrice)"
                    },
                    "frmCntCurrentValue": "1640.5700303350502",
                    "frmCntCondition": "greaterthan",
                    "frmCntFunction": 123,
                    "frmCntNumberformat": "",
                    "diamentionValue": [ "" ],
                    "filterValue": "",
                    "frmCntFieldValue": { "Field": [], "Value": "" },
                    "frmCntTrigger": "Scheduled",
                    "UserID": "User6",
                    "frmGrpShedules":
                    {
                        "SUN": "",
                        "MON": "",
                        "TUE": "",
                        "WED": "",
                        "THU": "",
                        "FRI": "",
                        "SAT": "",
                        "startTimeSchedule": "15:19",
                        "endTimeSchedule": "",
                        "dateSchedule": "",
                        "repeatCounts": "",
                        "intervalTimeScheduleMins": "",
                        "intervalTimeScheduleHours": ""
                    }
                }
            response = requests.put("http://localhost:4009/api/getdatabyalertid/{}".format(alert_id),data = edit_data)
            edit_alert = response.json()
            if edit_alert["nModified"] == 1:
                print("your record updated successfully")

            else:
                print("not updated")
        except Exception as e:
            print("Exception in edit_alert:", e)


if __name__ == '__main__':
    obj = QliksenseData()
    obj.qlik_connct()
    obj.app_list()
    #obj.measure_list('Sales Management and Customers Analysis')
    #obj.dimension_list('Sales Management and Customers Analysis')
    #obj.measure_value()
    #obj.filter_by_dimension()
    #obj.get_filter_value()
    #obj.edit_alert("114")
    #obj.alert_by_alertid("114")
    #obj.all_alertdata_userid("User8")
    #obj.all_alertdata_isnotactive("User8")
