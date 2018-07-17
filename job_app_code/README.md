Greetings, 

I'll try and sum up my methodology for the grocery store app made. 
I generally try to mimic real life as best as I can when coding even 
if it doesn't account for the fastest computational time. My reason for
this more deals with that I would like to work with AI one day and my 
impression is that artificial cognitive thought should follow reality 
more than simplicity (if that makes any sense).

So, in the context of this project, it would've been a lot easier to have made
a grocery object and then just allow the user to grab that object and put it in
his/ her cart. I decided instead to create an object which accounted for the total
inventory of an item in the store. For example, I made it there were maximum 50 apples
and so if a person requested 51, the code would shoot back that there were not enough
apples in inventory for this request. This equated ultimately to me "copying" the 
contents of an object and creating a new one which would go into cart itself (since I
don't think that "splitting" an object is possible). 

I also wanted to add a bit more authenticity to the store by creating aisles and subcategorizing
the objects to a given aisle. This way, one wouldn't see all the items in the store at once
but instead see all of the available groceries in a given aisle at a time. 

Other than that, the app works as one would expect: adding, removing, clearing the cart,
viewing the cart (and sorting) all work. The difference comes down to the checkout methods.

I wanted to include for cash and credit options. I implemented two separate bits of code
I had already written: one for giving change back when purchasing an item and the other
to check if a credit card number is valid. The method for the later doesn't work for every
card. It is based on the Luhn Algorithm. In the code, I have a print line which offers up
for example a working number. You are free to try one of yours yourself. Out of four of 
my credit cards, one of them did actually work which was pretty cool (note: it is not the 
sample one in case you were wondering.)