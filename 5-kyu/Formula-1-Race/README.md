You are a big fan of Formula 1.

There was a race last week-end, but ... you missed the live TV. You picked on the internet a list of the events during the race, and you want to get your champion's rank at the end of the race.

An event is a pilot ID followed by a type. There are two types of events:

'O' : a pilot is overtaking the one just in front of him
'I' : a pilot had an incident... and is forced to quit the race (and subsequently all pilots after this one gain one rank)
The list of events is passed as a string where events are separated with a space, first event first. e.g: "2 O 12 I" means the pilot#2 overtook, then the pilot#12 had an incident.

Your function will return the rank of your champion at the end of the race, given your champion's ID (as int) and the list of events. Return -1 if your champion had an incident.

NOTES:

there are 20 positions when the race starts (from 1 to 20, 1 being the one in front),
each pilot ID is his position when the races starts,
all events in entry lists are syntactically valid.
Final tests contains about 20 fixed events, and 100 random tests with race length between 10 to 30 events. In the tests (fixed and random): the leading pilot never overtakes, and after having an incident, the pilot never appears in further events.

Enjoy !

Thanks to the Best french developer Contest 2019

