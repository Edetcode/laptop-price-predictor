# Laptop Price Predictor

This project is a Streamlit application that predicts laptop prices based on various features. It utilizes a trained machine learning model to provide users with price estimates for laptops based on their specifications.

## Project Structure

```
laptop-price-predictor
├── app.py                  # Main entry point for the Streamlit application
├── model                   # Directory containing the trained model and preprocessor
│   ├── model.pkl           # Serialized trained machine learning model
│   └── preprocessor.pkl     # Serialized preprocessing pipeline
├── data                    # Directory containing the dataset
│   └── laptop_Price.csv    # Dataset used for training the model
├── requirements.txt        # List of dependencies required to run the application
└── README.md               # Documentation for the project
```

## Installation

To run this project, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd laptop-price-predictor
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To start the Streamlit application, run the following command in your terminal:
```
streamlit run app.py
```

This will open a new tab in your web browser where you can input laptop specifications and get price predictions.

## Usage

1. Enter the laptop specifications in the provided fields.
2. Click on the "Predict Price" button.
3. The predicted price will be displayed on the screen.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.