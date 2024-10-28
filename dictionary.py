meme_dict = {
"CRINGE": "Something strange or embarrassing",
"LOL": "A response to something funny",
"MINECRFT" : "The craft is mine",
'ROLEPLAY' : 'Role play',
'EZ' : 'To humiliate an opponent',
'AFK' : 'Taking a break from the game when the game starts'
}
word = input("enter words")
if word in meme_dict.keys():
print(meme_dict[word])
else:
print('word not in list')
