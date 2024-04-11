def greetings(name_lst, job_dict):
    full_name = ' '.join(name_lst)
    title_occupation = job_dict.get('title') + ' ' + job_dict.get('occupation')
    return f'Hello, {full_name}! Nice to have a {title_occupation} around.'
    




greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.   