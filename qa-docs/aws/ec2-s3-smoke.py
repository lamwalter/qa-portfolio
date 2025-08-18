import os, sys, time, uuid
from datetime import datetime

try:
    import boto3
    from botocore.exceptions import ClientError
except Exception as e:
    print("boto3 required. Install with: pip install boto3")
    sys.exit(2)

REGION = os.getenv("AWS_REGION", "us-east-1")
BUCKET = os.getenv("S3_BUCKET", "").strip()
PREFIX = os.getenv("S3_PREFIX", "smoke/")

if not BUCKET:
    print("Set S3_BUCKET env var (target bucket name).")
    sys.exit(2)

s3 = boto3.client("s3", region_name=REGION)

key = f"{PREFIX}health-{uuid.uuid4().hex[:8]}.txt"
payload = f"ec2->s3 ok @ {datetime.utcnow().isoformat()}Z\n"

t0 = time.time()
try:
    s3.put_object(Bucket=BUCKET, Key=key, Body=payload.encode("utf-8"))
    got = s3.get_object(Bucket=BUCKET, Key=key)
    back = got["Body"].read().decode("utf-8")
    ok = (back == payload)
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] wrote {len(payload)}B to s3://{BUCKET}/{key} (region={REGION})")
    if not ok:
        print("Mismatch on readback")
        sys.exit(1)
except ClientError as e:
    print("[FAIL] S3 error:", e)
    sys.exit(1)
finally:
    dt = (time.time() - t0) * 1000
    print(f"duration: {dt:.1f} ms")
