import json



def main():
	siteJsonPath = "site.json"
	with open(siteJsonPath) as f:
		sj = json.load(f)

	for a in sj["navbar"]:
		print(a["title"])
	pass

if __name__ == '__main__':
	main()
