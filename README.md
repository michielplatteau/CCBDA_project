# About project

We are excited to present our web application that offers in-depth insights into the Russian-Ukrainian armed struggle. Our platform provides a wide selection of interactive graphs and charts that highlight key facts and trends pertaining to this intricate battle. Users can investigate important parameters like casualties, equipment deployment, and other crucial issues through painstakingly curated data. The impact of the conflict is succinctly and clearly depicted in these visualizations, enabling users to comprehend the gravity of the situation and its changing dynamics.

The use of predictive analytics in our product is one of its unique advantages. We provide users forecasted trends and potential futures using historical data and sophisticated algorithms. By enabling analysts, researchers, and politicians to make defensible judgments based on data-driven projections, this vital tool improves strategic planning and risk assessment.

Our web application also features an immersive interactive map that highlights key moments during the war, in addition to the charts and graphs. Users can explore various areas, follow the development of the conflict, and develop a more detailed spatial grasp of the current dynamics. For journalists, researchers, and anybody else looking for a thorough grasp of the geographic backdrop of the war and its effects on the impacted areas, this feature is an extremely useful resource.

# Differences in scope from the project first draft

Added Features:

Interactive Map: We have successfully implemented an interactive map feature that visualizes the events and locations related to the Russian-Ukrainian war conflict. Users can explore the map, navigate different regions, and gain a spatial understanding of the conflict's impact. This feature enhances the user experience and provides a dynamic way to engage with the data.

Unimplemented Features (Adjusted Approach):

Automated Predictions: We have modified our strategy due to limitations in using SageMaker for automating predictions. Instead, in order to produce predictions based on the given data, we created Python code and made use of modules from other libraries. We will put in place an automatic updating mechanism to make sure that projections are updated appropriately because the data is not real-time and is only updated every two weeks. With this strategy, even in the absence of real-time data integration, we can retain forecast accuracy and give consumers insightful information.


# How does the code do the above? Description and architectural diagram of the different parts.

Everyone will tell something about his part:
-	Machine learning
-	Bootstrap and layout
-	ChartJS
-	Leaflet
-	Deployment
-	
## Designing wireframes and implementing layout

Our web application's development process started with the creation of wireframes using the well-known design program Figma. Wireframes helped us define the positioning and interactions of various elements on the user interface as well as the initial structure and layout of the program. Before beginning the implementation stage, this step assisted us in visualizing the overall design and layout. After the wireframes were complete, we went on to design the Django application's layout. With the help of the robust web framework Django, we can create scalable and dynamic web applications since it adheres to the Model-View-Controller (MVC) architectural pattern. We used Bootstrap, a well-known front-end framework that offers a variety of pre-built components and styles, to speed up the layout building process. However as we moved from them to actual implementation, we discovered that several design aspects were difficult to implement or incompatible with the selected front-end framework, Bootstrap. To guarantee the design integrity while working within the framework's limitations, we had to make tweaks and discover other alternatives. Although Bootstrap offered a broad variety of pre-built components and styles, there were occasionally restrictions on how we might modify these components to meet our own design or functionality needs. In order to provide a uniform user interface and user experience, we had to carefully balance the modification requirements with the framework's capabilities. We were able to develop a unified and user-friendly online application that shows data in an intuitive and aesthetically pleasing way by combining the back-end capabilities of Django, Bootstrap's responsive design, and JavaScript's interaction.




# Discussion on the use of the twelve-factor methodology as stated in the requirements.
Michiel

# Description of the methodology used to create the project: division of responsibilities, meetings organization, exchange of ideas and documentation, created working environments (development, production, staging), tools used, etc.

Samar

# Description of the main problems encountered and the solutions implemented regarding coding, team organization, services, and resources used.

Everyone will tell something about his problems

# For each of the services and resources used, explanation on how project benefits from them. Giving some alternatives to obtain similar results and briefly explaining why have been discarded.

Martin 

# Listing the hours invested, by each member, for all the main tasks of the project (i.e., architectural design, research and documentation on services and resources, coding, meetings, written documentation, etc). What is the project deviation in hours. How could the team have deviated less from the initial hour count breakdown?

Guillem













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
