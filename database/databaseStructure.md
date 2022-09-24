# What is database structure?

- Database structure refers to how data is arranged in a database. Within a database, related data are grouped into tables, each of which consists of rows (also called tuples) and columns, like in a spreadsheet.

- The structure of a database consists of a set of key components. These include:

    1. Tables or entities, where the data is stored.

    2. Attributes which are details about the table or entity. In other words, attributes describe the table.

    3. Fields, which are columns used to capture attributes.

    4. A record, which is one row of details about a table or entity.

    5. And the primary key, which is a unique value for an entity.

## Table

- A table contains all the fields,attributes and records for a type of entity. A database will most probably contain more than one table.

## Fields

- Column headings are known as fields. Each field contains a different attribute. For every table, a unit of data is entered into each field. It’s also known as a column value. Each column has a data type. For example, the “agent_name” column has a data type of text, and the “commission” column has a numeric data type.

## Column value or unit of data

- Each individual piece of data entered into a column is a unit of data. These units are also called data elements or column values.

## Records

- A record consists of a collection of data for each entity. It’s also known as a row in the table.

## Data types

- To keep the data consistent from one record to the next, an appropriate data type is assigned to each column

- The data type of a column determines what type of data can be stored in each column.

- Data types are also a way of classifying data values or column values.

### Some common data types used in databases are:

1. Numeric data types such as INT, TINYINT, BIGINT, FLOAT, REAL.

2. Date and time data types such as DATE, TIME, DATETIME.

3. Character and string data types such as CHAR, VARCHAR.

4. Binary data types such as BINARY, VARBINARY.

- And miscellaneous data types such as:

1. Character Large Object (CLOB), for storing a large block of text in some form of text encoding.

2. Binary Large Object (BLOB), for storing a collection of binary data such as images.

## Logical database structure

- The logical structure of a database is represented using a diagram known as the Entity Relationship Diagram (ERD)

- It is a visual representation of how the database will be implemented into tables during physical database design, using a *Database Management System (DBMS)* like *MySQL* or *Oracle*, for example.

- A part of the logical database structure is how relationships are established between entities.

- These relationships are established between the instances of the entities. Accordingly, there can be three ways in which entity instances can be related to each other:

    1. One-to-one relationships

    2. One-to-many relationships

    3. Many-to-many relationships

## Physical Database Structure

- In the physical database structure, where entities are implemented as tables, the relationships are established using a field known as a foreign key

- A foreign key is a field in one table that refers to a common field in another table (usually the primary key).
