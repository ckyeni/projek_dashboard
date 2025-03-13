# Dashboard Penyewaan Sepeda🚲
Berikut Dashboard Peryewaan Sepeda menggunakan dataset hour.csv dari Bike Sharing Dataset yang merupakan hasil proyek analisis data dari modul "Belajar Analisis Data dengan Python"

## Setup Environment - Visual Studio Code
```
Buka terminal di Visual Studio Code dan jalankan perintah berikut untuk membuat environment baru:
python -m venv env
.\env\Scripts\activate #aktifkan environment
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir Proyek_Analisis_Data
cd Proyek_Analisis_Data
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```

```
submission
├───dashboard
| ├───data_penyewaan.csv
| └───Dashboard.py
├───data
| ├───hour.csv
| └───data_penyewaan.csv
├───Proyek_Analisis_Data.ipynb
├───README.md
└───requirements.txt
└───url.txt : http://192.168.43.172:8502
```