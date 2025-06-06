import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import lit

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# ✅ Load policy data
df_policy = spark.read.option("header", "true").csv("s3://life-insurance-project/raw/pt_il_policy.csv")

# ✅ Load claim transaction data
df_claim = spark.read.option("header", "true").csv("s3://life-insurance-project/raw/ps_il_drcr.csv")

# ✅ Standardize column names if needed (example: policy_id)
# df_policy = df_policy.withColumnRenamed("POL_ID", "policy_id")
# df_claim = df_claim.withColumnRenamed("POL_ID", "policy_id")

# ✅ Get claimed policies using inner join
df_claimed = df_policy.join(df_claim, on="policy_id", how="inner") \
                      .withColumn("SourceSystem", lit("LifeApp")) \
                      .withColumn("ClaimStatus", lit("CLAIMED"))

# ✅ Get active, not claimed policies
df_active = df_policy.filter(df_policy["policy_status"] == "ACTIVE")  # use actual column name
df_not_claimed_active = df_active.join(df_claim, on="policy_id", how="left_anti") \
                                  .withColumn("SourceSystem", lit("LifeApp")) \
                                  .withColumn("ClaimStatus", lit("NOT_CLAIMED_ACTIVE"))

# ✅ Convert to DynamicFrames
dyf_claimed = DynamicFrame.fromDF(df_claimed, glueContext, "dyf_claimed")
dyf_not_claimed = DynamicFrame.fromDF(df_not_claimed_active, glueContext, "dyf_not_claimed")

# ✅ Write claimed data to PostgreSQL
glueContext.write_dynamic_frame.from_options(
    frame=dyf_claimed,
    connection_type="postgresql",
    connection_options={
        "url": "jdbc:postgresql://<host>:5432/<dbname>",
        "user": "<user>",
        "password": "<password>",
        "dbtable": "public.claimed_policies",
        "redshiftTmpDir": "s3://life-insurance-project/temp/"
    }
)

# ✅ Write not claimed active data to PostgreSQL
glueContext.write_dynamic_frame.from_options(
    frame=dyf_not_claimed,
    connection_type="postgresql",
    connection_options={
        "url": "jdbc:postgresql://<host>:5432/<dbname>",
        "user": "<user>",
        "password": "<password>",
        "dbtable": "public.not_claimed_active_policies",
        "redshiftTmpDir": "s3://life-insurance-project/temp/"
    }
)

job.commit()
