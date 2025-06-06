# util.py
import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError: # Catch ValueError if location not found
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    # Check if artifacts are already loaded to avoid reloading on every request
    if __model is None:
        try:
            with open("columns.json", "r") as f:
                __data_columns = json.load(f)['data_columns']
                __locations = __data_columns[3:]  # first 3 are sqft, bath, bhk

            with open('banglore_home_prices_model.pickle', 'rb') as f:
                __model = pickle.load(f)
            print("loading saved artifacts...done")
        except FileNotFoundError:
            print("Error: Model files (columns.json or banglore_home_prices_model.pickle) not found.")
            print("Please ensure 'columns.json' and 'banglore_home_prices_model.pickle' are in the same directory as util.py")
            # Handle error, perhaps by exiting or raising an exception
            exit() # Exit for demonstration, or raise a custom exception
    else:
        print("Artifacts already loaded.")


def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # Example of a location not in the model for testing