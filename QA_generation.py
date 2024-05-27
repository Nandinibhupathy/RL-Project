from cwd import *
import ql
import infer
words_hints=[]
def keyword_generation(para,num):
    
    #words_hints=[ ['plasma', ''], ['redbloodcells', 'gem'], ['whitebloodcells', 'popular'], ['platelets', 'time'], ['heart', 'bottle']]

    #words_hints=[['honey', 'bee'], ['rose', 'flower'], ['emerald', 'gem'], ['fame', 'popular']]

    #words_hints= [['sun', 'What is the ultimate source of energy on earth?'], ['evapotranspiration', 'What is the process that occurs when evaporation occurs through the leaves of plants?'], ['precipitation', 'What is the process that occurs when snow or ice changes directly into water vapour without becoming water?'], ['sublimation', 'What is the process that occurs when water droplets freeze and fall as snow or hail?']]
    
    words_hints=infer.inference(para,num)
    
    print(words_hints)

    
    p = Crossword(30, 30, '-', 5000, words_hints)
    p.compute_crossword(2)
    p.grids=p.get_grid()
    p.pass_to_function()
    list1,list2,goal=p.get_lists()
    
    

    #print(p.solution())
    #print(p.word_details)
    print("list1 =",list1)
    print("list2 =",list2)
    print("goal =",goal)

 
    q_table_df = ql.execute_ql(list1,list2,goal)
    #print(list1,list2,goal)
   
    return p.get_puzzle(),p.get_words(),q_table_df,words_hints
    