query = {}

query['balance'] = """select player_id, currency, amount
from
    (select id as player_id, currency, balance as amount
    from users
    union all
    select id as player_id, 'UNIT' as currency, units as amount
    from users) t WHERE player_id IN (
        SELECT user_id FROM log_balance WHERE created BETWEEN %s AND %s
    )
order by player_id, currency;"""

query['transactions'] = """SELECT user_id as player_id, currency, sum(amount) as amount, count(*) as qtty, op_type as nature
FROM
    (SELECT user_id, currency, amount,
           CASE
               WHEN op_type LIKE 'IN-%' AND status='SUCCESS' THEN 'deposit'
               WHEN op_type LIKE 'OUT-%' AND status='SUCCESS' THEN 'complete withdraw'
               WHEN op_type LIKE 'OUT-%' AND status NOT IN ('CANCELED','SUCCESS') THEN 'incomplete withdraw'
               WHEN op_type LIKE 'OUT-%' AND status='CANCELED' THEN 'refund'
            END as op_type
    FROM transactions WHERE updated_at BETWEEN %s AND %s) t
WHERE t.op_type in ('deposit','complete withdraw','incomplete withdraw','refund')
GROUP BY player_id, currency, op_type
ORDER BY player_id;
"""

query['turnover_casino'] = """SELECT player_id, 'bet' AS nature, currency, amount, count(*) AS qtty
FROM (SELECT * FROM bets_casino
WHERE inserted_at BETWEEN %s AND %s AND action = 'bet') b WHERE rollback is null or rollback = 0 GROUP BY player_id, currency

UNION ALL

SELECT player_id, 'win' AS nature, currency, amount, count(*) AS qtty
FROM (SELECT * FROM bets_casino
WHERE inserted_at BETWEEN %s AND %s AND action = 'win') b WHERE rollback is null or rollback = 0 GROUP BY player_id, currency;
"""


query['turnover_sport_old'] = """select player_id, nature, currency, amount, qtty
from
    (select player_id, 'bet' as nature,currency as currency, sum(bet_amount) as amount, count(*) as qtty
    from s_bets WHERE date_created BETWEEN %s AND %s GROUP BY player_id, currency

    union all

    select player_id, 'win' as nature, payout_currency as currency, sum(payout_amount) as amount, count(*) as qtty
    from s_bets WHERE date_paid BETWEEN %s AND %s GROUP BY player_id, payout_currency
        ) t
order by player_id, nature;
"""

query['turnover_crazy_rocket'] = """select *
from
     (select player_id, 'bet' as nature, currency, sum(amount) as amount, count(*) as qtty
    from nr_bets where action='bet' and updated_at BETWEEN %s AND %s AND (rollbacked is null or rollbacked=0)
    group by player_id

    union all

    select player_id, 'win' as nature, currency, sum(amount) as amount, count(*) as qtty
    from nr_bets where action='win' and updated_at BETWEEN %s AND %s AND (rollbacked is null or rollbacked=0)
    group by player_id) t
order by player_id, nature;
"""












query['turnover_keno'] = """SELECT acc_id AS player_id, 'bet' AS nature, currency, sum(package_sum) AS amount, count(*) AS qtty
FROM s_stakes_k
WHERE dt BETWEEN %s AND %s AND is_header=TRUE
GROUP BY acc_id, currency

UNION ALL

SELECT acc_id AS player_id, 'win' AS nature, currency, sum(payout_sum) AS amoun, count(*) AS qtty
FROM s_stakes_k
WHERE vdt BETWEEN %s AND %s AND is_header=TRUE
GROUP BY acc_id, currency;

"""





query['turnover_colorboom'] = """SELECT acc_id AS player_id, 'bet' AS nature, currency, sum(package_sum) AS amount, count(*) AS qtty
FROM s_stakes_kb
WHERE dt BETWEEN %s AND %s AND is_header=TRUE
GROUP BY acc_id, currency

UNION ALL

SELECT acc_id AS player_id, 'win' AS nature, currency, sum(payout_sum) AS amoun, count(*) AS qtty
FROM s_stakes_kb
WHERE vdt BETWEEN %s AND %s AND is_header=TRUE
GROUP BY acc_id, currency;
"""





query['turnover_wof'] = """SELECT acc_id AS player_id, 'bet' AS nature, currency, sum(package_sum) AS amount, count(*) AS qtty
FROM s_stakes_wof
WHERE dt BETWEEN %s AND %s AND is_header=TRUE
GROUP BY acc_id, currency

UNION ALL

SELECT acc_id AS player_id, 'win' AS nature, currency, sum(payout_sum) AS amoun, count(*) AS qtty
FROM s_stakes_wof
WHERE vdt BETWEEN %s AND %s AND is_header=TRUE
GROUP BY acc_id, currency;
"""




query['turnover_toto'] = """SELECT acc_id AS player_id, 'bet' AS nature, currency, sum(package_sum) AS amount, count(*) AS qtty
FROM s_stakes_toto
WHERE dt BETWEEN %s AND %s AND is_header=TRUE
GROUP BY acc_id, currency

UNION ALL

SELECT acc_id AS player_id, 'win' AS nature, currency, sum(payout_sum) AS amoun, count(*) AS qtty
FROM s_stakes_toto
WHERE vdt BETWEEN %s AND %s AND is_header=TRUE
GROUP BY acc_id, currency;
"""






query['turnover_turbo_keno'] = """SELECT acc_id AS player_id, 'bet' AS nature, currency, sum(package_sum) AS amount, count(*) AS qtty
FROM eg_keno_stakes
WHERE dt BETWEEN %s AND %s
GROUP BY acc_id, currency

UNION ALL

SELECT acc_id AS player_id, 'win' AS nature, currency, sum(payout_sum) AS amoun, count(*) AS qtty
FROM eg_keno_stakes
WHERE vdt BETWEEN %s AND %s AND ststatus=2
GROUP BY acc_id, currency;
"""






query['turnover_turbo_wof'] = """SELECT user_id AS player_id, 'bet' AS nature, currency, sum(package_sum) AS amount, count(*) AS qtty
FROM eg_wof_stakes
WHERE dt BETWEEN %s AND %s
GROUP BY user_id, currency

UNION ALL

SELECT user_id AS player_id, 'win' AS nature, currency, sum(payout_sum) AS amoun, count(*) AS qtty
FROM eg_wof_stakes
WHERE vdt BETWEEN %s AND %s AND ststatus=2
GROUP BY user_id, currency;
"""



########################################################################################################################
###################################################### S H O P S #######################################################
########################################################################################################################







