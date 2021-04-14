from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#extract针对有限数据，返回有可能的匹配；extractOne 返回最佳匹配
choices = ['Yes', 'No', 'Maybe', 'N/A']
print(process.extract('ya', choices, limit=2))
print(process.extractOne('ya', choices))
print(process.extract('nope', choices, limit=2))
print(process.extractOne('nope', choices))
#数据模糊处理

my_records = [
    {'favorite_book': 'Grapes of Wrath', 'favorite_movie': 'Free Willie', 'favorite_show': 'Two Broke Girls',},
    {'favorite_book': 'The Grapes of Wrath', 'favorite_movie': 'Free Willy', 'favorite_show': '2 Broke Girls', }]

my_records2 = [
    {'favorite_food': 'cheeseburgers with bacon','favorite_drink': 'wine, beer, and tequila','favorite_dessert': 'cheese or cake',},
    {'favorite_food': 'burgers with cheese and bacon','favorite_drink': 'beer, wine, and tequila','favorite_dessert': 'cheese cake',
}]

#ratio 比较字符串之间的相似度，返回整数
print(fuzz.ratio(my_records[0].get('favorite_book'), my_records[1].get('favorite_book')))

print (fuzz.ratio(my_records[0].get('favorite_movie'), my_records[1].get('favorite_movie')) )

print (fuzz.ratio(my_records[0].get('favorite_show'), my_records[1].get('favorite_show')))


print (fuzz.partial_ratio(my_records[0].get('favorite_book'),my_records[1].get('favorite_book')))
print (fuzz.partial_ratio(my_records[0].get('favorite_movie'),my_records[1].get('favorite_movie')))
print (fuzz.partial_ratio(my_records[0].get('favorite_show'),my_records[1].get('favorite_show')))



#比较字符串之间顺序相似度
print (fuzz.token_sort_ratio(my_records2[0].get('favorite_food'),my_records2[1].get('favorite_food')))
print (fuzz.token_sort_ratio(my_records2[0].get('favorite_drink'),my_records2[1].get('favorite_drink')))
print (fuzz.token_sort_ratio(my_records2[0].get('favorite_dessert'),my_records2[1].get('favorite_dessert')))

#比较的是标记组成的集合，得出两个集合的交集和差集
print (fuzz.token_set_ratio(my_records2[0].get('favorite_food'),my_records2[1].get('favorite_food')))
print (fuzz.token_set_ratio(my_records2[0].get('favorite_drink'),my_records2[1].get('favorite_drink')))
print (fuzz.token_set_ratio(my_records2[0].get('favorite_dessert'),my_records2[1].get('favorite_dessert')))