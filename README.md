# TO DO IN THIS PROJECT

Une épicerie souhaite disposer d'une application informatique pour la gestion de ses tâches quotidiennes. L'analyse nous a conduit à produire les fichiers suivants :

### Produit (RéférencePro, DesignationPro, PrixPro, QuantiteStock)

### Ventes (DateVente, ReferencePro, QuantiteVendue)

### Entrees (DateEntree, Quantite, ReférencePro, RaisonSocialeFournisseur)

Remarque :

· Deux produits ne peuvent pas avoir la même désignation

## Votre application doit fournir un menu général qui permet à l'épicier d'accéder aux différentes fonctionnalités offertes par l'application. Soit :

### La gestion des produits

### La gestion des entrées de produits

### La vente de produits

### L'état des ventes

---

## La gestion de produits permet de :

· _Créer un produit_ : A la création d'un produit, la quantité en stock est égale à 0

· _Modifier un produit_

· _Supprimer un produit_

· _Rechercher un produit par code ou par désignation_

· _Afficher les produits en rupture de stock_

### **La gestion des entrées** :

permet d'enregistrer une entrée en stock d'un produit (vérifier que les produits fournis existent au niveau du fichier "produits.txt" et mettre à jour le stock

### **La gestion des ventes** :

permet d'enregistrer une opération de vente (la quantité vendue doit être disponible en stock et une fois la vente enregistrées la quantité en stock pour le produit vendu doit être mise à jour)

### **L'état des ventes**

affiche pour chaque produit les ventes effectuées

# HOW TO RUN THIS ?

1 - clone the repo
2 - pip3 install -r requirements.txt
3 - python3 main.py
