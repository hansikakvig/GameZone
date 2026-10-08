USE gamezone;

UPDATE Player
SET age = 22
WHERE player_id = 1;

SELECT * FROM Player;

SELECT
    team_id,
    SUM(score) AS total_score
FROM Score
GROUP BY team_id
HAVING SUM(score) > 20;

DROP VIEW IF EXISTS Player_Team_View;

CREATE VIEW Player_Team_View AS
SELECT
    p.player_id,
    p.player_name,
    t.team_name
FROM Player p
JOIN Team_Member tm
    ON p.player_id = tm.player_id
JOIN Team t
    ON tm.team_id = t.team_id;

SELECT * FROM Player_Team_View;

DROP TRIGGER IF EXISTS check_player_age;

DELIMITER //

CREATE TRIGGER check_player_age
BEFORE INSERT ON Player
FOR EACH ROW
BEGIN
    IF NEW.age < 13 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Player age must be 13 or above';
    END IF;
END //

DELIMITER ;

SHOW TRIGGERS;