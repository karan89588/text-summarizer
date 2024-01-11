# from textSummarizer.pipeline.stage_01_data_ingestion import (
#     DataIngestionTrainingPipeline,
# )
# from textSummarizer.pipeline.stage_02_data_validation import (
#     DataValidationTrainingPipeline,
# )
# from textSummarizer.pipeline.stage_03_data_transformation import (
#     DataTransformationTrainingPipeline,
# )
# from textSummarizer.pipeline.stage_05_model_evaluation import (
#     ModelEvaluationTrainingPipeline,
# )
# from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from textSummarizer.logging import logger

from textSummarizer.pipeline.prediction import PredictionPipeline

# STAGE_NAME = "Data Ingestion Stage"
# try:
#     logger.info(f">>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<")
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info(f">>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx========x")
# except Exception as e:
#     logger.exception(e)
#     raise e


# STAGE_NAME = "Data Validation Stage"
# try:
#     logger.info(f">>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<")
#     data_validation = DataValidationTrainingPipeline()
#     data_validation.main()
#     logger.info(f">>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx========x")
# except Exception as e:
#     logger.exception(e)
#     raise e

# STAGE_NAME = "Data Transformation Stage"
# try:
#     logger.info(f">>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<")
#     data_transformation = DataTransformationTrainingPipeline()
#     data_transformation.main()
#     logger.info(f">>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx========x")
# except Exception as e:
#     logger.exception(e)
# # # #     raise e

# STAGE_NAME = "Model Training Stage"
# try:
#     logger.info(f">>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<")
#     model_trainer = ModelTrainerTrainingPipeline()
#     model_trainer.main()
#     logger.info(f">>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx========x")
# except Exception as e:
#     logger.exception(e)
#     raise e

# STAGE_NAME = "Model Evaluation Stage"
# try:
#     logger.info(f">>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<")
#     model_evaluation = ModelEvaluationTrainingPipeline()
#     model_evaluation.main()
#     logger.info(f">>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx========x")
# except Exception as e:
#     logger.exception(e)
#     raise e

pipe = PredictionPipeline()
text = "Deep learning is a branch of machine learning which is based on artificial neural networks. It is capable of learning complex patterns and relationships within data. In deep learning, we dont need to explicitly program everything. It has become increasingly popular in recent years due to the advances in processing power and the availability of large datasets. Because it is based on artificial neural networks (ANNs) also known as deep neural networks (DNNs). These neural networks are inspired by the structure and function of the human brains biological neurons, and they are designed to learn from large amounts of data Deep Learning is a subfield of Machine Learning that involves the use of neural networks to model and solve complex problems. Neural networks are modeled after the structure and function of the human brain and consist of layers of interconnected nodes that process and transform data.The key characteristic of Deep Learning is the use of deep neural networks, which have multiple layers of interconnected nodes. These networks can learn complex representations of data by discovering hierarchical patterns and features in the data. Deep Learning algorithms can automatically learn and improve from data without the need for manual feature engineering.Deep Learning has achieved significant success in various fields, including image recognition, natural language processing, speech recognition, and recommendation systems. Some of the popular Deep Learning architectures include Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and Deep Belief Networks (DBNs).Training deep neural networks typically requires a large amount of data and computational resources. However, the availability of cloud computing and the development of specialized hardware, such as Graphics Processing Units (GPUs), has made it easier to train deep neural networks.In summary, Deep Learning is a subfield of Machine Learning that involves the use of deep neural networks to model and solve complex problems. Deep Learning has achieved significant success in various fields, and its use is expected to continue to grow as more data becomes available, and more powerful computing resources become available."
summary = pipe.predict(text, 250)
print(f"Length of original text : {len(text)}")
print(f"Length of summary text : {len(summary)}")
print(f"Summary :\n{summary}")
