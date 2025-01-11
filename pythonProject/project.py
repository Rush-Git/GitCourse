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
#from dateutil import parser
con = psycopg2.connect("dbname=RushTest host=localhost  user=user password=password port=5432")
cur = con.cursor()
#connection = psycopg2.connect(user="user",
                              #password="password",
                              #host="localhost",
                              #port="5432",
                              #database="RushTest")
#cursor = connection.cursor()
#cursor.execute("select current_database()")
#db_name = cursor.fetchone()[0]
#Query = "select * from pg_catalog.pg_tables where schemaname='public'"
#cursor.execute(Query)
#records = cursor.fetchall()
#print(records)

cal_clientId = ""
cal_ext_ref_num = ""

cal_instrmnt_id = ""

cal_product_ref_type = ""

cal_product_ref = ""

tnx_amt = 0

vltndt = None

cal_netflow = 0

total_inflow = 0

total_outflow = 0

cal_contribution = 0

cal_withdrawal = 0

cal_income = 0

cal_distribution = 0

cal_netfees = 0

cal_bmv = 0

cal_emv = 0

Mtd_contribution = 0

Mtd_withdrawal = 0

mtd_income = 0

mtd_distribution = 0

mtd_net_fees = 0

mtd_net_flow = 0

Mtd_contribution_1 = 0

Mtd_withdrawal_1 = 0

mtd_income_1 = 0

mtd_distribution_1 = 0

mtd_net_fees_1 = 0

mtd_net_flow_1 = 0

vltn_currentValue = None

periodic_bmv_date = None

periodic_Emv_date = None

#old_inc_date = 0

new_inc_date1 = None

new_inc_date = None

stamp_inc_date = None

accntdtls_inc_date1 = None

Periodic_Bmv = 0

Periodic_Emv = 0

isEmptyval = True

isEmptytrans = True

Data_Present_for_month = False

#int_ref_num = 0

int_refr = None

query3 = None

query4 = None
query5 = None

mtd_inflow = 0

mtd_outflow = 0

mtd_inflow1 = 0

mtd_outflow1 = 0

tnx_amt1 = 0

total_inflow1 = 0

total_outflow1 = 0

inflow = 0

outflow = 0
#old_inc = 0
new_inc = 0
new_inc1 = 0
accntdtls_inc_dt = None
accntdtls_inc = None

isoformat = None
quote = "'"
quote1 = "'"
rss = None

accounts = []
instruments1 = []
vltn_set = []

int_ref_numarr = ["12062024"]


def timetuple(toDateStr):
    pass


