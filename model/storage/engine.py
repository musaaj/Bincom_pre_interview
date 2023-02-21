#!/usr/bin/python3
"""storage engine for"""
import psycopg2
from psycopg2.extras import execute_batch
from psycopg2 import Error


class Engine:
    """database storage engine"""

    def __init__(self,
            host='',
            port='', 
            user='',
            password='',
            dbname=''):
        try:
            self.connection = psycopg2.connect(host=host,
                                                port=port,
                                                user=user,
                                                password=password,
                                                dbname=dbname)
        except Error:
            raise Error('Invalid credentials')

    def save(self, colors):
        cursor = self.connection.cursor()
        create_query = """CREATE TABLE IF NOT EXISTS colors
                        (name VARCHAR(256), freq INTEGER);"""
        insert_query = """INSERT INTO colors(name, freq) VALUES (%s, %s)"""
        cursor.execute(create_query)
        execute_batch(cursor, insert_query, colors.get_dict().items())
        self.connection.commit()
        cursor.close()
        self.connection.close()
