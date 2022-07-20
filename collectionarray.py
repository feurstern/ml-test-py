#List
myLanguagePreferences=["Germany", "Japan", "Australia", "New Zealand", "China"]
print(myLanguagePreferences[4])
#change itme of list
myLanguagePreferences[4]="Japan"
print(myLanguagePreferences[4])
#change range list
myLanguagePreferences[1:2]=["Russia","Turky"]
print(myLanguagePreferences)
#Count the list
print(len(myLanguagePreferences))
# Add list Item 
myLanguagePreferences.append("South Korea")
print(myLanguagePreferences)
# Another alternative ways to add list item
myLanguagePreferences.insert(4,"USA")
print(myLanguagePreferences)
# Alternative ways to add list item
anotherLanguagpreferences = list(("United Kingdom"))
myLanguagePreferences.extend(anotherLanguagpreferences)
print(myLanguagePreferences)

thisUserAge = list((23,30,40,50)) 
userProfile = list(("Hatsune Miku", "Nazi Germany"))



