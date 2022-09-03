# 1. Description
Regular expressions are pivotal when you want to find something that matches a pattern. How many regular expressions are there? They are infinite! We don't need to memorize all of them. Why not make a program to store all the information for us? This is the most efficient way – we will have a preview of every input that users have provided and the result of comparing it to a string.

To accomplish that, we need to connect a database.

# 2. Objectives
To begin with, let's make a plan of how we will manage our data. In our case, user input plays a vital role. If you think of the pattern that should match itself, you will realize that we expect two things from users: a pattern and a text that may or may not contain this pattern. That's what we need to store! Furthermore, we also need the outcome of the comparison to understand whether the pattern occurs or not. We must keep both the regex and the tested text in one entry to make sure that the result comes from the same test. That's where we come up with the data model.

Your `Record` model should contain `regex`, `⁣text`, and `result` fields. The `regex` contains an expression of not more than 50 symbols. As for the `text` field, the max length is 1024. The `result` field must be boolean.

In this project, we're going to use SQLAlchemy and sqlite.

For testing reasons, name the database as `db.sqlite3`

```
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
```
