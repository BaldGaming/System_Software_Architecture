class DatabaseConnection:
    connection = None

    def __new__(cls):
        if cls.connection is not None:
            return cls.connection
        cls.connection = super().__new__(cls)
        return cls.connection

print('First:')
first_connection = DatabaseConnection()
print(first_connection)
print('\nSecond:')
second_connection = DatabaseConnection()
print(second_connection)

# super() - reuses a def that is defined above it to avoid copies of the same code