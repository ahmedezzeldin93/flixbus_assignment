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
- Run the all tests.
```
python -m pytest tests/ 
```


Comments:
- The 4hr was not enough for this task.

TODO:
- Enhance main trips_rank function.
- Add more test and mocking.
- Fix bugs in the flask API.


