% instance
%student(jack).
%student(anna).
%completedthesis(jack).

% encoding
%graduated(Person) :- student(Person), completedthesis(Person).
%notgraduated(Person) :- student(Person), not completedthesis(Person).

workyears(1, 4).
workyears(2, 10).

dom(1..2).

#preference(p, more(weight)){
  X :: workyears(x)
}.

hired(Candidate) :- workyears(Candidate, 3..50).

#optimize(p).
