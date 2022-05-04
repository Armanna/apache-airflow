import Queries as q

import mysql.connector
import datetime as dt

def iteration_log(last_id, last_date_start, last_date_end, last_status):
    last_id += 1
    if last_status == 'success':
        last_date_start = last_date_end + dt.timedelta(seconds=1)
        last_date_end = last_date_start + dt.timedelta(minutes=59, seconds=59)

    frequency = 'hourly'
    last_status = 'pending'

    new_row = [(last_id, last_date_start, last_date_end, frequency, last_status)]

    query = "INSERT INTO iteration_log VALUES(%s,%s,%s,%s,%s)"

    cursor_1.executemany(query, new_row)
    connection_1.commit()


connection_1 = mysql.connector.connect(host='localhost',
                                     database='HABESHA',
                                     user='arman30600',
                                     password='')

cursor_1 = connection_1.cursor()

########################################################################################################################
########################################################################################################################
######################################## I T E R A T I O N    L O G ####################################################
########################################################################################################################
########################################################################################################################

cursor_1.execute("select * from iteration_log order by id desc limit 1;")
last_row = cursor_1.fetchone()

frequency = 'hourly'
status = 'pending'

if last_row is None:
    id = 0
    date_start = '2022-01-01 00:00:00'
    date_end = '2022-01-01 00:59:59'

    first_row = [(id, date_start, date_end, frequency, status)]

    query = "INSERT INTO iteration_log VALUES(%s,%s,%s,%s,%s)"

    cursor_1.executemany(query, first_row)
    connection_1.commit()
else:
    last_id = last_row[0]
    last_date_start = last_row[1]
    last_date_end = last_row[2]
    last_status = last_row[4]

    iteration_log(last_id, last_date_start, last_date_end, last_status)


cursor_1.execute("select * from iteration_log order by id desc limit 1;")
last_row = cursor_1.fetchone()

iteration_id = last_row[0]
date_start = last_row[1]
date_end = last_row[2]

cursor_1.close()
connection_1.close()




connection_0 = mysql.connector.connect(host='51.178.74.117',
                                     database='ZHABESHAETH',
                                     user='robin',
                                     password='RobPazz7755')

cursor_0 = connection_0.cursor()


########################################################################################################################
########################################################################################################################
##################################################### B A L A N C E ####################################################
########################################################################################################################
########################################################################################################################

balance = True

try:
    cursor_0.execute(q.query['balance'], [date_start, date_end])
    balance_table = cursor_0.fetchall()
    print("Everything is OK with BALANCE")
except:
    print("Something went wrong with BALANCE")
    balance = False




########################################################################################################################
########################################################################################################################
############################################# T R A N S A C T I O N S ##################################################
########################################################################################################################
########################################################################################################################

transactions = True

try:
    cursor_0.execute(q.query['transactions'], [date_start, date_end])
    transactions_table = cursor_0.fetchall()
    print("Everything is OK with TRANSACTIONS")
except:
    print("Something went wrong with TRANSACTIONS")
    transactions = False


########################################################################################################################
########################################################################################################################
###################################### T U R N O V E R    C A S I N O ##################################################
########################################################################################################################
########################################################################################################################

turnover_casino = True

try:
    cursor_0.execute(q.query['turnover_casino'], [date_start, date_end, date_start, date_end])
    turnover_casino_table = cursor_0.fetchall()
    print("Everything is OK with TURNOVER_CASINO")
except:
    print("Something went wrong with TURNOVER_CASINO")
    turnover_casino = False


print(turnover_casino_table)



########################################################################################################################
########################################################################################################################
###################################### T U R N O V E R    S P O R T    OLD #############################################
########################################################################################################################
########################################################################################################################

turnover_sport_old = True

try:
    cursor_0.execute(q.query['turnover_sport_old'], [date_start, date_end, date_start, date_end])
    turnover_sport_old_table = cursor_0.fetchall()
    print("Everything is OK with TURNOVER_SPORT_OLD")
except:
    print("Something went wrong with TURNOVER_SPORT_OLD")
    turnover_sport_old = False


