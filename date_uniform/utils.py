# -*- coding: UTF-8 -*-
# @Time : 2021/11/29 20:36
# @Author : 洛基Nickey

import time
from .date_re_pattern import *


def text_preprocess(source):
    string = source.lower()
    string = string.replace('\n', ' ').replace('  ', ' ')  # 用正则匹配将多个空格变成一个空格： to do
    for cn, nmb in zip(CN_Number[0], CN_Number[1]):
        string = string.replace(cn, nmb)
    string = string.translate(CE_table)
    return string


def year_process(year):
    if len(year) == 2:
        return '20' + year
    return year


def month_process(month):
    if len(month) == 2:
        return month
    elif len(month) == 1:
        return '0' + month
    if month in MONTH_table:
        return MONTH_table[month]
    return month


def day_process(day):
    if len(day) == 1:
        return '0' + day
    return day


def day_map(extract_date_temp):
    for key in DAY_table:
        if key in extract_date_temp:
            return DAY_table[key]
    return None


def extract_date(source):
    priority_a = {'YMD_1': YMD_1, 'YMD_2': YMD_2, 'MDY_1': MDY_1, 'MDY_2': MDY_2, 'DMY_1': DMY_1, 'DMY_2': DMY_2,
                  'DMY_3': DMY_3, 'DMY_4': DMY_4}
    priority_b = {'YMD_3': YMD_3, 'YMD_4': YMD_4}
    priority_c = {'YM_1': YM_1, 'YM_4': YM_4}
    priority_d = {'YM_2': YM_2, 'YM_3': YM_3, 'MD_1': MD_1, 'M_2': M_2, 'MD_3': MD_3, 'DM_1': DM_1, 'DM_2': DM_2,
                  'DM_3': DM_3, 'DM_4': DM_4, 'DM_5': DM_5}
    priority_e = {'BR_M_1': BR_M_1, 'BR_MD_2': BR_MD_2, 'BR_D_3': BR_D_3, 'BR_M_4': BR_M_4, 'BR_MY_5': BR_MY_5}
    all_priority = [priority_a, priority_b, priority_c, priority_d, priority_e]

    string = text_preprocess(source)
    string = string.translate(CE_table)
    for priority in all_priority:
        for template_name, template in priority.items():
            outcome = template.search(string)
            if outcome:
                date_form = {}
                if 'Y' in template_name:
                    date_form['year'] = year_process(outcome.group('year'))
                else:
                    date_form['year'] = None
                if 'M' in template_name:
                    date_form['month'] = month_process(outcome.group('month'))
                else:
                    date_form['month'] = None
                if 'D' in template_name:
                    date_form['day'] = day_process(outcome.group('day'))
                else:
                    date_form['day'] = day_map(outcome.group())  # 上旬 or None
                return template_name, outcome.group(), date_form
    return None


def date_before(year, month, day, year_2, month_2, day_2):
    if year:
        if int(year) > int(year_2):
            return False
        elif int(year) < int(year_2):
            return True
    if month:
        if int(month) > int(month_2):
            return False
        elif int(month) < int(month_2):
            return True
    if day:
        if int(day) > int(day_2):
            return False
        elif int(day) < int(day_2):
            return True
    return True  # 如果年月日都相等，默认小于当前时间


# date format function
def date_format(source):
    try:
        extraction = extract_date(source)
        if not extraction:
            return None
        # 获取当前时间
        date_now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        year_now, month_now, day_now = date_now.split('-')
        # 获取提取到的时间
        template_name, extract_str, date_form = extraction
        year, month, day = date_form['year'], date_form['month'], date_form['day']
        # 假如未提取到相应的时间，默认用今天的时间填充
        if not month:
            month = '01'
        if not day:
            day = '01'
        if not year:
            year = year_now
            # if date_before(year, month, day, year_now, month_now, day_now):
            #     year = str(int(year_now) + 1)

        date_output = year + '-' + month + '-' + day + ' ' + '00:00:00'
        # return template_name, extract_str, date_output  # 正则模板， 提取出的span， 规范化后的时间字符串
        return date_output
    except Exception as e:
        print(str(e))
        return None
