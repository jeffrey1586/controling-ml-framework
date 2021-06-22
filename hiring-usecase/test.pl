% probablistic fact on workyears
0.08::workyears_0_female.
0.08::workyears_0_male.

% probablistic fact on motivation
0.083::motivation_2_female.
0.167::motivation_2_male.

% probablistic fact on motivation
0.0::workyears_4_female.
0.667::workyears_4_male.


% Rules
hired_female :- workyears_0_female, motivation_2_female, workyears_4_female.
hired_male :- workyears_0_male, motivation_2_male, workyears_4_male.
hired :- hired_female; hired_male.

% Queries
query(hired_female).
query(hired_male).
