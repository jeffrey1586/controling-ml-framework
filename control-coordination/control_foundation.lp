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
