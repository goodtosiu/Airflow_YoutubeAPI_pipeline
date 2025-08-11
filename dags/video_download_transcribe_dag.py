from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from modules.downloader import download_video
from modules.transcriber import generate_subtitle

with DAG(
    #dag_id="video_download_transcribe_dag",
    dag_id="video_download_transcribe_test_dag",
    start_date=datetime(2025, 7, 25),
    schedule_interval=None,
    catchup=False,
    #tags=["youtube", "step1"],
    tags=["youtube", "step1", "test"],
) as dag:

    download = PythonOperator(
        task_id="download_video",
        python_callable=download_video,
        op_kwargs={
            #"video_url": "{{ dag_run.conf['video_url'] }}",
            #"output_path": "/opt/airflow/data/videos/{{ dag_run.conf['video_id'] }}.mp4"
            "video_url": "https://www.youtube.com/watch?v=IZATGidlVK0",
        },
    )

    transcribe = PythonOperator(
        task_id="generate_subtitle",
        python_callable=generate_subtitle,
        op_kwargs={
            # "video_path": "/opt/airflow/data/videos/{{ dag_run.conf['video_id'] }}.mp4",
            # "output_path": "/opt/airflow/data/subtitles/{{ dag_run.conf['video_id'] }}.txt"
            "video_path": "{{ ti.xcom_pull(task_ids='download_video') }}", # XCom에서 경로 가져오기
            "output_path": "/opt/airflow/data/subtitles/IZATGidlVK0.txt"
        },
    )

    download >> transcribe
    #개쩌는 쏜애플 이유 라이브 영상
    #https://www.youtube.com/watch?v=Q97ojy28_m8&list=RDQ97ojy28_m8&start_radio=1