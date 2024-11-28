import wikipedia

def get_pages_of_wiki(title):
  try:
    stranica = wikipedia.page(title,auto_suggest=False)
    stranica_tekst = stranica.content
    return stranica_tekst
  except Exception as e:
    print(e)
    print(title)
    return ""


titlovi_tema1 = ["Nikola Tesla","Ivo Andric","Milutin Milanković","Mihajlo Pupin","Mileva Marić","Meša Selimović","Serbia","Yugoslavia","Isidora Sekulić","Gavrilo Princip","Alexander I of Yugoslavia","Prince Paul of Yugoslavia","Nikola Pašić","Miloš Crnjanski","Ivan Meštrović"] # Značajni ljudi i događaji u prvoj polovini 20. veka u Srbiji/Jugoslaviji
titlovi_tema2 = ["Thomas Edison","Albert Einstein","Alexander Graham Bell","Mark Twain","John Jacob Astor IV","Great Depression","New York City","Olivia Langdon Clemens","William Faulkner","John Steinbeck","Franklin D. Roosevelt","Henry Ford","J. Robert Oppenheimer","Zora Neale Hurston"] # Značajni ljudi i događaji u prvoj polovini 20. veka u Americi
titlovi_tema3 = ["Fountain (Duchamp)","Marcel Duchamp","Man Ray","Pablo Picasso","Jackson Pollock","Andy Warhol","Banksy","Frida Kahlo","Mark Rothko","Stenberg brothers","Roy Lichtenstein","René Magritte","The Kiss (Klimt)","Barnett Newman"] # Savremena umetnost sa naglaskom na polovinu 20. veka
titlovi_tema4 = ["World War II","Attack on Pearl Harbor","Operation Overlord","Battle of Stalingrad","Battle of Berlin","Allies of World War II","Axis powers","Case White","Case Black","German bombing of Belgrade","Operation Rösselsprung","Atomic bombings of Hiroshima and Nagasaki","Manhattan Project"] # Drugi svetski rat

titlovi_tema_svi = titlovi_tema1+titlovi_tema2+titlovi_tema3+titlovi_tema4

tekstovi = [get_pages_of_wiki(t) for ind,t in enumerate(titlovi_tema_svi)]

for ind in range(len(titlovi_tema_svi)):
  with open("wiki_tekstovi/"+titlovi_tema_svi[ind].replace(" ","_")+".txt","w") as f:
    f.write(tekstovi[ind])

with open("wiki_tekstovi/titlovi.txt","w") as f:
  f.write("\n".join(titlovi_tema_svi))