for n in int_ref_numarr:
    int_ref_num = n
    delete_daily_pos = "delete from test1_pp_daily_pos_attributes where int_ref_num = '" + int_ref_num + "'"
    cur.execute(delete_daily_pos)
    #q1 = cur.fetchone()

    old_inc_dt = "select * from pp_daily_pos_attributes where int_ref_num = '" + int_ref_num + "'"
    cur.execute(old_inc_dt)
    old_inc = cur.fetchone()
    print(old_inc)

    while old_inc:
        #inception_dt = "inception_date"
        old_inc_date = old_inc[3] #println('max_date---' + max_date)
        break

    if old_inc_date is None:
        new_inc_dt = "select *  from if_capital_valuation where ext_ref_num = '" + str(
            int_ref_num) + "' order by vltn_dt"
        cur.execute(new_inc_dt)
        new_inc = cur.fetchone()
        print(new_inc)

        while new_inc:
            new_inc_date = new_inc[2]
            stamp_inc_date = new_inc_date
            break

    else:
        new_inc_dt1 = "select * from if_capital_valuation where ext_ref_num = '" + str(int_ref_num) + "' order by vltn_dt"
        accntdtls_inc_dt = "select * from account_dtls where int_ref_num = '" + str(int_ref_num) + "'"
        cur.execute(new_inc_dt1)
        new_inc1 = cur.fetchone()
        print(new_inc1)

        while new_inc1:
            new_inc_date1 = new_inc1[2]  # println('max_date---' + max_date)
            break

    #datetime.datetime.now().isoformat()
    d1 = new_inc_date1
    d2 = old_inc_date

    if d1 < d2:
        stamp_inc_date = new_inc_date1

    else:
        #print("new minimum valuation is " + new_inc_date1)
        cur.execute(accntdtls_inc_dt)
        accntdtls_inc = cur.fetchone()
        print(accntdtls_inc)

        while accntdtls_inc:
            accntdtls_inc_date1 = accntdtls_inc[2]  #println('max_date---' + max_date)
            break

    #print("new inception date is " + accntdtls_inc_date1)
    if new_inc_date1 == accntdtls_inc_date1:
        stamp_inc_date = new_inc_date1
    else:
        stamp_inc_date = old_inc_date

    stamp_inc_date = quote + str(stamp_inc_date) + quote1
    #println("stamped inc date : " +stamp_inc_date )

    #println(delete_daily_pos);
    #println(delete_periodic_pos);

    sql_1 = "select max(vltn_dt) from if_capital_valuation where ext_ref_num = '" + int_ref_num + "'"
    cur.execute(sql_1)
    rss = cur.fetchone()

    if rss is not None:
        max_date = rss[0]  #println('max_date---' + max_date)

    sql_2 = "select * from if_capital_valuation where ext_ref_num ='" + int_ref_num + "' order by vltn_dt"
    cur.execute(sql_2)
    rs1s = cur.fetchone()
    while rs1s:
        inception_dt = rs1s[2]
        #inception_dt = inception_date.replace('-', '')
        #System.out.println("inception_date---  " + inception_dt);
        break

    start_date = inception_dt
    end_date = max_date

    max_date_1 = end_date
    start_date1 = start_date
    #System.out.println("end date is " + max_date_1);
    #System.out.println("start date is " + start_date1);

    fromDateStr = start_date1
    toDateStr = max_date_1

    c = max_date
    try:
        c = max_date
    except ValueError as e:
        print("Error parsing date: {e}")

    max_date_2 = c
                  #strftime('%Y-%m-%d'))

    #c.set(Calendar.DAY_OF_MONTH, getActualMaximum(Calendar.DATE));
    #c.set(sdf.parse(Calendar.DAY_OF_MONTH, c.getActualMaximum(Calendar.DAY_OF_MONTH)));

    #min_day = '1'
    #res = max_date_2.replace('20', min_day)

    res = max_date_2.replace(day=1)
    MTD_BMV_Date = res
    #System.out.println(MTD_BMV_Date);
    MTD_BMV = MTD_BMV_Date
    fromDate = fromDateStr
    toDate = toDateStr
    currentmonth2 = fromDateStr

    currentMonth3 = (currentmonth2.year, currentmonth2.month)
    currentMonth = fromDate

    # Print the Year and Month
    #print(f"Year and Month from currentmonth2: {year_month_current_month2}")
    #print(f"Year and Month from fromDate: {year_month_from_date}")

    # Date Formatting (similar to DateTimeFormatter in Java)
    formatter = "%Y-%m-%d"
    formatted_currentmonth2 = currentmonth2.strftime(formatter)
    formatted_fromDate = fromDate.strftime(formatter)

    #currentMonth = fromDate.strftime('%Y-%m-%d')


    #print(f"Formatted currentmonth2: {formatted_currentmonth2}")
    #print(f"Formatted fromDate: {formatted_fromDate}")
    #currentMonth = strftime('currentMonthh')
    while currentMonth <= toDate:
        #Initialize xy variable
        xy = None

        # Check if currentMonth equals currentMonth3
        if currentMonth == currentMonth3:
            monthStart = currentmonth2
        else:
            monthStart = currentMonth.replace(day=1)

        # Format monthStart using the formatter pattern
        xy = monthStart.strftime(formatter)

        # Print or use the formatted date
        print(f"Formatted monthStart: {xy}")

        # Move to the next month
        if currentMonth.month == 12:
            currentMonth = currentMonth.replace(year=currentMonth.year + 1, month=1)
        else:
            currentMonth = currentMonth.replace(month=currentMonth.month + 1)

        monthEnd = None
        yx = MTD_BMV.strftime(formatter)

        currentMonthDateTime = datetime.combine(currentMonth, datetime.min.time())

        if xy != yx:
            # Find the last day of the current month
            first_day_of_next_month = (currentMonthDateTime + relativedelta(months=1)).replace(day=1)
            monthEnd = first_day_of_next_month - relativedelta(days=1)
            #monthEnd = ((currentMonth + relativedelta(months=1)) - timedelta(days=1))
        else:
            # Same logic applied here; can be adjusted as needed
            first_day_of_next_month = (currentMonthDateTime + relativedelta(months=1)).replace(day=1)
            monthEnd = first_day_of_next_month - relativedelta(days=1)
            #monthEnd = ((currentMonth + relativedelta(day=1, months=1)).month - timedelta(days=1))


        # Format monthEnd using the formatter pattern
        xyz = monthEnd.strftime(formatter)

        # Print the start and end dates of the current month
        print(f"Month: {currentMonth.strftime('%B %Y')}")
        print(f"End Date: {monthEnd.strftime(formatter)}")

        # Example quote usage
        quote = '"'
        monthEndDate = f"{quote}{xyz}{quote}"
        print(f"Formatted Month End Date: {monthEndDate}")

        # Move to the next month (if needed)
        currentMonth = (currentMonth + relativedelta(months=1)).replace(day=1)

        sql = "select * from if_capital_valuation where ext_ref_num = '" + int_ref_num + "' and vltn_dt >='" + str(monthStart) + "' and vltn_dt <='" + str(monthEnd) + "' order by vltn_dt,instrmnt_id"
        cur.execute(sql)
        rs1 = cur.fetchone()

        vltn_set = []

        Data_Present_for_month = False

        while rs1:
            #String account = rs1.getString("ext_ref_num");
            #String instrument = rs1.getString("instrmnt_id");
            vltn_dt = rs1[2]
            Data_Present_for_month = True

            if vltn_dt in vltn_set:
                pass
            else:
                vltn_set.append(vltn_dt)
        #accounts.append("Account1")
        #instruments.append("Instrument1")
        #vltn_set.append("VLTN1")
                break

