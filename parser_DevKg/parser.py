import requests
from bs4 import BeautifulSoup
from time import sleep


MAIN_URL = 'https://devkg.com'

def get_jobs():
	for el in range(1, 100):
		url = f'{MAIN_URL}/ru/jobs?page={el}'

		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'lxml')
		jobs = soup.find('div', class_= 'jobs-list').find_all('article', class_='item')
		for job in jobs:
			yield job

def get_info_job(key_words):
	job_info_list = []
	for job in get_jobs():
		if job.find('a', class_='link archived'):
			return job_info_list
			exit()
			#raise KeyboardInterrupt

		job_position = job.find('div', class_='jobs-item-field position').text\
						.replace('\n', '').replace(' ', '').replace('Должность', '')
		job_url = job.find('a', class_='link').get('href')
		for key_word in key_words:
			if key_word in job_position.lower():
				full_job_url = MAIN_URL + job_url
				job_info_list += [job_position + '\n' + full_job_url]

