# # import re
#
# inp = "NUM( Sum(IsNotCompliant) / Sum(TOTAL IsNotCompliant) , '##0.00%')"
# # res = (''.join(e for e in inp if e.isalnum()))
# res = filter(str.isalnum,inp)
# print("data after filter is:",res)
import re

# strs = "NUM( Sum(IsNotCompliant) / Sum(TOTAL IsNotCompliant) , '##0.00,%')"
strs =input("please enter the custom expression:")
import pdb; pdb.set_trace()
print("entered value is:",strs)
ans1 = strs.split(',', 1)[0] 
ans = strs.split(',', 1)[1]  

nstr = re.sub(r"[-\",#@;:<>{}`+=~|!?,]", "", ans)
final_ans = ans1 + ',' + nstr 
# nstr = re.sub(r'[?|$|.|!|#|%|*|@|*|,]',r'',strs)
# nstr = strs.replace("#$%?@*","")
print("modified value is nstr:",final_ans)
# nestr = re.sub(r'[^a-zA-Z0-9 ]',r'',nstr)
# print nestr