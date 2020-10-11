import yaml

with open('config.dat') as f:
    
    docs = yaml.load(f, Loader=yaml.FullLoader)
    print(docs)
    docs.append('mumbai')

with open('config.dat', 'w') as file:
     yaml.safe_dump(docs, file)
    
    # for doc in docs:
        
    #     for k, v in doc.items():
    #         print(k, "->", v)
