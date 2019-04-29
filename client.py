import requests


# Our get request (get table name where table_id == 2)
r = requests.get(url="http://127.0.0.1:5001/get_table_info_request", json={"table_id": 2})

data = r.text
status = r.status_code
print(data)

# Our post request (add new table)
r = requests.post(url="http://127.0.0.1:5001/add_new_table", json={"table_id":3, "table_name": "thanksgiving"})
data = r.text
print(data)

print(r.status_code)
