from spotify import dataset

total = 0 #Nombre total d'utilisateurs
churned = 0 #Nombre d'utilisateurs churned

for record in dataset:
    total += 1
    if record['is_churned'] == '1':
        churned = churned + 1
churn_rate = churned / total * 100
print(f"Taux de churn: {churn_rate:.2f}% ({churned} churned sur {total} utilisateurs)")