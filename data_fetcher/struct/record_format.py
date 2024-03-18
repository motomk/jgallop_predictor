# format仕様
# (位置, データ構造の繰り返し回数, データ構造, バイト合計)
# データ構造は1,もしくはtupleである。
# tupleの場合は、tupleの構造で繰り返す。
# 例:
# 固定長: 1234567890ABCDEFGHIJKLMN
# format_sample = [
#   (1,1,1,1),(2,1,1,1),(3,1,1,1),(4,1,2,2),(6,1,(1,2,1),4)(10,1,(2,2,1),5),(15,2,(1,2,1),8),(23,1,1,1),(24,1,1,1)
# ]
# 1,2,3,45,6,78,9,0A,BC,D,E,F,GH,E,FG,H,I,JK,L,M,N

H1_csv_header = [
    "record_type_id",  # レコード種別ID
    "data_category",  # データ区分
    "data_creation_date",  # データ作成年月日
    "event_year",  # 開催年
    "event_date",  # 開催月日
    "race_track_code",  # 競馬場コード
    "event_number",  # 開催回_第N回
    "event_day",  # 開催日目_N日目
    "race_number",  # レース番号
    "registered_horses",  # 登録頭数
    "starting_horses",  # 出走頭数
    "betting_flag_win",  # 発売フラグ_単勝
    "betting_flag_place",  # 発売フラグ_複勝
    "betting_flag_quinella_place",  # 発売フラグ_枠連
    "betting_flag_quinella",  # 発売フラグ_馬連
    "betting_flag_wide",  # 発売フラグ_ワイド
    "betting_flag_exacta",  # 発売フラグ_馬単
    "betting_flag_trio",  # 発売フラグ_3連複
    "place_payoff_key",  # 複勝着払キー
    "return_horse_number_info",  # 返還馬番情報
    "return_frame_number_info",  # 返還枠番情報
    "return_same_frame_info",  # 返還同枠情報
    "win_bets_horse_number",  # 単勝票数_馬番
    "win_bets_count",  # 単勝票数_票数
    "win_bets_popularity_order",  # 単勝票数_人気順
    "place_bets_horse_number",  # 複勝票数_馬番
    "place_bets_count",  # 複勝票数_票数
    "place_bets_popularity_order",  # 複勝票数_人気順
    "quinella_place_bets_combination_number",  # 枠連票数_組番
    "quinella_place_bets_count",  # 枠連票数_票数
    "quinella_place_bets_popularity_order",  # 枠連票数_人気順
    "quinella_bets_combination_number",  # 馬連票数_組番
    "quinella_bets_count",  # 馬連票数_票数
    "quinella_bets_popularity_order",  # 馬連票数_人気順
    "wide_bets_combination_number",  # ワイド票数_組番
    "wide_bets_count",  # ワイド票数_票数
    "wide_bets_popularity_order",  # ワイド票数_人気順
    "exacta_bets_combination_number",  # 馬単票数_組番
    "exacta_bets_count",  # 馬単票数_票数
    "exacta_bets_popularity_order",  # 馬単票数_人気順
    "win_bets_total",  # 単勝票数合計
    "place_bets_total",  # 複勝票数合計
    "quinella_place_bets_total",  # 枠連票数合計
    "quinella_bets_total",  # 馬連票数合計
    "wide_bets_total",  # ワイド票数合計
    "exacta_bets_total",  # 馬単票数合計
    "trio_bets_total",  # 3連複票数合計
    "win_bets_return_total",  # 単勝返還票数合計
    "place_bets_return_total",  # 複勝返還票数合計
    "quinella_place_bets_return_total",  # 枠連返還票数合計
    "quinella_bets_return_total",  # 馬連返還票数合計
    "wide_bets_return_total",  # ワイド返還票数合計
    "exacta_bets_return_total",  # 馬単返還票数合計
    "trio_bets_return_total",  # 3連複返還票数合計
]

