import general_response as gr
import random

def astro(given):
    compare2=[]
    given=given.lower()
    compare = list(gr.astronomy_terms.keys())
    for i in compare:
        j = i.replace(' ','')
        j = j.replace('-', '')
        j = j.lower()
        compare2.append(j)
    if given in compare2:
        x=compare2.index(given)
        response = gr.astronomy_terms[list(gr.astronomy_terms.keys())[x]]
    else:
        index=random.randrange(len(gr.No_term_Response))
        response=gr.No_term_Response[index]
    return response