# set some initial variables. Set the initial temperature low                                                                      
faren = -1000

# we dont want this going on forever, let's make sure we cannot have too many attempts                                                                                                                           
max_attempts = 6
attempt = 0

while faren < 100:
     # let's get the user to tell us what temperature it is                                                                                                                                                      
     newfaren = float(input("Enter the temperature (in Fahrenheit): "))
     if newfaren > faren:
             print("It's getting hotter")
     elif newfaren < faren:
             print("It's getting cooler")
     else:
         # nothing has changed, just continue in the loop                                                                                                                                                        
         continue
     faren = newfaren # now set the current temp to the new temp just entered                                                                                                                                    
     attempt += 1 # bump up the attempt number                                                                                                                                                                   
     if attempt >= max_attempts:
         # we have to bail out                                                                                                                                                                                   
         break
if attempt >= max_attempts:
     # we bailed out because of too many attempts                                                                                                                                                                
     print("Too many attempts at raising the temperature.")
else:
     # we got here because it's hot                                                                                                                                                                              
     print("it's hot here, people.")