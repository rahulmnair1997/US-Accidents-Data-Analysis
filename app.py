'''
make County, Street and City lowercase

'''

import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
import pandas as pd
import pickle


app = Flask(__name__)
model = pickle.load(open('model_xgb.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
zip_c = pickle.load(open('Zipcode.pkl', 'rb'))
airport_c = pickle.load(open('Airport_Code.pkl', 'rb'))
city_f = pickle.load(open('City.pkl', 'rb'))
county_f = pickle.load(open('County.pkl', 'rb'))
street_f = pickle.load(open('Street.pkl', 'rb'))	
cat = ['Amenity', 'Crossing', 'Junction', 'Railway', 'Station', 'Stop', 'Traffic_Signal', 'month', 'Side', 'State', 'Sunrise_Sunset', 'Timezone', 'Weather_Condition', 'Wind_Direction']
one_hot = {}
for i in cat:
	one_hot[i] = pickle.load(open('one_hot_'+i+'.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    main_features = [x for x in request.form.values()]
    int_features = [float(x) for x in main_features[0:15]]
    string_features = [x for x in main_features[15:26]]
    features = int_features + string_features
    zip_freq = zip_c[zip_c['Zipcode'] == string_features[6]]['Zipcode_freq'].values[0]
    airport_code_freq = airport_c[airport_c['Airport_Code'] == string_features[7]]['Airport_Code_freq'].values[0]
    city_freq = city_f[city_f['City'] == string_features[8].lower()]['City_freq'].values[0]
    county_freq = county_f[county_f['County'] == string_features[9].lower()]['County_freq'].values[0]
    street_freq = street_f[street_f['Street'] == string_features[10].lower()]['Street_freq'].values[0]
    num_list = ['Distance', 'Temperature', 'Humidity', 'Pressure', 'Visibility', 'Wind_Speed', 'Duration', 'Visibility']
    d = {}
    for i in range(0,8):
    	d[num_list[i]] = int_features[i]
    test_df = pd.DataFrame([[d['Distance'], d['Temperature'], d['Humidity'], d['Pressure'] ,d['Visibility'], d['Wind_Speed'], d['Duration'], zip_freq, airport_code_freq, city_freq, county_freq, street_freq]], columns=['Distance', 'Temperature', 'Humidity', 'Pressure', 'Visibility', 'Wind_Speed', 'Duration', 'zip', 'airport_code', 'city', 'county', 'street'])
    d_2 = {}
    cat_features = [int(x) for x in features[7:15]]
    cat_features = cat_features + features[15:21]
    for i in range(len(cat_features)):
    	d_2[cat[i]] = cat_features[i]
    one_hot_df = pd.DataFrame([[d_2['Amenity'], d_2['Crossing'], d_2['Junction'], d_2['Railway'],  d_2['Station'], d_2['Stop'], d_2['Traffic_Signal'], d_2['month'], d_2['Side'], d_2['State'], d_2['Sunrise_Sunset'], d_2['Timezone'], d_2['Weather_Condition'], d_2['Wind_Direction']]], columns=['Amenity', 'Crossing', 'Junction', 'Railway', 'Station', 'Stop', 'Traffic_Signal', 'month', 'Side', 'State', 'Sunrise_Sunset', 'Timezone', 'Weather_Condition', 'Wind_Direction'])
    for i in cat:
    	ohe = one_hot[i].transform(one_hot_df[i].values.reshape(-1,1)).toarray()
    	dfone_hot = pd.DataFrame(ohe, columns=[i+str(one_hot[i].categories_[0][j]) 
                                           for j in range(len(one_hot[i].categories_[0]))])
    	test_df = test_df.join(dfone_hot)
    test_df = scaler.transform(test_df)
    pred = model.predict(test_df)[0]
    return render_template('index.html', prediction_text='The Severity of accident would be {}'.format(pred))



@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)