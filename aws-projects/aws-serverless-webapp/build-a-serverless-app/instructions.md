# Exercise 4
## Task 1
1. Download the zip file
wget <s3-url-for-zip-file>
2. Unzip the contents
unzip <zip-file-name>
3. Send message comand
aws sqs send-message --queue-url <your-queue-url> --message-body file://message-body-1.json 

# Exercise 5
## Task 2
1. Change to backend folder
cd ~/build-a-serverless-app/Part-2/DCTProductPurchaseForm/backend/
2. Edit the index.js and modify the queue URL
sudo nano index.js
3. Zip up the files
zip -r backend.zip *

Use the following path to download: /home/cloudshell-user/build-a-serverless-app/Part-2/DCTProductPurchaseForm/backend/backend.zip

4. Or, use the following command to copy to Lambda directly
aws lambda update-function-code --function-name productPurchasesSendDataToQueue --zip-file fileb://backend.zip


# Exercise 6
## Task 1
### Step 10
1. Copy the zip file to the frontend directory (modify the zip file name)
cp ~/javascript_XXXXXXXXX.zip ~/build-a-serverless-app/Part-2/DCTProductPurchaseForm/frontend/
2. Change directory
cd ~/build-a-serverless-app/Part-2/DCTProductPurchaseForm/frontend
3. Delete the following file and folder
rm -rf apigClient.js lib
4. Unzip the zip file (change the name)
unzip javascript_XXXXXXXXX.zip
5. Copy the following file and folder from the SDK to the frontend directory
cp apiGateway-js-sdk/apigClient.js ./
cp -r apiGateway-js-sdk/lib/ ./
6. Delete unnecessary files and folders
rm -rf apiGateway-js-sdk/
rm -rf javascript_XXXXXXXXX.zip

# Exercise 7
## Task 1
8. Copy all files from the fronted directory to the S3 bucket (change the bucket name)
aws s3 sync ./ s3://product-purchases-webform-2e312sd13

# Optional Extension

## Create a method of processing multiple order entries submitted in json files to an S3 bucket

1. Create an S3 bucket named 'bucket-for-adding-order-files-24d3dq'
2. Create a Lambda function using Python 3.9 named 'load-data-from-s3'
3. Add the code from the 'event-notification-add-to-queue.py' file in the optional-extension folder to the lambda function
4. Edit the execution role and add S3 ready only permissions and the 'productPurchasesSendMessage' policy
5. Create an event notification for S3 object creation events with the Lambda function as the target
6. Upload the 'items-for-ddb.json' file to the S3 bucket. 10 new records should now appear in the DynamoDB table