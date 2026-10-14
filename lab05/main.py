from tablestats import total_minutes, to_csv, count_types, read_rows

def main():
    table_name = input()
    with open(table_name, 'r', encoding='utf-8') as table:
        rows = read_rows(table)


    print(len(rows))
    print(len(count_types(rows)))
    print(total_minutes(rows, 'ошибка'))

    with open('summary.csv', 'w', encoding='utf-8') as out:
        out.write(to_csv(count_types(rows)))

if __name__ == '__main__':
    main()
