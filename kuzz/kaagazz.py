import json


class KaagazzApp():
	def __init__(self):
		kaagazzJsonPath = "kzapp/data/json/kaagazz.json"
		with open(kaagazzJsonPath) as f:
			self.meta = json.load(f)
		pass

	def Run(self):
		print(self)
		pass

	def __str__(self):
		return self.meta["meta"]["title"] + " is on " + self.meta["meta"]["version"] + "."


