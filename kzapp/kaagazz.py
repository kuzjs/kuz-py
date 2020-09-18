import json
from .site import KZSite



class KaagazzApp():
	def __init__(self):
		self.SetupMeta()
		self.SetupBlackadder()
		self.site = KZSite(self)
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
		print(self.site)
		pass

	def Run(self):
		self.CunningPlan()
		pass

	def __str__(self):
		return self.meta["meta"]["title"] + " is on " + self.meta["meta"]["version"] + "."


