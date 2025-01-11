from _pydatetime import timedelta
from decimal import Decimal, ROUND_HALF_UP
from time import strftime

import psycopg2
from psycopg2 import sql
from psycopg2._psycopg import cursor
import instr
import psycopg2
import sqlite3
import datetime
from datetime import datetime
from psycopg2 import sql
import calendar
from dateutil.relativedelta import relativedelta

con = psycopg2.connect("dbname=RushTest host=localhost  user=user password=password port=5432")
cur = con.cursor()

insertQuery = None
trans_SF_otherinstr1 = None
trans_SF_otherinstr2 = None

external_swp = 0
external_cusip = 0
dates = None
vltn_dt = None
SF_BMV = 0
SF_EMV = 0
ext_ref_num = None
valuation_date = None
product_ref = None
product_ref_type = None
product_ref_trans = None
product_ref_type_trans = None
product_ref_trans1 = None
product_ref_type_trans1 = None
product_ref_trans2 = None
product_ref_type_trans2 = None
bmv1 = 0
emv1 = 0
q = "'"
txn_amt = 0
txn_amt1 = 0
txn_amt2 = 0
txn_amt_flag1 = 0
txn_amt_flag2 = 0
SF_txn_amt = 0
SF_txn_amt1 = 0
SF_txn_amt2 = 0
trade_date = None
trade_date1 = None
trade_date2 = None
total_inflow = 0
total_outflow = 0
cal_contribution = 0
cal_withdrawal = 0
cal_income = 0
cal_distribution = 0
cal_netfees = 0
previous_inflow = 0
previous_outflow = 0
total_flowin = 0
total_flowout = 0
total_flowin1 = 0
total_flowout1 = 0
inflow_SF = 0
outflow_SF = 0
cal_netfees1 = 0
cal_netfees2 = 0
vltn_set = []

int_ref_numarr = ["12062024"]

