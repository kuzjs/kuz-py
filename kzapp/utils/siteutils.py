from ..renderables import all as Renderables



def SetupNextPrevious(arr):
	for index in range(0, len(arr)):
		arr[index].index = index
		arr[index].next = arr[index + 1] if (index + 1) < len(arr) else None
		arr[index].previous = arr[index - 1] if (index > 1) else None

def GetEntities(site, EntityClass):
	entity = EntityClass()
	arr = [entity]
	SetupNextPrevious(arr)
	return arr
	pass

def GetAuthors(site):
	return GetEntities(site, Renderables.Author)
	pass

def GetCategories(site):
	return GetEntities(site, Renderables.Category)
	pass

def GetTags(site):
	return GetEntities(site, Renderables.Tag)
	pass

def GetCollections(site):
	return GetEntities(site, Renderables.Collection)
	pass

def GetPages(site):
	return []
	pass


		