insertQuery = None

accnt = int_ref_num
for k in vltn_set:
    vltn_Value = k
    vltn_currentValue = quote + str(vltn_Value) + quote

sql2 = "select * from if_capital_valuation where ext_ref_num = '" + int_ref_num + "' and vltn_dt ='" + str(vltn_currentValue) + "' order by vltn_dt,instrmnt_id"
instruments1 = ()
cur.execute(sql2)
rs2 = cur.fetchone()

instruments1 = []
while rs2:
    instrument1 = rs2[3]
    if instrument1 in instruments1:
        pass
    else:
        instruments1.append(instrument1)

    if "9999SWPSF" in instrument1:
        instrument1.replace("9999CSH", '')
        instrument1.replace("9999SWP", '')
        #instrument1.replace("MRGINSF")
    break

q = 0
Mtd_contribution = 0
Mtd_withdrawal = 0
mtd_income = 0
mtd_distribution = 0
mtd_net_fees = 0
mtd_net_flow = 0
Mtd_contribution_1 = 0
Mtd_withdrawal_1 = 0
mtd_income_1 = 0
mtd_distribution_1 = 0
mtd_net_fees_1 = 0
mtd_net_flow_1 = 0
mtd_inflow1 = 0
mtd_outflow1 = 0

for m in instruments1:
    iinstrmnt_id1 = m

    if iinstrmnt_id1 == '9999SWPSF':
        old_inc_dt = "select *  from pp_daily_pos_attributes where int_ref_num = '" +int_ref_num  +"' and int_instrmnt_id = '9999SWP'  limit 1"
    else:
        old_inc_dt = "select *  from pp_daily_pos_attributes where int_ref_num = '" +int_ref_num  +"' and int_instrmnt_id = '"+ iinstrmnt_id1 + "'  limit 1"

        cur.execute(old_inc_dt)
        old_inc = cur.fetchone()

        while old_inc:
            old_inc_date = old_inc.getString("inception_date") #println('max_date---' + max_date)
        break

    new_inc_dt = "select min(vltn_dt) from test_if_capital_valuation where ext_ref_num = '" + int_ref_num + "' and instrmnt_id = '" + iinstrmnt_id1 + "'"
    cur.execute(new_inc_dt)
    new_inc = cur.fetchone()

    while new_inc.next:
        new_inc_date = new_inc[2]
        stamp_inc_date = new_inc_date
        break

