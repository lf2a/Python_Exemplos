#!/usr/bin/python3
# -*- coding: utf-8 -*-

try:
    from stock_module import stock
    import json
except ImportError as e:
    print(e)

def search(item):
    v = p.search(item)

    js = json.loads(v)
    js = js['quotes']

    print('=================================================')
    for json_stock in js:
        arr = []
        for v in json_stock.keys():
            arr.append(v)

        i = 0
        for s in arr:
            print(f'{s}: {str(json_stock[s])}', end='\n')
            if i == 3:
                pass
            i += 1
        print('=================================================')

def print_js(jss):
    js = jss
    arr = []
    
    for keys in js.keys():
        arr.append(keys)
    
    print('\n=================================================')
    
    for k in range(0, len(arr)):
        print( arr[k] + ': ' + js[arr[k]])
        
    print('=================================================\n')

def menu():
    print('search :  Pesquisar por ação ou criptomoeda')
    print('stock  :  Obter info de ação ou moeda (ex: dolar)')
    print('coin  :  Obter info de criptomoeda')

if __name__ == '__main__':
    p = stock.Stock()
    
    while True:
        menu()
        inp = str(input('> '))
        
        if inp == 'exit':
            break
        
        elif inp == 'search':
            inp = str(input('(insira o item a ser buscado) > '))
            search(inp)
            
        elif inp == 'stock':
            inp = str(input('(insira o simbolo ex: ^BVSP) > '))
            n_input = 'https://finance.yahoo.com/quote/' + inp + '?p=' + inp
            js_s = p.get_stock(n_input)
            print_js(js_s)
            
        elif inp == 'coin':
            inp = str(input('(insira o simbolo ex: BTC-USD) > '))
            n_input = 'https://finance.yahoo.com/quote/' + inp + '?p=' + inp
            js_c = p.get_cryptocoin(n_input)
            print_js(js_c)
            
