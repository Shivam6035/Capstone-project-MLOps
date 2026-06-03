# # register model

# import json
# import mlflow
# import logging
# from src.logger import logging
# import os
# import dagshub
# import datetime
# import json

# import warnings
# warnings.simplefilter("ignore", UserWarning)
# warnings.filterwarnings("ignore")

# # Below code block is for production use
# # -------------------------------------------------------------------------------------
# # # Set up DagsHub credentials for MLflow tracking
# # dagshub_token = os.getenv("CAPSTONE_TEST")
# # if not dagshub_token:
# #     raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

# # os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
# # os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

# # dagshub_url = "https://dagshub.com"
# # repo_owner = "vikashdas770"
# # repo_name = "YT-Capstone-Project"
# # # Set up MLflow tracking URI
# # mlflow.set_tracking_uri(f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')
# # -------------------------------------------------------------------------------------


# # Below code block is for local use
# # -------------------------------------------------------------------------------------
# mlflow.set_tracking_uri('https://dagshub.com/Shivam6035/Capstone-project-MLOps.mlflow')
# dagshub.init(repo_owner='Shivam6035', repo_name='Capstone-project-MLOps', mlflow=True)
# # -------------------------------------------------------------------------------------


# def load_model_info(file_path: str) -> dict:
#     """Load the model info from a JSON file."""
#     try:
#         with open(file_path, 'r') as file:
#             model_info = json.load(file)
#         logging.debug('Model info loaded from %s', file_path)
#         return model_info
#     except FileNotFoundError:
#         logging.error('File not found: %s', file_path)
#         raise
#     except Exception as e:
#         logging.error('Unexpected error occurred while loading the model info: %s', e)
#         raise

# def register_model(model_name: str, model_info: dict):
#     """Register the model to the MLflow Model Registry."""
#     try:
#         model_uri = f"runs:/{model_info['run_id']}/{model_info['model_path']}"
        
#         # Register the model
#         model_version = mlflow.register_model(model_uri, model_name)

#         # Transition the model to "Staging" stage
#         client = mlflow.tracking.MlflowClient()
#         client.transition_model_version_stage(
#             name=model_name,
#             version=model_version.version,
#             stage="Staging"
#         )

#         logging.debug(f'Model {model_name} version {model_version.version} registered and transitioned to Staging.')

#         # Write a small registration record file so DVC can track this stage's output
#         os.makedirs('reports', exist_ok=True)
#         registration_record = {
#             'model_name': model_name,
#             'version': int(model_version.version),
#             'stage': 'Staging',
#             'run_id': model_info.get('run_id'),
#             'model_path': model_info.get('model_path'),
#             'registered_at': datetime.datetime.utcnow().isoformat() + 'Z'
#         }
#         record_path = os.path.join('reports', 'model_registration.json')
#         with open(record_path, 'w') as f:
#             json.dump(registration_record, f, indent=2)

#         logging.debug('Wrote model registration record to %s', record_path)
#         return registration_record
#     except Exception as e:
#         logging.error('Error during model registration: %s', e)
#         raise

# def main():
#     try:
#         model_info_path = 'reports/experiment_info.json'
#         model_info = load_model_info(model_info_path)
        
#         model_name = "my_model"
#         register_model(model_name, model_info)
#     except Exception as e:
#         logging.error('Failed to complete the model registration process: %s', e)
#         print(f"Error: {e}")

# if __name__ == '__main__':
#     main()






import mlflow
import json
import os
from src.logger import logging

def main():
    try:
        # 1. Get the latest run from your MLflow experiment
        # If you use a specific experiment name, change "0" to your experiment ID or use get_experiment_by_name
        experiment_id = "0" # Default experiment ID in MLflow
        runs = mlflow.search_runs(experiment_ids=[experiment_id], order_by=["start_time DESC"], max_results=1)
        
        if runs.empty:
            raise ValueError("No MLflow runs found. Make sure your training script ran successfully.")

        # Extract the newest Run ID
        latest_run_id = runs.iloc[0].run_id
        logging.info(f"Found latest run ID: {latest_run_id}")

        # 2. Build the correct Model URI using the generic "runs:/" format
        # This matches the "model" artifact path we set in the training script
        model_uri = f"runs:/{latest_run_id}/model"

        # 3. Register the model
        model_name = "my_model"
        registered_model = mlflow.register_model(model_uri=model_uri, name=model_name)
        logging.info(f"Model registered successfully: {registered_model.name}, version: {registered_model.version}")

        # 4. Create the JSON output file that DVC is expecting
        output_dir = "reports"
        os.makedirs(output_dir, exist_ok=True)
        
        output_data = {
            "model_name": registered_model.name,
            "model_version": registered_model.version,
            "run_id": latest_run_id,
            "model_uri": model_uri
        }
        
        output_file_path = os.path.join(output_dir, "model_registration.json")
        with open(output_file_path, "w") as f:
            json.dump(output_data, f, indent=4)
            
        logging.info(f"Registration report saved to {output_file_path}")

    except Exception as e:
        logging.error(f"Error during model registration: {e}")
        print(f"Error: {e}")

if __name__ == '__main__':
    main()