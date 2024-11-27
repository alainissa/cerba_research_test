# Introduction
The aim of this project is to 
1. **Extract** data from Wikipedia using the MediaWiki API
2. **Load** it into a PostgreSQL database (in this example the database is in localhost)
3. **Transform** the data by writing a few dbt models to gain some insights. 

### Pre-requisite & Installation
In order to run this project you will need the following dependencies (you can find the version of each dependency of the interpreter at the time of the writing in the requirement.txt)

##### (Optional) Configuring a virtual environment
Create a new venv: 
```
# create the environment
python3 -m venv dbt-env	   
```

Activate the virtual environment :
```
source dbt-env/bin/activate			# activate the environment for Mac and Linux OR
dbt-env\Scripts\activate			# activate the environment for Windows
```

Installing the postgres adapter
```
python3 -m pip install dbt-core dbt-postgres
```
to initialize the dbt project
```
dbt init
```
Install python requirement:
```
pip3 install -r requirements.txt
```


### Data Extraction & Load
In order to extract & load the data, four python scripts have been developed
1. A **main** program that do a call of each needed class/method
2. A **WikipediaAPI** class that will handle the calls to the Wikimedia API
3. A **WikipediaDataLoader** that will handle the loading step to the database
4. A **WikipediaDatabase** that will act as a link to the database and allow to perform actions (write actions) 

in order to execute the python script, use the below command 
```
python3 main.py
```
### Transform
For this step, we first needed to clean the data.
Indeed the page and recent_changes tables are considered as raw data as they are directly coming from the source without being cleaned

That is why two models have been created
- **cleaned_page.sql** that is basically removing the unvalid pages (the one having null in their fields). Note that for the sake of the exercise and to simulate a small data cleaning process, the nulls values have been introduced (we could have get rid of them before the load)
- **cleaned_recent_changes.sql** that is removing the unvalid changes. Indeed, we noticed that some changes does not have a valid page reference.

Note that we could have done far more checks to clean the recent_changes table (i.e. removing potential duplicates etc.) or the page table but this would have taken us maybe too far. 

After this process, we have created a last model named **changes_repartition.sql** which computes in which timestmap we have the most changes 


### Running
In order to run the models, run the following commands inside the cerba_reasearch folder
```
dbt build
dbt run
```

At the end of the process, the new tables described in the models should have been created