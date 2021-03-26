# Python---Poker-Game
An individual playing card is represented as a string of two characters:
•	the first character is from "23456789TJQKA" and represents the rank, i.e., the number or value of the card. (Note that 10 is encoded as letter T to make all card ranks to be single letters)
•	the second character is from "cdhs" and represents the suit (clubs, diamonds, hearts and spades respectively).

For example, "Jd" would be the jack of diamonds, and "4s" would be the four of spades.

A 'hand' is made up of five cards and is given as string encoding all those cards consecutively. For example, "Kh3h7s8h2h" represents a five-card hand that happens to have one spade and four hearts. Note that the cards can be listed inside the string in any order, not necessarily sorted by suit or rank. The suits and ranks are also case sensitive, with the rank always given as a digit or an uppercase letter, and the suit always given as a lowercase letter from the four possible letters cdhs.

The program has a function evaluate(hand) that identifies and returns what kind of poker hand is represented by the 10-character string hand. There are six (and only six) types of hands that are recognized:
(1)	four of a kind -- four cards have the same rank (it is not possible to have five cards with the same rank)
(2)	full house -- two cards have one same rank and three cards have another same rank
(3)	flush -- all five cards have the same suit
(4)	three of a kind -- three cards (not more) have the same rank
(5)	pair -- two cards (not more) have the same rank
(6)	<highest rank> high -- none of (1) - (5) applies, so you return just the highest rank in the hand followed by the word 'high'. For example, '9 high' or 'K high'. Rank increases from left to right  in "23456789TJQKA".
 
The program assumes that every input is correct, so it does not perform any error check or recover from illegal input.

An example run of the program might look like the following, with the values of hand followed by the string that evaluate(hand) returns:

Qs7s2s4s5s - flush 
7h8hKsTs8s - pair 
2h4d2d4s4c - full house 
KsKhKc8sKd - four of a kind 
3s9hTh9s9d - three of a kind 
2s8hThQs9d - Q high 
