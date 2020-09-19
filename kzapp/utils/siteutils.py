from ..renderables import all as Renderables



def SetupNextPrevious(arr):
	for index in range(0, len(arr)-1):
		arr[index].index = index
		arr[index].next = arr[index + 1] if arr[index + 1] else None
		arr[index].previous = arr[index - 1] if arr[index - 1] else None

def GetEntities(site):
	pass

def GetAuthors(site):
	return []
	pass

def GetCategories(site):
	return []
	pass

def GetTags(site):
	return []
	pass

def GetCollections(site):
	return []
	pass

def GetPages(site):
	return []
	pass

