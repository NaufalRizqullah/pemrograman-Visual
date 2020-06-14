import pandas as pd
import xlsxwriter
import pymysql

conn = pymysql.connect(host="localhost", user="root",
                       password="", db="futsal", port=3306, autocommit=True)

with pd.ExcelWriter("Output.xlsx", engine="xlsxwriter", options={'strings_to_numbers': True, 'strings_to_formulas': False}) as writer:
    try:
        df = pd.read_sql(
            "SELECT id, nama, waktu, lapangan, no_hp, pemesanan, pembayaran FROM pesanan", conn)
        df.to_excel(writer, sheet_name="Sheet1", header=True, index=False)
        print("File saved successfully!")
    except:
        print("There is an error")
