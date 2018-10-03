#!/home/tech/.pyenv/shims/python

# -*- coding: utf-8 -*-

import sys
import urllib.request
import mysql.connector
import re
from bs4 import BeautifulSoup

def get_job_details(table_name, url_lists):

	# MySQL接続
	conn = mysql.connector.connect(
	host='xxx.xxx.xxx.xxx',
	port='xxxx',
	db='xxxxxxxxxxxxxxxxxxx',
	user='xxxxxxxxx',
	password='xxxxxxxxx',
	charset='utf8'
	)

	cursor = conn.cursor()

	for int_classification in url_lists:

		# 変数初期化
		establishment = ""
		representative = ""
		capital = ""
		amount_of_sales = ""
		employees = ""
		office = ""
		industry = ""
		business_contents = ""
		job_description = ""
		job_description_detail = ""
		requested_personnel = ""
		requested_personnel_detail = ""
		work_location = ""
		transportation = ""
		region = ""
		salary = ""
		annual_income_example = ""
		working_hours = ""
		start_time = ""
		finish_time = ""
		holiday = ""
		welfare = ""

		url = int_classification
		res = urllib.request.urlopen(url)
		soup = BeautifulSoup(res, 'html.parser')

		aaa = soup.find_all('tr', class_='rnn-tableGrid')
		cnt = 0

		for a in aaa:
			bbb = a.find_all('td', class_='rnn-col-10')
			for b in bbb:
				b = str(b).replace('<td class="rnn-col-10">','')
				b = str(b).replace('</td>','')
				b = str(b).replace('<p>','')
				b = str(b).replace('</p>','')
				b = str(b).replace(' ','')
				b = str(b).replace(',',' ')
				b = str(b).replace('<br/>','\n')
				b = str(b).replace('\r\n','')
				b = str(b).replace('<tdclass="rnn-col-10rnn-grouprnn-group--xm">','')

				ccc = a.find_all('th', class_='rnn-col-2')
				for c in ccc:
					if(c.string == '仕事の内容'):
						tmp_job_description = str(b)
						tmp_job_description = tmp_job_description.split("【具体的には】")
						job_description = tmp_job_description[0]
						job_description_detail = tmp_job_description[1]
#						print("仕事の内容：" + job_description)
						break
					if(c.string == '求めている人材'):
						tmp_requested_personnel = str(b)
						tmp_requested_personnel = tmp_requested_personnel.split("【具体的には】")
						requested_personnel = tmp_requested_personnel[0]
						requested_personnel_detail = tmp_requested_personnel[1]
#						print("求めている人材：" + requested_personnel)
						break
					if(c.string == '勤務地'):
						tmp_work_location = str(b)
						# get 勤務地
						tmp_work_location = tmp_work_location.split("→リクナビＮＥＸＴ上の地域分類では……")
						work_location = tmp_work_location[0]

						# get [勤務地]  or   get [勤務地・交通手段]
						work_index = tmp_work_location[1].find("【交通手段】")
						if( work_index != -1):
							tmp_work_location = tmp_work_location[1].split("【交通手段】")
							region = tmp_work_location[0]
							transportation = tmp_work_location[1]
						else:
							region = tmp_work_location[1]
#						print("勤務地：" + work_location)
						break
					if(c.string == '給与'):
						tmp_salary = str(b)
						salary_index = tmp_salary.find("【年収例】")
						if( salary_index != -1):
							tmp_salary = tmp_salary.split("【年収例】")
							#get 給与
							salary = tmp_salary[0]
							#get 年収例
							annual_income_example = tmp_salary[1]
						else:
							salary = tmp_salary

#						print("給与：" + salary)
						break
					if(c.string == '勤務時間'):
						working_hours = str(b)
						tmp_working_hours = working_hours
						wh_matchObj = re.search("(\d{1,2})[:：](\d{2})\W(\d{1,2})[:：](\d{2})", tmp_working_hours)
						if wh_matchObj:
							start_time = wh_matchObj.group(1) + ":" + wh_matchObj.group(2)
							finish_time = wh_matchObj.group(3) + ":" + wh_matchObj.group(4)
#						print("勤務時間：" + working_hours)
						break
					if(c.string == '休日・休暇'):
						holiday = str(b)
