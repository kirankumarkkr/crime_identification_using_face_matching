# Crime Identification Using Face Matching
---
**Crime Identification Using Face Matching** is a mobile application designed to streamline the process of identifying criminals using advanced face recognition technology. It empowers law enforcement officers to quickly retrieve detailed criminal records, ensuring accuracy and efficiency in criminal investigations.

---

## 📝 **Table of Contents**
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📌 **Problem Statement**

Traditional methods of criminal identification are time-consuming, prone to human error, and often lack accuracy. Retrieving a suspect's background information requires extensive manual effort, leading to delays in critical situations.

This project addresses these challenges by leveraging face recognition technology to:
- Accurately identify suspects.
- Retrieve comprehensive criminal profiles, including name, case number, and associated crimes.
- Enable law enforcement to act swiftly and effectively.

---

## 🚀 **Features**
- **Face Recognition**: Uses AI to match a suspect’s face with a database of known criminals.
- **Quick Search**: Retrieve criminal details like name, photo, case history, and location in real-time.
- **User Roles**:
  - **Admin**: Upload criminal records and manage the database.
  - **Police Officer**: Search for and identify criminals.
- **Mobile-First Design**: Optimized for mobile devices, making it accessible in the field.
- **Secure Storage**: Ensures all data is encrypted and protected.

---

## 🛠️ **Technologies Used**
- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: MySQL
- **Face Recognition**: OpenCV, TensorFlow (or similar libraries)
- **Mobile Integration**: WebView (Android Studio)
- **Authentication**: Role-based user authentication

---

## 🔧 **Installation**

1. Clone this repository:
   ```bash
   git clone https://github.com/kirankumarkkr/crime-identification-face-matching.git
   cd crime-identification-face-matching
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the database in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the server:
   ```bash
   python manage.py runserver
   ```

6. Open the app in your browser or connect it to the mobile application.

---

## 📖 **Usage**

1. **Admin Role**:
   - Log in with admin credentials.
   - Upload new criminal records with images and details.
   - Manage existing records.

2. **Police Role**:
   - Log in with police credentials.
   - Use the search feature to identify criminals using photos or text-based queries.
   - View retrieved criminal history.

---

## 🤝 **Contributing**

Contributions are welcome! Please follow these steps:
1. Fork this repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## 📜 **License**
This project is licensed under the [MIT License](LICENSE).

---

## 📧 **Contact**
- **Author**: Kiran Kumar R  
- **Email**: kirankumarkkr29@gmail.com  
- **LinkedIn**: https://www.linkedin.com/in/kiran-kumar-065734273 .  
- **Instagram**: https://www.instagram.com/_kiran_kumar_r_.

