import json



class KZSite():
	def __init__(self, app):
		self.app = app
		self.SetupMeta()
		pass

	def SetupMeta(self):
		siteJsonPath = "site.json"
		with open(siteJsonPath) as f:
			self.meta = json.load(f)
		pass

	def SetupRenderables(self):
		pass

	def __str__(self):
		return self.meta["meta"]["SITE_URL"]


