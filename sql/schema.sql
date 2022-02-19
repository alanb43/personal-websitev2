PRAGMA foreign_keys = ON;
CREATE TABLE users(
  username VARCHAR(20) PRIMARY KEY,
  fullname VARCHAR(40),
  filename VARCHAR(64),
  password VARCHAR(256),
  created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);  

CREATE TABLE posts(
  postid INTEGER PRIMARY KEY AUTOINCREMENT,
  owner VARCHAR(20),
  filename VARCHAR(64),
  caption VARCHAR(2048),
  created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (owner) 
    REFERENCES users(username) 
    ON DELETE CASCADE
);

CREATE TABLE comments(
    commentid INTEGER PRIMARY KEY AUTOINCREMENT,
    owner VARCHAR(20),
    postid INTEGER,
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    text VARCHAR(1024),
    FOREIGN KEY (owner) 
      REFERENCES users(username) 
      ON DELETE CASCADE
    FOREIGN KEY (postid) 
      REFERENCES posts(postid) 
      ON DELETE CASCADE
);
