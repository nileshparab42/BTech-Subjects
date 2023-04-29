female(devi).
female(sangita).
female(poonam).
female(riya).
female(rushali).

male(ram).
male(arvind).
male(vinay).
male(ronak).

parent(devi,vinay).
parent(devi,sangita).
parent(ram,vinay).
parent(ram,sangita).
parent(vinay,riya).
parent(poonam,riya).
parent(arvind,rushali).
parent(sangita,rushali).
parent(arvind,ronak).
parent(sangita,ronak).

mother(X,Y):-parent(X,Y),female(X).
father(X,Y):-parent(X,Y),male(X).
sister(X,Y):-parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.
grandmother(X,Z):-mother(X,Y),parent(Y,Z).
grandfather(X,Z):-father(X,Y),parent(Y,Z).
siblings(X,Y):-(brother(X,Y);sister(X,Y)),X\==Y.
uncle(X,Y):-parent(Z,Y),brother(X,Z).
aunty(X,Y):-parent(Z,Y),sister(X,Z).
cousin(X,Y):-parent(A,X),parent(B,Y),siblings(A,B).


