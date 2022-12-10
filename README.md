# date-uniform
## 功能：输入日期文本（中、英文形式的字符串），以标准的日期格式返回
## 示例：
input:15. MARCH. 2021, output:2021-03-15 00:00:00
input:2-DEC-21, output:2021-12-02 00:00:00
input:2-十二月-21, output:2021-12-02 00:00:00
input:2-十二月-20, output:2020-12-02 00:00:00
input:2-十二月-22, output:2022-12-02 00:00:00
input:28 - Jul - 21, output:2021-07-28 00:00:00
input:June.8,2021, output:2021-06-08 00:00:00
input:12月 4日, output:2022-12-04 00:00:00
input:2021 - 07 - 05, output:2021-07-05 00:00:00
input:2021.07.29, output:2021-07-29 00:00:00
input:2021年8月30日, output:2021-08-30 00:00:00
input:2021 年06 月06 日, output:2021-06-06 00:00:00
input:2021 / 09 / 11, output:2021-09-11 00:00:00
input:2021 / 6 / 11日, output:2021-06-11 00:00:00
input:21 / 9 / 2, output:2022-09-02 00:00:00
input:Jun, 15, 2021, output:2021-06-15 00:00:00
input:AUG - 08, 2021, output:2021-08-08 00:00:00
input:JUL 16, 2020, output:2020-07-16 00:00:00
input:4 / 21 / 2021, output:2022-04-21 00:00:00
input:6 / 22 / 2021, output:2022-06-22 00:00:00
input:15 / OCT. / 2021, output:2022-10-15 00:00:00
input:04 / Apr / 2021, output:2021-04-04 00:00:00
input:28 - Jul - 21, output:2021-07-28 00:00:00
input:28 - Sep - 2021, output:2021-09-28 00:00:00
input:30th Aug.2021, output:2021-08-30 00:00:00
input:14 Jul, 2021, output:2021-07-14 00:00:00
input:22, MAY, 2021, output:2021-05-22 00:00:00
input:5.18, output:2022-05-18 00:00:00
input:12.14, output:2022-12-14 00:00:00
input:9月14日, output:2022-09-14 00:00:00
input:6 月11号, output:2022-06-11 00:00:00
input:4 月2 号, output:2022-04-02 00:00:00
input:8 - 8日, output:2022-08-08 00:00:00
input:AUG 17, output:2022-08-17 00:00:00
input:Oct25, output:2022-10-25 00:00:00
input:7 - 5号, output:2022-07-05 00:00:00
input:01 - 08, output:2022-01-08 00:00:00
input:4 / 30, output:2022-04-30 00:00:00
input:28 - Jul, output:2022-07-28 00:00:00
input:12 - JUL, output:2022-07-12 00:00:00
input:7 - 九月, output:2022-09-07 00:00:00
input:14th - July, output:2022-07-14 00:00:00
input:06TH  JULY, output:2022-07-06 00:00:00
input:32th july, output:None
input:31th july, output:2022-07-31 00:00:00

## todo
①未做日期检查，比如现有程序中，2月31日会被视为合法日期
②只做了初步的数据预处理，对于一些纯中文表示的日期可能会识别错误
③只识别年月日，未识别时分秒
④一次只处理一个日期，如果字符串中包含多个日期，只会识别第一个匹配到的日期
