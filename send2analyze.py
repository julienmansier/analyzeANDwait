import requests
import argparse
import json
import time

wait = False
token = ""
url = ""

def ready(hashid):
    full_url = "https://"+url+"/api/samples/status/"
    payload = {"hash_values": [hashid]}

    headers = {
        "Authorization": f"Token {token}"
    }

    # Add verify=False in the request if you are using a self-signed SSL certificate
    response = requests.post(full_url, headers=headers, json=payload)

    if response.ok:
        status = response.json()["results"][0]["status"]
        return status
    else:
        # Issue with request
        print(f"Status Code: {response.status_code}")
        print(response.text)
        return "ERROR"

def main():
    global wait, token, url

    parser = argparse.ArgumentParser(description="Process needed files")
    parser.add_argument('--filePath', type=str,required=True, help="Full File Path")
    parser.add_argument('--sampleName', type=str,required=True, help="File Name")
    parser.add_argument( '--token', type=str,required=True, help="API Token")
    parser.add_argument( '--url', type=str,required=True, help="Spectra Analyze URL")
    parser.add_argument( '--wait', type=str, help="Wait until processing completes?")
    args = parser.parse_args()

    # Change the values of hash_value and token
    file_path = args.filePath
    sample_name = args.sampleName
    token = args.token
    url = args.url

    if 'true' in args.wait.lower():
        wait = True

    full_url = "https://"+url+"/api/uploads/"

    files=[('file', (sample_name, open(file_path,'rb'),'application/octet-stream'))]

    headers = {"Authorization": f"Token {token}"}
    
    response = requests.post(full_url, headers=headers, files=files)

    if response.ok:
        hashid = response.json()["detail"]["sha1"]
    else:
        # Issue with request
        print(f"Status Code: {response.status_code}")

    
    if wait:
        while ready(hashid) != "processed":
            print("Waiting on sample to process...")
            time.sleep(1)
        print("Sample has been processed and has the sha1: "+ hashid)
    else:
        print("Sample has been uploaded and has the sha1: "+ hashid)



if __name__ == "__main__":
    main()