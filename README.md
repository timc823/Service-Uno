![Program Image](https://github.com/cct823/Service-Uno/blob/master/Source/uno.png)

# Install and Run
**Install Program**

    Install virtualenv:
    ~Service-Uno> pip install virtualenv

    Create virtual environment:
    ~Service-Uno> virtualenv venv

    Activate virtual environment:
    Windows:
        ~Service-Uno> .\venv\Scripts\activate
    Mac:
        ~Service-Uno> source venv/bin/activate


**Run Program**    

    Clone the repo:
    git clone https://github.com/cct823/Service-Uno.git

    Install packages:
    ~Service-Uno> pip install -r requirements.txt

    Run customer rating program :
    Windows:
        python serviceuno.py
    Mac:
        python3 serviceuno.py
        
    Run dashboard program :
    Windows:
        python dash.py
    Mac:
        python3 dash.py
**Run Tests**

    pytest -v tiptest.py



# Course
IST-303 Software Development (Claremont Graduate University)


# Team Name:
ServiceUno
# Team Members:
Jovany Funes  
Tim Chen  
Penny Peng    
Kevin Jin

# ServiceUNO Project (Concept):

ServiceUNO will be an application with a web interface; it will eventually be integrated by using hardware such as the raspberry pi. ServiceUNO will collect key data that will be quantified based on key services provided by the server and bartender. This information will also be valuable to businesses; the business will benefit from the data to evaluate customer service experience and improve their services by customer feedback. ServiceUNO will rate the server and feature their great customer service skills to maximize their gaining potential (TIPS).


# Stake Holder

## Customers

Customers will be our main focus user, we noticed that customers at restaurants have had complaints and bad experiences with the service at restaurants. When customers want to complain, they have outlets such as Yelp, but this platform rates the restaurant not the server. With our program we will create a platform that will allow customers to rate the service of a server so when people visit the restaurant they know what to expect from their service. Our program will also have a generating recommended tip amount based on the service provided.

## Restaurant business owners

As a restaurant business owner, the goal is to keep the customer happy and retain their business. When a customer complains about the service it can affect the business reputation. A business owner wants to improve and identify where the service need is and with our program, the business owner will know how a customer is rating the service in real time, this is important because the managers can come over and “check in” on the customer to better their experience. For servers that provide good quality services, the business owner may offer some bonus or rewards. The data will also help improve servers that are not preforming to the standards of delivering great customer. Those servers may need additional support and our program will be able to inform business owners and managers to give additional support to those servers.


## Servers (restaurants)

As a server working in the restaurant, they are providing service to customers and because of this service, customers will tip based on their interactions with the server. With our program, servers will be able to understand how to improve their customer service and provide excellent service to maximize their tips. Our program will rate the server and people that come to the restaurant may want to get that server, with our program they can see if their favorite server is able to serve them. This connection with customer and server will bring back customers to the restaurant.  


# User Stories

## User Welcome Screen – Priority 10 – 1 day

As a **Customer**, I want to be welcomed to the ServiceUNO program, so that I can begin my best customer experience with the server.

## User Information – Priority 10 – 3 days

As a **Customer**, I want to create a customer profile for my restaurant experience inputting my name, email, and server, so that I can rate my server and experience.

## User Questions – Priority 10 – 3 days

As a **Customer**, I want to answer questions based on the service provided in real time, so that, the right data is being collected.

## User GUI – Priority 10 – 5 days

As a **Customer**, I want a nice interface that prompts questions, so that, I can provide the correct information.

## Database – Priority 10 – 7 days

As a **Customer**, Server, Owner I want the information inputted by the customer to go into a database, so that, the data can be analyzed.

## Business Dashboard – Priority 20 – 4 days

As a Business **Owner**, Server, I want to have a dashboard showing the data that is being collected in real time, so that, I can talk to servers and customers to provide the best customer experience.

## User Suggested Tip – Priority 40 – 5 days

As a **Customer**, I want to know the right amount to tip based off of my experience, so that, I can tip the server for their effort.

## Server Ranks – Priority 40 – 5 days

As a **Server**, I want to know the top 5 servers in the restaurant, so that, the server can improve ranking.

**Total days: 33		
Divide by 4 developers / 9 days per developer   
Velocity : 0.5		
Work done: 66**



# Milestone 1

## Iteration 1

**Schedule**

    •	Start Feb 19, 2019
    •	Due by Mar 13, 2019
    •	Duration: 24 days
**Effort**

    •	Developers: 4
    •	Proposed Velocity: 0.5
    •	Days : 12
    •	Work Team can Handle: 24 days

**Task Details**

    |    Feature         |                               Title                         |   Days  | Assigned |
    | ----------------   | ----------------------------------------------------------- | ------- | -------- |
    | Welcome Screen     | Python Ascii Graphics in Python                             |   0.5   | Tim      |
    | Welcome Screen     | Wireframe Welcome screen                                    |   0.5   | Penny    |
    | User Information   | Create Information options for Customer in GUI with outputs |   2.0   | Tim      |
    | User Information   | Wireframe Information                                       |   1.0   | Penny    |
    | Customer Questions | Develop questions for customer                              |   0.5   | Jovany   |
    | Customer Questions | Develop python code for asking customer questions           |   1.0   | Tim      |
    | Customer Questions | Search for Database to hold customer question               |   1.5   | Jovany   |
    | Interface GUI      | Develop interface GUI on Python                             |   3.0   | Kevin    |
    | Interface GUI      | Wireframe interface for program                             |   1.0   | Penny    |
    | Interface GUI      | Validate GUI interface functioning                          |   1.0   | All      |


## Iteration 2

**Schedule**

    •	Start Mar 13, 2019
    •	Due by Apr 7, 2019
    •	Duration: 24 days
**Effort**

    •	Developers: 4
    •	Proposed Velocity: 0.5
    •	Days : 21
    •	Work Team can Handle: 24 days


**Task Details**

    |    Feature         |                               Title                         |   Days  | Assigned|
    | ----------------   | ----------------------------------------------------------- | ------- | --------|
    | User Information   | Create Information options for Customer in GUI with outputs |   5.0   | Kevin   |
    | Data collection    | Save the data to the csv file for dashboard                 |   3.0   | Tim     |
    | Customer Questions | Develop questions 8-10 for customer                         |   4.0   | Kevin   |
    | Interface GUI      | Redesign the interface for costomer                         |   4.0   | Kevin   |
    | Data collection    | Update the database                                         |   5.0   | Penny   |
    | Dashboard          | Create the dashboard for business owner                     |   3.0   | Jovany  |
## Burn Down Graph

![Burn Down Image](https://github.com/cct823/Service-Uno/blob/master/Source/Burndown.PNG)



# Forms of Communication

## Slack

Period: Daily (Can provide chat if needed)

## Face to Face meeting

Period: Weekly (Every Wednesday Before & After Class)



# Three most important things we learned about project development:
    
1. The closer to the deadline to finish the milestone, that faster our team worked in order to produce our tasks.

2. Testing is important. Tests can help you find out the bug in your program. For example, we did not prevent customer input negative bill amount or other text. If we test is, we will know how to prevent it. Hence, when we were working on iteration two we know we have to test everything to prevent the bugs.
 
3. Researching, browsing the internet is a must. There are many ways and different types of approaches to build on your code, you have to search through documents, videos, stack overflow, ask people, or ask the professor.