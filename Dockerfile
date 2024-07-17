# استخدام Python 3.12 كقاعدة
FROM python:3.12

# تحديث مستودعات APT وتثبيت الأدوات الأساسية
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# إضافة الملفات المشروع إلى مجلد /app في الصورة
COPY . /app
WORKDIR /app

# ترقية pip وتثبيت متطلبات المشروع
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# إعداد الأمر الافتراضي لتشغيل التطبيق عند تشغيل الصورة
CMD ["python", "manage.py", "runserver"]
