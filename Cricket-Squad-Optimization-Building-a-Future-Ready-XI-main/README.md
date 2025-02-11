# 🏏 Squad Optimization: Building a Future-Ready XI  

As a **Cricket Analytics Consultant**, our task is to build an optimal **Playing XI** for a franchise team, ensuring competitiveness for at least **five years**. The focus is on selecting **young, high-potential players** who align with T20 cricket strategies while providing the **best return on investment** within a budget of **₹100 Crores**.  

---

## ✨ Authors  

- [@Irfan](#)  
- [@Mokith](#)  
- [@Ametha](#)  
- [@Naahid](#)  

---

## 📌 Table of Contents  

- [Installation](#installation)  
- [Requirements](#requirements)  
- [Deployment](#deployment)  
- [Embedding Power BI Dashboard](#embedding-power-bi-dashboard)

---

## ⚡ Installation  

Follow these steps to set up and run the project locally:  

### 1️⃣ Clone the repository  

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### 2️⃣ Install required dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install Flask (if not already installed)

```bash
pip install flask
```

### 4️⃣ Verify Power BI dashboard is published to Power BI Service

---

## 📋 Requirements 

| Dependency                  | Version                         |
|-----------------------------|---------------------------------|
| **Python**                  | 3.8 or higher                   |
| **pip**                     | Latest                          |
| **Flask**                   | Latest                          |
| **Power BI Desktop**         | Required for `.pbix` creation  |
| **Microsoft Power BI Service** | Required for dashboard hosting |

---

## 🚀 Deployment 

To run the Flask application locally, execute the following steps:

### 1️⃣ Run the Flask app

```bash
python app.py
```

### 2️⃣ Open your browser and go to
http://127.0.0.1:5000

---

## 📊 Embedding Power BI Dashboard

Follow these steps to embed your Power BI dashboard into the Flask application:

### 1️⃣ Publish the .pbix file to Power BI Service
- Open your .pbix file in Power BI Desktop
- Navigate to File → Publish → Publish to Power BI
### 2️⃣ Get the Embed Code
- In Power BI Service, navigate to your report
- Click File → Embed Report → Website or Portal
- Copy the embed URL
### 3️⃣ Modify index.html
- Open the index.html file in your project folder
- Replace the placeholder iframe with your Power BI embed link

```bash
<iframe width="100%" height="600" src="<your-embed-url>" frameborder="0" allowFullScreen="true"></iframe>
```

---

### 🎯 Key Features  

✅ **Automated Selection** of high-potential young players  
✅ **Power BI Dashboard Integration** for better data visualization  
✅ **Budget Optimization** with smart salary allocation  
✅ **User-Friendly Web Interface** powered by Flask  
✅ **Interactive Squad Filtering** based on key performance indicators  

