'''from Chest_Cancer_classifier import logger

logger.info("Welcome to the Chest_Cancer_classifier package!")'''

from Chest_Cancer_classifier import logger
from Chest_Cancer_classifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from Chest_Cancer_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Chest_Cancer_classifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from Chest_Cancer_classifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f">>>>>stage {STAGE_NAME} started<<<<<<")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>stage {STAGE_NAME} completed<<<<<<")

except Exception as e:
        logger.exception(e)
        raise e # re-raise the exception

STAGE_NAME = "Prepare base model"

try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Training"

try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e