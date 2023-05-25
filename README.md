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
understanding of the conflict's impact. Additionally, they can choose which type of events are wanted to be shown in the 
map. This feature enhances the user experience and provides a dynamic way to engage with the data.

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

### Charts and maps

With the idea of the layout present, we have thought of different alternatives to implement different alternatives that
were compatible with our implementation. One of the tools that we have considered is Tableau, which is an excellent tool
to create elegant dashboards. We have finally opted for Chart.js, which allows more customization to add our own
predicted models and can be easily embedded in our web application. Apart from charts we have added to our application
an interactive map to show recent events related to
the war. The events shown in the map can be filtered by the type. This map has been created through Leaflet.

The data shown in the visualizations have to be up-to-date all the time, so it have to be retrieved from a database that
is periodically updated with new data every time the web is requested. To do this we have made use of Django models that
allow us to define data instance types. This instance types are linked to tables in a relational database such as Amazon
RDS.



### Machine learning
For the preprocessing I have started by displaying a summary of the dataset,  fill in missing values, categorizing the data and plot some graphs in order to see the relationship between the datasets.
After the preprocessing of the data I have started with the prediction using the SVM (Support vector machine) method and the RF (Random Forest) method. In implementing the two methods I have used the libraries pandas, numpy, scipy and sklearn.
I have compared the performance metrics of the two methods (with the R2 and RMSE) which showed that the two methods have almost the same performance. But I was not quite convinced with the predicted data since the predicted results do not go well with the real data.
So I tried a different library, the Prophet library which is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. prophet is robust to missing data and shifts in the trend, and typically handles outliers well.
Using this library we got the best predicted results, we had a value of R2=0.79 while with the other methods we had a value of R2=0.4 and for the prediction performance the closest the value of R2 to 1 the better.
So we proceeded with these results and we plotted the graph of the predicted data with the bound showing the prediction intervals or uncertainty bounds around the forecasted values.
To plot the graphs we have used the library matplotlib.pyplot.


# Discussion on the use of the twelve-factor methodology as stated in the requirements.

1. Codebase
 * We used github for the codebase. The labs teached us to work with github and we notice that we
can work with it way better than in february. All our code is pushed to the github repo as much as possible. 
 * We used different branches for different development fases, so we always had a stable main branch. Different
team members could work on different branches at the same time to develop different things. Then github allows us to
merge everything into a stable deployment branch with all the features working.
 * We did have to use .gitignore to
prevent pushing too much, such as pychache, big data files, our virtual environment and pycharm's
.idea files.
2. Dependencies
 * It is really important to declare and control dependencies. We used pip freeze > requirements.txt
for this. It is really easy to use, and we used it throughout the project to keep the
requirements.txt file up to date.
 * Not every depency was through pip, so we used a markdown file
to keep eachother up to date, e.g. 
npm install luxon chartjs-adapter-luxon --save.
3. Configuration
 * We made the configuration environment to connect to postgres optional. This way the code automatically recognizes is the environment is filled in, which is the best practice.
 * But in case one of us didn't want to do this, they could just write their credentials in the settings file.
 * Reviewing this right now, we see that this was not the best approach, as credentials can be pushed to the repo in this way. In future works we should avoid doing this and use configurations, as we learned in the labs.
4. Backing services
 * We used postgres SQL as a database. This way all our data is saved in a stateless way and is replacable
by other equivalent resources. Our data gets loaded from the database by our main application during run time.
 * This reduces our codes complexity, seperates different processes and increases flexibility. 
 * We treat this as an attached resource
5. Build, release, run 
 * The build stage involves compiling and assembling the application's source code, dependencies, and assets into a deployable artifact. This stage is responsible for transforming the source code into an executable form that can be executed by the runtime environment.
We do tests and database migrations before we move on to the next step.
 * The release stage takes the built artifact from the build stage and combines it with the necessary configuration to create a deployable release. It involves bundling the application code with its specific configuration, such as environment variables or deployment parameters. The release should be versioned and represent a ready-to-deploy package of the application.
We combine our built artifact with the configuration for the database etc for launching.
 * The run stage is where the application is executed or deployed in the target environment. It involves launching the application and its dependencies in the runtime environment, configuring any necessary resources (such as databases or queues), and managing the execution of the application.
This is where elastic beanstalk comes into play. We launch our website through this AWS service, which takes care of a lot of things for us.
6. Processes
 * Our Django application follows the principle of stateless processes. In a stateless architecture, each request is handled independently without relying on the state stored in the server.
 * Elastic beanstalk takes care of the horizontal scalability of our processes without having to worry about it to much.
7. Port binding
 * Since we have a web application we use HTTP requests. The Django framework is really versatile and allows for a lot of options. But it still takes care of a lot of boiler plate code for us.
 * We use the 8000 port for our application, this is the internet port. For the database, postgresql listens to the 5432 port.
8. Concurrency
 * We deploy our application on Elastic beanstalk.
Elastic Beanstalk is a platform-as-a-service (PaaS) offering from AWS that simplifies the deployment and management of applications.
 * Elastic beanstalk can be combined with elastic load balancer if we needed to scale.
9. Disposability
 * Our Django application has a short life instace. We can start it up and shut it down really fast.
 * Due to the design of the framework, the whole web application doesn't fail due to a single error.
 * For example, if there is an error loading some icon, the application as a whole doesn't fail.
10. Dev/prod parity
 * We keep consistent configurations througout the different development and production environments as much as possible.
 * We didn't develop everything seperately and merged at the end, which would be a real hassle. We developed
