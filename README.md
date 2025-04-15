# analyzeANDwait
Send a file to Spectra Analyze, then wait for the analysis to be done.

## Requirements
1) Python Requests installed via PyPi: https://pypi.org/project/requests/

#### Command Line Arguments
1) --filePath : Full path to the file to upload
2) --sampleName : Name you want to appear in the Analyze Dashboard
3) --token : API token
4) --url : URL of the A1000/Analyze instance
5) --wait : Waits until the file is finished processing before ending the script 

##### Example
```
python3 send2analyze.py --filePath ./Examples/7zz --sampleName 7z --token 80sr098d098sdf098gsdf --url a1000.example.com --wait true
```
