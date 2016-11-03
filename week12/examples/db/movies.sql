-- https://sqlbolt.com/lesson/select_queries_introduction
CREATE TABLE movies
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title NOT NULL,
  director NOT NULL,
  year INTEGER,
  length_minutes INTEGER
);

INSERT INTO movies (title, director, year, length_minutes) VALUES
	("Toy Story", "John Lasseter", 1995, 81),
	("A Bug's Life", "John Lasseter", 1998, 95),
	("Toy Story 2", "John Lasseter", 1999, 93),
	("Monsters, Inc.", "Pete Docter", 2001, 92),
	("Finding Nemo", "Andrew Stanton", 2003, 107),
	("The Incredibles", "Brad Bird", 2004, 116),
	("Cars", "John Lasseter", 2006, 117),
	("Ratatouille", "Brad Bird", 2007, 115),
	("WALL-E", "Andrew Stanton", 2008, 104),
	("Up", "Pete Docter", 2009, 101);