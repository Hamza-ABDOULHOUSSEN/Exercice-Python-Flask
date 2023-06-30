from sqlalchemy import create_engine, text
from datetime import datetime

HOST = 'db'
USER = 'user'
PASSWORD = 'user'
DATABASE = 'operation_db'


def persist_operation(operation: str, result: str) -> None:
    """
    persist the operation into the mySQL database
    :return: None
    """
    engine = create_engine(f"mysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}")

    stmt = f'INSERT INTO operation (operation, result, time) VALUES ("{operation}", "{result}", "{datetime.now().isoformat()}"); '

    with engine.connect() as conn:
        result = conn.execute(text(stmt))
        conn.commit()


def get_all_csv() -> str:
    """
    Select all data in operation and return it as csv
    :return: None
    """

    engine = create_engine(f"mysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}")

    stmt = f'SELECT * FROM operation'

    csv_buffer_header = 'id, operation, result, time\n'

    with engine.connect() as conn:
        result = conn.execute(text(stmt))
        conn.commit()

    buffer_row_list = [f'{row[0]}, {row[1]}, {row[2]}, {row[3]}' for row in result.fetchall()]
    csv_buffer = '\n'.join(buffer_row_list)
    return csv_buffer_header + csv_buffer
