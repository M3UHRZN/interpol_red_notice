# Python 3.11 imajını kullanalım
FROM python:3.11

# Çalışma dizinini /app olarak ayarlayalım
WORKDIR /app

# Gerekli Python paketlerini kurmak için requirements.txt dosyasını kopyalayalım
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Proje dosyalarını kopyalayalım
COPY fetch_interpol_data.py fetch_interpol_data.py

# İmajı çalıştırmak için gerekli komutu belirleyelim
CMD ["python", "fetch_interpol_data.py"]
