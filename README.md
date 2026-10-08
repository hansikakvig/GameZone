<div align="center">

# 🎮 GAMEZONE

### Gaming Tournament Management System

**DBMS Mini Project**

![DBMS](https://img.shields.io/badge/DBMS-Mini%20Project-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-Flask-orange?style=for-the-badge)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?style=for-the-badge)
![Frontend](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-red?style=for-the-badge)

</div>

---

## 🎯 About The Project

**GameZone** is a web-based **Gaming Tournament Management System** developed as a **DBMS Mini Project**.

It is designed to manage gaming tournament information such as players, teams, games, tournaments, matches, scores and leaderboard.

The project demonstrates the practical implementation of important **DBMS concepts** using a real-world web application.

---

## ✨ Features

- 👤 Player Management
- 👥 Team Management
- 🎮 Game Management
- 🏆 Tournament Management
- ⚔️ Match Management
- 🥇 Leaderboard
- 🔄 CRUD Operations
- 🔗 SQL JOIN
- 📊 GROUP BY
- 🔍 HAVING
- 👁️ VIEW
- ⚡ TRIGGER

---

## 🛠️ Technologies Used

**Frontend**
- HTML5
- CSS3
- JavaScript

**Backend**
- Python
- Flask

**Database**
- MySQL
- MySQL Workbench

---

## 🗄️ Database

The project uses a MySQL database named **gamezone**.

### Tables

| Table | Purpose |
|---|---|
| Player | Stores player information |
| Team | Stores team information |
| Team_Member | Connects players and teams |
| Game | Stores game details |
| Tournament | Stores tournament details |
| Registration | Stores tournament registrations |
| GameMatch | Stores match information |
| Score | Stores team scores |

---

## 📚 DBMS Concepts Implemented

- CREATE
- INSERT
- SELECT
- UPDATE
- DELETE
- PRIMARY KEY
- FOREIGN KEY
- CONSTRAINTS
- JOIN
- COUNT()
- SUM()
- COALESCE()
- GROUP BY
- HAVING
- VIEW
- TRIGGER

---

## 🔄 CRUD Operations

### Create
New records can be added to the database.

### Read
Records are retrieved from MySQL and displayed on the website.

### Update
Existing records can be modified using SQL UPDATE.

### Delete
Records can be removed using SQL DELETE.

---

## 🔗 JOIN

JOIN is used to combine data from related tables.

Example:

    SELECT Team.team_name, Player.player_name AS captain
    FROM Team
    LEFT JOIN Player
    ON Team.captain_id = Player.player_id;

---

## 📊 GROUP BY & HAVING

The leaderboard uses aggregation and grouping to calculate team scores.

    SELECT team_id, SUM(score) AS total_score
    FROM Score
    GROUP BY team_id
    HAVING SUM(score) > 20;

---

## 👁️ VIEW

A view named **Player_Team_View** combines player and team information.

    CREATE VIEW Player_Team_View AS
    SELECT p.player_id, p.player_name, t.team_name
    FROM Player p
    JOIN Team_Member tm
    ON p.player_id = tm.player_id
    JOIN Team t
    ON tm.team_id = t.team_id;

---

## ⚡ TRIGGER

A trigger named **check_player_age** validates player age before insertion.

    CREATE TRIGGER check_player_age
    BEFORE INSERT ON Player
    FOR EACH ROW
    BEGIN
        IF NEW.age < 13 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Player age must be 13 or above';
        END IF;
    END;

---

## 🏗️ Project Architecture

**Frontend → Python Flask → MySQL Database**

The frontend provides the user interface, Flask handles the backend logic, and MySQL stores the application data.

---

## 📸 Screenshots

### 🌐 GameZone Web Application


<img width="1350" height="673" alt="image" src="https://github.com/user-attachments/assets/eea91d94-f821-4005-b189-368a947d243f" />

<img width="1366" height="721" alt="image" src="https://github.com/user-attachments/assets/e6e84fbd-99c9-4cc6-8944-0d81fe2c8e15" />

### 🗃️ MySQL Workbench


<img width="1366" height="721" alt="image" src="https://github.com/user-attachments/assets/97d30d3f-4709-420f-9dec-064b7e7ee5be" />


---

## 🚀 How To Run

### Clone the Repository

    git clone https://github.com/hansikakvig/GameZone.git

### Open Project

    cd GameZone

### Create Virtual Environment

    python -m venv venv

### Activate Environment

    venv\Scripts\activate

### Install Dependencies

    pip install flask mysql-connector-python

### Setup Database

Create the MySQL database:

    CREATE DATABASE gamezone;

Then create the required tables and insert the project data.

### Run Application

    python app.py

Open in browser:

    http://127.0.0.1:5000

---

## 🎮 Project Workflow

**User → GameZone Website → Flask Backend → SQL Queries → MySQL Database → Website**

---

## 🎓 Project Information

**Project:** GameZone – Gaming Tournament Management System

**Type:** DBMS Mini Project

**Domain:** Gaming / Tournament Management

**Frontend:** HTML, CSS, JavaScript

**Backend:** Python Flask

**Database:** MySQL

---

## 👩‍💻 Developed By

**Hansika Vig**

B.Tech Computer Engineering

---

<div align="center">

### 🎮 Manage. Compete. Conquer. 🏆

**GameZone — A Practical Implementation of DBMS Concepts**

⭐ If you like this project, consider giving it a star!

</div>
