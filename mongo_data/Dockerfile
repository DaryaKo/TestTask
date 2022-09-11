

FROM mongo

COPY employees.json /employees.json
CMD mongoimport --host db --db test_db --collection employee --type json --file /employees.json --jsonArray
