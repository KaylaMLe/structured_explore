import pandas as pd
from preswald import text, load

text("# Your resume")

connection_name = load("resume.csv", "resume_connection")

data = pd.read_csv("resume.csv")

for index, row in data.iterrows():
	for value in row:
		text(value)