if old_inc_date is None:
    d1 = new_inc_date
    d2 = old_inc_date
    if d1 < d2:
        stamp_inc_date = old_inc_date

#stamp_inc_date = quote + stamp_inc_date + quote1;


    query1 = "select * from arch14_incr.if_capital_valuation where  ext_ref_num = '" + accnt + "' and vltn_dt = " + vltn_currentValue + " and instrmnt_id = '" + instrmnt_id1 + "' order by vltn_dt,ext_ref_num,instrmnt_id"
    query2 = "select * from arch14_incr.if_capital_transactions where  ext_ref_num = '" + accnt + "' and trade_dt = " + vltn_currentValue + " and instrmnt_id = '" + instrmnt_id1 + "' order by trade_dt,ext_ref_num,instrmnt_id"
    query3 = "select * from arch14_incr.if_capital_transactions where ext_ref_num = '" + accnt + "' and trade_dt = " + vltn_currentValue + " and instrmnt_id = '" + instrmnt_id1 + "' and updt_mv_flg is null and cash_sensitive_txn_flg is null and fee_flg is null and cr_dr_flg is null order by trade_dt,ext_ref_num,instrmnt_id"

    cur.execute(query1)
    valuation_set = cur.fetchone()
    cur.execute(query2)
    transaction_set = cur.fetchone()
    cur.execute(query3)
    flows_set1 = cur.fetchone()

    isEmptyval = True
    while valuation_set:
        isEmptyval = False
        bmv1 = valuation_set["bmv"]
        bmv_dt = valuation_set["vltn_dt"]
        cal_bmv = cal_bmv + bmv1
    if q == 0:
        Periodic_Bmv = cal_bmv
        #println(Periodic_Bmv);
        periodic_bmv_date = quote + bmv_dt + quote1

    emv1 = valuation_set["emv"]
    cal_emv = cal_emv + emv1
    Periodic_Emv = cal_emv
    periodic_Emv_date = vltndt
    cal_ext_ref_num = quote + accnt + quote1
    cal_clientId = None
    #cal_clientId = valuation_set.getString("ext_client_id");
    #println(cal_clientId)
    product_ref_type = valuation_set["prod_ref_type"]
    cal_product_ref_type = quote + product_ref_type + quote1
    instrmnt_id1 = valuation_set["instrmnt_id"]
    #System.out.println(iinstrmnt_id);
    if instrmnt_id1.equals("9999SWPSF"):
        instrmnt_id1 = "9999SWP"

    cal_instrmnt_id = quote + instrmnt_id1 + quote1
    product_ref = valuation_set["product_ref"]
    cal_product_ref = quote + product_ref + quote1

    isEmptytrans = True
    while transaction_set:
        isEmptytrans = False
        tnx_amt = transaction_set["transaction_amt"]
        flow_flag = transaction_set["flow_flg"]
        cash_sensitive_flag = transaction_set["cash_sensitive_txn_flg"]
        upd_mv_flag = transaction_set["updt_mv_flg"]
        fee_flag = transaction_set["fee_flg"]
    while flows_set1:
        flow_flag1 = flows_set1.getLong("flow_flg")
        tnx_amt1 = flows_set1.getDouble("transaction_amt")

    if flow_flag1 == 1:
        total_inflow1 = total_inflow1 + tnx_amt1

    elif flow_flag1 == 2:
        total_outflow1 = total_outflow1 + tnx_amt1

    if flow_flag == 1:
        total_inflow = total_inflow + tnx_amt

    elif flow_flag == 2:
        total_outflow = total_outflow + tnx_amt

    cal_netflow = total_inflow - total_outflow
    inflow = total_inflow1
    outflow = total_outflow1

