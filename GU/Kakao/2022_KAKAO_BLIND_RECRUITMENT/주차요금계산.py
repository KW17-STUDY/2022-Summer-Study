def countTime(accumul_record,number, out_time, in_time):
    out_hour, out_min = out_time.split(':')
    in_hour, in_min = in_time.split(':')
    out_hour, out_min, in_hour, in_min = int(out_hour), int(out_min), int(in_hour), int(in_min)
    if out_min > in_min:
        diff_time = out_hour - in_hour
        diff_min = out_min - in_min
    else:
        diff_min = (out_min+60) - in_min
        diff_time = out_hour- 1 - in_hour
    if number not in accumul_record.keys():
        return diff_time * 60 + diff_min
    else:
        return accumul_record[number] + diff_time * 60 + diff_min
    

def solution(fees, records):
    a = []
    a.append('str')
    print(a)
    if 'str' in a:
        a.remove('str')
    print(a)
    
    answer = []
    base_hour, base_fee, unit_time, unit_fee = fees
    record_dict = dict()
    accumul_record = dict()
    pay_dict = dict()
    print_order = []

    for record in records:
        time, number, behavior = record.split()
        if behavior == 'OUT':
            accumul_record[number] = countTime(accumul_record, number,time, record_dict[number]['IN'])
        record_dict[number] = {behavior: time}
    
    # 나가지 않은 차들에 대한 누적 분 구하기
    for number in record_dict:
        for behavior in record_dict[number]:
            if behavior == 'IN':
                time = record_dict[number][behavior]
                accumul_record[number] = countTime(accumul_record, number,'23:59', time)
            record_dict[number] = {'OUT': '23:59'}
    
    print(accumul_record)
    for number in accumul_record:
        time = accumul_record[number]
        ex_time = time - base_hour
        if ex_time < 0 :
            have_to_pay = base_fee
        else:
            unit = int(ex_time / unit_time) if ex_time % unit_time == 0 else int(ex_time / unit_time)+1
            have_to_pay = unit * unit_fee + base_fee
        pay_dict[number] = have_to_pay
    order = list(pay_dict.keys())
    order.sort()
    for i in order:
        answer.append(pay_dict[i])
            
    return answer