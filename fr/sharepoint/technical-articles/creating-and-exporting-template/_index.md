---
title: Création et exportation de modèle
linktitle: Création et exportation de modèle
type: docs
weight: 10
url: /fr/sharepoint/creating-and-exporting-template/
lastmod: "2026-06-18"
description: Vous pouvez créer et exporter des modèles au format PDF dans SharePoint en utilisant l'API PDF SharePoint.
---

{{% alert color="primary" %}}

Cet article montre comment créer et exporter des modèles en utilisant Aspose.PDF for SharePoint.

À partir d'Aspose.PDF for SharePoint 1.9.2, la prise en charge des modèles PDF couvre également les sous-sites SharePoint.

{{% /alert %}}

## **Création et exportation de modèles**
{{% alert color="primary" %}}

Pour utiliser la fonction d'exportation d'Aspose.PDF for SharePoint, créez d'abord une liste qui utilise “PDF Templates”.

Création d’une liste qui utilise des modèles PDF:

![todo:image_alt_text](creating-and-exporting-template_1.png)

Deux modèles de documents, Modèles de formulaire de tâche et Modèles de liste de tâche sont créés:

![todo:image_alt_text](creating-and-exporting-template_2.png)



Le formulaire du modèle vous permet de saisir les informations suivantes:

- **Name**: le nom de fichier du modèle.
- **Title**: le titre du modèle. (Par défaut, le même que le nom de fichier.)
- **Description**: une description du modèle. Une bonne description facilite l’utilisation du modèle.
- **Types de listes assignés**: IDs de listes séparés par des virgules (liés au modèle. Ce champ peut également contenir la valeur **AllListTypes**. Ce champ n'est applicable que lorsque le champ **Type** est défini sur **List**).
- **Types de contenu assignés**: IDs de types de contenu séparés par des virgules (liés au modèle. Ce champ peut être défini sur **AllListTypes**. Ce champ n'est applicable que lorsque le champ **Type** est défini sur **Item**).
- **Type** : soit un modèle de liste, soit un modèle d'élément.
- **Statut** : les options sont actif, inactif (invisible pour tous) et débogage (visible uniquement pour les administrateurs).

**Formulaire des modèles de listes de tâches** :

![todo:image_alt_text](creating-and-exporting-template_3.png)




**Formulaire des modèles de formulaires de tâches** :

![todo:image_alt_text](creating-and-exporting-template_4.png)




Lorsqu'ils sont enregistrés, les nouveaux modèles apparaissent dans la liste des modèles, prêts à être utilisés :

**Deux modèles de listes de tâches :**

![todo:image_alt_text](creating-and-exporting-template_5.png)



**Un modèle de formulaires de tâche :**

![todo:image_alt_text](creating-and-exporting-template_6.png)



#### **Développement de modèles**
Un modèle est un fichier XML basé sur Aspose XML PDF. Pour créer un modèle pour une liste, placez des marqueurs spéciaux liés au nom interne du champ du type de contenu cible SharePoint dans le fichier XML PDF.
##### **Marqueurs**
- **SPListItemsCount** – remplacé par le nombre d'éléments de la liste.
- **SPListTitle** – remplacé par le titre de la liste.
- **SPTableIterator** – placé dans la première cellule du tableau et marque le tableau pour une itération complète.
- **SPRowIterator** – placé dans la première cellule du tableau et marque le tableau pour une itération de ligne.
- **SPField** – remplacé par la valeur du champ de l'élément.

Pour référence, veuillez télécharger [fichiers XML de modèle](attachments/8421394/8618082.zip).
#### **Exporter en PDF**
Lorsque un modèle est complètement configuré, vous êtes prêt à exporter des listes ou des éléments vers des fichiers PDF.

**Exportation d'une liste vers PDF à l'aide d'un modèle de liste de tâches :**

![todo:image_alt_text](creating-and-exporting-template_7.png)

{{% /alert %}}
