import cc_dat_utils

#Part 1
input_dat_file = "data/pfgd_test.dat"

#Use cc_dat_utils.make_cc_data_from_dat() to load the file specified by input_dat_file
#print the resulting data

f= open("data/pfgd_test.txt","w+")



print(cc_dat_utils.make_cc_data_from_dat(input_dat_file), file = f)

#f.close()