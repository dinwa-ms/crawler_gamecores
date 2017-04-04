import csv

count = 0

with open("gcore_result_all.csv", "a+") as f:
	writer = csv.writer(f, delimiter=",")
	writer.writerow(["No.", "time", "title", "subtitle", "likes", "comments"])
	for i in range (0, 9):
		with open('gcore_result_{}.csv'.format(i), 'rb') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',')
			for row in spamreader:
				count += 1
				article = ', '.join(row[1:])
				writer.writerow([count, row[1], row[2], row[3], row[4], row[5]])
