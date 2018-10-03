#!/home/tech/.pyenv/shims/python

# -*- coding: utf-8 -*-

import sys
import urllib.request
import mysql.connector
import re

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

	# カウンター初期化
	cnt_java = 0
	cnt_javascr = 0
	cnt_python = 0
	cnt_php = 0
	cnt_ruby = 0
	cnt_cpp = 0
	cnt_cs = 0
	cnt_perl = 0
	cnt_objc = 0
	cnt_swift = 0
	cnt_sql = 0
	cnt_html = 0
	cnt_css = 0
	cnt_vb = 0
	cnt_asp = 0
	cnt_rpg = 0
	cnt_cobol = 0
	cnt_assem = 0

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

	# Create Query
	sql = "SELECT * FROM rikunabi_lst_jb0505020000"

	# Exec MySQL
	cursor.execute(sql)

	# クエリの現在行から残り全行を取得
	records = cursor.fetchall()

	# コミット
	conn.commit()

	# MySQL切断
	cursor.close()
#	conn.close()

	for record in records:

		# 単語をピックアップしてカウントする

		################# 12 #######################

		java_matchObj12 = re.search("Java[^Ss]", record[12])
		if( java_matchObj12 is not None ):
			cnt_java = cnt_java + 1

		javascr_matchObj12 = re.search("[Jj][Aa][Vv][Aa]Script", record[12])
		if( javascr_matchObj12 is not None ):
			cnt_javascr = cnt_javascr + 1

		python_matchObj12 = re.search("Python", record[12])
		if( python_matchObj12 is not None ):
			cnt_python = cnt_python + 1

		php_matchObj12 = re.search("PHP", record[12])
		if( php_matchObj12 is not None ):
			cnt_php = cnt_php + 1

		ruby_matchObj12 = re.search("[Rr]uby", record[12])
		if( ruby_matchObj12 is not None ):
			cnt_ruby = cnt_ruby + 1

		cpp_matchObj12 = re.search("C\+\+", record[12])
		if( cpp_matchObj12 is not None ):
			cnt_cpp = cnt_cpp + 1

		cs_matchObj12 = re.search("C#", record[12])
		if( cs_matchObj12 is not None ):
			cnt_cs = cnt_cs + 1

		perl_matchObj12 = re.search("Perl", record[12])
		if( perl_matchObj12 is not None ):
			cnt_perl = cnt_perl + 1

		objc_matchObj12 = re.search("Objective-C", record[12])
		if( objc_matchObj12 is not None ):
			cnt_objc = cnt_objc + 1

		swift_matchObj12 = re.search("[Ss][Ww][Ii][Ff][Tt]", record[12])
		if( swift_matchObj12 is not None ):
			cnt_swift = cnt_swift + 1

		sql_matchObj12 = re.search("SQL", record[12])
		if( sql_matchObj12 is not None ):
			cnt_sql = cnt_sql + 1

		html_matchObj12 = re.search("HTML", record[12])
		if( html_matchObj12 is not None ):
			cnt_html = cnt_html + 1

		css_matchObj12 = re.search("CSS", record[12])
		if( css_matchObj12 is not None ):
			cnt_css = cnt_css + 1

		vb_matchObj12 = re.search("VB", record[12])
		if( vb_matchObj12 is not None ):
			cnt_vb = cnt_vb + 1

		asp_matchObj12 = re.search("ASP", record[12])
		if( asp_matchObj12 is not None ):
			cnt_asp = cnt_asp + 1

		rpg_matchObj12 = re.search("RPG", record[12])
		if( rpg_matchObj12 is not None ):
			cnt_rpg = cnt_rpg + 1

		cobol_matchObj12 = re.search("COBOL", record[12])
		if( cobol_matchObj12 is not None ):
			cnt_cobol = cnt_cobol + 1

		assem_matchObj12 = re.search("アセンブラ", record[12])
		if( assem_matchObj12 is not None ):
			cnt_assem = cnt_assem + 1

		################# 13 #######################

		java_matchObj13 = re.search("Java[^Ss]", record[13])
		if( java_matchObj13 is not None ):
			cnt_java = cnt_java + 1

		javascr_matchObj13 = re.search("[Jj][Aa][Vv][Aa]Script", record[13])
		if( javascr_matchObj13 is not None ):
			cnt_javascr = cnt_javascr + 1

		python_matchObj13 = re.search("Python", record[13])
		if( python_matchObj13 is not None ):
			cnt_python = cnt_python + 1

		php_matchObj13 = re.search("PHP", record[13])
		if( php_matchObj13 is not None ):
			cnt_php = cnt_php + 1

		ruby_matchObj13 = re.search("[Rr]uby", record[13])
		if( ruby_matchObj13 is not None ):
			cnt_ruby = cnt_ruby + 1

		cpp_matchObj13 = re.search("C\+\+", record[13])
		if( cpp_matchObj13 is not None ):
			cnt_cpp = cnt_cpp + 1

		cs_matchObj13 = re.search("C#", record[13])
		if( cs_matchObj13 is not None ):
			cnt_cs = cnt_cs + 1

		perl_matchObj13 = re.search("Perl", record[13])
		if( perl_matchObj13 is not None ):
			cnt_perl = cnt_perl + 1

		objc_matchObj13 = re.search("Objective-C", record[13])
		if( objc_matchObj13 is not None ):
			cnt_objc = cnt_objc + 1

		swift_matchObj13 = re.search("[Ss][Ww][Ii][Ff][Tt]", record[13])
		if( swift_matchObj13 is not None ):
			cnt_swift = cnt_swift + 1

		sql_matchObj13 = re.search("SQL", record[13])
		if( sql_matchObj13 is not None ):
			cnt_sql = cnt_sql + 1

		html_matchObj13 = re.search("HTML", record[13])
		if( html_matchObj13 is not None ):
			cnt_html = cnt_html + 1

		css_matchObj13 = re.search("CSS", record[13])
		if( css_matchObj13 is not None ):
			cnt_css = cnt_css + 1

		vb_matchObj13 = re.search("VB", record[13])
		if( vb_matchObj13 is not None ):
			cnt_vb = cnt_vb + 1

		asp_matchObj13 = re.search("ASP", record[13])
		if( asp_matchObj13 is not None ):
			cnt_asp = cnt_asp + 1

		rpg_matchObj13 = re.search("RPG", record[13])
		if( rpg_matchObj13 is not None ):
			cnt_rpg = cnt_rpg + 1

		cobol_matchObj13 = re.search("COBOL", record[13])
		if( cobol_matchObj13 is not None ):
			cnt_cobol = cnt_cobol + 1

		assem_matchObj13 = re.search("アセンブラ", record[13])
		if( assem_matchObj13 is not None ):
			cnt_assem = cnt_assem + 1

