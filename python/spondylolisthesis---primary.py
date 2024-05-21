# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"N384300","system":"readv2"},{"code":"N384000","system":"readv2"},{"code":"N384200","system":"readv2"},{"code":"7J48500","system":"readv2"},{"code":"7J48511","system":"readv2"},{"code":"N384.00","system":"readv2"},{"code":"N384100","system":"readv2"},{"code":"65017.0","system":"readv2"},{"code":"61817.0","system":"readv2"},{"code":"73565.0","system":"readv2"},{"code":"66732.0","system":"readv2"},{"code":"52889.0","system":"readv2"},{"code":"2895.0","system":"readv2"},{"code":"12371.0","system":"readv2"},{"code":"104348.0","system":"readv2"},{"code":"53931.0","system":"readv2"},{"code":"M43.1","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('spondylolisthesis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["spondylolisthesis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["spondylolisthesis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["spondylolisthesis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
