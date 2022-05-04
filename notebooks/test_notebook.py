# Databricks notebook source
#!mkdir /dbfs/FileStore/pyexample
!cp ../ /dbfs/FileStore/pyexample -r
!pip install -e /dbfs/FileStore/pyexample

# COMMAND ----------

from python_example.python_example import my_function

my_function()

# COMMAND ----------