in small increments, that ways errors and bugs were visible early on. We merged into the main application every time, tried deploying it.
This way our "released" application was updated as much as possible and as small steps as possible.
 * By debugging and "releasing" feature by feature we caught and resolved errors early on (we sure as hell encounterd errors along the way, I guess thats part of learning as well)
11. Logs
 * Our application is not super big and we are a relatively small development team with 5 people.
 * The django framework and postgres connecting (psycopg2) take care of
a lot of logging and inform us live when errors occur, we saw a lot of 404's...
 * Further than that we used the standard output, printing to terminal to output different variables etc to check if everything is working correctly.
 * We also use the python "assert" to catch errors early on during development
12. Admin processes
 * We use different codes for housekeeping, such as filling the database, cleaning the data, doing machine learning.
 * By seperating this we keep everything as clean as possible.
 * A lot of housekeeping is done by the Django framework. Such as cleaning tasks, monitoring and alerting.
 * Since we don't have a really complex project we didn't implement an immense ammount of admin processes.

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

## Data science and cleaning (Samar)

The problem that I have encountered while working on the data is the lack of resources and the fact that some resources had restricted access so searching for open source data was a bit challenging.
The other problem was after the preprocessing part where I had to do it all over again each time I change the machine learning method I'm working with for the prediction.
The usual prediction methods such as the SVM (Support Vector Machine) and the RF (Random Forest) were not very convincing on the data predicted since the data we had was time series data, so I had to look for other, more accurate, libraries and to learn how they are implemented. I found the Prophet library which is an open source software released by Facebook’s Core Data Science team. In using it, I looked for some examples I found on the internet about previous projects and I also used the library's documentation that helped me in understanding how are its methods implemented.

## Creation of designs in figma and developing frontend with help of bootstrap (Roman)

I ran into a few difficulties while creating wireframes in Figma. Firstly, determining the optimal layout and composition for the page proved to be crucial. Deciding on the placement of different elements such as headers, navigation menus, content sections, and call-to-action buttons required careful consideration to ensure a visually appealing and user-friendly design. Since I was working with this tool for the first time, I also made many mistakes that cost me some effort to correct (such as incorrect grouping of elements), but designs in wireframes are still much easier to change than the layout of the created page itself, and that is why their initial creation is very important.

I also encountered some difficulties while using Bootstrap for the development process. Customizing the Bootstrap default styles to fit the intended visual design was one of the main problems. It was frequently necessary to alter CSS and override default classes in order to adapt the framework to the particular project requirements while keeping responsiveness. Managing the responsive behavior of the layout across various devices and screen sizes was another difficulty. In order to ensure seamless performance and functionality, it was occasionally necessary to resolve conflicts or inconsistencies that resulted from integrating third-party libraries and customized JavaScript functions into the Bootstrap framework.


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

## Chartjs

Chartjs worked really well from the start with basic dummy data. We were happy with the responsiveness, interactiveness and the fact that everything rescales well to the window size. When working with the real data we noticed it was a lot harder to customize everything exactly how we wanted it and using the dynamically loaded data. In general we are happy with the result, but we wanted to do more. For example we wanted to make a date selector to choose on the web application for which period we want to see the graphs. After a lot of trying different things, we saw that it messed with other things and we didn't get it to propoerly work. So we decided to not include it and settled on this final result. Although we wated to make it better, we still learned a lot from the process.

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

### ChartJS


1. Chart.js is a popular JavaScript library for creating interactive and visually appealing charts on the web. Chart.js was chosen for the following reasons:

   1. Charting Capabilities: Chart.js provides a wide range of chart types, including line charts, scatter charts, pie charts, and more. It offers extensive customization options to tailor the charts' appearance, labels, tooltips, and animations.
   Getting acquainted with this could really help us in our future.

   2. Interactive: Chart.js allows for interactive features like hovering over data points to display tooltips, zooming, and click events. The charts are responsive, automatically adjusting to different screen sizes, thats great compared to just using png graphs.

   3. Integration with Django: Chart.js can be easily integrated with Django, enabling you to dynamically generate charts based on the war data stored in our database. Models.py allow us to easily pass the data.

   4. Open-Source and Well-Maintained: Chart.js is an open-source library with an active community and continuous development. It receives regular updates, bug fixes, and new features.

2. Alternatives we considered for charting:

   1. Pyplot (Matplotlib): Pyplot is a popular option for creating static visualizations. However, compared to Chart.js, it does not provide the same level of interactivity and responsiveness for a web-based application. Plus: we allready can work quite well with this and we would learn less by implementing this.

   2. Tableau: Tableau is a powerful data visualization tool that offers a wide range of features and capabilities, and it was suggested by the professor. However, after trying it and not getting it to work immediately. We
   did some further research and discovered more options. Internet articles made it clear that chart js might be a better fit for us and we really liked the interactiveness and the design.



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


| Team member | Task                                                             | Time invested |
|-------------|------------------------------------------------------------------|---------------|
| Michiel     | Creating a first Django application and connecting to postgres   | 3 hours       |
| Michiel     | Researching different chart options (pyplot, tableau, chartjs)   | 2 hours       |
| Michiel     | Implementing the first chart prototype with dummy data           | 4 hours       |
| Michiel     | Making the graphs work in chartjs with the cleaned data          | 2 hours       |
| Michiel     | Making the graphs interactive                                    | 4 hours       |
|             |                                                                  |               |


One of the things we could have done to improve our plan is trying to parallelize the tasks and plan more than one cycle
per task. For example, once we had our first working Django app, we could have worked in parallel on the web design and
addition of the visualizations of the data in the web and discuss the advancements made during the week on the weekly
meetings we have had every week. This iterative approach in which the development of the project is carried out in 
cycles of development-review is more or less the one we have followed in the actual project.