H1_format = [
    # 1			レコード種別ID	1	1	2 	2
    (1, 1, 2, 2),
    # 2			データ区分	3	1	1 	1
    (3, 1, 1, 1),
    # 3			データ作成年月日	4	1	8 	8
    (4, 1, 8, 8),
    # 4		○	開催年	12	1	4 	4
    (12, 1, 4, 4),
    # 5		○	開催月日	16	1	4 	4
    (16, 1, 4, 4),
    # 6		○	競馬場コード	20	1	2 	2
    (20, 1, 2, 2),
    # 7		○	開催回[第N回]	22	1	2 	2
    (22, 1, 2, 2),
    # 8		○	開催日目[N日目]	24	1	2 	2
    (24, 1, 2, 2),
    # 9		○	レース番号	26	1	2 	2
    (26, 1, 2, 2),
    # 10			登録頭数	28	1	2 	2
    (28, 1, 2, 2),
    # 11			出走頭数	30	1	2 	2
    (30, 1, 2, 2),
    # 12			発売フラグ　単勝	32	1	1 	1
    (32, 1, 1, 1),
    # 13			発売フラグ　複勝	33	1	1 	1
    (33, 1, 1, 1),
    # 14			発売フラグ　枠連	34	1	1 	1
    (34, 1, 1, 1),
    # 15			発売フラグ　馬連	35	1	1 	1
    (35, 1, 1, 1),
    # 16			発売フラグ　ワイド	36	1	1 	1
    (36, 1, 1, 1),
    # 17			発売フラグ　馬単	37	1	1 	1
    (37, 1, 1, 1),
    # 18			発売フラグ　3連複	38	1	1 	1
    (38, 1, 1, 1),
    # 19			複勝着払キー	39	1	1 	1
    (39, 1, 1, 1),
    # 20			返還馬番情報(馬番01～28)	40	28	1 	28
    (40, 28, 1, 28),
    # 21			返還枠番情報(枠番1～8)	68	8	1 	8
    (68, 8, 1, 8),
    # 22			返還同枠情報(枠番1～8)	76	8	1 	8
    (76, 8, 1, 8),
    # 23			<単勝票数>	84	28	15 	420
    # 	a		　　馬番	(   1)		2
    # 	b		　　票数	(   3)		11
    # 	c		　　人気順	(  14)		2
    (84, 28, (2, 11, 2), 420),
    # 24			<複勝票数>	504	28	15 	420
    # 	a		　　馬番	(   1)		2
    # 	b		　　票数	(   3)		11
    # 	c		　　人気順	(  14)		2
    (504, 28, (2, 11, 2), 420),
    # 25			<枠連票数>	924	36	15 	540
    # 	a		　　組番	(   1)		2
    # 	b		　　票数	(   3)		11
    # 	c		　　人気順	(  14)		2
    (924, 36, (2, 11, 2), 540),
    # 26			<馬連票数>	1464	153	18 	2754
    # 	a		　　組番	(   1)		4
    # 	b		　　票数	(   5)		11
    # 	c		　　人気順	(  16)		3
    (1464, 153, (4, 11, 3), 2754),
    # 27			<ワイド票数>	4218	153	18 	2754
    # 	a		　　組番	(   1)		4
    # 	b		　　票数	(   5)		11
    # 	c		　　人気順	(  16)		3
    (4218, 153, (4, 11, 3), 2754),
    # 28			<馬単票数>	6972	306	18 	5508
    # 	a		　　組番	(   1)		4
    # 	b		　　票数	(   5)		11
    # 	c		　　人気順	(  16)		3
    (6972, 306, (4, 11, 3), 5508),
    # 29			<3連複票数>	12480	816	20 	16320
    # 	a		　　組番	(   1)		6
    # 	b		　　票数	(   7)		11
    # 	c		　　人気順	(  18)		3
    (12480, 816, (6, 11, 3), 16320),
    # 30			単勝票数合計	28800	1	11 	11
    (28800, 1, 11, 11),
    # 31			複勝票数合計	28811	1	11 	11
    (28811, 1, 11, 11),
    # 32			枠連票数合計	28822	1	11 	11
    (28822, 1, 11, 11),
    # 33			馬連票数合計	28833	1	11 	11
    (28833, 1, 11, 11),
    # 34			ワイド票数合計	28844	1	11 	11
    (28844, 1, 11, 11),
    # 35			馬単票数合計	28855	1	11 	11
    (28855, 1, 11, 11),
    # 36			3連複票数合計	28866	1	11 	11
    (28866, 1, 11, 11),
    # 37			単勝返還票数合計	28877	1	11 	11
    (28877, 1, 11, 11),
    # 38			複勝返還票数合計	28888	1	11 	11
    (28888, 1, 11, 11),
    # 39			枠連返還票数合計	28899	1	11 	11
    (28899, 1, 11, 11),
    # 40			馬連返還票数合計	28910	1	11 	11
    (28910, 1, 11, 11),
    # 41			ワイド返還票数合計	28921	1	11 	11
    (28921, 1, 11, 11),
    # 42			馬単返還票数合計	28932	1	11 	11
    (28932, 1, 11, 11),
    # 43			3連複返還票数合計	28943	1	11 	11
    (28943, 1, 11, 11),
]

