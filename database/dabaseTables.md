# Tables

- A table is the most basic type of database object in relational databases. It is responsible for storing data in the database. Like any other table, a database table also consists of rows and columns.

## What are data types?

- A data type defines the type of value that can be stored in a table column.

- The rows in a table contains the **records**.

## Table in a relational database

- In a relational database there are multiple tables representing the structure of the back end of a software system.

- In relational database terminology a table is also known as a relation

- A table row or a record is also known as a tuple.

- Each table or relation in a database has its own schema. *Schema* simply means the structure

- The structure includes:

      the name of the table or relation,

      its attributes,

      their names

      and data type.

## What is a Primary Key?

- In a table, there is a field or column that is known as a key which can uniquely identify a particular tuple (row) in a relation (table). This key is specifically known as a *primary key*.

- In some cases, the primary key can comprise more than one column or field.

## What is a Foreign Key?

- Tables in a database do not stay isolated from each other. They need to have relationships between them. Tables are linked with one another through a key column (the primary key) of one table that’s also present in the related table as a *foreign key*.

### Integrity constraints

- Every table in a database should abide by rules or constraints. These are known as integrity constraints.

- There are three main integrity constraints:

1. Key constraints

2. Domain constraints

3. Referential integrity constraints

### What is a Key Constraints

- In every table there should be one or more columns or fields that can be used to fetch data from tables.In other words, a *primary key*.

- In every table there should be one or more columns or fields that can be used to fetch data from tables

- This key attribute or primary key should never be **NULL** or the same for two different rows of data

### What is a Domain Constraints?

- Domain constraints refer to the rules defined for the values that can be stored for a certain column.

- For instance, you cannot store the home address of a student in the first name column. Similarly, a contact number cannot exceed ten digits.

### What are referential integrity constraints?

- When a table is related to another table via a foreign key column, then the referenced column value must exist in the other table


