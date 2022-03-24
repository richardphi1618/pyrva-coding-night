import sqlalchemy as db

engine = db.create_engine("sqlite:///example_data.db")
connection = engine.connect()
metadata = db.MetaData()
ssh_logins = db.Table("logins", metadata, autoload=True, autoload_with=engine)
# Print the column names
print(ssh_logins.columns.keys())
# Print full table metadata
print(repr(metadata.tables["logins"]))


select * from example_data.logins
limit 100