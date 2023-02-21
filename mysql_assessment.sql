
# How many rows in tables?
SELECT 'games_sales', COUNT(*) 
FROM games_sales;

# How many columns allow null values in games_sales?
SELECT 'games_sales', COUNT(*)
FROM information_schema.columns
WHERE table_name = 'games_sales'
AND is_nullable = 'YES';

SELECT 'games_reviews', COUNT(*)
FROM information_schema.columns
WHERE table_name = 'games_reviews'
AND is_nullable = 'YES';


# Rename ï»¿code column to game_id in both tables 
ALTER TABLE games_sales 
RENAME COLUMN ï»¿code to game_id;

# Datatype of game_name in the games_sales table is currently text, modify this to varchar with a character limit of 200.
ALTER TABLE games_sales
MODIFY game_name VARCHAR(200);

# What are the top 10 games sold worldwide?
SELECT game_name, publisher, total_shipped, year
FROM games_sales
ORDER BY total_shipped DESC
LIMIT 10;

# Top 5 publishers and how many games they have appeared in games_sales?
SELECT publisher, count(total_shipped) 
FROM games_sales
GROUP BY publisher
ORDER BY count(total_shipped) DESC
LIMIT 5;

# Does FIFA 11 appear in games_sales, if so, in what platforms? 
SELECT game_name, platform
FROM games_sales
WHERE game_name LIKE 'FIFA%11' 
OR game_name LIKE 'fifa%11';

# Are there any games where critics have scored it 9 or above but players have scored it below average (less than 5)?
SELECT *
FROM games_reviews
WHERE critic_score >= 9
AND user_score <= 5;

SELECT * 
FROM games_sales
WHERE game_id = '1207';

# Select an appropriate join type where our final result presents all data from both tables together.
SELECT *
FROM games_sales
JOIN games_reviews ON games_sales.game_id = games_reviews.game_id;

# Bottom 5 years by average critic scores of the games.
SELECT year, AVG(critic_score) AS avg_critic
FROM games_sales
JOIN games_reviews ON games_reviews.game_id = games_sales.game_id
WHERE critic_score > 0 
GROUP BY year 
ORDER BY avg_critic 
LIMIT 5;

# Top 3 platforms by total games sold. How many copies did the top platform sell (millions)?
SELECT SUM(total_shipped), platform 
FROM games_sales
JOIN games_reviews ON games_reviews.game_id = games_sales.game_id
GROUP BY platform
ORDER BY SUM(total_shipped) DESC 
LIMIT 3;

# Most sold game in 2010’s decade where critics and players gave a rating above 9, exclude Nintendo as the publisher. 
SELECT game_name, platform, year, total_shipped
FROM games_sales
JOIN games_reviews ON games_reviews.game_id = games_sales.game_id
WHERE year >= 2010 
AND critic_score > 9 
AND user_score > 9 
AND publisher != 'Nintendo'
LIMIT 5;

# Produce a table in the results tab that shows Nintendo as publisher and their yearly average of games sold, since 2000
SELECT year,publisher, AVG(total_shipped) AS avg_shipped
FROM games_sales
JOIN games_reviews ON games_reviews.game_id = games_sales.game_id
WHERE publisher = 'Nintendo' 
AND year >= 2000
GROUP BY year
ORDER BY avg_shipped desc;
