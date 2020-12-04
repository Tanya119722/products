import os # operating system

# 读取档案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if 'a商品,价格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products	

# 让使用者输入
def user_input(products):
	while True:
		name = input('pls input the name of the product:')
		if name == 'q':
			break
		price = input('pls input the price of the product:')
		products.append([name, price])
	print(products)
	return products

# 输出所有购买记录
def print_products(products):
	for p in products:
		print(p[0],'的价格是', p[1])

# 写入档案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('a商品,价格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile('filename'):
		print('yeah, I found the file')
		products = read_file('filename')
	else:
		print('I can not find the file')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()