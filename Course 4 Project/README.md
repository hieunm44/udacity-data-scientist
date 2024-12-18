# Disaster Response Pipeline Project

## Instructions:
1. Run the following commands in the project's root directory to set up your database and model.
    - To run ETL pipeline that cleans data and stores in database
        ```sh
        python3 data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
        ```
    - To run ML pipeline that trains classifier and saves
        ```sh
        python3 models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
        ```
2. Go to `app` directory: `cd app`
3. Run your web app: `python run.py`