for n in int_ref_numarr:
    int_ref_num = n
    delete_IF_VAL = "delete from test_if_capital_valuation where ext_ref_num = '" + int_ref_num + "'"
    delete_IF_trnas = "delete from test_if_capital_transactions where ext_ref_num = '" + int_ref_num + "'"
    cur.execute(delete_IF_VAL)
    cur.execute(delete_IF_trnas)
    cusip9 = "select * from if_capital_valuation where ext_ref_num ='" + int_ref_num + ("' and instrmnt_id in ("
                                                                                            "'9999SWP','9999CSH') order "
                                                                                            "by vltn_dt")
    cur.execute(cusip9)
    cusip9_res = cur.fetchone()
    vltn_set = []
    while cusip9_res:
        dates = cusip9_res[2]
        if dates in vltn_set:
            pass
        else:
            vltn_set.append(dates)
        break

    val_dump = "insert into test_if_capital_valuation select * from if_capital_valuation where ext_ref_num ='" +int_ref_num+ "' and instrmnt_id  not in ('9999SWPSF')"
    trans_dump = "insert into test_if_capital_transactions select * from if_capital_transactions where ext_ref_num ='" +int_ref_num+ "' and instrmnt_id not in ('9999SWPSF')"

    cur.execute(val_dump)
    cur.execute(trans_dump)
    con.commit()

    for i in vltn_set:
        vltn_dt = i

        val_SF = "select * from if_capital_valuation where ext_ref_num ='" + int_ref_num + "' and vltn_dt = '" + str(vltn_dt) + "' and instrmnt_id in ('9999SWP','9999CSH') order by vltn_dt"
        cur.execute(val_SF)
        Val_res = cur.fetchone()

        while Val_res:
            ext_ref_num = Val_res[1]
            valuation_date = Val_res[2]
            product_ref = Val_res[4]
            product_ref_type = Val_res[5]
            instrmntId = Val_res[3]
            ext_ref_num = q + ext_ref_num + q
            valuation_date = q + str(valuation_date) + q
            product_ref = q + product_ref + q
            product_ref_type = q + product_ref_type + q
            bmv1 = Val_res[8]
            emv1 = Val_res[7]
            if instrmntId == '9999CSH':
                bmv1 = bmv1 * -1
                emv1 = emv1 * -1
                break


            SF_BMV = SF_BMV + bmv1
            SF_EMV = SF_EMV + emv1

        if ext_ref_num is not None:
            insertQuery = (("INSERT INTO test_if_capital_valuation(ext_client_id, ext_ref_num, vltn_dt, instrmnt_id, "
                               "product_ref, prod_ref_type, portfolio_reference, emv, bmv) values (null, ") + ext_ref_num
                               + ", " + str(valuation_date) + ", '9999SWPSF', " + product_ref + ", " + product_ref_type +
                               ", null, " + str(SF_EMV) + ", " + str(SF_BMV) + ")")
            cur.execute(insertQuery)
            con.commit()
            notnullupt1 = None
            notnullflow1 = None
            notnullcash1 = None
            notnullfee1 = None
            flow_flag = None
            cash_sensitive_flag = None
            upd_mv_flag = None
            fee_flag = None
            flow_flag3 = None
            cash_sensitive_flag3 = None
            upd_mv_flag3 = None
            fee_flag3 = None
            stlmnt_date = None
            trans_SF = "select trade_dt,updt_mv_flg, cash_sensitive_txn_flg,flow_flg,fee_flg,stlmnt_dt, COUNT(*) from if_capital_transactions where ext_ref_num ='" + int_ref_num + "' and trade_dt = '" + str(vltn_dt) + "'  and instrmnt_id in ('9999SWP','9999CSH') GROUP BY trade_dt,updt_mv_flg, cash_sensitive_txn_flg,flow_flg,fee_flg,stlmnt_dt HAVING COUNT(*) >= 1 order by trade_dt"
            trans_SF1 = "select trade_dt,updt_mv_flg, cash_sensitive_txn_flg,flow_flg,fee_flg,stlmnt_dt, COUNT(*) from if_capital_transactions where ext_ref_num ='" + int_ref_num + "' and trade_dt = '" + str(vltn_dt) + "'  and instrmnt_id not in ('9999SWP','9999CSH','9999SWPSF') GROUP BY trade_dt,updt_mv_flg, cash_sensitive_txn_flg,flow_flg,fee_flg,stlmnt_dt HAVING COUNT(*) >= 1 order by trade_dt"
            cur.execute(trans_SF)
            trans_res = cur.fetchone()

        while trans_res:
            flow_flag = trans_res[3]
            cash_sensitive_flag = trans_res[2]
            upd_mv_flag = trans_res[1]
            fee_flag = trans_res[4]
            stlmnt_date = trans_res[5]
            if upd_mv_flag is not None:
                notnullupt1 = "in (" + str(upd_mv_flag) + ")"
            else:
                    notnullupt1 = "is null"

            if flow_flag is not None:
                notnullflow1 = "in (" + str(flow_flag) + ")"
            else:
                notnullflow1 = "is null"

            if cash_sensitive_flag is not None:
                notnullcash1 = "in (" + str(cash_sensitive_flag) + ")"
            else:
                notnullcash1 = "is null"

            if fee_flag is not None:
                notnullfee1 = "in (" + str(fee_flag) + ")"
            else:
                notnullfee1 = "is null"

            trans_SF2 = None
            if stlmnt_date is not None:
                trans_SF2 = "select * from if_capital_transactions where ext_ref_num ='" + int_ref_num + ("' and "
                                                                                                              "trade_dt = "
                                                                                                              "'") + str(
                    vltn_dt) + "' and stlmnt_dt = '" + str(stlmnt_date) + ("'  and instrmnt_id   in ('9999SWP','9999CSH') "
                                                                          "and updt_mv_flg ") + notnullupt1 +(" and "
                                                                                                              "cash_sensitive_txn_flg ") + notnullcash1 + " and flow_flg " + notnullflow1 + " and fee_flg " + notnullfee1 + ""
            else:
                trans_SF2 = "select * from if_capital_transactions where ext_ref_num ='" + int_ref_num + ("' and "
                                                                                                              "trade_dt = "
                                                                                                              "'") + str(
                        vltn_dt) + "' and stlmnt_dt is " + stlmnt_date + ("  and instrmnt_id  in ('9999SWP','9999CSH') and "
                                                                          "updt_mv_flg  ") + notnullupt1 +(" and "
                                                                                                           "cash_sensitive_txn_flg  ") + notnullcash1 + " and  flow_flg  " + notnullflow1 + " and fee_flg  " + notnullfee1 + ""

            cur.execute(trans_SF2)
            trans_res2 = cur.fetchone()
            while trans_res2:
                trans_amt = 0

                flow_flag3 = trans_res2[13]
                cash_sensitive_flag3 = trans_res2[10]
                upd_mv_flag3 = trans_res2[9]
                fee_flag3 = trans_res2[11]
                if upd_mv_flag3 is not None or cash_sensitive_flag3 is not None or flow_flag3 is not None or fee_flag3 is not None:
                    trans_amt = trans_res2[8]
                    trade_date1 = trans_res2[2]
                    settlement_date1 = trans_res2[27]
                    product_ref_trans1 = trans_res2[4]
                    product_ref_type_trans1 = trans_res2[5]
                    trade_date1 = q + str(trade_date1) + q
                settlement_date1 = trans_res2[27]
                if settlement_date1 is None:
                    pass
                else:
                    settlement_date1 = q + str(settlement_date1) + q
                    product_ref_trans1 = q + str(trans_res2[4]) + q
                    product_ref_type_trans1 = q + str(trans_res2[5]) + q
                    txn_amt1 = txn_amt1 + trans_res2[8]
                if upd_mv_flag is not None or cash_sensitive_flag is not None or flow_flag is not None or fee_flag is not None:
                    trans_SFF1 = "INSERT INTO test_if_capital_transactions(ext_client_id, ext_ref_num, trade_dt, instrmnt_id, product_ref, prod_ref_type, txn_pos_id, txn_pos_type, portfolio_reference, transaction_amt, updt_mv_flg, cash_sensitive_txn_flg, fee_flg, cr_dr_flg, flow_flg,stlmnt_dt) VALUES (null, " + ext_ref_num + ", " + str(trade_date1) + ", '9999SWPSF', " + product_ref_trans1 + ", " + product_ref_type_trans1 + ", 0, 'bancs', 'bancsp1', " + str(txn_amt1) + ", " + upd_mv_flag + ", " + cash_sensitive_flag + ", " + fee_flag + ", null, " + flow_flag + "," + str(settlement_date1) + ")"
                    cur.execute(trans_SFF1)
                    cur.commit()
                break
            break

        flow_flag = None
        cash_sensitive_flag = None
        upd_mv_flag = None
        fee_flag = None
        flow_flag3 = None
        cash_sensitive_flag3 = None
        upd_mv_flag3 = None
        fee_flag3 = None
        txn_amt1 = 0

        flow_flag2 = None
        cash_sensitive_flag2 = None
        upd_mv_flag2 = None
        fee_flag2 = None
        flow_flag4 = None
        cash_sensitive_flag4 = None
        upd_mv_flag4 = None
        fee_flag4 = None
        stlmnt_date2 = None
        cur.execute(trans_SF1)
        trans_res1 = cur.fetchone()
        notnullupt = None
        notnullflow = None
        notnullcash = None
        notnullfee = None
        while trans_res1:
            flow_flag2 = trans_res1[3]
            cash_sensitive_flag2 = trans_res1[2]
            upd_mv_flag2 = trans_res1[1]
            fee_flag2 = trans_res1[4]
            stlmnt_date2 = trans_res1[5]
            if upd_mv_flag2 is not None:
                notnullupt = "in (" + str(upd_mv_flag2) + ")"
            else:
                notnullupt = "is null"

            if flow_flag2 is not None:
                notnullflow = "in (" + str(flow_flag2) + ")"
            else:
                notnullflow = "is null"

            if cash_sensitive_flag2 is not None:
                notnullcash = "in (" + str(cash_sensitive_flag2) + ")"
            else:
                notnullcash = "is null"

            if fee_flag2 is not None:
                notnullfee = "in (" + str(fee_flag2) + ")"
            else:
                notnullfee = "is null"

            trans_SF3 = None
            if stlmnt_date2 is not None:
                trans_SF3 = "select * from if_capital_transactions where ext_ref_num ='" + int_ref_num + "' and trade_dt = '" + str(vltn_dt) + "' and stlmnt_dt = '" + str(stlmnt_date2) + "'  and instrmnt_id  not in ('9999SWP','9999CSH','9999SWPSF') and updt_mv_flg " + notnullupt + " and cash_sensitive_txn_flg " + notnullcash + " and flow_flg " + notnullflow + " and fee_flg " + notnullfee + ""
            else:
                trans_SF3 = "select * from if_capital_transactions where ext_ref_num ='" + int_ref_num + "' and trade_dt = '" + str(vltn_dt) + "' and stlmnt_dt is " + str(stlmnt_date2) + "  and instrmnt_id  not in ('9999SWP','9999CSH','9999SWPSF') and updt_mv_flg  " + notnullupt + " and cash_sensitive_txn_flg  " + notnullcash + " and  flow_flg  " + notnullflow + " and fee_flg  " + notnullfee + ""

            cur.execute(trans_SF3)
            trans_res3 = cur.fetchone()
            while trans_res3:
                trans_amt2 = 0
                flow_flag4 = trans_res3[13]
                cash_sensitive_flag4 = trans_res3[10]
                upd_mv_flag4 = trans_res3[9]
                fee_flag4 = trans_res3[11]
                settlement_date2 = trans_res3[27]
                if upd_mv_flag4 is not None or cash_sensitive_flag4 is not None or flow_flag4 is not None or fee_flag4 is not None:
                    trans_amt2 = trans_res3[8]
                    trade_date2 = trans_res3[2]
                    settlement_date2 = trans_res3[27]
                    product_ref_trans2 = trans_res3[4]
                    product_ref_type_trans2 = trans_res3[5]

                    trade_date2 = q + str(trade_date2) + q
                if settlement_date2 is None:
                    pass
                else:
                    settlement_date2 = q + str(settlement_date2) + q

                    product_ref_trans2 = q + product_ref_trans2 + q
                    product_ref_type_trans2 = q + product_ref_type_trans2 + q
                    txn_amt2 = txn_amt2 + trans_amt2

                if flow_flag4 is not None:
                    if flow_flag4 == "1":
                        flow_flag4 = "2"
                    elif flow_flag4 == '2':
                        flow_flag4 = '1'

                if cash_sensitive_flag4 is not None:
                    if cash_sensitive_flag4 == "1":
                        cash_sensitive_flag4 = "2"
                    elif cash_sensitive_flag4 == "2":
                        cash_sensitive_flag4 = "1"

                if fee_flag4 is not None:
                    if fee_flag4 == "1":
                        fee_flag4 = "2"
                    elif fee_flag4 == "2":
                        fee_flag4 = "1"

                if upd_mv_flag4 is not None:
                    upd_mv_flag4 = None

                if upd_mv_flag4 is not None or cash_sensitive_flag4 is not None or flow_flag4 is not None or fee_flag4 is not None:
                    trans_SFF1 = "INSERT INTO test_if_capital_transactions(ext_client_id, ext_ref_num, trade_dt, instrmnt_id, product_ref, prod_ref_type, txn_pos_id, txn_pos_type, portfolio_reference, transaction_amt, updt_mv_flg, cash_sensitive_txn_flg, fee_flg, cr_dr_flg, flow_flg,stlmnt_dt) VALUES (null, "+str(ext_ref_num)+", "+str(trade_date2)+", '9999SWPSF', "+str(product_ref_trans2)+", "+str(product_ref_type_trans2)+", 0, 'bancs', 'bancsp1', "+str(txn_amt2)+", null, "+str(cash_sensitive_flag4)+", "+str(fee_flag4)+", null, "+str(flow_flag4)+","+str(settlement_date2)+")"
                    cur.execute(trans_SFF1)
                    con.commit()
                break
            break




    flow_flag2 = None
    cash_sensitive_flag2 = None
    upd_mv_flag2 = None
    fee_flag2 = None
    flow_flag4 = None
    cash_sensitive_flag4 = None
    upd_mv_flag4 = None
    fee_flag4 = None
    txn_amt2 = 0

    SF_BMV = 0
    SF_EMV = 0
    bmv1 = 0
    emv1 = 0
    txn_amt1 = 0
    trans_date = None
    dates2 = None
    instrmnts2 = None
    insertQuery2 = None
    missing_val = "select * from if_capital_transactions where ext_ref_num ='"+int_ref_num+"' order by trade_dt"
    cur.execute(missing_val)
    missing_val_res = cur.fetchone()
    trans_set = []
    while missing_val_res:
        dates1 = missing_val_res[2]
        if dates1 in trans_set:
            pass
        else:
            trans_set.append(dates1)
        break

    for k in trans_set:
        trans_date = k
        transaction_pos = "select distinct(instrmnt_id) from if_capital_transactions where ext_ref_num ='" + int_ref_num + "' and trade_dt = '" + str(trans_date) + "' "
        cur.execute(transaction_pos)
        transaction_pos1 = cur.fetchone()
        while transaction_pos1:
            instrmnts2 = transaction_pos1[0]
            if not instrmnts2 == "9999CSH":
                val_pos = "select * from if_capital_valuation where ext_ref_num ='" + int_ref_num + "' and vltn_dt = '" + str(trans_date) + "' and instrmnt_id = '" + instrmnts2 + "'"
                cur.execute(val_pos)
                val_pos1 = cur.fetchone()
            if val_pos1:
                pass
            else:
                insertQuery2 = "INSERT INTO test_if_capital_valuation(ext_client_id, ext_ref_num, vltn_dt, instrmnt_id, product_ref, prod_ref_type, portfolio_reference, emv, bmv) values (null, " + int_ref_num + ", '" + str(trans_date) + "',  '" + instrmnts2 + "', '" + instrmnts2 + "','TICK', null, 0, 0)"
                cur.execute(insertQuery2)
                cur.commit()
                break
            break
        break
print("completed : " + int_ref_num)

con.close()
