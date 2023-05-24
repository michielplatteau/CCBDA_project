# About project

We are excited to present our web application that offers in-depth insights into the Russian-Ukrainian armed struggle.
Our platform provides a wide selection of interactive graphs and charts that highlight key facts and trends pertaining
to this intricate battle. Users can investigate important parameters like casualties, equipment deployment, and other
crucial issues through painstakingly curated data. The impact of the conflict is succinctly and clearly depicted in
these visualizations, enabling users to comprehend the gravity of the situation and its changing dynamics.

The use of predictive analytics in our product is one of its unique advantages. We provide users forecasted trends and
potential futures using historical data and sophisticated algorithms. By enabling analysts, researchers, and politicians
to make defensible judgments based on data-driven projections, this vital tool improves strategic planning and risk
assessment.

Our web application also features an immersive interactive map that highlights key moments during the war, in addition
to the charts and graphs. Users can explore various areas, follow the development of the conflict, and develop a more
detailed spatial grasp of the current dynamics. For journalists, researchers, and anybody else looking for a thorough
grasp of the geographic backdrop of the war and its effects on the impacted areas, this feature is an extremely useful
resource.

# Differences in scope from the project first draft

Added Features:

Interactive Map: We have successfully implemented an interactive map feature that visualizes the events and locations
related to the Russian-Ukrainian war conflict. Users can explore the map, navigate different regions, and gain a spatial
understanding of the conflict's impact. This feature enhances the user experience and provides a dynamic way to engage
with the data.

Unimplemented Features (Adjusted Approach):

Automated Predictions: We have modified our strategy due to limitations in using SageMaker for automating predictions.
Instead, in order to produce predictions based on the given data, we created Python code and made use of modules from
other libraries. We will put in place an automatic updating mechanism to make sure that projections are updated
appropriately because the data is not real-time and is only updated every two weeks. With this strategy, even in the
absence of real-time data integration, we can retain forecast accuracy and give consumers insightful information.


# How does the code do the above? Description and architectural diagram of the different parts.

Everyone will tell something about his part:
-	Machine learning
-	Bootstrap and layout
-	ChartJS
-	Leaflet
-	Deployment
### Deployment
The deployment process is handled by the AWS Elastic Beanstalk service.
The use of this service is also described in the services section. 
Beanstalk helped us a lot and made the deployment process quite convenient,
however there was still a lot of work to do to deploy our Django application
successfully. 
First thing that was necessary for the deployment to work, was to have a list of dependencies for our application.
This was not a big deal, and using pip we managed to get the dependencies list with
one command (pip freeze). We saved the list into a file requirements.txt, which is automatically
installed on the target machine (EC2) upon deployment. 
There were also some dependencies that were needed for the EC2 instance to be able to connect to PostgreSQL database.
These are listed in this [file](.ebextensions/01_packages.config). Since the instance runs
on a Amazon Linux machine, these packages are installed using yum package manager.

In another [file](.ebextensions/02_starter.config) more configuration has been done in order to run
the Django application successfully. Some options are for configuring environment upon deployment,
these include updating the path to the application wsgi. There also needed to be a setting
to proxy the requests on static files to the right directory. Then there was a few extra
settings for setting environment variables such as which hosts can be served by the application, or whether
to run the application in debug mode or not. In the same file also
migrations are handled, meaning the application creates migrations and applies them to the production database upon 
deployment, creating relational tables for newly created models. This helps to keep the production and development
databases in sync. 

After configuring all these settings, all one needs to do to deploy the application to the production environment
is to run the "eb deploy" command and wait few minutes. (Of course this is a bit more complicated
with the AWS education account as new access credentials are generated each time a lab session is started.)


### Designing wireframes and implementing layout

Our web application's development process started with the creation of wireframes using the well-known design program
Figma. Wireframes helped us define the positioning and interactions of various elements on the user interface as well as
the initial structure and layout of the program. Before beginning the implementation stage, this step assisted us in
visualizing the overall design and layout. After the wireframes were complete, we went on to design the Django
application's layout. With the help of the robust web framework Django, we can create scalable and dynamic web
applications since it adheres to the Model-View-Controller (MVC) architectural pattern. We used Bootstrap, a well-known
front-end framework that offers a variety of pre-built components and styles, to speed up the layout building process.
However, as we moved from them to actual implementation, we discovered that several design aspects were difficult to
implement or incompatible with the selected front-end framework, Bootstrap. To guarantee the design integrity while
working within the framework's limitations, we had to make tweaks and discover other alternatives. Although Bootstrap
offered a broad variety of pre-built components and styles, there were occasionally restrictions on how we might modify
these components to meet our own design or functionality needs. In order to provide a uniform user interface and user
experience, we had to carefully balance the modification requirements with the framework's capabilities. We were able to
develop a unified and user-friendly online application that shows data in an intuitive and aesthetically pleasing way by
combining the back-end capabilities of Django, Bootstrap's responsive design, and JavaScript's interaction.

