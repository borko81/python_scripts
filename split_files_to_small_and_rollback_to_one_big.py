#IMPORT SOME MODULES
import os		#OPEN FILE
import sys		#GET PARAM FROM CONSOLE AND USE TO EXIT IF ERROR RAISE
import re 		#REGULAR EXSPRESION

#HARDCODE PARAM IS HERE
#PATH TO SEARCH BIG FILE
PATH = r'C:\\Users\\Borko\\Desktop\\split_files\\Errors.log'

#PATH TO FOLDER WHERE PUT RESULT AND FROM WHERE CREATE FILE BACK
PATH2 = r'C:\\Users\\Borko\\Desktop\\'

#CHUNK SIZE TO READ FILE 1Mb
CHUNK_SIZE = (1024*1024)

#NAME TO SMALL FILES
some_name = 'some_name'

#Check Path exists close program if not
try:
	open(PATH, 'r')
except FileNotFoundError as fr :
	print(fr)
	sys.exit()


#OPEND FILE USE CHUNK AND ITER RESULT WITH YIELD
def read_file(PATH):
	lines = open(PATH, 'br').read()
	while lines:
		chunk = lines[:CHUNK_SIZE]
		lines = lines[CHUNK_SIZE:]
		yield chunk


#WRITE SMALL CHUNK TO NEW SMALL FILES WITH NOT EXTENSION
#EXTENSION FOR SMALL FILES COME FROM PARAM count
def write_to_files(PATH2):
	count = 1
	for res in read_file(PATH):
		name = '{}{}'.format(some_name, count)
		w = open(os.path.join(PATH2, name), 'bw')
		w.write(res)
		w.close()
		count += 1


#READ FOLDER PATH2 AND SEARCH FOR FILES'S THEN RETURN LIST WITH THEM
def concat_chunk_file_to_one():
	found_chink_files = []
	for file in os.listdir(PATH2):
		if re.search('({})\d+'.format(some_name), file):
			found_chink_files.append(os.path.join(PATH2, file))
	return sorted(found_chink_files)


#CONCAT ALL FOUND SMALL FILES TO ONE BIG
def write_concat_to_one_big():
	w = open(PATH2+'\\'+'BIG_FILE.txt', 'a')
	for line in concat_chunk_file_to_one():
		w.write(open(line, 'r').read())
		#print(line)
	w.close()


if __name__ == '__main__':
	#UNCOMENT TO SPLIT FILE TO SMALL
	#write_to_files(PATH2)
	
	#UNCOMENT TO JOIN SMALL FILES TO ONE BIG
	#write_concat_to_one_big()

