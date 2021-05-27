% Rule
adult(Person) :- age(Person, X), X > 17.

% Data
age(zack, 11).
gender(zack, male).

age(cody, 18).
gender(cody, male).

age(sarah, 5).
gender(sarah, female).

age(brock, 32).
gender(brock, male).

age(nicole, 22).
gender(nicole, female).

 % each sampled answer set represents exactly one random person
1{thePerson(zack); thePerson(cody); thePerson(sarah); thePerson(brock); thePerson(nicole)}1.

thePersonIsAdultFemale :- thePerson(X), gender(X, female), adult(X).

thePersonIsAdultMale :- thePerson(X), gender(X, male), adult(X).

_eval_("f(thePersonIsAdultFemale)", "?").

_eval_("f(thePersonIsAdultMale)", "?").
