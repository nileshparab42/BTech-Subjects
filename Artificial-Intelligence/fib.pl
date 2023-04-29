male(sushil).
male(yogesh).
male(ashok).
male(nilesh).
male(harsh).

female(sulbha).
female(tanuja).
female(asha).
female(akshaya).

parent(sulbha,yogesh).
parent(sushil,yogesh).
parent(sulbha,asha).
parent(sushil,asha).
parent(ashok,nilesh).
parent(asha,nilesh).
parent(yogesh,harsh).
parent(yogesh,akshaya).
parent(tanuja,harsh).
parent(tanuja,akshaya).

mother(X,Y):-parent(X,Y),female(X).
father(X,Y):-parent(X,Y),male(X).
grandmother(Z,X):- mother(Z,Y),parent(Y,X).
sister(X,Y):-parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.
siblings(X,Y):- (brother(X,Y);sister(X,Y)),X\==Y.
uncle(X,Y):-parent(Z,Y),brother(X,Z).
aunty(X,Y):-parent(Z,Y),sister(X,Z).
