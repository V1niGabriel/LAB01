# Não precisa importar Calculator e DatabaseConnection aqui!

def test_database_connection(db):
    result = db.connect()
    assert result == "Connected to database"
    assert db.connected is True

def test_database_query(db):
    db.connect()
    results = db.query("SELECT * FROM users")
    assert len(results) == 1
    assert results[0]["name"] == "test"

def test_calculator_with_db_flow(db, calc):
    db.connect()
    db_data = db.query("SELECT value FROM config")[0]
    result = calc.add(10, db_data["id"])
    assert result == 11