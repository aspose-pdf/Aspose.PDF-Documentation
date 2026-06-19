---
title: Table des matières Liste des tableaux ou des figures
linktitle: Table des matières Liste des tableaux ou des figures
type: docs
weight: 10
url: /fr/reportingservices/table-of-contents-list-of-tables-or-figures/
description: Apprenez comment ajouter une table des matières, une liste des tableaux ou des figures dans les rapports PDF en utilisant Aspose.PDF for Reporting Services.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Designer ne prend pas en charge l’ajout d’une table des matières aux documents de rapport. Avec Aspose.Pdf for Reporting Services, vous pouvez facilement indiquer au rendu PDF de produire des documents PDF avec une table des matières, ou une liste des tableaux ou des figures. Vous pouvez le faire en suivant les étapes suivantes :

{{% /alert %}}

{{% alert color="primary" %}}
Assurez-vous que le fichier Aspose.Pdf.ListSectionStyle.xml existe dans ```<Instance>```/bin, où ```<Instance>``` est le répertoire du serveur de rapports. Si le fichier n'existe pas, créez-le dans le ```<Instance>```Répertoire /bin et placez le balisage suivant à l'intérieur.

## Table des matières

**Exemple**

```cs
<ListSection ListType="TableOfContents">
              <Title Alignment="Center">
            <Segment IsTrueTypeFontBold="true" FontSize="30">TableOfContents</Segment>
              </Title>
              <ListLevelFormat Level="1" LeftMargin="0">
            <TextInfo IsTrueTypeFontBold="true" IsTrueTypeFontItalic="true"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="2" LeftMargin="10">
            <TextInfo IsUnderline="true" FontSize="10"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="3" LeftMargin="20">
            <TextInfo IsTrueTypeFontBold="true"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="4" LeftMargin="30">
            <TextInfo IsTrueTypeFontBold="true"></TextInfo>
              </ListLevelFormat>
</ListSection>
```

##  Liste des tables

**Exemple**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Liste des figures

**Exemple**

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Veuillez vous référer à la section 'Working with TOC' de la documentation en ligne d'Aspose.Pdf.

**2-** Ajoutez le paramètre de rapport 'IsListSectionSupported' et définissez la valeur sur True comme indiqué dans le paragraphe 'List Section'.
**3-** Ajoutez une propriété personnalisée pour l'élément de rapport que vous souhaitez voir répertorié dans la Table des matières, la Liste des tableaux ou la Liste des figures.

{{% /alert %}}

{{% alert color="primary" %}}

**Nom de la propriété personnalisée** :IsInList
**Valeur de la propriété** :Boolean
**Valeur de la propriété personnalisée** : Vrai ou Faux

{{% alert color="primary" %}}

Marque l'élément de rapport actuel comme répertorié par index dans la table des matières, ou la liste des tableaux ou des figures.

{{% /alert %}}

**Nom de la propriété personnalisée** : Titre
**Type de propriété personnalisée** : Chaîne

{{% alert color="primary" %}}

Le titre de l'élément affiché dans la table des matières, la liste des tableaux ou des figures.
{{% /alert %}}

**Nom de la propriété personnalisée** : NiveauListe
**Type de propriété personnalisée** : Entier

{{% alert color="primary" %}}

Le niveau des éléments répertoriés affichés dans la table des matières.

{{% /alert %}}

{{% /alert %}}