### Machine learning



# Discussion on the use of the twelve-factor methodology as stated in the requirements.
Michiel

# Description of the methodology used to create the project: division of responsibilities, meetings organization, exchange of ideas and documentation, created working environments (development, production, staging), tools used, etc.
Creating this project involved several steps and methodologies that helped us divide tasks equally and work in a harmonious environment and in synergy:

Division of Responsibilities:
Project Manager: We chose ... to be our project manager, he coordinates between the team members divide tasks and makes sure that everyone completed his task. 

Development Team: 
Roman was responsible for designing the wireframes and developing the website using the Django framework.
Martin was responsible for creating and managing the AWS services that we needed for our project, collecting each team member's work and creating a connection between the application and the database.
... Was responsible for designing the interactive visualizations.
 Samar was responsible for the preprocessing of the data and she worked on the Machine learning part where she tested several methods and libraries for the prediction, compared their performances and plotted the predictions with the best performing method.
.........

Meeting organization:
 Kick-off Meeting: This meeting was held at the project's start in which we discussed project goals, objectives, and initial plans and we had this meeting on Zoom.
 
 Regular Meetings: 
 In order to divide tasks, stay up to date on what each member has done and make sure that the work is going as planned, each week on Thursday we have a meeting in which we discuss the problems that we have encountered and the improvements that we should make, we also discuss with the professor what we have done and ask for guidance and for tools that may help us with developing the project.
 After each meeting we define and prioritize tasks for the next sprint and we come up with a plan for the next week that we put on that we practically respect everytime, and if we couldn't fully finish the last week's tasks we discuss the problem that we have encountered and come up with ideas to overcome them. During these weeks each group member did his best in developing the project and delivering a good work, the work may not have been equally divided each week but in the end everyone has done as everyone else.
 
 Working environments:
Also during the week we discuss and exchange ideas via a social media and we present the progress that we are doing, help each other when someone has a problem in his part.
For dividing the tasks we were using the Trello platform in order to share the plan and the tasks advancement with everyone.
For uploading the work done we used this Github repo in which we gathered the work of each member.
 

# Description of the main problems encountered and the solutions implemented regarding coding, team organization, services, and resources used.

