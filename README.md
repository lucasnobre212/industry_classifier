# Industries Classifier

This is a script to predict the industry from a given text.
The model is already trained, you will only need to read the models, the categories dictionary and run the function I've prepared

## Installation

* Install the dependencies by going to this project directory and running 
```
pip install -r requirements.txt
```

* Model and Categories
  * The model should be in the models folder. If something goes wrong you can download them here:
  https://drive.google.com/file/d/1--JbO8S6dJ7lt4lxsz6XVh7avqZ2PSKf/view?usp=sharing,%20https://drive.google.com/file/d/1XIK9_J1xN9AM8lM5WWksQviGOAdYkTun/view?usp=sharing
  * The categories dictionary should be in the project folder, if not please download it here: https://drive.google.com/file/d/1DfeimhfZJYsqr3zSX-akTxU_3UxvPi6g/view?usp=sharing
  
## Execution
I have added a single function and how to use it in the main.py file. Since this will be implemented in a API, I've figured you should only need the function instead of running a script.  
You should load the models and categories only once before calling the function, that is why we are using them as parameters in the get_prediction_from_text function. You can also test some predictions by changing the text variable in the main function.
