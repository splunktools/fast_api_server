# import requests module
import requests
import json
from requests.auth import HTTPBasicAuth
  

def get_token():

    # Making a get request
    response = requests.get('http://127.0.0.1:8000/auth',
                auth = HTTPBasicAuth('name', 'password'))
    
    # print request object
    if response.status_code!=200:
        print("Unable to authenticate")
    else:
        print("Authenticated")
        session_key = response.text.replace('"', '')
    return session_key

def get_devices():
    session_key=get_token()

    if session_key:
        headers={'api-key':session_key}
        r = requests.get('http://127.0.0.1:8000/getdevices',
                headers=headers)  
        data=json.loads(r.text )
        number_of_results=data["number_of_results"]
        num_pages=data["num_pages"]
        results={'data':[]}
        for i in range(int(num_pages)):
            r = requests.get('http://127.0.0.1:8000/getdevices?page={}'.format(i),
                headers=headers)
            data=json.loads(r.text )
            for item in data["data"]:
                print("{}".format(item))
                results['data'].append(item)
        #r = requests.post('http://127.0.0.1:8000/containdevice?nt_host=CA_VQXG5197',
        #        headers=headers)
        
        #print(data)
        #number_of_results=data["number_of_results"]
        #num_pages=data["num_pages"]

        #print(r.text)

def get_device_by_hostname(hostname):
    session_key=get_token()
    if session_key:
        headers={'api-key':session_key}
        r = requests.get('http://127.0.0.1:8000/getdevice/hostname/{}'.format(hostname),
                headers=headers)  
        print(r.text )

def get_device_by_ip(ip):
    session_key=get_token()
    if session_key:
        headers={'api-key':session_key}
        r = requests.get('http://127.0.0.1:8000/getdevice/ip/{}'.format(ip),
                headers=headers)  
        print(r.text )

def get_device_by_mac(mac):
    session_key=get_token()
    if session_key:
        headers={'api-key':session_key}
        r = requests.get('http://127.0.0.1:8000/getdevice/mac/{}'.format(mac),
                headers=headers)  
        print(r.text )            

def get_users():
    session_key=get_token()

    if session_key:
        headers={'api-key':session_key}
        r = requests.get('http://127.0.0.1:8000/getusers',
                headers=headers)  
        data=json.loads(r.text )
        number_of_results=data["number_of_results"]
        num_pages=data["num_pages"]
        results={'data':[]}
        for i in range(int(num_pages)):
            r = requests.get('http://127.0.0.1:8000/getusers?page={}'.format(i),
                headers=headers)
            data=json.loads(r.text )
            for item in data["data"]:
                print("{}".format(item))
                results['data'].append(item)

def get_device_by_username(user):
    session_key=get_token()
    if session_key:
        headers={'api-key':session_key}
        r = requests.get('http://127.0.0.1:8000/getuser/username/{}'.format(user),
                headers=headers)  
        print(r.text ) 

def get_device_by_userid(user):
    session_key=get_token()
    if session_key:
        headers={'api-key':session_key}
        r = requests.get('http://127.0.0.1:8000/getuser/userid/{}'.format(user),
                headers=headers)  
        print(r.text ) 

def contain_device(device):
    session_key=get_token()
    if session_key:
        if device:
            data={'nt_host':device}
            headers={'api-key':session_key}
            r = requests.post('http://127.0.0.1:8000/containdevice?nt_host={}'.format(device), 
                    headers=headers)  
            print(r.text ) 
        else:
            print("device needs to be supplied")


def main():
    print("******STARTING DRIVER**********")
    get_device_by_hostname("CA_QPHD1397")
    get_device_by_ip("205.155.6.243")
    get_device_by_mac("8E-6D-45-A1-9A-73")
    get_devices()
    get_users()
    get_device_by_username("gburdfieldrr")
    get_device_by_userid(999)
    contain_device("CA_QPHD1397")

if __name__ == "__main__":
    main()