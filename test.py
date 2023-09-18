import pandas as pd

# Replace 'your_dataset.csv' with the path to your CSV file
csv_file_path = r"C:\Users\User\Documents\New folder\GreyWolfOptimization-MKSVM\dataset\php3YXJ45.csv"

# Load your CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
#print(df.head())
#print(df.columns)
#print(df['Class'].unique())

# Define the class and method for preprocessing
class DatasetProcessor:
    def __init__(self, df):
        self.df = df
        self.X = None
        self.Y = None

    def preprocessing(self):
        print("Start preprocessing the dataset")

        # Separate the target variable (Y) from the features (X)
        self.Y = self.df['Class']
        self.X = self.df.drop(['Class'], axis=1)

        print("Preprocessing complete")

    def fit(self, l):
        print("Start creating the fit")
        # Assuming you have a function called 'classify' to perform the fitting
        return classify(self.X, self.Y, l)


# Create an instance of DatasetProcessor and pass your DataFrame
sample_df = df.shape  #(2800, 27)
print(sample_df)
processor = DatasetProcessor(df)
processor.preprocessing()

# Access the preprocessed data
X_data = processor.X
Y_data = processor.Y

# Print the preprocessed data
#print("Preprocessed X:")
#print(X_data)
#print("\nPreprocessed Y:")
#print(Y_data)
#print(X_data.keys())
keys = X_data.keys()
print(len(keys))
X_temp = X_data.drop(keys[0],axis=1)
#print(X_temp)
X_data = X_data.drop(keys[0],axis=1)
#print(X_data)
# Fit the model using the 'fit' method
#l_value = [1., 1., 0. ,0. ,0. ,1. ,1. ,0., 1. ,1., 0. ,1. ,0., 1. ,1., 0., 1., 1. ,1., 1. ,0., 1., 0., 1.] 
#result = processor.fit(l_value)
#print("\nFit result:", result)

