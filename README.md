Documentation

To access the admin, use this account:
Username: harry
Password: 1234

Dummy data is generated using Faker

1.	At least five tables/models in the database:
    •	Author, Book, Publisher, Reviewer, and Magazine models are present.

2.	One-to-many and many-to-many relationships:

    •	One-to-many relationships exist, such as Book to Author, Publisher to Book, etc.
    •	Many-to-many relationships exist, like Publisher to Book, Reviewer to Book, and Magazine to Author.

3.	Field types available in the database:
    •	Various field types are used, including DateField, DateTimeField, CharField, TextField, EmailField, ImageField, IntegerField, and DecimalField.

4.	Models inherit from BaseModel:
    •	All models inherit from BaseModel, which includes created_at and updated_at fields.

5.	__str__ method in every model:
    •	The __str__ method is defined in every model to provide a human-readable representation.

6.	Class-based or function-based views:
    •	The views are function-based, which is a valid choice.

7.	Bootstrap as a front-end framework:
    •	Bootstrap is used for styling and layout.


8.	Template inheritance with separate templates:
    •	Template inheritance is implemented with separate templates for pagination, footer, and menu.
