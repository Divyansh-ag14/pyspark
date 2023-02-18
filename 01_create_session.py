# %%
import pyspark
# %%
os.environ["SPARK_HOME"] = "C:/Users/divyansh/Spark/spark-3.3.1-bin-hadoop3"
# %%
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("myApp").getOrCreate()

# %%
spark

# %%
