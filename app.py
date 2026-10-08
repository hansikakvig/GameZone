from flask import Flask, render_template, request, redirect
from database import get_db_connection

app = Flask(__name__)


# =========================
# DASHBOARD
# =========================

@app.route("/")
def dashboard():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM Player")
    players = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Team")
    teams = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Game")
    games = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Tournament")
    tournaments = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM GameMatch")
    matches = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return render_template(
        "index.html",
        players=players,
        teams=teams,
        games=games,
        tournaments=tournaments,
        matches=matches
    )


# =========================
# PLAYERS
# =========================

@app.route("/players")
def players():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Player ORDER BY player_id")
    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("players.html", players=data)


@app.route("/add_player", methods=["POST"])
def add_player():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Player
        (player_name, email, age, country)
        VALUES (%s, %s, %s, %s)
    """, (
        request.form["player_name"],
        request.form["email"],
        request.form["age"],
        request.form["country"]
    ))

    connection.commit()
    cursor.close()
    connection.close()

    return redirect("/players")


@app.route("/delete_player/<int:id>")
def delete_player(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Team_Member WHERE player_id = %s", (id,))
    cursor.execute("UPDATE Team SET captain_id = NULL WHERE captain_id = %s", (id,))
    cursor.execute("DELETE FROM Player WHERE player_id = %s", (id,))

    connection.commit()
    cursor.close()
    connection.close()

    return redirect("/players")


# =========================
# TEAMS
# =========================

@app.route("/teams")
def teams():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT Team.team_id, Team.team_name,
               Player.player_name AS captain
        FROM Team
        LEFT JOIN Player
        ON Team.captain_id = Player.player_id
        ORDER BY Team.team_id
    """)

    data = cursor.fetchall()

    cursor.execute("SELECT player_id, player_name FROM Player")
    players = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "teams.html",
        teams=data,
        players=players
    )


@app.route("/add_team", methods=["POST"])
def add_team():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Team (team_name, captain_id)
        VALUES (%s, %s)
    """, (
        request.form["team_name"],
        request.form["captain_id"]
    ))

    connection.commit()
    cursor.close()
    connection.close()

    return redirect("/teams")


@app.route("/delete_team/<int:id>")
def delete_team(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Team_Member WHERE team_id = %s", (id,))
    cursor.execute("DELETE FROM Registration WHERE team_id = %s", (id,))
    cursor.execute("""
        UPDATE GameMatch
        SET winner_team_id = NULL
        WHERE winner_team_id = %s
    """, (id,))
    cursor.execute("DELETE FROM GameMatch WHERE team1_id = %s OR team2_id = %s", (id, id))
    cursor.execute("DELETE FROM Team WHERE team_id = %s", (id,))

    connection.commit()
    cursor.close()
    connection.close()

    return redirect("/teams")


# =========================
# GAMES
# =========================

@app.route("/games")
def games():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Game ORDER BY game_id")
    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("games.html", games=data)


@app.route("/add_game", methods=["POST"])
def add_game():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Game (game_name, game_type)
        VALUES (%s, %s)
    """, (
        request.form["game_name"],
        request.form["game_type"]
    ))

    connection.commit()
    cursor.close()
    connection.close()

    return redirect("/games")


@app.route("/delete_game/<int:id>")
def delete_game(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Tournament WHERE game_id = %s", (id,))
    cursor.execute("DELETE FROM Game WHERE game_id = %s", (id,))

    connection.commit()
    cursor.close()
    connection.close()

    return redirect("/games")


# =========================
# TOURNAMENTS
# =========================

@app.route("/tournaments")
def tournaments():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT Tournament.*, Game.game_name
        FROM Tournament
        LEFT JOIN Game
        ON Tournament.game_id = Game.game_id
        ORDER BY tournament_id
    """)

    data = cursor.fetchall()

    cursor.execute("SELECT game_id, game_name FROM Game")
    games_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "tournaments.html",
        tournaments=data,
        games=games_data
    )


@app.route("/add_tournament", methods=["POST"])
def add_tournament():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Tournament
        (tournament_name, game_id, start_date, end_date, prize_pool)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        request.form["tournament_name"],
        request.form["game_id"],
        request.form["start_date"],
        request.form["end_date"],
        request.form["prize_pool"]
    ))

    connection.commit()
    cursor.close()
    connection.close()

    return redirect("/tournaments")


# =========================
# MATCHES
# =========================

@app.route("/matches")
def matches():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            GameMatch.match_id,
            Tournament.tournament_name,
            T1.team_name AS team1,
            T2.team_name AS team2,
            GameMatch.match_date,
            Winner.team_name AS winner
        FROM GameMatch
        LEFT JOIN Tournament
            ON GameMatch.tournament_id = Tournament.tournament_id
        LEFT JOIN Team T1
            ON GameMatch.team1_id = T1.team_id
        LEFT JOIN Team T2
            ON GameMatch.team2_id = T2.team_id
        LEFT JOIN Team Winner
            ON GameMatch.winner_team_id = Winner.team_id
        ORDER BY GameMatch.match_id
    """)

    data = cursor.fetchall()

    cursor.execute("SELECT tournament_id, tournament_name FROM Tournament")
    tournaments_data = cursor.fetchall()

    cursor.execute("SELECT team_id, team_name FROM Team")
    teams_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "matches.html",
        matches=data,
        tournaments=tournaments_data,
        teams=teams_data
    )


@app.route("/add_match", methods=["POST"])
def add_match():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO GameMatch
        (tournament_id, team1_id, team2_id, match_date, winner_team_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        request.form["tournament_id"],
        request.form["team1_id"],
        request.form["team2_id"],
        request.form["match_date"],
        request.form["winner_team_id"]
    ))

    connection.commit()
    cursor.close()
    connection.close()

    return redirect("/matches")


# =========================
# LEADERBOARD
# =========================

@app.route("/leaderboard")
def leaderboard():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            Team.team_name,
            COALESCE(SUM(Score.score), 0) AS total_score,
            COUNT(Score.score_id) AS matches_played
        FROM Team
        LEFT JOIN Score
            ON Team.team_id = Score.team_id
        GROUP BY Team.team_id, Team.team_name
        ORDER BY total_score DESC
    """)

    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("leaderboard.html", leaderboard=data)


# =========================
# RUN
# =========================

if __name__ == "__main__":
    app.run(debug=True)