#Calculate Contribution & withdrawal
    if cash_sensitive_flag == 1:
        cal_contribution = cal_contribution + tnx_amt

    elif cash_sensitive_flag == 2:
        cal_withdrawal = cal_withdrawal + tnx_amt

#calculate income and distribution
    if upd_mv_flag == 1:
        cal_income = cal_income + tnx_amt

    elif upd_mv_flag == 2:
        cal_distribution = cal_distribution + tnx_amt

#calculate net_fees
    if fee_flag == 1:
        cal_netfees = cal_netfees + tnx_amt

    query4 = "select * from arch14_incr.test_pp_daily_pos_attributes where  int_ref_num = " + accnt + " and perf_dt >='" + monthStart + "'and perf_dt < " + vltn_currentValue + " and int_instrmnt_id = '" + instrmnt_id1 + "' order by perf_dt desc"

    cur.execute(query4)
    MTD_values = cur.fetchone()
    while MTD_values:
        Mtd_contribution_1 = MTD_values["Mtd_contribution"]
        Mtd_withdrawal_1 = MTD_values["Mtd_withdrawal"]
        mtd_income_1 = MTD_values["mtd_income"]
        mtd_distribution_1 = MTD_values["mtd_distribution"]
        mtd_net_fees_1 = MTD_values["mtd_net_fees"]
        mtd_net_flow_1 = MTD_values["mtd_net_flow"]
        mtd_inflow1 = MTD_values["mtd_flow_in"]
        mtd_outflow1 = MTD_values["mtdflow_out"]
        break

#Mtd_contribution_1 = cal_contribution;

Mtd_contribution = cal_contribution + Mtd_contribution_1

#Mtd_withdrawal_1 = cal_withdrawal;

Mtd_withdrawal = cal_withdrawal + Mtd_withdrawal_1

#mtd_income_1 = cal_income;
mtd_income = cal_income + mtd_income_1

#mtd_distribution_1 = cal_distribution;

mtd_distribution = cal_distribution + mtd_distribution_1

#mtd_net_fees_1 = cal_netfees;

mtd_net_fees = cal_netfees + mtd_net_fees_1

#mtd_net_flow_1 = cal_netflow;

mtd_net_flow = cal_netflow + mtd_net_flow_1

#mtd_inflow1 = inflow;
mtd_inflow = inflow + mtd_inflow1

#mtd_outflow1 = outflow;
mtd_outflow = outflow + mtd_outflow1

#cal_bmv = cal_bmv.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

if not isEmptytrans:
    cal_bmv = round(cal_bmv, 2)
    cal_emv = round(cal_emv, 2)
    cal_netflow = round(cal_netflow, 7)
    cal_contribution = round(cal_contribution, 7)
    cal_withdrawal = round(cal_withdrawal, 7)
    cal_income = round(cal_income, 7)
    cal_netfees = round(cal_netfees, 7)
    cal_distribution = round(cal_distribution, 7)
    Mtd_contribution = round(Mtd_contribution, 7)
    Mtd_withdrawal = round(Mtd_withdrawal, 7)
    mtd_income = round(mtd_income, 7)
    mtd_distribution = round(mtd_distribution, 7)
    mtd_net_fees = round(mtd_net_fees, 7)
    mtd_net_flow = round(mtd_net_flow, 7)
    inflow = round(inflow, 7)
    mtd_inflow = round(mtd_inflow, 7)
    mtd_outflow = round(mtd_outflow, 7)
