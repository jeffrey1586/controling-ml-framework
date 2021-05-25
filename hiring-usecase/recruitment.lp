% Simple example of recruiting candidates for a certain programming job

% jack
candidate(jack).
gender(jack, male). % e.g. extract from cv
bachelor(jack). % e.g. extract from cv
workyears(jack, 1). % e.g.  extract from cv
biorating(jack, 8). % e.g. rating (0-10) from ML module assesing motivation
programming(jack, moderate). % e.g. rated from programming exercise

% anna
candidate(anna).
gender(anna, female).
bachelor(anna).
master(anna).
workyears(anna, 3).
biorating(anna, 7).
programming(anna, moderate).

% elon
candidate(elon).
gender(elon, male).
master(elon).
workyears(elon, 5).
biorating(elon, 8).
programming(elon, moderate).

% becky
candidate(becky).
gender(becky, female).
highschool(becky).
workyears(becky, 4).
biorating(becky, 4).
programming(becky, advanced).


% core inference for hired candidate
hired(Candidate) :- candidate(Candidate), education(Candidate),
experience(Candidate), motivation(Candidate), not -skilled(Candidate).

% default rule for not hired candidate
-hired(Candidate) :- candidate(Candidate), not hired(Candidate).

education(Candidate) :- master(Candidate).
education(Candidate) :- bachelor(Candidate).
experience(Candidate) :- workyears(Candidate, X), X > 2.
motivation(Candidate) :- biorating(Candidate, X), X > 5. % good motivation
-skilled(Candidate) :- programming(Candidate, low). % not enough experience

% Show who is hired
#show Candidate : hired(Candidate).
#show "Candidate(s) hired:".
#show .

% Show who is not hired
%#show Candidate : -hired(Candidate).
%#show "Candidate(s) not hired:".
%#show .
