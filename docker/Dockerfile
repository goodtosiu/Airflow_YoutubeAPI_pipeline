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

# 🧾 requirements.txt 복사
COPY requirements.txt /opt/airflow/requirements.txt

# Airflow 컨테이너는 'airflow' 유저로 파이썬 패키지 설치 권장
USER airflow

# 🔼 pip 최신화 + 프로젝트 의존성 설치 + yt-dlp 최신화
#  - requirements.txt 설치 후 yt-dlp를 별도로 최신화하여
#    requirements에 pin이 있더라도 최종적으로 최신 yt-dlp가 사용되도록 함
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /opt/airflow/requirements.txt \
    && pip install --no-cache-dir --upgrade yt-dlp