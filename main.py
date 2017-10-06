



def main():
    entities = []
    with open('bibliography.bib', 'r') as f:
        counter = 0
        entity = ""
        for line in f.readlines():
            # print line
            if line.strip() == '' or line.strip()=='\n':
                continue
            entity += line
            for c in line:
                if c =='{':
                    counter+=1
                if c =='}':
                    counter-=1
            if counter == 0:
                # print "------------ "
                # print entity
                entities.append(entity)
                entity = ""

            # if line.startswith('@'):
            #     print line
        print entities

    entitiesMap = {}
    for entity in entities:
        # print entity
        if entity.startswith('@') and '{' in entity:
            keword = entity.split('{')[1].split(',')[0]
            print "keyword: "+keword
            print '*****'
            entitiesMap[keword] = entity

    with open('sortedBibliography', 'w') as sortedFile:
        for key in sorted(entitiesMap):
            print "%"+key
            print entitiesMap[key]
            sortedFile.write('%'+key+'\n')
            sortedFile.write(entitiesMap[key] + '\n')


if __name__ == '__main__':
    main()

