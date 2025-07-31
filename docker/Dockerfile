FROM apache/airflow:2.7.2-python3.10

USER root

# 🧱 필수 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 🏗️ 작업 디렉토리
WORKDIR /opt/airflow

# 🧾 requirements.txt 복사 및 설치
COPY requirements.txt .

# 🧩 Airflow 전용: 추가적으로 환경변수가 필요하면 docker-compose에서 설정

USER airflow

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt