5. selection stmt:
      Syntax: <ifstmt> --> if ( <boolexpr>) <stmt> [ else <stmt>]

    M_if (if) (<boolexpr>) <stmt>, s) -->
        if M_bool (<boolexpr>, s) == error
            return error
        if M_bool (<boolexpr>, s) 
            if M_bool (<boolexpr>, s) == error
                return error
            return error
    
     (if) (<boolexpr>) <stmt> else, s) -->
        if M_bool (<boolexpr>, s) == error
            return error;
        if M_bool (<boolexpr>, s) 
            if M_bool (<stmt1>, s) == error
                return error
            return M_stmt (<stmt1>, s)
        else
            if M_bool (<stmt2>, s) == error
                return error
            return M_stmt (<stmt2>, s)
        


6. loop stmt:
    while loop
    Syntax: <while>--> 'while' (  <bool_stmt> ) <stmt>
       Semantics:   if M_b(<boo_stmt>, s)
                      if M_stmt(<stmt1>, s) == error
                            return error
                    else
                        return M_stmt(<stmt1>, s)

7. expr: 

8. expr -> bool
    Syntax: <expr> -> 

9. rules:
    G) Assign natural to real:
       Syntax: <asign> -> var <id> = <expr>
           Semantics: <expr>.expectedType <- <id>.actualType>
           if (<expr>.actualType == nat_num) && (<id>.actualT == real_num)
                then  <id> = <expr>
            else
                <id> | <string> | <bool>
    
    H) Syntax: <assignment> -> var <id> = <expr>
        Semantics: <expr>.expectedType <- <id>.actualType>
            if(<expr>.actualType == <id>.actualType)
                then <id> = <expr>
            else 
                error

10. 

11. axiomatic semantics (find the weakest precondition):
