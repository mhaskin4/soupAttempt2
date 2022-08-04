#import beautifulsoup and request here
import json
from unittest import result
from bs4 import BeautifulSoup
import requests

#function to get job list from url f'https://www.talent.com/jobs?k={role}&l={location}'

def getJobList(role,location):
    url = f'https://www.talent.com/jobs?k={role}&l={location}'
    # Complete the missing part of this function here
    response = requests.get(f'https://www.talent.com/jobs?k={role}&l={location}')
    # print the status code here
    print(response.status_code)
    soup =   BeautifulSoup(response.text, "html.parser")
    JobDetails = soup.find_all('div', class_='card card__job')
    # Create an array Here
    jobArray = []
    for job in JobDetails:
       jobTitle = job.find('h2', class_='card__job-title').text.strip()
       company = job.find('div', class_='card__job-empname-label').text.strip()
       description = job.find('p', class_='card__job-snippet').text.replace('\n', '').replace("'", "").strip()
       jobDetailsjson = {
           "Title": jobTitle,
           "Company": company,
           "Description": description
       }
       # Add jobDetailsjson to that array
       jobArray.append(jobDetailsjson)
       
    return jobArray



#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    with open('jobDetails.json', 'w') as filePointer:
        json.dump(jobDetails, filePointer)
        print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    print("Enter job location you want to search")
    location = input()
    # Complete the missing part of this function here
    print("Job location: " + location)
    print("Role: " + role)
    resultArray = getJobList(role, location)
    print(resultArray)
    saveDataInJSON(resultArray)


    
if __name__ == '__main__':
    main()