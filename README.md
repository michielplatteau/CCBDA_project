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