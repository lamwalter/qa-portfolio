# AWS Smoke – EC2 → S3

Small smoke to prove an EC2 instance can write to S3 (IAM/Networking/Region OK).

## Options to run

### Option 1: AWS CLI (simplest)
Prereq: AWS CLI configured on the EC2 (instance profile **or** `aws configure`).

```bash
aws s3 cp README.md s3://$S3_BUCKET/smoke/README.copy --region $AWS_REGION
aws s3 ls s3://$S3_BUCKET/smoke/ | grep README.copy
