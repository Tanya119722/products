# 读取档案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if 'a商品,价格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

# 让使用者输入
while True:
	name = input('pls input the name of the product:')
	if name == 'q':
		break
	price = input('pls input the price of the product:')
	products.append([name, price])
print(products)

# 输出所有购买记录
for p in products:
	print(p[0],'的价格是', p[1])

# 写入档案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('a商品,价格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

