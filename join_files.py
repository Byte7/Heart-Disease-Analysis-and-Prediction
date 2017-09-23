'''
Program to join the files in the cleveland, hungarian, long-beach-va, and
switzerland databases after a final cleaning to remove incomplete records.
To use it, type:
    python join_files.py
Input files are assumed to be in the data/ subdirectory.  Output file goes
in the same subdirectory.
'''
input_files = ["cleveland14.csv", "hungarian14r.csv", "long_beach_va14.csv",
               "switzerland14.csv"]
output_file = "heart_disease_all14.csv"
data_dir = "data/"

output = open(data_dir+output_file, 'w')
total_input = 0
total_output = 0
for input_file in input_files:
    input = open(data_dir+input_file, 'r')
    nlines_through = 0
    nlines_total = 0
    for line in input:
        total_input += 1
        nlines_total += 1
        if ("-9" not in line) and ("?" not in line):
            features_list = line.split(",")
            features_list = [float(item) for item in features_list[0:14]]
            corrected_line = ",".join(map(str, features_list))
            output.write(corrected_line+"\n")
            total_output += 1
            nlines_through += 1
    print 'Transferred %i out of %i records from %s' % (nlines_through,
                                                        nlines_total,
                                                        input_file)
    input.close()
print 'Total records read in: %i' % total_input
print 'Total records written out to %s: %i' % (output_file, total_output)
output.close()