#						print("休日・休暇：" + holiday)
						break
					if(c.string == '待遇・福利厚生'):
						welfare = str(b)
#						print("待遇・福利厚生：" + welfare)
						break
					if(c.string == '設立'):
						establishment = str(b)
#						print("設立：" + establishment)
						break
					if(c.string == '代表者'):
						representative = str(b)
#						print("代表者：" + representative)
						break
					if(c.string == '資本金'):
						capital = str(b)
						# 円のところまで取得
						capi_index = capital.find("円")
						capital = capital[:capi_index + 1]
						capital = capital.replace(',','')
						capital = capital.replace(' ','')
#						print("資本金：" + capital)
						break
					if(c.string == '売上高'):
						amount_of_sales = str(b)
						amount_index = amount_of_sales.find("円")
						amount_of_sales = amount_of_sales[:amount_index + 1]
						amount_of_sales = amount_of_sales.replace(',','')
						amount_of_sales = amount_of_sales.replace(' ','')
#						print("売上高：" + amount_of_sales)
						break
					if(c.string == '従業員数'):
						employees = str(b)
						employ_index = employees.find("名")
						employees = employees[:employ_index + 1]
						employees = employees.replace('人','名')
						employees = employees.replace('約','')
						employees = employees.replace(',','')
						employees = employees.replace('名','')
						employees = employees.replace('【連結】','')
						employees = employees.replace('連結','')
						employees = employees.replace('単体','')
						employees = employees.replace('万','')
						employees = employees.replace(' ','')
#						print("従業員数：" + employees)
						break
					if(c.string == '事業所'):
						office = str(b)
#						print("事業所：" + office)
						break
					if(c.string == '業種'):
						industry = str(b)
#						print("業種：" + industry)
						break
					if(c.string == '事業内容'):
						business_contents = str(b)
#						print("事業内容：" + business_contents)
						break


		# 企業名
		company_name = soup.find('p', class_='rnn-offerCompanyName')
		#print("企業名：" + company_name.string)


		# Create Query
		sql = "INSERT INTO rikunabi_" + table_name + " (id, company_name, establishment, representative, capital, \
									 amount_of_sales, employees, office, industry, business_contents, \
									 job_description, job_description_detail, requested_personnel, requested_personnel_detail, work_location, \
									 transportation, region, salary, annual_income_example, working_hours, start_time, \
									 finish_time, holiday, welfare) \
				VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		val = (company_name.string, establishment, representative, capital, amount_of_sales, \
			   employees, office, industry, business_contents, job_description, job_description_detail, \
			   requested_personnel, requested_personnel_detail, work_location, transportation, region, salary, \
			   annual_income_example, working_hours, start_time, finish_time, holiday, welfare)

		# Exec MySQL
		cursor.execute(sql,val)

		# 変数初期化
		establishment = ""
		representative = ""
		capital = ""
		amount_of_sales = ""
		employees = ""
		office = ""
		industry = ""
		business_contents = ""
		job_description = ""
		job_description_detail = ""
		requested_personnel = ""
		requested_personnel_detail = ""
		work_location = ""
		salary = ""
		annual_income_example = ""
		working_hours = ""
		start_time = ""
		finish_time = ""
		transportation = ""
		region = ""
		holiday = ""
		welfare = ""

	# コミット
	conn.commit()

	# MySQL切断
	cursor.close()
	conn.close()


def info_acquisition(soup , it_classification , total_count):

	page = [
			'51','101','151','201','251','301','351','401','451','501',
			'551','601','651','701','751','801','851','901','951','1001',
			'1051','1101','1151','1201','1251','1301','1351','1401','1451','1501',
			'1551','1601','1651','1701','1751','1801','1851','1901','1951','2001',
			'2051','2101','2151','2201','2251','2301','2351','2401','2451','2501',
			'2551','2601','2651','2701','2751','2801','2851','2901','2951','3001'
			]

	lists = []
	url_lists = []
	

	# 詳細ページのリンク取得
	links = [a.get("href") for a in soup.find_all('a', class_='rnn-linkText rnn-linkText--black', limit = total_count)]
	for link in links:
