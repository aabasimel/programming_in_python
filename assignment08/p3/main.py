from mod_conversion import in2cm_table
start = float(input("Enter start length in inches: "))
end = float(input("Enter end length in inches: "))
step = float(input("Enter step size in inches: "))

cm=in2cm_table(start,end,step)
print(cm)