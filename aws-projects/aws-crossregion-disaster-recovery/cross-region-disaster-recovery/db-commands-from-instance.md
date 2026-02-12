# Connect to database from Linux command line

mysql -h RDS-ENDPOINT -u admin -p

# Connect to DB named "sample"

use sample;

# Show tables

show tables;

# Create orders table

CREATE TABLE orders (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, ordernumber VARCHAR(30) NOT NULL, customername VARCHAR(30) NOT NULL, address VARCHAR(150) NOT NULL, item VARCHAR(50) NOT NULL, price DECIMAL(10,2) NOT NULL, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);

# Validate orders tables exists

show tables;

# View table contents (after adding orders)

SELECT * FROM orders;