---
title: Création et Exportation de Modèle
type: docs
weight: 10
url: /fr/sharepoint/creating-and-exporting-template/
lastmod: "2020-12-16"
description: Vous pouvez créer et exporter des modèles en PDF dans SharePoint en utilisant PDF SharePoint API.
---

{{% alert color="primary" %}}

Cet article montre comment créer et exporter des modèles en utilisant Aspose.PDF pour SharePoint.

À partir de Aspose.PDF pour SharePoint 1.9.2, le support des modèles PDF couvre également les sous-sites SharePoint.

{{% /alert %}}

## **Création et Exportation de Modèles**
{{% alert color="primary" %}}

Pour utiliser la fonctionnalité d'exportation d'Aspose.PDF pour SharePoint, commencez par créer une liste qui utilise “PDF Templates”.

Créer une liste qui utilise des PDF Templates :

![todo:image_alt_text](creating-and-exporting-template_1.png)

Deux modèles de documents, Modèles de Formulaire de Tâche et Modèles de Liste de Tâches sont créés :

![todo:image_alt_text](creating-and-exporting-template_2.png)

Le formulaire de modèle vous permet de saisir les informations suivantes :

- **Name**: le nom de fichier du modèle.
- **Title**: le titre du modèle.
 - **Description**: une description du modèle. Une bonne description rend le modèle plus facile à utiliser.
- **Assigned List Types**: liste d'IDs séparés par des virgules (liés au modèle. Ce champ peut également contenir la valeur **AllListTypes**. Ce champ est applicable uniquement lorsque le champ **Type** est défini sur **List**).
- **Assigned Content Types**: liste d'IDs de type de contenu séparés par des virgules (liés au modèle. Ce champ peut être défini sur **AllListTypes**. Ce champ est applicable uniquement lorsque le champ **Type** est défini sur **Item**.
- **Type**: soit modèle de liste, soit modèle d'élément.
- **Status**: les options sont actif, inactif (invisible pour tous), et débogage (visible uniquement pour les administrateurs).

**Le formulaire des modèles de liste de tâches :**

![todo:image_alt_text](creating-and-exporting-template_3.png)




**Le formulaire des modèles de formulaire de tâche :**

![todo:image_alt_text](creating-and-exporting-template_4.png)




Une fois enregistrés, les nouveaux modèles apparaissent dans la liste des modèles, prêts à être utilisés :


**Deux modèles de liste de tâches :**
![todo:image_alt_text](creating-and-exporting-template_5.png)

**Un modèle de formulaire de tâche :**

![todo:image_alt_text](creating-and-exporting-template_6.png)

#### **Développement de Modèles**
Un modèle est un fichier XML basé sur Aspose XML PDF. Pour créer un modèle pour une liste, placez des marqueurs spéciaux liés au nom interne du champ de type de contenu cible SharePoint dans le fichier XML PDF.
##### **Marqueurs**
- **SPListItemsCount** – remplacé par le nombre d'éléments de la liste.
- **SPListTitle** – remplacé par le titre de la liste.
- **SPTableIterator** – placé dans la première cellule du tableau et marque le tableau pour une itération complète.
- **SPRowIterator** – placé dans la première cellule du tableau et marque le tableau pour une itération de ligne.
- **SPField** – remplacé par la valeur du champ de l'élément.

Pour référence, veuillez télécharger [fichiers XML de modèle](attachments/8421394/8618082.zip).
#### **Exporter en PDF**
Lorsqu'un modèle est complètement configuré, vous êtes prêt à exporter des listes ou des éléments vers des fichiers PDF.

**Exportation d'une liste en PDF à l'aide d'un modèle de liste de tâches :**
![todo:image_alt_text](creating-and-exporting-template_7.png)

{{% /alert %}}