#   print(java_matchObj.group()[:-1])
	print( "Java =" , cnt_java )
	print( "JavaScript =" , cnt_javascr )
	print( "Python =" , cnt_python )
	print( "PHP =" , cnt_php )
	print( "Ruby =" , cnt_ruby )
	print( "C++ =" , cnt_cpp )
	print( "C# =" , cnt_cs )
	print( "Perl =" , cnt_perl )
	print( "Objective-C =" , cnt_objc )
	print( "Swift =" , cnt_swift )
	print( "SQL =" , cnt_sql )
	print( "HTML =" , cnt_html )
	print( "CSS =" , cnt_css )
	print( "VB =" , cnt_vb )
	print( "ASP =" , cnt_asp )
	print( "RPG =" , cnt_rpg )
	print( "COBOL =" , cnt_cobol )
	print( "アセンブラ =" , cnt_assem )

	# 配列に保存
	lang_list = []
	lang_list.extend([cnt_java, cnt_javascr, cnt_python, cnt_php, cnt_ruby,
                      cnt_cpp, cnt_cs, cnt_perl, cnt_objc, cnt_swift, cnt_sql,
                      cnt_html, cnt_css, cnt_vb, cnt_asp, cnt_rpg, cnt_cobol, cnt_assem
                    ])

	cursor = conn.cursor()

	# DB更新
	for lang_cnt in range(17):
		sql = "UPDATE program_language SET total_count = " + str(lang_list[lang_cnt]) + " where id = " + str(lang_cnt+1)
		cursor.execute(sql)

	conn.commit()
	cursor.close()
	conn.close()


if __name__ == '__main__':
	main()
