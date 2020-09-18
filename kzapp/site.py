import json
from .renderables import all as Renderables



class KZSite():
	def __init__(self, app):
		self.app = app
		self.SetupMeta()
		self.SetupRenderables()
		pass

	def SetupMeta(self):
		siteJsonPath = "site.json"
		with open(siteJsonPath) as f:
			self.meta = json.load(f)
		pass

	def SetupRenderables(self):
		self.SetupPages()
		pass

	def SetupPages(self):
		page = Renderables.Page()
		pass

	def __str__(self):
		return self.meta["meta"]["SITE_URL"]


