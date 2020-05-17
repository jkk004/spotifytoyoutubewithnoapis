import requests
import re

print("Please copy and paste your spotify link here (make sure the playlist is public, for obvious reasons): ")
print("Also don't forget to press enter after you input the link. You will have to press space after your link and then enter. If not it will just go to a webpage of your playlist without running any code")
link = str(input())

final_output = []
song_names = []
artist = []
combined = []
conv_links = []
f = requests.get(link)
leng = [m.start() for m in re.finditer('"track-name"', f.text)]

def song_name_generator(i):
    res = [m.start() for m in re.finditer('"track-name"', f.text)]
    check = ""
    tally = 0
    for j in range(res[i],res[i]+100):
        if f.text[j] == "<":
            tally += 1
        if f.text[j] == "&":
            tally -= 1
        if tally == 1:
            check += f.text[j]
        if tally == 2:
            break
        if f.text[j] == ";":
            tally += 1
        if f.text[j] == ">":
            tally += 1
    song_names.append(check)
def artist_generator(i):
    res1 = [m.start() for m in re.finditer('</span></a> ', f.text)]
    check1 = ""
    tally = 0
    for z in range(res1[i]-19,res1[i]):
        if f.text[z] == "<":
            tally += 1
        if tally == 2:
            break
        if tally == 1:
            check1 += f.text[z]
        if f.text[z] == ">":
            tally += 1
    artist.append(check1)
for i in range(len(leng)):
    song_name_generator(i)
    artist_generator(i)
    combined.append(song_names[i] + " " + artist[i] + " official")

#for comb in combined:
#    check = ""
#    results = YoutubeSearch(str(comb), max_results=10).to_json()
#    loc = results.index("/watch")
#    for i in range(loc,loc + 100):
#        tally = 1
#        if results[i] == '"':
#            tally += 1
#            break
#        if tally == 1:
#            check += results[i]
#    conv_links.append("https://www.youtube.com" + check)
for comb in combined:
    check = ""
    r = requests.get("https://www.youtube.com/results?search_query=" + comb)
    results = r.text
    loc = results.index("/watch")
    for i in range(loc,loc + 100):
        tally = 1
        if results[i] == '"':
            tally += 1
            break
        if tally == 1:
            check += results[i]
    conv_links.append("https://www.youtube.com" + check)
for i in range(len(combined)):
    final_output.append(combined[i] + " " + conv_links[i])

for i in final_output:
    print(i)
