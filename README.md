# AWS EC2 Scheduler Automation using Lambda & EventBridge

## Project Overview

This project demonstrates how to automate the starting and stopping of Amazon EC2 instances using:

- AWS Lambda
- Amazon EventBridge (Schedules)
- Python (Boto3)
- IAM Roles & Policies

The automation helps reduce AWS cloud costs by automatically stopping EC2 instances when they are not needed and starting them again at scheduled times.

This is a beginner-friendly AWS automation project built using serverless services.

---

# Architecture

```text
Amazon EventBridge
        ↓
AWS Lambda Function
        ↓
Amazon EC2 Instance
```

---

# AWS Services Used

| Service | Purpose |
|---|---|
| Amazon EC2 | Virtual server to automate |
| AWS Lambda | Executes Python automation code |
| Amazon EventBridge | Triggers Lambda on schedule |
| IAM | Manages permissions |
| CloudWatch Logs | Stores Lambda logs |

---

# Prerequisites

Before starting this project, make sure you have:

- AWS Account
- Basic knowledge of AWS Console
- An EC2 instance running
- GitHub account
- Python basics

---

# Project Workflow

1. EventBridge triggers Lambda at a scheduled time.
2. Lambda executes Python code.
3. Lambda starts or stops the EC2 instance.
4. CloudWatch stores execution logs.

---

# Step-by-Step Implementation

---

# Step 1 — Create EC2 Instance

## 1. Login to AWS Console

Open:

https://console.aws.amazon.com/

---

## 2. Navigate to EC2

Search:

```text
EC2
```

Click:
- EC2 Dashboard

---

## 3. Launch Instance

Click:

```text
Launch Instance
```

Fill:

| Field | Value |
|---|---|
| Name | MySchedulerInstance |
| AMI | Amazon Linux 2 |
| Instance Type | t2.micro |
| Key Pair | Create or Select Existing |
| Security Group | Allow SSH |

Click:

```text
Launch Instance
```

---

## 4. Copy Instance ID

Example:

```text
i-0123456789abcdef0
```

Save this ID because it will be used in Lambda code.

---

# Step 2 — Create IAM Role for Lambda

Lambda requires permission to start and stop EC2 instances.

---

## 1. Open IAM

Search:

```text
IAM
```

---

## 2. Create Role

Click:

```text
Roles → Create Role
```

Choose:

```text
AWS Service
```

Use Case:

```text
Lambda
```

Click:

```text
Next
```

---

## 3. Attach Policies

Attach these policies:

### AWSLambdaBasicExecutionRole

This allows Lambda to write logs to CloudWatch.

---

## 4. Create Custom Policy

Go to:

```text
Policies → Create Policy
```

Choose:

```text
JSON
```

Paste:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "*"
    }
  ]
}
```

Click:
- Next
- Give name:

```text
EC2SchedulerPolicy
```

Click:

```text
Create Policy
```

---

## 5. Attach Policy to Role

Return to your Lambda role.

Attach:
- EC2SchedulerPolicy

Click:
- Create Role

Example role name:

```text
LambdaEC2SchedulerRole
```

---

# Step 3 — Create Lambda Function (Start EC2)

---

## 1. Open Lambda

Search:

```text
Lambda
```

Click:

```text
Create Function
```

---

## 2. Configure Function

Choose:

```text
Author from Scratch
```

Fill:

| Field | Value |
|---|---|
| Function Name | StartEC2Instance |
| Runtime | Python 3.x |
| Permissions | Use Existing Role |

Select:

```text
LambdaEC2SchedulerRole
```

Click:

```text
Create Function
```

---

## 3. Add Python Code

Replace default code with:

```python
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    instance_id = 'YOUR_INSTANCE_ID'

    ec2.start_instances(
        InstanceIds=[instance_id]
    )

    print("EC2 Instance Started")

    return {
        'statusCode': 200,
        'body': 'EC2 Started Successfully'
    }
```

Replace:

```python
YOUR_INSTANCE_ID
```

with your EC2 instance ID.

Example:

```python
instance_id = 'i-0123456789abcdef0'
```

---

## 4. Deploy Function

Click:

```text
Deploy
```

---

## 5. Test Lambda Function

Click:

```text
Test
```

Create test event:
- Event Name: TestStart

Click:
- Save
- Test

Your EC2 instance should start.

---

# Step 4 — Create Lambda Function (Stop EC2)

Repeat the same steps.

Function Name:

```text
StopEC2Instance
```

Use this code:

```python
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    instance_id = 'YOUR_INSTANCE_ID'

    ec2.stop_instances(
        InstanceIds=[instance_id]
    )

    print("EC2 Instance Stopped")

    return {
        'statusCode': 200,
        'body': 'EC2 Stopped Successfully'
    }
```

Deploy and test.

---

# Step 5 — Configure EventBridge Schedule

EventBridge automatically triggers Lambda functions at specific times.

---

# Create Start Schedule

---

## 1. Open EventBridge

Search:

```text
Amazon EventBridge
```

---

## 2. Create Rule

Click:

```text
Rules → Create Rule
```

---

## 3. Configure Rule

| Field | Value |
|---|---|
| Name | StartEC2Rule |
| Rule Type | Schedule |

Choose:

```text
Recurring Schedule
```

---

## 4. Add Cron Expression

Example:

```text
cron(0 8 * * ? *)
```

This starts EC2 daily at 8 AM UTC.

---

## 5. Select Target

Target Type:

```text
AWS Service
```

Select:

```text
Lambda Function
```

Choose:

```text
StartEC2Instance
```

Click:

```text
Create Rule
```

---

# Create Stop Schedule

Repeat the same steps.

Rule Name:

```text
StopEC2Rule
```

Cron Expression:

```text
cron(0 18 * * ? *)
```

This stops EC2 daily at 6 PM UTC.

Target:

```text
StopEC2Instance
```

---

# Step 6 — Verify Automation

Wait for scheduled time or manually test EventBridge rules.

You should see:
- EC2 automatically starts
- EC2 automatically stops

---

# Step 7 — Monitor Logs

Open:

```text
CloudWatch → Logs
```

Check Lambda logs for:
- Successful execution
- Errors
- Execution time

---

# Project Folder Structure

```text
aws-ec2-scheduler-automation/
│
├── lambda_start.py
├── lambda_stop.py
├── policy.json
├── README.md

```

---


# Learning Outcomes

Through this project I learned:

- AWS Lambda fundamentals
- Event-driven automation
- Amazon EventBridge scheduling
- IAM permission management
- Python automation using Boto3
- EC2 management
- Cloud cost optimization

---

# Future Improvements

Possible enhancements:

- Manage multiple EC2 instances
- Add email notifications using SNS
- Create Infrastructure using Terraform
- Add monitoring dashboard
- Add environment variables
- Use tags for instance management

---

# Conclusion

This project demonstrates a simple and effective serverless automation solution using AWS services. It helps automate EC2 operations while reducing unnecessary cloud costs.

---

# Author

## Althaf Muhammed Paracheri Parambil




