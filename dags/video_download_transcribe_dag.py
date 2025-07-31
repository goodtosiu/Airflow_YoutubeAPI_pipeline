from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from modules.downloader import download_video
from modules.transcriber import generate_subtitle

with DAG(
    dag_id="video_download_transcribe_dag",
    start_date=datetime(2025, 7, 25),
    schedule_interval=None,
    catchup=False,
    tags=["youtube", "step1"],
) as dag:

    download = PythonOperator(
        task_id="download_video",
        python_callable=download_video,
        op_kwargs={
            "video_url": "{{ dag_run.conf['video_url'] }}",
            "output_path": "/opt/airflow/data/videos/{{ dag_run.conf['video_id'] }}.mp4"
        },
    )

    transcribe = PythonOperator(
        task_id="generate_subtitle",
        python_callable=generate_subtitle,
        op_kwargs={
            "video_path": "/opt/airflow/data/videos/{{ dag_run.conf['video_id'] }}.mp4",
            "output_path": "/opt/airflow/data/subtitles/{{ dag_run.conf['video_id'] }}.txt"
        },
    )

    download >> transcribe