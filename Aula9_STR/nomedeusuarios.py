lemais = ['fulano123@email.com.br']
lnomes = []
for email in lemais:
    lnomes.append(email[: email.find('@')])
print(lnomes)