Everyone will tell something about his problems
## Django application deployment / AWS services management (Martin)
Deploying a simple python application with no frameworks and dependencies is 
very simple thanks to Elastic Beanstalk. However, when a framework such as Django is included,
and the application also needs to communicate with a database from different service
it becomes a bit more challenging. At first, I thought it could be as simple as following some tutorial,
unfortunately I was wrong. Many problems arose due to the fact that some things changed with newer versions 
of Elastic Beanstalk or Django, and finding the right syntax to do some tasks, mainly within the [.ebextensions](.ebextensions)
folder was quite challenging. It took me some time to figure out how to configure the WSGIPath for the application, 
as well as static files option "aws:elasticbeanstalk:environment:proxy:staticfiles", which got changed in recent versions
of Elastic Beanstalk.
Then there was also the problem with serving static content
from S3 bucket, which is described in the [Amazon S3](#amazon-s3) section.
It was also a bit tricky to find the reasons of unsuccessful deployment,
however after a while I learned how to orientate in the log files, and it was fine.
Overall, this kind of work was quite new to me, maybe that's why it took me a bit longer,
however when all problems got resolved and the application was running and accessible on a public address
without any problems, it was a very satisfying feeling.

# For each of the services and resources used, explanation on how project benefits from them. Giving some alternatives to obtain similar results and briefly explaining why have been discarded.

### Elastic Beanstalk
As planned in the project proposal, the backbone of our project is the AWS Elastic Beanstalk service.
It helps us greatly as it simplifies the deployment process very much. It automates the deployment tasks 
and handles infrastructure provisioning, load balancing, and auto-scaling,
allowing us to focus on the application code, instead of how to bring it to the production environment and keep it functioning.
Elastic Beanstalk frees us from handling the underlying infrastructure of our application, from tasks such as OS patching or server configuration.
It also makes it easy to integrate with other AWS services, in our case it was Amazon RDS to host the PostgreSQL database.
Another process that becomes super easy with Elastic Beanstalk is the management of different environments. It wasn't really needed 
for this project as we don't have an application with live traffic and one environment - production was just enough for our purposes,
but we could see how profitable it would be to set up multiple environments to make the rolling out and testing of new changes 
really convenient.

Possible alternative for managing the deployment process could be to include the application in a container and run it 
using for example AWS Fargate or Amazon ECS. However, we did not go down this path,
since the process of setting up these services looked way too complex for the scope of this project.


Another option to deploy the application and manage it could be to use and setup each of the services grouped by Elastic Beanstalk manually. 
We could connect to an EC2 instance using SSH and set the environment up by installing all necessary dependencies, then put the application code there and run it.
But we don't see any reason how we could profit from this approach, Elastic Beanstalk makes all of it much more simple.


### Amazon RDS
Another crucial service for our project is Amazon RDS. Its responsibility is to run a relational database, in our case PostgreSQL.
It not only handles running the database and making it accessible to our application, but also
patching or backups. Setting the service up to work with our Elastic Beanstalk was also very convenient.


In the project proposal we were also considering the use of Aurora or DynamoDB. 
Based on the data we chose to use in our application, we realized that it 
will be better to use a relational database. Therefore, DynamoDB was not a possible choice anymore
as it is a NoSQL database. That left us with Aurora and RDS which are both relational
database services and both of them are compatible with PostgreSQL database. We found out that Aurora 
might achieve a better performance, but with a higher cost. As we knew that our application won't be working
with that big amounts of data, where the database performance could be limiting, we decided to go on with Amazon RDS.


### Amazon S3
We planned to use amazon S3 service to serve our static content. We tried to set up our application to do so,
however we ran into a problem while granting our AWS root user programmatic access
to the S3 bucket, due to insufficient permissions (probably we are only using the education account).
Because of this, we were not able to collect our static files and place it to the S3 bucket when deploying 
a new version of the application. If we still wanted to leverage the use of S3 bucket to serve our static content (images, css...),
we would have to upload each new file into the bucket manually. That seemed too inconvenient, hence we decided
to store the static content within our EC2 instances. 
AWS S3 service is however still used within Elastic Beanstalk to store different versions of our deployments. 

### AWS IAM
As mentioned in the S3 section, we tried to grant our root AWS user some permissions, but it did not go well. 
This was with the use of AWS IAM service. We can imagine the use of the service to achieve
various goals, however it does not seem that useful within the education account, where we don't have many permissions.

# Listing the hours invested, by each member, for all the main tasks of the project (i.e., architectural design, research and documentation on services and resources, coding, meetings, written documentation, etc). What is the project deviation in hours. How could the team have deviated less from the initial hour count breakdown?

[//]: # (Guillem)
We had planned to spend 23 hours every week for this project. In our first draft we wrote that the tasks we wanted to
complete in these project were the following ones:
- Identifying the data sources and their datasets that we wanted to use for the visualizations
- Preprocessing data
- Determining the AWS services that we will use
- Building the web application and designing its interactive visualizations (maps and charts)
- Implementing predictive models using machine learning techniques
- Deploying the application with Elastic Beanstalk
- Identifying problems, testing and optimising the application

Initially we had planned to spend the first week deciding the idea we wanted to develop in this project, then accomplish
the first two tasks in the second week; in the following two weeks we planned to build the application and the fifth was
for creating the predictive models. In the sixth week we had to deploy the application and the last week had to be
devoted to testing and fixing problems.

It has not been possible to follow this initial plan exactly because we have not been able to complete fully complete 
the tasks every week. Instead, we have had to revisit the work we had done previous weeks because of the
errors that were found or to implement new ideas or improvements. Even if we have not finished the tasks in the
corresponding weeks, we have not fully deviated from the initial plan.

The amount of time we have spent on every task has been more or less the one we had planned initially, about 5 hours per
member and per week.


| Team member | Task | Time invested |
|-------------|------|---------------|
|             |      |               |
|             |      |               |
|             |      |               |

One of the things we could have done to improve our plan is trying to parallelize the tasks and plan more than one cycle
per task. For example, once we had our first working Django app, we could have worked in parallel on the web design and
addition of the visualizations of the data in the web and discuss the advancements made during the week on the weekly
meetings we have had every week. This iterative approach in which the development of the project is carried out in 
cycles of development-review is more or less the one we have followed in the actual project.















# CCBDA_project

## Dependencies

For the plots I used chart.js, these are the things I needed to install to get this working:

```
pip install chartjs

npm install luxon chartjs-adapter-luxon --save
```

I might have forgotten something, in that case send me a message. Michiel.

## Reference

This is how the result should look:

![img_charts_v1.png](images%2Fimg_charts_v1.png)

## Where?

After running the django server you can find the chart prototype it under the /test/ page: http://127.0.0.1:8000/test/.

## Links

I used this tutorial for chart.js with django:

https://pybit.es/articles/how-to-make-a-nice-graph-using-django-and-chart-js/.

## Relevant files to this part

- war_info/settings.py:
  - I added chartjs, connected to postgres and added the template
- war_info/templates/war_info/graphs.html:
  - Front-end html file for displaying charts
- war_info_app/models.py:
  - Django models (I used TestModel3 for this mock up)
- war_info_app/views.py:
  - In the index(request) function I add some data to the table,
then put this data into a context dict to pass it to the graphs.html file
- war_info_app/urls:
  - I added path('test/', views.index), to the urls
