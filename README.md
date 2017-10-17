# Flixbus assignment

Installation

- To install virtualenv and 
```
sudo pip install virtualenv
mkdir ~/virtualenvs
sudo pip install virtualenvwrapper
export WORKON_HOME=~/virtualenvs
echo "export WORKON_HOME=~/virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
mkvirtualenv flixbus
```
- If you already have the virtualenv
```
workon flixbus

```
- Install the requirement files.
```
pip install -r requirements.txt
```
- To Run the all tests.
```
python -m pytest tests/ 
```
- To Run the flask app
```
cd trip_ranking/trip_ranking_api
FLASK_APP=run.py flask run
```
- To test the API ranking v1
```
curl -H "Content-Type: application/json" -X POST \
-d '{"trips": [
    [9, [2017,10,6,12,0], 3, 1, 110, 60],
    [12, [2017,10,6,12,0], 2, 1, 80, 50],
    [13, [2017,10,6,12,0], 1, 1, 60, 20],
    [7, [2017,10,6,12,0], 3, 1, 60, 30],
    [14, [2017,10,7,12,0], 2, 1, 50, 30],
    [4, [2017,10,7,12,0], 2, 1, 30, 50],
    [2, [2017,10,7,12,0], 1, 1, 40, 20],
    [8, [2017,10,8,12,0], 2, 1, 90, 50],
    [6, [2017,10,8,12,0], 4, 1, 120, 100],
    [18, [2017,10,8,12,0], 2, 1, 120, 50]
]}' http://127.0.0.1:5000/rank_trips
```
- To test the API ranking v2
```
curl -H "Content-Type: application/json" -X POST \
-d '{"trips": [
    [9, [2017,10,6,12,0], 3, 1, 110, 60],
    [12, [2017,10,6,12,0], 2, 1, 80, 50],
    [13, [2017,10,6,12,0], 1, 1, 60, 20],
    [7, [2017,10,6,12,0], 3, 1, 60, 30],
    [14, [2017,10,7,12,0], 2, 1, 50, 30],
    [4, [2017,10,7,12,0], 2, 1, 30, 50],
    [2, [2017,10,7,12,0], 1, 1, 40, 20],
    [8, [2017,10,8,12,0], 2, 1, 90, 50],
    [6, [2017,10,8,12,0], 4, 1, 120, 100],
    [18, [2017,10,8,12,0], 2, 1, 120, 50]
]}' http://127.0.0.1:5000/rank_trips_v2
```

TODO:
- Add more test and mocking.
- Fix bugs in docker
