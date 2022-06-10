#import the required modules for this application

import requests
import datetime as DT

''' 
This Section is for the module definitions that I have implemented for this 
program.   
'''

def get_api_data(): 
  # set variables, set time period 
  today = DT.date.today()
  week_ago = today - DT.timedelta(days=7)
  #I picked a challeging repo with several pull requests in flight.  I also tested on pygithub which only has 3 or 4 PRs. 
  #I will include testing results in the readme
  owner = "argoproj"
  repo = "argo-cd"
  print_email_info(repo)
  num = 1
  size = 0
  #Without being in the network, I am doing a non-token request to the api for future enhancement we should 
  #store a token that is kept in some type of secrets enginge.  
  query_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
  #Putting a while loop to enter the logic so that if the initial count is 1 or if the return size of data is the full 100,
  #we can check the next page for more information
  while (size == 100 or  num == 1): 
    params = {
      "is"       : "pr",
      "per_page" : 100,
      "state"    : "all",
      "since"    : week_ago,
      "page"     : num
    }
    #this call is basically getting the data back from the api
    data = requests.get(query_url, params=params)
    #call to manipulate the data and print it out, if we were using an email client, we would store this in array and send that 
    #as the email body or even better create a cvs file and send it as an attachement in email. 
    manip_data(data)
    #basic calculations to see if we get the maximum results and increment the counter
    size = len(data.json())
    num = num + 1

def print_email_info(repo):
  #set variable as if I was emailing this to someone
  from_email = "from: tony.powell22@outlook.com"
  to_email = "to: tp2870@gmail.com"
  subject = "subject: Report for open/closed pull request over the last week for repo" 
  #printing email header information as I did not do email and just printed to the screen
  print ("\n\n")
  print (from_email)
  print (to_email,"\n\n")
  print (subject,repo,"\n\n")
  #printing actual body columns of the email message
  header = "PR".ljust(15)+"Date Created".ljust(30)+"Status".ljust(5)
  print (header)

def manip_data(return_data):
  #basically going through the json data and making it possible to format it into a table for easier consumption
  for temp in return_data.json():
    pr=str(temp['number'])
    cdate = temp['created_at']
    status = temp['state']
    report_data = pr.ljust(15)+cdate.ljust(30)+status.ljust(5)
    print(report_data)

#this is my main line, I could do an __init__main__ but decided just to call the function. 
#calling main runner of the application and getting data and repo back 
get_api_data()
