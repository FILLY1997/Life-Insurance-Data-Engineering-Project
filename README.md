# Life-Insurance-Data-Engineering-Project
AWS Cloud Data Lake &amp; ETL Pipeline for Life Insurance Management System
# Project Overview:
 This project demonstrates how to design an end-to-end AWS-based data pipeline to ingest, transform, and store life insurance domain data from various operational systems for reporting and analytics.
 # AWS Services Used:

| Layer                  | Service                    | Purpose                                          |
|------------------------|----------------------------|--------------------------------------------------|
| 🗄️ Storage Layer       | Amazon S3                  | Raw & transformed data lake                      |
| ⚙️ ETL Engine          | AWS Glue (PySpark Script)  | Ingest & transform source tables                 |
| 🧮 Database Layer      | Amazon RDS (PostgreSQL)    | Store cleaned, structured, transformed data      |
| 🔍 Query Layer         | Amazon Athena              | Ad-hoc analysis or reporting                     |
| ⏱️ Orchestration       | AWS Glue Workflows         | Scheduling & job chaining                        |
| 📈 Logging/Monitoring  | Amazon CloudWatch Logs     | Job monitoring and failure alerts                |
# Architecture
### 🔄 ETL Pipeline Data Flow (Claimed & Not Claimed Active)
![ETL Flow](C:\Users\91701\OneDrive\Documents\architecuture.png)