'''
########################################################################################################################
########################################################################################################################
################################### T U R N O V E R    C R A Z Y    R O C K E T ########################################
########################################################################################################################
########################################################################################################################

turnover_crazy_rocket = True

try:
    cursor.execute(q.query['turnover_crazy_rocket'], [date_start, date_end, date_start, date_end])
    turnover_crazy_rocket_table = cursor.fetchall()
    print("Everything is OK with TURNOVER_CRAZY_ROCKET")
except:
    print("Something went wrong with TURNOVER_CRAZY_ROCKET")
    turnover_crazy_rocket = False
'''

########################################################################################################################
########################################################################################################################
################################### T U R N O V E R    K E N O #########################################################
########################################################################################################################
########################################################################################################################

turnover_keno = True

try:
    cursor_0.execute(q.query['turnover_keno'], [date_start, date_end, date_start, date_end])
    turnover_keno_table = cursor_0.fetchall()
    print("Everything is OK with TURNOVER_KENO")
except:
    print("Something went wrong with TURNOVER_KENO")
    turnover_keno = False



########################################################################################################################
########################################################################################################################
################################## T U R N O V E R   C O L O R B O O M #################################################
########################################################################################################################
########################################################################################################################

turnover_colorboom = True

try:
    cursor_0.execute(q.query['turnover_colorboom'], [date_start, date_end, date_start, date_end])
    turnover_colorboom_table = cursor_0.fetchall()
    print("Everything is OK with TURNOVER_COLORBOOM")
except:
    print("Something went wrong with TURNOVER_COLORBOOM")
    turnover_colorboom = False



########################################################################################################################
########################################################################################################################
########################################### T U R N O V E R   W O F ####################################################
########################################################################################################################
########################################################################################################################

turnover_wof = True

try:
    cursor_0.execute(q.query['turnover_wof'], [date_start, date_end, date_start, date_end])
    turnover_wof_table = cursor_0.fetchall()
    print("Everything is OK with TURNOVER_WOF")
except:
    print("Something went wrong with TURNOVER_WOF")
    turnover_wof = False


########################################################################################################################
########################################################################################################################
########################################### T U R N O V E R   T O T O ##################################################
########################################################################################################################
########################################################################################################################

turnover_toto = True

try:
    cursor_0.execute(q.query['turnover_toto'], [date_start, date_end, date_start, date_end])
    turnover_toto_table = cursor_0.fetchall()
    print("Everything is OK with TURNOVER_TOTO")
except:
    print("Something went wrong with TURNOVER_TOTO")
    turnover_toto = False



########################################################################################################################
########################################################################################################################
################################# T U R N O V E R   T U R B O    K E N O ###############################################
########################################################################################################################
########################################################################################################################

turnover_turbo_keno = True

try:
    cursor_0.execute(q.query['turnover_turbo_keno'], [date_start, date_end, date_start, date_end])
    turnover_turbo_keno_table = cursor_0.fetchall()
    print("Everything is OK with TURNOVER_TURBO_KENO")
except:
    print("Something went wrong with TURNOVER_TURBO_KENO")
    turnover_turbo_keno = False



########################################################################################################################
########################################################################################################################
################################# T U R N O V E R   T U R B O    W O F #################################################
########################################################################################################################
########################################################################################################################

turnover_turbo_wof = True

try:
    cursor_0.execute(q.query['turnover_turbo_wof'], [date_start, date_end, date_start, date_end])
    turnover_turbo_wof_table = cursor_0.fetchall()
    print("Everything is OK with TURNOVER_TURBO_WOF")
except:
    print("Something went wrong with TURNOVER_TURBO_WOF")
    turnover_turbo_wof = False


cursor_0.close()
connection_0.close()




connection_1 = mysql.connector.connect(host='localhost',
                                     database='HABESHA',
                                     user='arman30600',
                                     password='')

cursor_1 = connection_1.cursor()



if (balance * transactions * turnover_casino * turnover_sport_old
        * turnover_keno * turnover_colorboom * turnover_wof * turnover_toto * turnover_turbo_keno * turnover_turbo_wof) == 1:

    ########## BALANCE ##########
    result = []
    for i in balance_table:
        l = list(i)
        l.append(1)
        t = tuple(l)
        result.append(t)
    
    
    query = "INSERT INTO balance(player_id, currency, amount, iteration_id) VALUES(%s,%s,%s,%s)"
    cursor_1.executemany(query, result)
    connection_1.commit()
    
    cursor_1.close()
    connection_1.close()


    
