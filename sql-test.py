#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import pandas as pd
import pymysql
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://shop:linker@r-cust-db:3306/se_shoplinker', echo=False)

data = pd.read_sql('show databases', engine)
print(data)
