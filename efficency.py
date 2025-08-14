def backtracking_search(assignment ,csp):
    if assignment ==True : return assignment
var = select_unassigned_var(assignment ,csp)
 for value in domain-values(var ,assignment, csp):
    if value consistent with assignment :
       add { var = value } to assignment
    result = backtrack(assignment, csp)
    if result != failure : return result
 remove {ver = value} from assignment
return failure

csp = {
#constraint satisfaction problem


}
unassigned_var = {
   a , b, c, d
   
}
doamin-values = {
   monday ,
   thuasday ,
   wednesday

}

def select_unassigned_var(assignment ,csp):
   
#################################################3


#maintaining arc_consistency:



   def backtracking_search(assignment ,csp):
    if assignment ==True : return assignment
var = select_unassigned_var(assignment ,csp)
  for value in domain-values(var ,assignment, csp):
    if value consistent with assignment :
       add { var = value } to assignment
       inferences = inference(assignment ,csp)
       if inferences != failure : add inferences to assignment
    result = backtrack(assignment, csp)
    if result != failure : return result
  remove {ver = value} and inferences from assignment
 
return failure