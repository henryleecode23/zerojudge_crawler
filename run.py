from zerojudge_crawler import zj_crawler

print()
print("請輸入題目編號")
inp_text = input()

try:
    zj = zj_crawler(inp_text)

    print("-----------------------------")
    print(zj.title)
    print()
    print("說明")
    print()
    print(zj.problem_content)
    print("輸入說明:")
    print()
    print(zj.input_illustrate)
    print("輸出說明:")
    print()
    print(zj.output_illustrate)
    c = 1
    for t in range(zj.ex_test_case_quantity):
        print(f"範例測資#{c}:\n")
        print(f"範例輸入{c}:")
        print(zj.test_case_list[t][0])
        print(f"範例輸出{c}:")
        print(zj.test_case_list[t][1])
    print("標籤:")
    for t in range(len(zj.tags_list)):
        print(zj.tags_list[t]," ",end="")
    print()
    print("-----------------------------")
except:
    print("Error")
