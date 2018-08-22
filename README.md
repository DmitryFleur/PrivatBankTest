Task description is in the `task_description.txt` file <br /><br />

How to run:<br />
1. Make migrations / migrate<br />
2. Generate dummy data<br />
3. `python manage.py runserver`<br /><br />

To run tests do `python manage.py test`<br /><br />

NOTES:<br />
To generate a dummy data, make a GET request to '/load_data. <br />
By default it will generate 100 records. In order to change the value make request in this format: `/load_data/?records_number=500`<br />