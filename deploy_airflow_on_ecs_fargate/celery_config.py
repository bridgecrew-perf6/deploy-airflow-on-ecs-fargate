import os

from airflow.config_templates.default_celery import DEFAULT_CELERY_CONFIG

CELERY_CONFIG = {
    **DEFAULT_CELERY_CONFIG,
    "broker_transport_options": {
        **DEFAULT_CELERY_CONFIG["broker_transport_options"],
        "predefined_queues": {
            "airflow-worker-broker": {
                "url": os.getenv("X_AIRFLOW_SQS_CELERY_BROKER_PREDEFINED_QUEUE_URL")
            },
        },
    },
}
