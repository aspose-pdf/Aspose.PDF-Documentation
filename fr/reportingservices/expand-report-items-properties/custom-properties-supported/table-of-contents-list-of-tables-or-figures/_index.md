---
title: Table des matières Liste des tableaux ou figures
linktitle: Table des matières Liste des tableaux ou figures
type: docs
weight: 10
url: /reportingservices/table-of-contents-list-of-tables-or-figures/
description: Découvrez comment ajouter une table des matières, une liste de tableaux ou des figures dans des rapports PDF à l'aide d'Aspose.PDF pour Reporting Services.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Report Designer ne prend pas en charge l'ajout de table des matières pour les documents de rapport. Avec Aspose.PDF pour Reporting Services, vous pouvez facilement demander au rendu PDF de produire des documents PDF avec une table des matières ou une liste de tableaux ou de figures. Vous pouvez le faire en procédant comme suit :

{{% /alert %}}

Assurez-vous que le fichier Aspose.Pdf.ListSectionStyle.xml existe dans le répertoire ```<Instance>```/bin, where ```<Instance>``` is the directory of the Report Server. If the file does not exist, create it in the ```<Instance>```/bin et placez le balisage suivant à l'intérieur.

## Table des matières

### Exemple

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

##  Liste des tableaux

### Exemple

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Liste des figures

### Exemple

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Veuillez vous référer à la section « Travailler avec la table des matières » de la documentation en ligne Aspose.Pdf.

**2-** Ajoutez le paramètre de rapport `IsListSectionSupported` et définissez la valeur sur True comme indiqué dans le paragraphe `List Section`.
**3-** Ajoutez une propriété personnalisée pour l'élément de rapport que vous souhaitez répertorier dans la table des matières, la liste des tableaux ou des figures.

```text
Custom Property Name: IsInList
Property Value: Boolean
Custom Property Value: True or False
```

Marque l'élément de rapport actuel comme répertorié par index dans la table des matières ou dans la liste des tableaux ou des figures.

```text
Custom Property Name: Title
Custom Property Type: String
```

Le titre de l'élément affiché dans la table des matières, la liste des tableaux ou des figures.

```text
Custom Property Name: ListLevel
Custom Property Type: Integer
```

Le niveau des éléments répertoriés affichés dans la table des matières.
