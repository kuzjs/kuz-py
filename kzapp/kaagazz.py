import json


class KaagazzApp():
	def __init__(self):
		self.SetupMeta()
		self.SetupBlackadder()
		pass

	def SetupMeta(self):
		kaagazzJsonPath = "kzapp/data/json/kaagazz.json"
		with open(kaagazzJsonPath) as f:
			self.meta = json.load(f)
		pass

	def SetupBlackadder(self):
		blackadderJsonPath = "kzapp/data/json/blackadder.json"
		with open(blackadderJsonPath) as f:
			self.blackadder = json.load(f)
		pass

	def CunningPlan(self):
		for quote in self.blackadder["quotes"]:
			text = self.blackadder["quotes"][quote]
			print(text)
			pass
		pass

	def Run(self):
		self.CunningPlan()
		pass

	def __str__(self):
		return self.meta["meta"]["title"] + " is on " + self.meta["meta"]["version"] + "."


