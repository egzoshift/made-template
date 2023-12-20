#!/bin/bash
python3 ./automatedPipeline.py
echo "Pipeline executed v5"

python3 ./test.py
echo "Pipeline tested v5"

# To run the tests you need kaggle credentials to pull data from kaggle.
# To do so: 
#   1. please copy the kaggle credentials: username: "egzoow", key: "25d6981fb22a3330e52d3601fe6a3a38"
#   2. create kaggle.json in root directory with the credentials from step 1 .
#   3. run chmod +x ./project/tests.sh
#   4. run ./project/tests.sh
