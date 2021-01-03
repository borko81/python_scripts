# ИМПОРТИРАТ СЕ МОДУЛИТЕ ЗА РАБОТА
import csv
import fdb
import os
from collections import defaultdict

# ПЪТ ДО БАЗАТА
FILE = 'info_reserve.csv'

# ПАРАМЕТРИ НА БАЗАТА
path_to_database = {
    'host': 'localhost',
    'database': r'path_to_base',
    'user': 'username',
    'password': 'password'
}

# ОЧАКВАНИ ДАННИ СА ВЪВ ФОРМАТ:
'''
Номер на резерация;Дата на приситгане;Брой нощувки;Стая-номер;договор име
3305;30.11.2019;1;09;1;150
3305;30.11.2019;1;09;1;150
3306;1.12.2019;5;08;3;100
'''


def con_to_fb_database(query):
    ''' ВРЪЗКА С БАЗАТА '''
    con = fdb.connect(host=path_to_database['host'], database=path_to_database['database'],
                      user=path_to_database['user'], password=path_to_database['password'])
    cur = con.cursor()
    cur.execute(query)
    con.commit()


class Read_File_With_Res:

    result = defaultdict(list)

    def try_to_read_data(self):
        ''' ЧЕТЕ СЕ ФАИЛА '''
        with open(FILE, 'r') as f:
            csv_data = csv.reader(f, delimiter=';')
            for line in csv_data:
                Read_File_With_Res.result[line[0]].append(line[1:])
        return Read_File_With_Res.result

    def return_result(self):
        '''ВРЪЩА ГЕНЕРАТОР НА ПРОЧЕТЕНОТО ЗА ДА НЕ ИЗПУШИ ПАМЕТТА '''
        for line in self.try_to_read_data().items():
            yield line


def insert_data(data):
    query = '''
            execute block as
            declare variable R_ID integer;
            declare variable N_ID integer;
            declare variable MY_OPR_ID integer;
            declare variable GUEST_COUNT integer;
            declare variable ROOM_ID_GET integer;
            declare variable opr_id integer;
            declare variable smetka_nomer integer;
            declare variable mydepozit_id integer;
            begin
            GUEST_COUNT = '{counter_guest}';
            insert into opr (opr.opr_tip_id , opr.user_id, opr.pc_id) values (10, 1, 1)
            returning opr.id into :opr_id;
            insert into smetka (smetka.opr_id, smetka.suma, smetka.dds_id, smetka.num, smetka.dds_suma) values (:opr_id, '{depozit}', 3, 1, '{dep_float}')
            returning smetka.id into :smetka_nomer;
            insert into depozit (depozit.opr_id, depozit.dogovor_id, depozit.active_for) values (:opr_id, '{dogovor_id}', 1)
            returning depozit.id into :mydepozit_id;
            insert into payment_el (payment_el.smetka_id, payment_el.suma, payment_el.pay_tip_id, payment_el.val_id, payment_el.suma_val, payment_el.kurs_id, payment_el.deposit_id)
            values (:smetka_nomer, '{depozit}', 1, 1, '{depozit}', 1, :mydepozit_id);
            insert into reserve (reserve.flag_titul, reserve.ref_no) values(0, '{ref_n}')
            RETURNING reserve.id INTO :R_ID;
            while ( GUEST_COUNT > 0 ) do begin
                INSERT INTO nast (nast.room_id, nast.check_in_date, nast.days, nast.reserve_id, nast.last_opr_type, nast.dogovor_id, nast.depozit_id)
                VALUES((select rooms.id from rooms where rooms.name = '{room}'), '{date}', '{days}', :R_ID, 1, '{dogovor_id}', :mydepozit_id)
                returning nast.id into :N_ID;
                GUEST_COUNT = GUEST_COUNT - 1;
                insert into active_nast_reserve (active_nast_reserve.nast_id) values(:N_ID);
                insert into OPR  (OPR_TIP_ID, USER_ID, PC_ID) VALUES (1, 1,2)
                returning opr.id into :MY_OPR_ID;
                insert into RESERVE_HIST (RESERVE_ID, OPR_ID,NAST_ID) VALUES(:R_ID, :MY_OPR_ID, :N_ID);
            end
            end
    '''.format(**data)
    con_to_fb_database(query)


