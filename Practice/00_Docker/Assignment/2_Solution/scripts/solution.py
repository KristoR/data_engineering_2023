import requests 
import os
import sqlalchemy as sa



API_PATH = os.environ['API_PATH']
MYSQL_PATH = os.environ['MYSQL_PATH']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASS = os.environ['MYSQL_PASS']
DB_NAME = os.environ['DB_NAME']
TABLE_NAME = os.environ['TABLE_NAME']

def fetch_data_from_api():
    """You can execute this code from your machine by running:
    docker exec py bash -c "python \${SCRIPTS_PATH}/solution.py"
    """
    try:
        r = requests.get(API_PATH)
        insert_to_db(r.json())
        return "Success."
    except Exception as e:
        return "API fetching failed."

def insert_to_db(data):
    connection_string = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_PATH}:3306"
    engine = sa.create_engine(connection_string)
    with engine.connect() as conn:
        if not sa.inspect(engine).has_schema(DB_NAME):
            print("Creating database ...")
            conn.execute(sa.text(f"CREATE DATABASE {DB_NAME}"))
    engine = sa.create_engine(f"{connection_string}/{DB_NAME}")
    
    with engine.connect() as conn:
        metadata = sa.MetaData()
        iss_now = sa.Table(
            'iss_now',
            metadata,
            sa.Column("message", sa.String(100)),
            sa.Column("latitude", sa.Float),
            sa.Column("longitude", sa.Float),
            sa.Column("timestamp", sa.BigInteger)
        )
        if not sa.inspect(engine).has_table(TABLE_NAME, DB_NAME):
            print("Creating table ...")
            metadata.create_all(engine)

        print("Inserting data ...")
        stmt = sa.insert(iss_now).values(
            message=data["message"],
            latitude = data["iss_position"]["latitude"],
            longitude = data["iss_position"]["longitude"],
            timestamp = data["timestamp"]
            )
        result = conn.execute(stmt)
        conn.commit()
        print("Data inserted")

if __name__=="__main__":
    fetch_data_from_api()