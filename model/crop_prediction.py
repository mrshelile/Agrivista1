import pickle
import h5py
import joblib
import numpy as np
import os
from sklearn.linear_model import LinearRegression
import pandas as pd


class CropPrediction:
    
    def __init__(self) -> None:
        # import os
        # print(os.getcwd())

        self.path1 = "crop_prediction.h5"
        self.path2 = "crop_prediction.pkl"
        self.h5_filename = 'markerRegressor.pkl'
        # data = pd.read_excel("MarketDATA.xlsx")
        self.data = None
        self.marketModel = None
        self.model = None
        self.top_3_crops = None
        self.marketPredictionData =None
    
    async def load_model(self):
        if os.path.basename(os.getcwd()) != 'model':
            os.chdir('model')  # Change to the 'model' directory if not already there
            print("Changed to Directory:", os.getcwd())
        else:
            print("Already in Directory:", os.getcwd())
        self.data = pd.read_excel("MarketDATA.xlsx")
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        
        with h5py.File(self.path1, 'r') as hf:
            model_data = hf['random_forest'][:]
    
        # Save the buffer back to a .pkl file
        with open(self.path2, 'wb') as f:
            f.write(model_data.tobytes())
            self.model = joblib.load(self.path2)
            
        # open regressor
        with open(self.h5_filename , 'rb') as file:
            self.marketModel = pickle.load(file)
        print("Data and models loaded")
            
    async def make_prediction(self, input_data):
        # Prepare the input data as a numpy array for prediction
        input_data = np.array(input_data)
        crop_names = self.model.classes_
        predicted_probs = self.model.predict_proba(input_data)
        probabilities = predicted_probs[0]
        top_3_indices = probabilities.argsort()[-3:][::-1]
        top_3_crops = [(crop_names[i], probabilities[i]) for i in top_3_indices]
        
        self.top_3_crops = top_3_crops
        
    async def predict_market(self):
        selected_crops = []
        for crop in self.top_3_crops:
            selected_crops.append(crop[0])
        
        first =self.data[self.data['Crop'] == selected_crops[0]].iloc[-1].copy()
        second =self.data[self.data['Crop'] == selected_crops[1]].iloc[-1].copy()
        third =self.data[self.data['Crop'] == selected_crops[2]].iloc[-1].copy()
        
        # print(first)
        # print("*"*100)
        # print(second)
        # print("*"*100)
        # print(third)
        # print("*"*5)
        
        start_date = pd.to_datetime('2024-11-01')
        
        first_predictions = self.predict_future_margins_with_dates(selected_crops[0], first, start_date)
        second_predictions = self.predict_future_margins_with_dates(selected_crops[1], second, start_date)
        third_predictions = self.predict_future_margins_with_dates(selected_crops[2], third, start_date)
       
        # Combine predictions
        combined_predictions = pd.concat([first_predictions, second_predictions,third_predictions], ignore_index=True)
        combined_predictions['Date'] = pd.to_datetime(combined_predictions['Date'])
        
        # print(combined_predictions)
        
        self.marketPredictionData = pd.concat([combined_predictions,self.data],ignore_index=True)
        
        self.marketPredictionData['Date'] = pd.to_datetime(self.marketPredictionData['Date'])
        self.marketPredictionData.set_index('Date', inplace=True)

        # Ensure the index is sorted
        self.marketPredictionData.sort_index(inplace=True)
        
        self.marketPredictionData = self.marketPredictionData[self.marketPredictionData['Crop'].isin(selected_crops)]
        
        start_date = '2024-01-01'
        end_date = '2024-12-31'
        self.marketPredictionData = self.marketPredictionData.loc[start_date:end_date]
        self.marketPredictionData.to_csv('market.csv')
        # print(selected_crops)
        # print(self.marketPredictionData.tail(100))
        # Create a function to generate future data with dates
    def __generate_future_data_with_dates(self,last_row, start_date, months=2):
        future_data = []
        future_dates = pd.date_range(start=start_date, periods=months, freq='MS')  # Start of each month
        
        for date in future_dates:
            next_row = last_row.copy()
             # Add seasonal factor
             
            seasonal_factor = 1 + np.sin(date.month / 12 * 2 * np.pi) * 0.05  # Example of 5% seasonal fluctuation
            tan_factor = 1 + np.tan(date.month / 12 * np.pi / 4) * 0.02  # Adjust the multiplier to control sharpness
            # Estimate future Market Price and Production Cost with local volatility
            market_price_fluctuation = np.random.uniform(0.95, 1.05) * seasonal_factor *tan_factor # Apply small random factor
            production_cost_fluctuation = np.random.uniform(0.9, 1.15) * seasonal_factor *tan_factor # More volatility in cost
            # Estimate future Market Price and Production Cost
            next_row['Market_Price'] *= market_price_fluctuation  # Simulate price change
            next_row['Production_Cost'] *= production_cost_fluctuation  # Simulate cost change
            # print("-"*100)
            # print(next_row)
            # Update Previous Margin to the last predicted margin
            next_row['Previous_Margin'] = None  # Will be filled in later

            future_data.append((date, next_row))

        return future_data

    # Function to predict future margins for a specific crop
    def predict_future_margins_with_dates(self,crop_name, last_data_row, start_date, months=2):
        future_data = self.__generate_future_data_with_dates(last_data_row, start_date, months)
        
        predictions = []
    
        for date, row in future_data:
            previous_margin = self.marketModel.predict([row[['Market_Price', 'Production_Cost', 'Previous_Margin']]])[0]
            row['Previous_Margin'] = previous_margin
            
            predicted_margin = self.marketModel.predict([row[['Market_Price', 'Production_Cost', 'Previous_Margin']]])[0]
            predictions.append((date, predicted_margin, row['Market_Price'], row['Production_Cost']))

        predictions_df = pd.DataFrame(predictions, columns=['Date', 'Gross_Profit_Margin', 'Market_Price', 'Production_Cost'])
        predictions_df['Crop'] = crop_name
        
        return predictions_df

