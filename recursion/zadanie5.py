data = 'Nam strzelać nie kazano. - Wstąpiłem na działo I spójrzałem na pole; dwieście armat grzmiało. Artyleryi ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi'
v = ({'a' : 0,'i' : 0,'o' : 0,'u' : 0, 'e' : 0, 'y' : 0, 'ę' : 0, 'ą' : 0, 'ó' : 0  })
for i in data.lower(): 
    if i in v:
        v[i] += 1
print(v)

         


        

