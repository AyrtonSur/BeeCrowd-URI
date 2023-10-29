a,g,ra,rg=map(float, input().split())
pa=ra/a
pg=rg/g
if pa>pg:
    print('A')
elif pa<=pg:
    print('G')
