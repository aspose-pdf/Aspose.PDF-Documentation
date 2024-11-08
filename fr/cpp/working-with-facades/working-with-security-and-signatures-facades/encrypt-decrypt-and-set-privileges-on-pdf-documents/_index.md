---
title: Chiffrer, Déchiffrer et définir des privilèges sur les documents PDF
type: docs
weight: 10
url: /fr/cpp/encrypt-decrypt-and-set-privileges-on-pdf-documents/
---

## <ins>**Définir des Privilèges sur un Fichier PDF Existant**
Pour définir des privilèges sur un document PDF existant, vous pouvez utiliser la méthode **Document->Encrypt(...)**, qui prend un objet **DocumentPrivilege**. Une classe **DocumentPrivilege** est utilisée pour définir différents privilèges pour accéder au document PDF. De plus, il y a 4 façons suivantes d'utiliser cette classe :

1. En utilisant directement un privilège prédéfini.
1. Basé sur un privilège prédéfini et changer certaines autorisations spécifiques.
1. Basé sur un privilège prédéfini et changer une combinaison de certaines autorisations Adobe Professional spécifiques.
1. Mélange les façons 2 et 3.

Le code suivant démontrera les 4 manières ci-dessus de définir les privilèges des documents :