H6_csv_header = [
    "record_type_id",  # レコード種別ID
    "data_category",  # データ区分
    "data_creation_date",  # データ作成年月日
    "event_year",  # 開催年
    "event_date",  # 開催月日
    "race_track_code",  # 競馬場コード
    "event_number",  # 開催回_第N回
    "event_day",  # 開催日目_N日目
    "race_number",  # レース番号
    "registered_horses",  # 登録頭数
    "starting_horses",  # 出走頭数
    "betting_flag_trifecta",  # 発売フラグ_3連単
    "return_horse_number_info",  # 返還馬番情報
    "trifecta_bets_combination_number",  # 3連単票数_組番
    "trifecta_bets_count",  # 3連単票数_票数
    "trifecta_bets_popularity_order",  # 3連単票数_人気順
    "trifecta_bets_total",  # 3連単票数合計
    "trifecta_return_bets_total",  # 3連単返還票数合計
]

H6_format = [
    # 1			レコード種別ID	1	1	2 	2
    (1, 1, 2, 2),
    # 2			データ区分	3	1	1 	1
    (3, 1, 1, 1),
    # 3			データ作成年月日	4	1	8 	8
    (4, 1, 8, 8),
    # 4		○	開催年	12	1	4 	4
    (12, 1, 4, 4),
    # 5		○	開催月日	16	1	4 	4
    (16, 1, 4, 4),
    # 6		○	競馬場コード	20	1	2 	2
    (20, 1, 2, 2),
    # 7		○	開催回[第N回]	22	1	2 	2
    (22, 1, 2, 2),
    # 8		○	開催日目[N日目]	24	1	2 	2
    (24, 1, 2, 2),
    # 9		○	レース番号	26	1	2 	2
    (26, 1, 2, 2),
    # 10			登録頭数	28	1	2 	2
    (28, 1, 2, 2),
    # 11			出走頭数	30	1	2 	2
    (30, 1, 2, 2),
    # 12			発売フラグ　3連単	32	1	1 	1
    (32, 1, 1, 1),
    # 13			返還馬番情報(馬番01～18)	33	18	1 	18
    (33, 18, 1, 18),
    # 14			<3連単票数>	51	4896	21 	102816
    # 	a		　　組番	(   1)		6
    # 	b		　　票数	(   7)		11
    # 	c		　　人気順	(  18)		4
    (51, 4896, (6, 11, 4), 102816),
    # 15			3連単票数合計	102867	1	11 	11
    (102867, 1, 11, 11),
    # 16			3連単返還票数合計	102878	1	11 	11
    (102878, 1, 11, 11),
]

record_type_id_map = {
    "H1": H1_format,
    "H6": H6_format,
}
