Django Project
This project is a Django-based web application for publishing products and managing categories.  
Prerequisites
Python 3.x
pip (Python package installer)
MongoDB (for storing images)
Installation
Clone the repository:  
git clone https://github.com/afgarnicar/Antojos-EAFIT/tree/Rama-Cesar-Montoya/Taller%202/AgregarProducto
cd your-repository
Create a virtual environment:  
python -m venv venv
Activate the virtual environment:  
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
Install the dependencies:  
pip install -r requirements.txt
Set up the database: Make sure MongoDB is running on your local machine or update the connection string in your settings if using a remote MongoDB instance.  
Run database migrations:  
python manage.py migrate
Running the Server
Start the Django development server:  
python manage.py runserver
Open your web browser and navigate to:  
http://127.0.0.1:8000/

Usage
Publish Product: Navigate to the "Publish Product" page to add a new product.
Categories: Navigate to the "Categories" page to view and manage product categories.