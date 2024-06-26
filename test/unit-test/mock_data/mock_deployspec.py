import yaml

dummy_deployspec = yaml.safe_load(
    """
publishGenericEnvVariables: true
deploy:
  phases:
    install:
      commands:
      - npm install -g aws-cdk@2.20.0
      - pip install -r requirements.txt
    build:
      commands:
      - echo "This Dummy Module does nothing"
destroy:
  phases:
    install:
      commands:
      - npm install -g aws-cdk@2.20.0
      - pip install -r requirements.txt
    build:
      commands:
      - echo 'Look Ma....destroying'
    """
)
