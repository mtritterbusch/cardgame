# Card Game Challenge

* clone repo
* set up virtual environment (requires Python 3.6 or greater)
* once in virtual environment, run ```pip install -r requirements.txt```
* to run tests, ```python -m unittest tests/*.py```
* to run pylint:
  * ```python -m pylint *.py```
  * ```python -m pylint cardgame/classes/*.py```
  * ```python -m pylint tests/*.py```
* to run coverage:
  * ```coverage run -m unittest tests/*.py```
  * ```coverage report```
* how to play the Draw3 game, ```python play_draw3.py -h```
