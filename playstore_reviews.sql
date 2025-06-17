CREATE DATABASE playstore_reviews;

USE playstore_reviews;

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userName VARCHAR(255),
    score INT,
    content TEXT,
    reviewDate DATETIME,
    thumbsUpCount INT,
    sentiment VARCHAR(20)
);