#		print("https://next.rikunabi.com" + link)
		lists.append("https://next.rikunabi.com" + link)

	# 件数が51件以上ならページネートして全ての案件データを取得する
	if total_count >= 51:
		page_no = int(total_count / 51)
		i = 0
		while i < page_no:
			url = "https://next.rikunabi.com/tech_soft/" + it_classification + "/new/crn" + page[i] + ".html"
			res = urllib.request.urlopen(url)
			soup = BeautifulSoup(res, 'html.parser')

			# 詳細ページのリンク取得
			links = [a.get("href") for a in soup.find_all('a', class_='rnn-linkText rnn-linkText--black')]
			for link in links:
#				print("https://next.rikunabi.com" + link)
				lists.append("https://next.rikunabi.com" + link)
			i = i + 1

	# 「求人情報」が記載されているリンクを探す
	#  ※転職支援サービス案件は取得しない
	for lst in lists:
		url = lst
		res = urllib.request.urlopen(url)
		soup = BeautifulSoup(res, 'html.parser')

		# リクナビ求人は、ページタブが"求人情報"のみのケースと、"メッセージ"と"求人情報"があるケースに分かれており、
		# デフォルトではページタブは"メッセージ"にフォーカスされているので、
		# 検索でメッセージがヒットした場合は、再度"求人情報"を検索する
		for kkk in soup.find_all('span', class_='rnn-tabMenu__navi__itemText', limit = 1): 
			#print(kkk)
			if( kkk.string == 'メッセージ'):

				details_links = [a.get("href") for a in soup.find_all('a', class_='rnn-tabMenu__navi__itemlink', limit = 1)]
				for details_link in details_links:
					#print( "https://next.rikunabi.com" + details_link )
					url_lists.append("https://next.rikunabi.com" + details_link)

			else:
				#print(lst)
				url_lists.append(lst)

	return url_lists

def record_count(sp):

	for t in sp.find_all('span', class_='rnn-pageNumber rnn-textLl'):
		count = t.get_text()
		#print(count[0].text)
		#print(count)

		int_count = 0

		if count is None:
			int_count = 0
		else:
			int_count = int(count)

		return int_count

