
def main():
    arr_list = ['goiaba']
    arr_list_fruits = ['banana', 'maçã', 'uva', 'morango']
    arr_list_numeros = [1, 2, 3, 4, 5]
    arr_list_obj1 = [
        {"nome": "Zoka", "funcao": "zokar" },
        {"nome": "Xoka", "funcao": "xokar" }
    ]

    arr_list_obj2 = {"nome": "Zika", "funcao": "zikar" }
    

    arr_list_obj1.append(arr_list_obj2)
    print(arr_list_obj1)

    print("Lista sem append")
    print(arr_list)

    for item in arr_list_fruits:
        arr_list.append(item)

    
    print("Lista com append")
    print(arr_list)

    print("Lista com extend")
    print(arr_list)


if __name__ == "__main__":
    main()