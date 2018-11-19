lang = ["Java","Python","Javascript","C++","C#","Ruby","Perl","PHP","C","Android"]
demand = [61,47,37,32,26,18,14,14,9,7]
for i in range(len(lang)):
    print(f'{lang[i]:>10}:{"#"*demand[i]}')