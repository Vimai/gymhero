CREATE USER testuser WITH PASSWORD 'password';

CREATE DATABASE workout IF NOT EXISTS;
GRANT ALL PRIVILEGES ON DATABASE workout TO testuser;

CREATE DATABASE workout_test IF NOT EXISTS;
GRANT ALL PRIVILEGES ON DATABASE workout_test TO testuser;