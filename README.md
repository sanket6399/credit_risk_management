# CS267_PROJECT: Credit Risk Management

## Description

This project applies machine learning to manage and assess credit risk. It encompasses a variety of machine learning models, each encapsulated in a Jupyter notebook, a Flask web application for visualization and interaction, and is prepared for continuous integration and deployment through GitHub Actions.

## Installation

Before installation, ensure you have Python and Docker installed on your system. To set up this project:

1. Clone the repository to your local machine.
2. Navigate to the root directory of the project.
3. Create a virtual environment:
4. Activate the virtual environment:
- On Windows: `venv\Scripts\activate`
- On Unix or MacOS: `source venv/bin/activate`
5. Install the required dependencies:

pip install -r requirements.txt

## Usage

### Running Flask Application

To start the Flask application:

1. Navigate to the `app` directory.
2. Run the Flask app by executing:


The Flask server will start, and you can access the web interface by going to `http://127.0.0.1:5000/` in your web browser.

### Running Jupyter Notebooks

To interact with the machine learning models:

1. Ensure you have Jupyter installed, or install it using:
2. Start the Jupyter notebook server:
3. Navigate to the `models` directory in the Jupyter notebook UI.
4. Open any of the `.ipynb` files, such as `neural_network.ipynb`, `random_forest.ipynb`, or `xgboost_lg.ipynb`.
5. Run the cells in the notebook to train the model or make predictions.

### Cloud Deployment

To deploy this project on the cloud:

1. Navigate to the `.github/workflows/deploy.yml` file.
2. Change the secret keys and any other necessary configurations specific to your cloud provider.
3. Commit and push these changes to trigger the CI/CD pipeline.

## Contributing

If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## Credits

This project was developed by Sanket Kulkarni. Special thanks to all contributors and supporters of this project.

## License

Python3

