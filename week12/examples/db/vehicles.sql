-- https://sqlbolt.com/
CREATE TABLE vehicles
(
  id INTEGER PRIMARY KEY AUTOINCREMENT ,
  model TEXT NOT NULL,
  wheels INTEGER NOT NULL DEFAULT 4,
  doors INTEGER DEFAULT 0,
  type TEXT NOT NULL
);

INSERT INTO vehicles(model, wheels, doors, type)
  VALUES
  ('Ford Focus', 4, 4, 'Sedan'),
  ('Tesla Roadster',	4,	2,	'Sports'),
  ('Kawakasi Ninja',	2,	0,	'Motorcycle'),
  ('McLaren Formula 1',	4,	0,	'Race'),
  ('Tesla S',	4,	4,	'Sedan');