def main():
	it_classifications = [
                          'lst_jb0505010000', # システムコンサルタント・システムアナリスト・プリセールス
                          'lst_jb0505020000', # システム開発（Web・オープン・モバイル系）
                          'lst_jb0505030000', # システム開発（汎用機系）
                          'lst_jb0505040000', # システム開発（組み込み・ファームウェア・制御系）
                          'lst_jb0505050000', # パッケージソフト・ミドルウェア開発
                          'lst_jb0505060000', # ネットワーク・サーバ設計・構築（LAN・WAN・Web系）
                          'lst_jb0505070000', # 通信インフラ設計・構築（キャリア・ISP系）
                          'lst_jb0505080000', # 運用・保守・監視・テクニカルサポート
                          'lst_jb0505090000', # 社内SE・情報システム
                          'lst_jb0505100000', # 研究・特許・テクニカルマーケティング
                          'lst_jb0510030000'  # 品質管理
                        ]

	lst_jb0505010000 = []
	lst_jb0505020000 = []
	lst_jb0505030000 = []
	lst_jb0505040000 = []
	lst_jb0505050000 = []
	lst_jb0505060000 = []
	lst_jb0505070000 = [] 
	lst_jb0505080000 = []
	lst_jb0505090000 = []
	lst_jb0505100000 = []
	lst_jb0510030000 = []

	for it_classification in it_classifications:
		# 新着案件のトップページをスキル毎に取得する
		url = "https://next.rikunabi.com/tech_soft/" + it_classification + "/new/"
		res = urllib.request.urlopen(url)
		soup = BeautifulSoup(res, 'html.parser')

		# 新着件数取得(転職支援サービスも含んでる)
		total_count = record_count(soup)

		# 各スキルのページから「求人情報」が記載されているリンクを探す
		if it_classification == 'lst_jb0505010000':
			if total_count is not None:
				lst_jb0505010000 = info_acquisition(soup , it_classification , total_count)
				print("============= {0}  新着{1}件 ===============" . format(it_classification, len(lst_jb0505010000)))
				get_job_details(it_classification, lst_jb0505010000)
			else:
				print("============= {0}  新着0件 ===============" . format(it_classification))
		elif it_classification == 'lst_jb0505020000':
			if total_count is not None:
				lst_jb0505020000 = info_acquisition(soup , it_classification , total_count)
				print("============= {0}  新着{1}件 ===============" . format(it_classification, len(lst_jb0505020000)))
				get_job_details(it_classification, lst_jb0505020000)
			else:
				print("============= {0}  新着0件 ===============" . format(it_classification))
		elif it_classification == 'lst_jb0505030000':
			if total_count is not None:
				lst_jb0505030000 = info_acquisition(soup , it_classification , total_count)
				print("============= {0}  新着{1}件 ===============" . format(it_classification, len(lst_jb0505030000)))
				get_job_details(it_classification, lst_jb0505030000)
			else:
				print("============= {0}  新着0件 ===============" . format(it_classification))
		elif it_classification == 'lst_jb0505040000':
			if total_count is not None:
				lst_jb0505040000 = info_acquisition(soup , it_classification , total_count)
				print("============= {0}  新着{1}件 ===============" . format(it_classification, len(lst_jb0505040000)))
				get_job_details(it_classification, lst_jb0505040000)
			else:
				print("============= {0}  新着0件 ===============" . format(it_classification))
		elif it_classification == 'lst_jb0505050000':
			if total_count is not None:
				lst_jb0505050000 = info_acquisition(soup , it_classification , total_count)
				print("============= {0}  新着{1}件 ===============" . format(it_classification, len(lst_jb0505050000)))
				get_job_details(it_classification, lst_jb0505050000)
			else:
				print("============= {0}  新着0件 ===============" . format(it_classification))
		elif it_classification == 'lst_jb0505060000':
			if total_count is not None:
				lst_jb0505060000 = info_acquisition(soup , it_classification , total_count)
				print("============= {0}  新着{1}件 ===============" . format(it_classification, len(lst_jb0505060000)))
				get_job_details(it_classification, lst_jb0505060000)
			else:
				print("============= {0}  新着0件 ===============" . format(it_classification))
		elif it_classification == 'lst_jb0505070000':
			if total_count is not None:
				lst_jb0505070000 = info_acquisition(soup , it_classification , total_count)
				print("============= {0}  新着{1}件 ===============" . format(it_classification, len(lst_jb0505070000)))
				get_job_details(it_classification, lst_jb0505070000)
			else:
				print("============= {0}  新着0件 ===============" . format(it_classification))
		elif it_classification == 'lst_jb0505080000':
			if total_count is not None:
				lst_jb0505080000 = info_acquisition(soup , it_classification , total_count)
				print("============= {0}  新着{1}件 ===============" . format(it_classification, len(lst_jb0505080000)))
				get_job_details(it_classification, lst_jb0505080000)
			else:
				print("============= {0}  新着0件 ===============" . format(it_classification))
		elif it_classification == 'lst_jb0505090000':
			if total_count is not None:
				lst_jb0505090000 = info_acquisition(soup , it_classification , total_count)
				print("============= {0}  新着{1}件 ===============" . format(it_classification, len(lst_jb0505090000)))
				get_job_details(it_classification, lst_jb0505090000)
			else:
				print("============= {0}  新着0件 ===============" . format(it_classification))
		elif it_classification == 'lst_jb0505100000':
			if total_count is not None:
				lst_jb0505100000 = info_acquisition(soup , it_classification , total_count)
				print("============= {0}  新着{1}件 ===============" . format(it_classification, len(lst_jb0505100000)))
				get_job_details(it_classification, lst_jb0505100000)
			else:
				print("============= {0}  新着0件 ===============" . format(it_classification))
		elif it_classification == 'lst_jb0510030000':
			if total_count is not None:
				lst_jb0510030000 = info_acquisition(soup , it_classification , total_count)
				print("============= {0}  新着{1}件 ===============" . format(it_classification, len(lst_jb0510030000)))
				get_job_details(it_classification, lst_jb0510030000)
			else:
				print("============= {0}  新着0件 ===============" . format(it_classification))
		else:
			print("EEERRROOOOOORRR")

	print("")
	print("==========  Collection Complete  ===========")
	print("")

if __name__ == '__main__':
	main()