def insert_data_without_draws(data):
    query = '''
            execute block as
            declare variable R_ID integer;
            declare variable N_ID integer;
            declare variable MY_OPR_ID integer;
            declare variable GUEST_COUNT integer;
            declare variable ROOM_ID_GET integer;
            declare variable opr_id integer;
            declare variable smetka_nomer integer;
            declare variable mydepozit_id integer;
            begin
            GUEST_COUNT = '{counter_guest}';
            insert into reserve (reserve.flag_titul, reserve.ref_no) values(0, '{ref_n}')
            RETURNING reserve.id INTO :R_ID;
            while ( GUEST_COUNT > 0 ) do begin
                INSERT INTO nast (nast.room_id, nast.check_in_date, nast.days, nast.reserve_id, nast.last_opr_type, nast.dogovor_id, nast.depozit_id)
                VALUES((select rooms.id from rooms where rooms.name = '{room}'), '{date}', '{days}', :R_ID, 1, '{dogovor_id}', :mydepozit_id)
                returning nast.id into :N_ID;
                GUEST_COUNT = GUEST_COUNT - 1;
                insert into active_nast_reserve (active_nast_reserve.nast_id) values(:N_ID);
                insert into OPR  (OPR_TIP_ID, USER_ID, PC_ID) VALUES (1, 1,2)
                returning opr.id into :MY_OPR_ID;
                insert into RESERVE_HIST (RESERVE_ID, OPR_ID,NAST_ID) VALUES(:R_ID, :MY_OPR_ID, :N_ID);
            end
            end
    '''.format(**data)
    con_to_fb_database(query)


def return_to_database():
    forma = {}
    for line in test.return_result():
        # НОМЕР НА РЕЗЕРАЦИЯТА ВПИСВА СЕ В РЕФЕРЕНТЕН НОМЕР ПРИ НАС
        forma['ref_n'] = line[0]
        # НОМЕР НА СТАЯ ПРОВЕРЯВАМ ДАЛИ ТОЗИ НОМЕР ГО ИМА ПРИ НАС И СЕ ЗАПИВА ИД-ТО
        forma['room'] = line[1][0][2]
        # ДАТА НА ПРИСТИГАНЕ
        forma['date'] = line[1][0][0]
        # БРОЙ ДНИ НА ПОСЕЩЕНИЕ
        forma['days'] = line[1][0][1]
        # ДОГООВОР НОМЕР / АКО НЯМАМЕ ИД-ТАТА НА ДОГОВОРИТЕ СЕ ПРАВИ ЕКСЕЛКСИ ЗАПИС
        # =VLOOKUP("*"&A1&"*";$I$1:J2360;2;FALSE)
        forma['dogovor_id'] = line[1][0][3]
        # БРОИ НА ГОСТИТЕ. ЩЕ Е ЯКО АКО СЕ ВПИШЕ САМО ПО ЕДИН, НО НЕ СТАВА
        forma['counter_guest'] = len(line[1])
        try:
            ''' ПРОВЕРКАТА Е ДАЛИ ИМА ПОДАДЕНА СУМА ЗА ДЕПОЗИТ '''
            forma['depozit'] = float(line[1][0][4])
            forma['dep_float'] = float(line[1][0][4]) - (float(line[1][0][4]) / 1.09)
            insert_data(forma)
        except IndexError:
            ''' АКО НЯМА СЕ ИЗПЪЛНЯВА ПОДОБНА ЗАЯВКА НО С ИЗКЛЮЧЕНИ РЕДОВЕ НЕЗНАЯ КАК ДА ГО ОПРАВЯ 2 ЕДИН РЕД '''
            insert_data_without_draws(forma)


if __name__ == '__main__':
    test = Read_File_With_Res()
    return_to_database()
