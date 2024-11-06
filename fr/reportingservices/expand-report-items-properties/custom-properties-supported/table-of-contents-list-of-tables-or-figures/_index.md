---
title: Table des Matières Liste des Tableaux ou Figures
type: docs
weight: 10
url: fr/reportingservices/table-of-contents-list-of-tables-or-figures/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Le Concepteur de rapports ne prend pas en charge l'ajout de table des matières pour les documents de rapport. Avec Aspose.Pdf pour Reporting Services, vous pouvez facilement instruire le rendu PDF pour produire des documents PDF avec Table des Matières, ou Liste des Tableaux ou Figures. Vous pouvez le faire en suivant les étapes suivantes :

{{% /alert %}}

{{% alert color="primary" %}}
Assurez-vous que le fichier Aspose.Pdf.ListSectionStyle.xml existe dans ```<Instance>```/bin, où ```<Instance>``` est le répertoire du serveur de rapports. Si le fichier n'existe pas, créez-le dans le répertoire ```<Instance>```/bin et placez le balisage suivant à l'intérieur.

## Table des Matières

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

## Liste des Tables

**Exemple**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Liste des Figures

**Exemple**

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Veuillez vous référer à la section 'Travailler avec TOC' de la documentation en ligne Aspose.Pdf.

**2-** Ajoutez le paramètre de rapport 'IsListSectionSupported' et définissez la valeur sur True comme indiqué dans le paragraphe 'Liste Section'.
**3-** Ajoutez une propriété personnalisée pour votre élément de rapport que vous souhaitez lister dans la table des matières, la liste des tables ou des figures.

{{% /alert %}}

{{% alert color="primary" %}}

**Nom de la Propriété Personnalisée** :IsInList
**Valeur de la Propriété** :Boolean
**Valeur Personnalisée de la Propriété** : True ou False

{{% alert color="primary" %}}

Marque l'élément de rapport actuel comme listé par index dans la table des matières, ou la liste des tables ou figures.

{{% /alert %}}

**Custom Property Name** : Title  
**Custom Property Type** : String  

{{% alert color="primary" %}}

Le titre de l'élément affiché dans la table des matières, la liste des tableaux ou des figures.  
{{% /alert %}}

**Custom Property Name** : ListLevel  
**Custom Property Type** : Integer  

{{% alert color="primary" %}}

Le niveau des éléments répertoriés affichés dans la table des matières.  

{{% /alert %}}

{{% /alert %}}