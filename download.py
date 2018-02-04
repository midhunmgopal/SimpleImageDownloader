#image downaloder.
import urllib.request
import json
import datetime
from pathlib import Path


main_url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"

def download_image(url, file_name):
	'''
	Function to download the image with the url and save with the file_name.
	This function already checks before if the file is saved before.
	'''
	print ("Downloading Image....")
	print(file_name)
	if Path(file_name).exists() == False: 
		data = urllib.request.urlopen(url).read()
		print(len(data))
		print ("Download image completed....")

		file = open(file_name, "wb+")
		file.write(data)
		file.close()
		print ("Image saved....")

	else :
		print("File already exists..")


def get_filename(extension):
	'''
	Get the filename with the extension. if extension is not given the only filename is returned.
	'''
	file_name = datetime.datetime.now().strftime("%m-%d-%Y")
	if extension == "" :
		return file_name
	return file_name + "." + extension


def get_extension(url):
	'''
	Get the extension of the image we going to download.
	'''
	array_name = url.split("/")
	file_name = array_name[-1]
	array_extensions = file_name.split(".")
	return array_extensions[-1]


def download_metadata():
	'''
	Function to download the metadata of the image to download.
	'''
	print ("MedtaData Downloading....")
	data = urllib.request.urlopen(main_url).read().decode("utf-8")
	response = json.loads(data)
	image_url = response["images"][0]["url"]
	complete_url = get_complete_url(image_url)
	print ("MedtaData Download completed....")
	print (complete_url)
	extension = get_extension(complete_url)
	file_name = get_filename(extension)
	download_image(complete_url, file_name)


def get_complete_url(url):
	'''
	Function to get the complete image url.
	'''
	domain = "http://www.bing.com/"
	return domain + url


if __name__ == '__main__':
	print ("Main stared...")
	download_metadata()