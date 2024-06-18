# install dependencies
from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy

# initialize parameters
INSTANCE_CONNECTION_NAME = f"riccardo-blog-test-v1:us-central1:marvel-legends" # i.e demo-project:us-central1:demo-instance
print(f"Your instance connection name is: {INSTANCE_CONNECTION_NAME}")
DB_USER = "nate"
DB_PASS = "MySQLPa33word1234!"
DB_NAME = "legends"

# initialize Connector object
connector = Connector()

# function to return the database connection object
def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pymysql",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME,
        ip_type=IPTypes.PRIVATE
    )
    return conn

# create connection pool with 'creator' argument to our connection object function
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

# connect to connection pool
with pool.connect() as db_conn:
    # query database and fetch results
    results = db_conn.execute(sqlalchemy.text("SELECT * FROM figure")).fetchall()

    # show results
    for row in results:
        print(row)

# cleanup connector
connector.close()