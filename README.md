# CCBDA_project

For the plots I used chart.js, these are the things I needed to install to get this working:

```
pip install chartjs

npm install luxon chartjs-adapter-luxon --save
```

I might have forgotten something, in that case send me a message. Michiel.

This is how the result should look:

![img_charts_v1.png](images%2Fimg_charts_v1.png)

After running the django server you can find the chart prototype it under http://127.0.0.1:8000/test/.



Links:

I used this tutorial: https://pybit.es/articles/how-to-make-a-nice-graph-using-django-and-chart-js/.

Relevant files to this part:

- war_info/settings.py:
  - adding chartjs, connecting to postgres and adding the template
- war_info/templates/war_info/index.html:
  - front-end html file for displaying charts
- war_info_app/models.py:
  - django models (I used TestModel3 for this mock up)
- war_info_app/views.py:
  - in the index(request) function I add some data to the table,
then put this data into a context dict to pass it to the index.html file