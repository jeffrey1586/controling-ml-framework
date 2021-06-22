adult(Person) :- age(Person, X), X > 17.


% instance
%student(jack).
%student(anna).
%completedthesis(jack).

% encoding
%graduated(Person) :- student(Person), completedthesis(Person).
%notgraduated(Person) :- student(Person), not completedthesis(Person).

% First step:
% - ML modules (external view)
% - acceptable uses of information for certain conclusion
1{hired, -hired}1 :- [table]. % ML module 1
male = female : ?hired.


% Second step;
% - ML module is transformed in a series of rules
hired :- exp3.
exp3 :- exp2, age > 40.
...
male = female : ?hired.

hired(Candidate) :- exp4(Candidate).
exp4(Candidate) :- exp3(Candidate), education(Candidate).
exp3(Candidate) :- exp2(Candidate), experience(Candidate).
exp2(Candidate) :- exp1(Candidate), rating(Candidate).
exp1(Candidate) :- years(Candidate).

years(Candidate) :- workyears(Candidate, X), X > 2.
rating(Candidate) :- biorating(Candidate, X), X > 5.
experience(Candidate) :- programming(Candidate, high).
education(Candidate) :- master(Candidate).
education(Candidate) :- bachelor(Candidate).

Rules: {0: ' workyears > 4.50', 1: ' class: 1',
2: ' motivation > 5.50', 3: ' class: 1',
4: ' workyears <= 8.50', 5: ' class: 0', 6: ' class: 1'}
prob_male {0: 0, 1: 0.5066666666666667, 2: 0.08, 3: 0.4166666666666667, 4: 0.08333333333333333, 6: 0.3333333333333333}
prob_female {0: 0, 1: 0.3333333333333333, 2: 0.08, 3: 0.3333333333333333, 4: 0.16666666666666666, 5: 0.6666666666666666}

% Output answer
% hired_female:   0.05
%  hired_male:   0.24

% In this case you don't know how male and female are associate to exp2 and exp3
% e.g. at aggregate level:
hired :- exp3.
exp3 :- exp2, age > 40.
male = female : ?hired.

exp3 :- female. [.6]
female :- exp3. [.3]
exp3 :- male. [.2]
male :- exp3. [.2]

% by looking at those values we can understand at what level there is the maximal usage of the sex information in order to take a choice (e.g. age) and to what extent this preference occur.
% we might decide to accept it. [then we have].

% ---------- syntax control
% Specification program

module1 {
	hired :- gender(Gender), work(Work), Gender = male, work > 5.
}
module2 {
	hired :- work(Work), work > 5.
}
male = female : ?hired.

% Console input
?- hired.

% module1 is taken out.
% module2 is put in.
% ASP solver produces the answer.

% ---------- semantic control
% Specification program

module1 {
	hired :- gender(Gender), work(Work), Gender = male, work > 5.
}
module2 {
	hired :- work(Work), work > 5.
}
male = female : ?hired.
#reference [dataset].

% you need to construct for all the factors used in the module, how they connect with male and female.
% gender is evident as it is in your columns
% work you need to study the relative frequences in your dataset
module1 {
	hired :- gender(Gender), work(Work), Gender = male, work > 5.
}
module2 {
	hired :- work_exp.
	work_exp :- work(Work), work > 5.
}
male = female : ?hired.
reference {
	work_exp :- male [.6].
	work_exp :- female [.2].
}
