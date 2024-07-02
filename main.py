from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline
from cnnClassifier import logger



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "prepare base model"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    prepare_base_model = ModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    prepare_base_model = EvaluationPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e