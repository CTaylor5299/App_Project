# Fantasy Football CRUD Application
## Fundamental Project

Contents
* (holder)

## Brief

#### What was required
For this project, the goal that was asked of me was to be able to create an application that has the ability to utilise CRUD functionality (Create, Read, Update, Delete). I would achieve this using the tools and knowledge gained in the previous training modules covered in the weeks prior to this. I was given some objectives to meet in terms of certain aspects that were required, for example:
* A Trello board with full expansion
on user stories, use cases and tasks needed to complete the project.
* A relational database used to store data persistently for the
project
* Documentation from a design phase describing the application architecture
and a detailed Risk Assessment
* A functional CRUD application created in Python, following best
practices and design principles
* Fully designed test suites for the application, as
well as automated tests for validation of the application
* A functioning front-end website and integrated API's, using Flask
* Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine

#### My Approach
To hit these requirements, as well as creating something I would take an interest into, I decided to create a very basic Fantasy Football application that would allow the user to do the following:
* Create their own team including:
  * The Team Name
  * Owner Name
  
  So that they may create the team name they like and then also track it with their name being associated to their team. As well as this they will be able to:
  
* Add players into their team by adding in:
  * The Player's name
  * The real team that the player plays for

### Architecture

#### Database Structure
I have created an ERD diagram for before and after the project to show the structure of my database and the relationships taking place between the tables. Below is an evolution of my ERD diagrams as I planned it and as I had come to finish it.
##### ERD Diagram (Before)
The image below shows my first ERD diagram, I initially planned on creaating a practically working Fantasy premier league application with a points based system and a league table and the diagram below shows my original plans.
![erdfirst](https://imgur.com/Focl9Cm.png)
##### ERD Diagram 2 (After)
The next image below shows my final design for my ERD diagram, I've changed the structure of the application as at this point I had realised the difficulty of the first design, and also, based on the spec, it seemed quite unnecessary so I went for a simple design that allows to create a 'Fantasy Team' with no scoring system or league.  
![erdsecond](https://imgur.com/lBwo23b.png)
#### CI Pipeline
The image below represents my CI pipeline with the different processes and the apps/ tools used to do so. It displays the process and path of the development cycle in a sense and also how they were used to create a funtioning and aptly tested program.
![CIpipeline](https://imgur.com/wBmENAs.png)

### Project Tracking
For Project Management Trello was used to track the progress of the project's tasks and display my process, from planning to testing and finally to completion. Below is a screenshot of my board.
You can find the full Trello Board [Here](https://trello.com/b/vmdySd62/project-management).
![trello](https://imgur.com/6q2OwOt.png)

### Risk Assessment
Below is my risk assessment for the project. This is where I have outlined potential risks, their impacts and mitigation techniques that I may need. Similar to the ERD diagram I have done a before and after, however unlike the ERD, I have only added a couple of items to this and none have been removed.
Here is the first draft:
![riskassessment1](https://imgur.com/ChlWjGw.PNG)
And below is my final draft:
![riskassessment2](https://imgur.com/uJEB1Uu.PNG)

