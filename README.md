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
![ETL Flow](architecuture.png)
## 🔁 Data Flow

### 📥 1. Data Ingestion
Insurance data is ingested and stored in the Oracle database in table format

### ⚙️ 2. ETL Processing
**AWS Glue** jobs extract data from the oracle, perform necessary transformations (including **schema mapping** and **data masking**), and load the cleansed data into the **Amezon s3 buget**.  
✅ **Data quality checks** are enforced to maintain data integrity.

### 🗂️ 3. Data Cataloging
The **AWS Glue Data Catalog** indexes the processed data, making it discoverable and queryable for downstream applications.

### 📈 4. Business Intelligence
**Quick Sight** connects to the data in the Golden layer to generate **interactive dashboards**, providing insights into:
- Insurance trends
- Customer demographics
- Model performance

---

## 🧰 Technologies Used

### 🗄️ Data Storage & Lake:
- **Amazon S3**


### ⚙️ Data Processing & ETL:
- **AWS Glue**
- **AWS Glue Data Catalog**
- **PySpark**


### 📊 Business Intelligence:
- **Quicksight**

### 🧱 Infrastructure as Code:
- **Terraform** (for IAM, S3, and Glue module configurations)