insertQuery = "INSERT INTO test_pp_daily_pos_attributes(int_client_id, int_ref_num, int_prod_ref_type, int_product_ref, int_instrmnt_id, perf_dt, inception_date,computation_date, emv, bmv, net_flow, contribution_day, withdrawal_day, income_day, distribution_day, net_fees_day, pp_daily_pos_attributes_ver, dm_lstupddt, mtd_net_flow, mtd_contribution, mtd_withdrawal, mtd_income, mtd_distribution, mtd_net_fees,flow_in,flow_out,mtd_flow_in,mtd_flow_out) VALUES (" + cal_clientId + ", " + cal_ext_ref_num + ", " + cal_product_ref_type + ", " + cal_product_ref + ", " + cal_instrmnt_id + ", " + vltn_currentValue + ", " + stamp_inc_date + ", '2023-01-13', " + cal_emv + ", " + cal_bmv + ", " + cal_netflow + ", " + cal_contribution + ", " + cal_withdrawal + ", " + cal_income + ", " + cal_distribution + ", " + cal_netfees + ", 1, '2023-03-30'," + mtd_net_flow + "," + Mtd_contribution + ", " + Mtd_withdrawal + ", " + mtd_income + ", " + mtd_distribution + ", " + mtd_net_fees + "," + inflow + "," + outflow + "," + mtd_inflow + "," + mtd_outflow + ")"

#System.out.println(insertQuery);
st4 = cur.insertQuery
#System.out.println("Transction SQL Executed = "+ insertQuery);
cal_bmv = 0
cal_emv = 0
cal_netflow = 0
cal_contribution = 0
cal_withdrawal = 0
cal_income = 0
cal_distribution = 0
cal_netfees = 0
total_inflow = 0
total_outflow = 0
inflow = 0
outflow = 0
total_inflow1 = 0
total_outflow1 = 0

if isEmptytrans == True and isEmptyval != True:
    #Mtd_contribution_1 = cal_contribution;

    Mtd_contribution = cal_contribution + Mtd_contribution_1

    #Mtd_withdrawal_1 = cal_withdrawal;

    Mtd_withdrawal = cal_withdrawal + Mtd_withdrawal_1

    #mtd_income_1 = cal_income;
    mtd_income = cal_income + mtd_income_1

    #mtd_distribution_1 = cal_distribution;

    mtd_distribution = cal_distribution + mtd_distribution_1

    #mtd_net_fees_1 = cal_netfees;

    mtd_net_fees = cal_netfees + mtd_net_fees_1

    #mtd_net_flow_1 = cal_netflow;

    mtd_net_flow = cal_netflow + mtd_net_flow_1

    #mtd_inflow1 = inflow;
    mtd_inflow = inflow + mtd_inflow1

    #mtd_outflow1 = outflow;
    mtd_outflow = outflow + mtd_outflow1

cal_bmv = round(cal_bmv, 2)
cal_emv = round(cal_emv, 2)
Mtd_contribution = round(Mtd_contribution, 7)
Mtd_withdrawal = round(Mtd_withdrawal, 7)
mtd_income = round(mtd_income, 7)
mtd_distribution = round(mtd_distribution, 7)
mtd_net_fees = round(mtd_net_fees, 7)
mtd_net_flow = round(mtd_net_flow, 7)
mtd_inflow = round(mtd_inflow, 7)
mtd_outflow = round(mtd_outflow, 7)

cal_clientId = ''

