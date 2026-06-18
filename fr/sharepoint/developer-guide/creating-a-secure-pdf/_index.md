---
title: Créer un PDF sécurisé dans SharePoint
linktitle: Création d'un PDF sécurisé
type: docs
weight: 60
url: /fr/sharepoint/creating-a-secure-pdf/
lastmod: "2026-06-18"
description: En utilisant l'API PDF SharePoint, vous pouvez créer des PDF sécurisés et chiffrés et spécifier leurs mots de passe dans SharePoint.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint prend en charge la création de PDF sécurisés. L'installation d'Aspose.PDF for SharePoint ajoute une option **PDF Secure Settings** dans les Paramètres du site. Ici, vous pouvez définir le mot de passe utilisateur, le mot de passe propriétaire et toute valeur de la liste d'algorithmes pour chiffrer le PDF de sortie. La liste d'algorithmes offre différentes combinaisons d'algorithmes de chiffrement et de tailles de clé. Transmettez la valeur de votre choix.

Cet article montre comment utiliser Aspose.PDF for SharePoint pour générer un PDF chiffré.

{{% /alert %}}

## **Création d'un PDF sécurisé**

Pour démontrer la fonctionnalité, nous configurons d'abord l'option **PDF Secure Setting** pour le mot de passe propriétaire et le mot de passe utilisateur ainsi que l'algorithme de chiffrement. L'exemple fusionne ensuite deux documents provenant d'une bibliothèque de documents.

### **Paramétrage des options PDF Secure Setting**

Ouvrez l'option **PDF Secure Settings** depuis les Paramètres du site et définissez l'algorithme, le mot de passe propriétaire et le mot de passe utilisateur.

Spécifiez des mots de passe utilisateur et propriétaire différents lors du chiffrement du fichier PDF.

- Le mot de passe utilisateur, s'il est défini, est celui que vous devez fournir pour ouvrir un PDF. Acrobat Reader demande à l'utilisateur de saisir le mot de passe utilisateur. S'il est incorrect, le document ne s'ouvre pas.
- Le mot de passe propriétaire, s'il est défini, contrôle des autorisations telles que l'impression, la modification, l'extraction, les commentaires, etc. Acrobat Reader interdit ces fonctionnalités en fonction des paramètres d'autorisation. Acrobat nécessite ce mot de passe si vous souhaitez définir/modifier les autorisations.

![todo:image_alt_text](creating-a-secure-pdf_1.png)

### **Fusionner des documents**

Fusionnez deux documents en utilisant l'option **Convert to PDF**. Cette fonctionnalité fusionne plusieurs fichiers non PDF (HTML, texte ou image) en un fichier PDF.

1. Ouvrez une bibliothèque de documents et sélectionnez les documents souhaités dans la liste.

![todo:image_alt_text](creating-a-secure-pdf_2.png)


1. Utilisez l'option **Merge to PDF** de Library Tools pour enregistrer le fichier de sortie. Vous êtes invité à enregistrer le fichier de sortie sur le disque.

![todo:image_alt_text](creating-a-secure-pdf_3.png)

### **Sortie**

Le fichier de sortie est chiffré.

![todo:image_alt_text](creating-a-secure-pdf_4.png)

