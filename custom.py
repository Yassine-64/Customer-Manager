Nombre_client = int(input("Veuillez entrer le nombre de clients :"))
for i in range(1, Nombre_client + 1):
    nom_client = input(f"Donner le nom et prénom du client n{i} :")
    n_article = int(input(f"Donner le nombre d’articles pour le client {nom_client} :"))
    Montant_client = 0
    for j in range(1, n_article + 1):
        prix_article = float(input(f"Donner le prix de l’article {j} :"))
        Montant_ht = prix_article
        remise = Montant_ht * 0.02
        Montant_ttc = Montant_ht + (Montant_ht * 0.15)
        Montant_client += Montant_ttc
    print("Facture")
    print(f"Le Total à payer pour le client {nom_client} est : {Montant_client} DH")
