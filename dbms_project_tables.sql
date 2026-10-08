USE gamezone;

-- Delete old tables if they exist
DROP TABLE IF EXISTS Score;
DROP TABLE IF EXISTS GameMatch;
DROP TABLE IF EXISTS Registration;
DROP TABLE IF EXISTS Team_Member;
DROP TABLE IF EXISTS Tournament;
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Game;
DROP TABLE IF EXISTS Player;


-- 1. PLAYER
CREATE TABLE Player (
    player_id INT PRIMARY KEY AUTO_INCREMENT,
    player_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT,
    country VARCHAR(50)
);


-- 2. TEAM
CREATE TABLE Team (
    team_id INT PRIMARY KEY AUTO_INCREMENT,
    team_name VARCHAR(100) UNIQUE NOT NULL,
    captain_id INT,
    FOREIGN KEY (captain_id) REFERENCES Player(player_id)
);


-- 3. TEAM MEMBER
CREATE TABLE Team_Member (
    team_id INT,
    player_id INT,
    join_date DATE,
    PRIMARY KEY (team_id, player_id),
    FOREIGN KEY (team_id) REFERENCES Team(team_id),
    FOREIGN KEY (player_id) REFERENCES Player(player_id)
);


-- 4. GAME
CREATE TABLE Game (
    game_id INT PRIMARY KEY AUTO_INCREMENT,
    game_name VARCHAR(100) NOT NULL,
    game_type VARCHAR(50)
);


-- 5. TOURNAMENT
CREATE TABLE Tournament (
    tournament_id INT PRIMARY KEY AUTO_INCREMENT,
    tournament_name VARCHAR(100) NOT NULL,
    game_id INT,
    start_date DATE,
    end_date DATE,
    prize_pool DECIMAL(10,2),
    FOREIGN KEY (game_id) REFERENCES Game(game_id)
);


-- 6. REGISTRATION
CREATE TABLE Registration (
    registration_id INT PRIMARY KEY AUTO_INCREMENT,
    tournament_id INT,
    team_id INT,
    registration_date DATE,
    FOREIGN KEY (tournament_id) REFERENCES Tournament(tournament_id),
    FOREIGN KEY (team_id) REFERENCES Team(team_id)
);


-- 7. GAME MATCH
CREATE TABLE GameMatch (
    match_id INT PRIMARY KEY AUTO_INCREMENT,
    tournament_id INT,
    team1_id INT,
    team2_id INT,
    match_date DATE,
    winner_team_id INT,
    FOREIGN KEY (tournament_id) REFERENCES Tournament(tournament_id),
    FOREIGN KEY (team1_id) REFERENCES Team(team_id),
    FOREIGN KEY (team2_id) REFERENCES Team(team_id),
    FOREIGN KEY (winner_team_id) REFERENCES Team(team_id)
);


-- 8. SCORE
CREATE TABLE Score (
    score_id INT PRIMARY KEY AUTO_INCREMENT,
    match_id INT,
    team_id INT,
    score INT DEFAULT 0,
    FOREIGN KEY (match_id) REFERENCES GameMatch(match_id),
    FOREIGN KEY (team_id) REFERENCES Team(team_id)
);


-- CHECK ALL TABLES
SHOW TABLES;

USE gamezone;

-- =========================================
-- 1. PLAYER DATA
-- =========================================

INSERT INTO Player (player_name, email, age, country) VALUES
('Aarav Sharma', 'aarav@gmail.com', 21, 'India'),
('Riya Patil', 'riya@gmail.com', 20, 'India'),
('Kabir Khan', 'kabir@gmail.com', 22, 'India'),
('Ananya Joshi', 'ananya@gmail.com', 19, 'India'),
('Rahul Verma', 'rahul@gmail.com', 23, 'India'),
('Sneha Kulkarni', 'sneha@gmail.com', 21, 'India'),
('Aditya Singh', 'aditya@gmail.com', 22, 'India'),
('Meera Shah', 'meera@gmail.com', 20, 'India');


-- =========================================
-- 2. TEAM DATA
-- =========================================

INSERT INTO Team (team_name, captain_id) VALUES
('Phoenix Warriors', 1),
('Shadow Titans', 2),
('Cyber Legends', 3),
('Game Changers', 4);


-- =========================================
-- 3. TEAM MEMBER DATA
-- =========================================

INSERT INTO Team_Member (team_id, player_id, join_date) VALUES
(1, 1, '2026-01-10'),
(1, 5, '2026-01-11'),
(2, 2, '2026-01-12'),
(2, 6, '2026-01-13'),
(3, 3, '2026-01-14'),
(3, 7, '2026-01-15'),
(4, 4, '2026-01-16'),
(4, 8, '2026-01-17');


-- =========================================
-- 4. GAME DATA
-- =========================================

INSERT INTO Game (game_name, game_type) VALUES
('Valorant', 'FPS'),
('PUBG', 'Battle Royale'),
('Free Fire', 'Battle Royale'),
('FIFA 26', 'Sports');


-- =========================================
-- 5. TOURNAMENT DATA
-- =========================================

INSERT INTO Tournament
(tournament_name, game_id, start_date, end_date, prize_pool)
VALUES
('Valorant Championship 2026', 1, '2026-02-01', '2026-02-05', 50000.00),
('PUBG Battle Cup 2026', 2, '2026-03-10', '2026-03-15', 75000.00),
('Free Fire Masters 2026', 3, '2026-04-05', '2026-04-08', 40000.00),
('FIFA Pro League 2026', 4, '2026-05-01', '2026-05-03', 30000.00);


-- =========================================
-- 6. REGISTRATION DATA
-- =========================================

INSERT INTO Registration
(tournament_id, team_id, registration_date)
VALUES
(1, 1, '2026-01-20'),
(1, 2, '2026-01-21'),
(2, 2, '2026-02-20'),
(2, 3, '2026-02-21'),
(3, 3, '2026-03-20'),
(3, 4, '2026-03-21'),
(4, 1, '2026-04-20'),
(4, 4, '2026-04-21');


-- =========================================
-- 7. MATCH DATA
-- =========================================

INSERT INTO GameMatch
(tournament_id, team1_id, team2_id, match_date, winner_team_id)
VALUES
(1, 1, 2, '2026-02-02', 1),
(1, 3, 4, '2026-02-03', 3),
(2, 2, 3, '2026-03-12', 2),
(3, 3, 4, '2026-04-06', 4),
(4, 1, 4, '2026-05-02', 1);


-- =========================================
-- 8. SCORE DATA
-- =========================================

INSERT INTO Score (match_id, team_id, score) VALUES
(1, 1, 15),
(1, 2, 10),
(2, 3, 18),
(2, 4, 12),
(3, 2, 20),
(3, 3, 16),
(4, 3, 11),
(4, 4, 17),
(5, 1, 21),
(5, 4, 14);


-- =========================================
-- CHECK DATA
-- =========================================

SELECT * FROM Player;
SELECT * FROM Team;
SELECT * FROM Team_Member;
SELECT * FROM Game;
SELECT * FROM Tournament;
SELECT * FROM Registration;
SELECT * FROM GameMatch;
SELECT * FROM Score;