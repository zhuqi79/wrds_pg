#!/usr/bin/env python3
from wrds2pg.wrds2pg import wrds_update, run_file_sql
from wrds2pg.wrds2pg import make_engine, wrds_id

engine = make_engine()

updated = wrds_update("amend", "tfn")
updated = wrds_update("avgreturns", "tfn")
updated = wrds_update("company", "tfn", fix_cr=True)
updated = wrds_update("form144", "tfn")
updated = wrds_update("header", "tfn")
updated = wrds_update("idfhist", "tfn")
updated = wrds_update("idfnames", "tfn")
updated = wrds_update("rule10b5", "tfn")
updated = wrds_update("table1", "tfn")
updated = wrds_update("table2", "tfn")


