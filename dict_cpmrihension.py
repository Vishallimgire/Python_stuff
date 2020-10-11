users = [
    ('vishal', 12),
    ('saurabh', 13),
    ('suraj', 14),
    ('alen', 15),
    ('mahesh', 16)
]

filter_dict = [{'user':name,'Roll':roll } for name, roll in users]
print(filter_dict)