#insertQuery = ("INSERT INTO test_pp_daily_pos_attributes(int_client_id, int_ref_num, int_prod_ref_type, int_product_ref, int_instrmnt_id, perf_dt, inception_date,computation_date, emv, bmv, net_flow, contribution_day, withdrawal_day, income_day, distribution_day, net_fees_day, pp_daily_pos_attributes_ver, dm_lstupddt, mtd_net_flow, mtd_contribution, mtd_withdrawal, mtd_income, mtd_distribution, mtd_net_fees,flow_in,flow_out,mtd_flow_in,mtd_flow_out) VALUES ("+cal_clientId+ ", " + cal_ext_ref_num + ", " + cal_product_ref_type + ", " + cal_product_ref + ", " + cal_instrmnt_id + ", " + vltn_currentValue + ", " + stamp_inc_date + ", '2023-01-13', " + cal_emv + cal_bmv + 0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.0000000, 1, '2023-03-30', + mtd_net_flow + "," + Mtd_contribution + ", " + Mtd_withdrawal + ", " + mtd_income + ", " + mtd_distribution + ", " + mtd_net_fees + 0.0000000,0.0000000,+ mtd_inflow + "," + mtd_outflow + ")"
#println(insertQuery)
#st3.execute(insertQuery)
#System.out.println("Insert_Query Executed = " + insertQuery);

#System.out.println(cal_bmv);
#System.out.println(cal_emv);
#cal_bmv = 0
#cal_emv = 0
#cal_product_ref_type = ""
#cal_product_ref = ""
#cal_instrmnt_id = ""


#if Data_Present_for_month == True
#insertQuery = "INSERT INTO arch14_incr.test_pp_periodic_pos_attr(int_client_id, int_ref_num, int_prod_ref_type, int_product_ref, int_instrmnt_id, perf_dt,inception_date, computation_date, emv, bmv,bmv_dt, mtd_net_flow, mtd_contribution, mtd_withdrawal, mtd_income, mtd_distribution, mtd_net_fees, period_end_date, pp_periodic_pos_attr_ver, dm_lstupddt,mtd_flow_in,mtd_flow_out) VALUES ("+cal_clientId+", "+cal_ext_ref_num+", "+cal_product_ref_type+", "+cal_product_ref+", "+cal_instrmnt_id+", "+periodic_Emv_date+", "+stamp_inc_date+", '2023-01-13', "+Periodic_Emv+", "+Periodic_Bmv+","+periodic_bmv_date+","+mtd_net_flow+","+Mtd_contribution+", "+Mtd_withdrawal+", "+mtd_income+", "+mtd_distribution+", "+mtd_net_fees+", "+monthEndDate+",1, '2023-06-28',"+mtd_inflow+","+mtd_outflow+")";

#st4.execute(insertQuery)

#if (Data_Present_for_month == true) {
#insertQuery = "INSERT INTO arch14_incr.test_pp_periodic_pos_attr(int_client_id, int_ref_num, int_prod_ref_type, int_product_ref, int_instrmnt_id, perf_dt,inception_date, computation_date, emv, bmv,bmv_dt, mtd_net_flow, mtd_contribution, mtd_withdrawal, mtd_income, mtd_distribution, mtd_net_fees, period_end_date, pp_periodic_pos_attr_ver, dm_lstupddt) VALUES ("+cal_clientId+", "+cal_ext_ref_num+", "+cal_product_ref_type+", "+cal_product_ref+", "+cal_instrmnt_id+", "+vltndt+", '2023-01-13', '2023-01-13', "+Periodic_Emv+", "+Periodic_Bmv+","+periodic_bmv_date+","+mtd_net_flow+","+Mtd_contribution+", "+Mtd_withdrawal+", "+mtd_income+", "+mtd_distribution+", "+mtd_net_fees+", "+monthEndDate+",1, '2023-06-28')";


#st4.execute(insertQuery)


#except (Exception, psycopg2.Error) as error:
#print("Error while fetching data from PostgresSQL", error)

#finally:
# closing database connection.
#if connection:
#cursor.close()
#connection.close()
#print("PostgresSQL connection is closed")
