# NOTE TO USER
# -ISBNs are expected to be listed one per line in a .txt file,
# with no other information.
# -Either use the filename given below, or change isbn_filename to reflect
# the name of your file.
# -Rules will be exported to rule_filename, one per line, ready to copy and
# paste into the ILLiad Customization Manager.
# - If you want longer or shorter routing rules, change the value of
# isbns_per_rule (value must be an integer!)
import pyisbn


isbn_filename = 'isbns.txt'
rule_filename = 'routingrules.txt'
isbns_per_rule = 100

# DO NOT change the value of any variables below this line!
start_string = "t.ISSN IN ('"
join_string = "','"
end_string = "')\n"

isbns = set()
rules = []

isbnfile = open(isbn_filename,'r')
for line in isbnfile:
    isbn = line.strip()
    isbns.add(isbn)
    if len(isbn) == 10:
        isbns.add(pyisbn.convert(isbn))
    
isbnfile.close()

temp_list= []

for isbn in isbns:
    temp_list.append(isbn)

    # batch isbns into strings
    if len(temp_list) >= isbns_per_rule:
        rules.append( start_string + join_string.join(temp_list) + end_string )
        temp_list = []
        
# batch any remainder into a final string
if temp_list:
    rules.append( start_string + join_string.join(temp_list) + end_string )

rulefile = open(rule_filename,'w')
for rule in rules: rulefile.write(rule)
rulefile.close()



