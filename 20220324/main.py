from datetime import datetime

import sqlalchemy as db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = db.create_engine("sqlite:///example_data.db")
connection = engine.connect()
metadata = db.MetaData()
Base = declarative_base()
logins = db.Table("logins", metadata, autoload=True, autoload_with=engine)
# Print the column names
print(logins.columns.keys())
# Print full table metadata
print(repr(metadata.tables["logins"]))


class logins_table(Base):
    __tablename__ = "logins"  # redundant

    month = Column("Month", String, primary_key=True)
    day = Column("DayOftheMonth", String, primary_key=True)
    time = Column("Time", String, primary_key=True)
    username = Column("Username", String, primary_key=True)
    ip = Column("IPAddress", String)
    port = Column("Port", Integer)

    def __repr__(self):
        return f"User(month={self.month!r}, day={self.day!r}, time={self.time!r}, \
                    username={self.username!r}, ip={self.ip!r}, port={self.port!r} )"

    def date(self):
        time_parts = [int(part) for part in repr(self.time).split(":")]
        return datetime(2022, int(repr(self.month)), int(repr(self.day)))


# select * from example_data.logins
# limit 10
stmt1 = db.select(logins_table).limit(10)
result = connection.execute(stmt1)
print(f"\n~~~~~~~~\n{result}\n~~~~~~~~\n")

print(f"\n~~~~~~~~\n")
for i in connection.execute(stmt1):
    print(i)
print(f"\n~~~~~~~~\n")


# # generator tutorial
# def fib():
#     a = 0
#     b = 1
#     while True:
#         c = a + b
#         a, b = b, c
#         yield c


# for num in fib():
#     print(f"I got {num}")
#     if num > 100:
#         break
# #~~~~~~~~~~~~~~~~~~~
