from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:

    db = "user_cr"

    def __init__(self, data):
        self.id = data ['id']
        self.first_name = data ['first_name']
        self.last_name = data ['last_name']
        self.email = data ['email']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    # CREATE
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s)"""
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    # READ
    @classmethod
    def show_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL(cls.db).query_db(query)
        users = []

        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_one(cls, id):
        query = """SELECT * FROM users
                WHERE id = %(id)s; """
        results = connectToMySQL(cls.db).query_db(query, {"id": id})
        #results would be in a list 
        return cls(results[0])


    # DELETE
    @classmethod
    def delete(cls, id):
        query = """DELETE FROM users 
                WHERE id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query, {'id': id})
        return results
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        # test to make sure input matches pattern
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!', "email")
            is_valid = False
        if len(user['first_name']) < 1:
            flash ('First Name is required.', "first_name")
            is_valid = False
        if len(user['last_name']) < 1:
            flash ('Last Name is required.', "last_name")
            is_valid = False
        return is_valid
    