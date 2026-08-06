---
title: Création et exportation d'un modèle
linktitle: Création et exportation d'un modèle
type: docs
weight: 10
url: /fr/sharepoint/creating-and-exporting-template/
lastmod: "2020-12-16"
description: Vous pouvez créer et exporter des modèles au format PDF dans SharePoint à l'aide de l'API PDF SharePoint.
---

{{% alert color="primary" %}}

Cet article montre comment créer et exporter des modèles à l'aide d'Aspose.PDF pour SharePoint.

Depuis Aspose.PDF pour SharePoint 1.9.2, la prise en charge des modèles PDF couvre également les sous-sites SharePoint.

{{% /alert %}}

## Création et exportation de modèles

{{% alert color="primary" %}}

Pour utiliser la fonctionnalité d'exportation Aspose.PDF pour SharePoint, créez d'abord une liste qui utilise des « Modèles PDF ».

Création d'une liste qui utilise des modèles PDF :

![Créer une liste de modèles PDF](creating-and-exporting-template_1.png)

Deux modèles de documents, les modèles de formulaire de tâches et les modèles de liste de tâches, sont créés :

![Modèles de documents](creating-and-exporting-template_2.png)

Le formulaire modèle vous permet de saisir les informations suivantes :

- **Nom** : le nom du fichier du modèle.
- **Titre** : le titre du modèle. (Par défaut, identique au nom du fichier.)
- **Description** : une description du modèle. Une bonne description rend le modèle plus facile à utiliser.
- **Types de liste attribués** : ID de liste séparés par des virgules (liés au modèle. Ce champ peut également contenir la valeur
- **Tous les types de liste**. Ce champ n'est applicable que lorsque le champ **Type** est défini sur **Liste**).
- **Types de contenu attribués** : ID de type de contenu séparés par des virgules et liés au modèle. Ce champ peut contenir la valeur **AllListTypes**. Ce champ n'est applicable que lorsque le champ **Type** est défini sur **Item**.
- **Type** : soit un modèle de liste, soit un modèle d'élément.
- **Statut** : les options sont actives, inactives (invisibles pour tous) et débogage (visibles uniquement pour les administrateurs).

Le formulaire Modèles de liste de tâches :

![Modèles de liste de tâches](creating-and-exporting-template_3.png)

Le formulaire Modèles de formulaire de tâches :

![Modèles de formulaires de tâches](creating-and-exporting-template_4.png)

Une fois enregistrés, les nouveaux modèles apparaissent dans la liste des modèles, prêts à être utilisés :

Deux modèles de liste de tâches :*

![Modèles de liste de tâches](creating-and-exporting-template_5.png)

Un modèle de formulaires de tâches :

![Modèles de formulaires de tâches](creating-and-exporting-template_6.png)

### Développement de modèles

Un modèle est un fichier XML basé sur Aspose XML PDF. Pour créer un modèle de liste, placez des marqueurs spéciaux liés au nom interne du champ de type de contenu cible SharePoint dans le fichier PDF XML.

### Marqueurs

- **SPListItemsCount** – remplacé par le nombre d'éléments de liste.
- **SPListTitle** – remplacé par le titre de la liste.
- **SPTableIterator** – placé dans la première cellule du tableau et marque le tableau pour une itération complète.
- **SPRowIterator** – placé dans la première cellule du tableau et marque le tableau pour l'itération des lignes.
- **SPField** – remplacé par le champ valeur de l'élément.

Pour référence, veuillez télécharger [fichiers XML de modèle](attachments/8421394/8618082.zip).

### Exporter au format PDF

Lorsqu'un modèle est entièrement configuré, vous êtes prêt à exporter des listes ou des éléments vers des fichiers PDF.

Exporter une liste au format PDF à l'aide d'un modèle de liste de tâches :

![Exporter au format PDF](creating-and-exporting-template_7.png)

{{% /alert %}}

