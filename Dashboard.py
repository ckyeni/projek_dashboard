import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Header
st.title("Dashboard Penyewaan Sepeda🚲")
st.text('Oleh: Yeni Ckrisdayanti Manalu')

# Load data
df = pd.read_csv("C:/Users/Lenovo/Downloads/data_penyewaan.csv")

#Pertanyaan nomor 1
# Sidebar for Year and Month filters
st.sidebar.title("Filter Dashboard Penyewaan Sepeda")
year_option = st.sidebar.selectbox("Tahun", df["yr"].unique())
month_option = st.sidebar.radio(label="Bulan", options=df["mnth"].unique(), horizontal=False)
day_option = st.sidebar.selectbox("Pilih Hari", df["weekday"].unique())
workingday_option = st.sidebar.selectbox("Pilih Hari Kerja", df["workingday"].unique())

# **Filter Data Berdasarkan Tahun yang Dipilih**
filtered_df_year = df[df["yr"] == year_option]

#Line Chart 1
# **Total Penyewaan Sepeda Berdasarkan Bulan**
st.subheader("Tren Total Penyewaan Sepeda Berdasarkan Bulan")
monthly_trend = filtered_df_year.groupby("mnth")["cnt"].sum()

# Plot Line Chart for Monthly Trend
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=monthly_trend.index, y=monthly_trend.values, marker="*", label=f"{year_option}", ax=ax, linewidth=5)
ax.set_xticks(range(1, 13))
ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"])
ax.set_xlabel("")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title(f"Tren Total Penyewaan Sepeda per Bulan pada tahun {year_option}")
ax.legend()
ax.grid(False)
st.pyplot(fig)

#tambahan visualisasi
#Barchart
# **Perbandingan Total Penyewaan Sepeda Berdasarkan Hari Kerja**
st.subheader("Perbandingan Total Penyewaan Sepeda Berdasarkan Hari Kerja")
# Filter data based on the selected year and month
filtered_df = df[(df["yr"] == year_option) & (df["mnth"] == month_option)]

# Group the data by year and working day, then calculate the sum of the rentals
workingday_trend_yearly = filtered_df.groupby(["yr", "workingday"])["cnt"].sum().unstack()

# Display the data in Streamlit
st.write(workingday_trend_yearly)

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
workingday_trend_yearly.T.plot(kind="bar", ax=ax, colormap="viridis")

# Adjusting labels and title
ax.set_xticks([0, 1])
ax.set_xticklabels(["Non-Workday", "Workday"], rotation=0)
ax.set_xlabel("")
ax.set_ylabel("Total Penyewaan")
ax.set_title(f"Perbandingan Penyewaan Sepeda pada Hari Kerja pada {month_option}, Tahun {year_option}")

# Display the plot in Streamlit
st.pyplot(fig)

#Line Chart 2
# **Total Penyewaan Sepeda Berdasarkan Hari**
st.subheader("Tren Total Penyewaan Sepeda Berdasarkan Hari")
#filter bulan
filtered_df_month = df[df["mnth"] == month_option]
daily_trend = filtered_df_month.groupby("weekday")["cnt"].sum()

