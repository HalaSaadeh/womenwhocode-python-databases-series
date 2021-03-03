import sqlite3

conn = sqlite3.connect('chinook.db')
cur = conn.cursor()

# CREATE DATA
sqlstatement = CREATE TABLE IF NOT EXISTS CREDITCARD(cardID CHAR(4) NOT NULL, accountID INT NOT NULL, PRIMARY KEY(cardID), FOREIGN KEY accountID REFERENCES BANKACCOUNT(accountID))
cur.execute(sqlstatement)

# READ DATA
sqlstatement = "SELECT * FROM albums, artists WHERE artists.name = \"AC/DC\" AND albums.ArtistId=artists.ArtistId"
for row in cur.execute(sqlstatement):
    print(str(row))
    
# UPDATE DATA
sqlstatement = UPDATE PLAYLISTS set Name = "Music Play" WHERE Name = "Music"
cur.execute(sqlstatement)

# DELETE DATA
sqlstatement = DELETE FROM invoices WHERE BillingCountry = "France"
cur.execute(sqlstatement)

conn.close()
