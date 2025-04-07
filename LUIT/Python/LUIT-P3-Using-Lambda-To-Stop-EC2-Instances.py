#import boto3

'''
Foundational

1. Create a python script that stops all running EC2 instances.
2. Create a Lambda function using Python 3.8 or higher runtime to run your script.
3. Add a trigger to the Lambda to ensure it runs on a set schedule daily. No one should be working past 7pm. 
    (Note: to test you may need to modify the time accordingly so you aren't waiting for 7pm)
4. Push your code to GitHub and include the link in your write up.

'''


'''
Advanced

To insure only Dev machines are stoppped and not production. 
Add logic to your lambda that only stops running instances that have the Environment: Dev tag.

'''


'''
Complex

The engineering team would also like the ability to use an API to stop certain instances with tags via query parameters.
1. Use API Gateway to create a HTTP API that triggers the lambda.
2. Modify the lambda to get the query parameters if they exist
3. Modify the lambda to stop EC2 instances with the matching tag.

'''