# Plot Line Chart for Daily Trend
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=daily_trend.index, y=daily_trend.values, marker="o", label=f"{month_option}", ax=ax, linewidth=5)
ax.set_xticks(range(7))
ax.set_xticklabels(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
ax.set_xlabel("")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title(f"Tren Total Penyewaan Sepeda per Hari ({month_option})")
ax.legend()
ax.grid(False)
st.pyplot(fig)

#Barchart 1
# **Perbandingan Penyewaan Sepeda (Casual vs Registered) Berdasarkan Musim**
st.subheader("Perbandingan Total Penyewaan Sepeda (Casual vs Registered) Berdasarkan Musim")
filtered_df_season = df[df["yr"] == year_option]
casual_season = filtered_df_season.groupby("season")["casual"].sum()
registered_season = filtered_df_season.groupby("season")["registered"].sum()

# Create Layout with 2 Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("")
    fig, ax = plt.subplots(figsize=(3, 4))
    sns.barplot(x=casual_season.index, y=casual_season.values, palette="Blues", ax=ax)
    ax.set_xlabel("")
    ax.set_ylabel("Total Casual")
    ax.set_title("Casual Rentals")
    ax.set_xticklabels(casual_season.index, rotation=15)
    st.pyplot(fig)

with col2:
    st.subheader("")
    fig, ax = plt.subplots(figsize=(3, 4))
    sns.barplot(x=registered_season.index, y=registered_season.values, palette="Oranges", ax=ax)
    ax.set_xlabel("")
    ax.set_ylabel("Total Registered")
    ax.set_title("Registered Rentals")
    ax.set_xticklabels(casual_season.index, rotation=15)
    st.pyplot(fig)

#Pertanyaan nomor 2
#Barchart 2
# **Perbandingan Penyewaan Sepeda Berdasarkan Weathersit**
st.subheader("Perbandingan Total Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
filtered_df_season = df[df["mnth"] == month_option]
casual_season = filtered_df_season.groupby("weathersit")["casual"].sum()
registered_season = filtered_df_season.groupby("weathersit")["registered"].sum()

# Create Layout with 2 Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("")
    fig, ax = plt.subplots(figsize=(3, 4))
    sns.barplot(x=casual_season.index, y=casual_season.values, palette="Blues", ax=ax)
    ax.set_xlabel("")
    ax.set_ylabel("Total Casual")
    ax.set_title("Casual Rentals")
    ax.set_xticklabels(casual_season.index, rotation=25)
    st.pyplot(fig)
with col2:
    st.subheader("")
    fig, ax = plt.subplots(figsize=(3, 4))
    sns.barplot(x=registered_season.index, y=registered_season.values, palette="Oranges", ax=ax)
    ax.set_xlabel("")
    ax.set_ylabel("Total Registered")
    ax.set_title("Registered Rentals")
    ax.set_xticklabels(casual_season.index, rotation=25)
    st.pyplot(fig)

#Pertanyaan nomor 3
#Line chart 3
# **Total Penyewaan Sepeda Berdasarkan Jam**
st.subheader("Tren Total Penyewaan Sepeda Berdasarkan Jam")
# Filter data based on selected Year, Month, and Day of the Week
filtered_df = df[(df["yr"] == year_option) & (df["mnth"] == month_option) & (df["weekday"] == day_option)]

# Total Rentals per Hour (hr) for the selected Year, Month, and Day
hourly_trend = filtered_df.groupby("hr")["cnt"].sum()

# Plot Line Chart for Hourly Rentals on the selected day, month, and year
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hourly_trend.index, y=hourly_trend.values, marker="o", label=f"{day_option}", ax=ax, linewidth=2)
ax.set_xlabel("Jam (hr)")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title(f"Tren Total Penyewaan Sepeda per Jam pada {day_option}, {month_option}, Tahun {year_option}")
ax.grid(False)
st.pyplot(fig)

#Pertanyaan nomor 4
#Korelasi
st.subheader("Heatmap")
#Meninjau faktor" yang mempengaruhi Penyewaan Sepeda
# Menghitung korelasi antara variabel cuaca dan jumlah penyewaan sepeda
correlation = df[["cnt", "temp", "hum", "windspeed"]].corr()
print(correlation)

# Visualisasi menggunakan heatmap
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(correlation, annot=True, cmap="viridis", fmt=".2f", linewidths=0.5, ax=ax)

# Mengatur judul
plt.title("Korelasi antara Variabel yg Menjadi Faktor Penyewaan Sepeda")

# Menampilkan heatmap di Streamlit
st.pyplot(fig)

#Visualisasi Perbandingan Cluster
#Perbandingan hasil cluster
st.subheader("Perbandingan Hasil Cluster")

#Barchart Cluster
# Filter data based on the selected year, month, and working day
filtered_df = df[(df["yr"] == year_option) & (df["mnth"] == month_option) & (df["workingday"] == workingday_option)]

# Group the data by 'cluster' and calculate the sum of rentals
cluster_trend = filtered_df.groupby("Cluster")["cnt"].sum()

# Display the data in Streamlit
st.write(cluster_trend)

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=cluster_trend.index, y=cluster_trend.values, palette="viridis", ax=ax)

# Adjusting labels and title
ax.set_xlabel("Cluster")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title(f"Total Penyewaan Sepeda Berdasarkan Cluster ({year_option}) dan Bulan ({month_option}) pada Hari Kerja {workingday_option}")
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)

# Visualisasi Total Penyewaan
st.subheader("Total Penyewaan Sepeda per Cluster")
cluster_summary = df.groupby("Cluster")["cnt"].sum().reset_index()
fig, ax = plt.subplots()
sns.barplot(x="Cluster", y="cnt", data=cluster_summary, palette="coolwarm", ax=ax)
plt.xticks(rotation=30)
st.pyplot(fig)

# Rata-rata Penyewaan Sepeda
st.subheader("Rata-rata Penyewaan Sepeda per Cluster")
cluster_avg = df.groupby("Cluster")["cnt"].mean().reset_index()
fig, ax = plt.subplots()
sns.barplot(x="Cluster", y="cnt", data=cluster_avg, palette="magma", ax=ax)
plt.xticks(rotation=30)
st.pyplot(fig)

# Sidebar2
cluster_option = st.sidebar.selectbox("Pilih Cluster Dataset Penyewaan Sepeda yang ingin kamu eksplor", df["Cluster"].unique())

# Filter data berdasarkan cluster
filtered_df = df[df["Cluster"] == cluster_option]

# Menampilkan data
st.subheader(f"Dataset Penyewaan Sepeda Cluster {cluster_option}")
st.write(filtered_df)
