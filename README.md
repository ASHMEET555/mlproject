# Student Math Score Prediction Project

A machine learning project focused on predicting **students’ math performance scores** using demographic, academic, and socio-economic features. The project includes the full workflow — from data exploration and preprocessing to model training, evaluation, and deployment through a simple web application.

---

## 🚀 Project Overview

This project predicts **student math scores** based on features such as study habits, parental education levels, test preparation, and other academic indicators. It demonstrates:

* Feature engineering for educational datasets
* Model training and hyperparameter tuning
* Evaluation using regression metrics
* Saving trained models and transformers
* Deployment through a Flask web application

---

## ✅ Features

* Modular ML codebase inside `src/`
* EDA and model experimentation inside `notebook/`
* Automatic storage of model artifacts
* Web-based prediction interface
* Easy installation via `setup.py`
* Reproducible environment with `requirements.txt`

---

## 📂 Project Structure

```
mlproject/
├── artifacts/              # Stores trained models, logs, and outputs
├── catboost_info/          # CatBoost training metadata
├── notebook/               # Jupyter notebooks for exploration and experiments
├── src/                    # ML pipeline modules
│   ├── data/               # Data loading & preprocessing
│   ├── features/           # Feature engineering
│   ├── modeling/           # Training, evaluation, model building
│   ├── utils/              # Helper utilities
│   └── ...
├── templates/              # HTML templates for the web app (if applicable)
├── application.py          # Main web application
├── setup.py                # Package configuration
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Ignored files
```

---

## 🛠️ Getting Started

Follow these steps to set up and run the project.

### **Prerequisites**

* Python 3.7+
* (Optional) Virtual environment

### **Installation**

```bash
git clone https://github.com/ASHMEET555/mlproject.git
cd mlproject
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **Run the Application**

To start the web interface:

```bash
python application.py
```

Then visit the local URL shown in the terminal (e.g., `http://127.0.0.1:5000`).

---

## 📘 Usage

* Use notebooks in `notebook/` for EDA and training.
* Trained model artifacts are stored in `artifacts/`.
* `application.py` loads the model pipeline and exposes a UI/API.
* Extend the pipeline by modifying modules inside `src/`.

---

## 🧠 Technologies Used

* Python
* CatBoost / Sklearn (as used in the notebooks and pipeline)
* Flask / Web framework for UI
* Jupyter Notebooks

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`feature-xyz`)
3. Commit your changes
4. Push and open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 📬 Contact

Author: **Ashmeet**
GitHub: [ASHMEET555](https://github.com/ASHMEET555)

If you'd like badges, screenshots, or improvements to this README, feel free to ask!
