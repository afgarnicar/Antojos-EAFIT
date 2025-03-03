import os
import sys
import django
import csv

# 📌 Agregar el directorio base del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Taller2.settings")

# 📌 Configurar Django
django.setup()

# 📌 Importar modelos después de `django.setup()`
from emprendedores.models import Entrepreneur

def load_data():
    csv_file = os.path.join(os.path.dirname(__file__), "emprendedores.csv")

    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            Entrepreneur.objects.create(
                business_name=row.get('business_name') if row.get('location') else None,    # Normalizar vacíos a None
                location=row.get('location') if row.get('location') else None,  # Normalizar vacíos a None
                schedule=row.get('schedule') if row.get('location') else None,  # Normalizar vacíos a None
                contact_info=row.get('contact_info') if row.get('location') else None   # Normalizar vacíos a None
            )
    print("Datos cargados exitosamente.")


# 📌 Ejecutar solo si se llama directamente el script
if __name__ == "__main__":
    load_data()
