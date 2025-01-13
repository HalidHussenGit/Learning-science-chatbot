import re
import general_response as gr
import random




def bioChat(given):
    compare2=[]
    given = given.replace(' ', '')
    given = given.replace('-', '')
    given = given.lower()
    compare=list(gr.biological_terms.keys())
    for i in compare:
        i=i.replace('-','')
        i = i.replace(' ', '')
        i=i.lower()
        compare2.append(i)
    if given in compare2:
        index=compare2.index(given)
        term=list(gr.biological_terms.keys())
        response=gr.biological_terms[term[index]]
        return response
    else:
        return gr.No_term_Response[random.randrange(len(gr.No_term_Response))]