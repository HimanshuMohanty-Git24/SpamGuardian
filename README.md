# SpamGuardian 🛡️

SpamGuardian is a powerful Python-based project designed to detect spam messages using a robust Machine Learning model. With this tool, you can simply paste a message, and our AI will determine whether it's spam or not, helping you stay safe from unwanted and potentially harmful content.

## Tech Stack 🚀

### Python Libraries:
- **Streamlit:** Used for rendering and deploying the application.
- **NLTK:** Natural Language Toolkit for text processing and analysis.
- **Scikit-learn:** Utilized for building and training the Machine Learning model.
- **NumPy:** Essential for numerical operations.
- **Pandas:** Efficient data manipulation and analysis.

## Methodologies Used 🧠

1. **Data Cleaning:** Ensured high-quality data by removing irrelevant information and handling missing values.
2. **EDA (Exploratory Data Analysis):** Explored and visualized the dataset to gain insights into the distribution and characteristics of spam messages.
3. **Data Preprocessing:** Prepared the data for model training by tokenizing, stemming, and vectorizing text data.
4. **Model Building:** Employed machine learning techniques to build a robust spam detection model.
5. **Making PKL Files:** Created Pickle files to efficiently use the trained model in the main application (app.py).

## Deployment 🚀

The application is deployed on Streamlit, providing an easy-to-use and interactive interface for users to check messages for spam.

## How to Use 🤖

1. Visit the deployed application link.
2. Paste the message you want to check into the provided text area.
3. Click the "Check Spam" button.
4. Receive instant feedback on whether the message is spam or not.

Stay safe from spam with SpamGuardian! 🛡️💬

## How to Use in Local Environment 🖥️

To run SpamGuardian locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/HimanshuMohanty-Git24/SpamGuardian.git
   ```

2. Navigate to the project directory:

   ```bash
   cd SpamGuardian
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

5. Open your web browser and go to `http://localhost:8501` to access the SpamGuardian application.

## Acknowledgments 🙌

We would like to express our gratitude to the open-source community and the developers behind the libraries used in this project.

## License 📜

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute and make SpamGuardian even better! 🚀👩‍💻👨‍💻
