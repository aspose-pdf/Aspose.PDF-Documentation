---
title: Utilisation de FloatingBox pour la génération de texte
linktitle: Utilisation de FloatingBox
type: docs
weight: 30
url: fr/net/floating-box/
description: Cette page explique comment formater le texte à l'intérieur d'une boîte flottante.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Cette fonctionnalité fonctionne également dans la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Bases de l'utilisation de l'outil FloatingBox

L'outil Floating Box est un outil spécial pour placer du texte et d'autres contenus sur une page PDF. Sa principale caractéristique est le rognage du texte lorsqu'il dépasse la taille de la FloatingBox.

```cs
Document document = new Document();
Page page = document.Pages.Add();
var box = new FloatingBox(400, 30)
{
    Border = new BorderInfo(BorderSide.All, 1.5f, Color.DarkGreen),
    IsNeedRepeating = false,
};
var text = LoremNET.Lorem.Paragraph(20, 6);
box.Paragraphs.Add(new TextFragment(text));
page.Paragraphs.Add(box);
```  

Dans l'exemple ci-dessus, nous créons une FloatingBox avec une largeur de 400 pt et une hauteur de 30 pt.
Également, dans cet exemple, plus de texte a été créé intentionnellement que ce qui pourrait tenir dans la taille donnée.
En conséquence, le texte a été coupé.

![Image 1](image01.png)

La propriété `IsNeedRepeating` avec la valeur `false` limite le texte à 1 page.

Si nous définissons cette propriété sur `true`, le texte sera reflué à la page suivante dans la même position.

![Image 2](image02.png)

## Fonctionnalités avancées de FloatingBox

### Support multi-colonnes

#### Mise en page multi-colonnes (cas simple)

`FloatingBox` prend en charge la mise en page multi-colonnes. Pour créer une telle mise en page, vous devez définir les valeurs des propriétés ColumnInfo.

* `ColumnWidths` est une chaîne avec énumération de largeur en pt.
* `ColumnSpacing` est une chaîne avec la largeur de l'écart entre les colonnes.
* `ColumnCount` est un nombre de colonnes.

```cs
Document document = new Document();
Page page = document.Pages.Add();
page.PageInfo.Margin = new MarginInfo(36, 18, 36, 18);
var columnCount = 3;
var spacing = 10;
var width = page.PageInfo.Width 
    - page.PageInfo.Margin.Left 
    - page.PageInfo.Margin.Right 
    - (columnCount - 1) * spacing;
var columnWidth = width / 3;
var box = new FloatingBox()
{
    IsNeedRepeating = true
};
box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
box.ColumnInfo.ColumnSpacing = "{spacing}";
box.ColumnInfo.ColumnCount = columnCount;
var paragraphs = LoremNET.Lorem.Paragraphs(20, 8, 20);
foreach (var paragraph in paragraphs)
{
    box.Paragraphs.Add(new TextFragment(paragraph));
}

page.Paragraphs.Add(box);

document.Save("sample.pdf");
```
Nous avons utilisé la bibliothèque supplémentaire LoremNET dans l'exemple ci-dessus et créé 20 paragraphes. Ces paragraphes ont été divisés en trois colonnes et ont rempli les pages suivantes jusqu'à ce que le texte soit épuisé.

#### Mise en page multi-colonnes avec démarrage de colonne forcé

Nous ferons de même avec l'exemple suivant comme le précédent. La différence est que nous avons créé 3 paragraphes. Nous pouvons forcer FloatingBox à rendre chaque paragraphe dans la nouvelle colonne. Pour cela, nous devons définir `IsFirstParagraphInColumn` lorsque nous ajoutons du texte à l'objet FloatingBox.

```cs
Document document = new Document();
Page page = document.Pages.Add();
page.PageInfo.Margin = new MarginInfo(36, 18, 36, 18);
var columnCount = 3;
var spacing = 10;
var width = page.PageInfo.Width 
    - page.PageInfo.Margin.Left 
    - page.PageInfo.Margin.Right 
    - (columnCount - 1) * spacing;
var columnWidth = width / 3;
var box = new FloatingBox()
{
    IsNeedRepeating = true
};
box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
box.ColumnInfo.ColumnSpacing = "{spacing}";
box.ColumnInfo.ColumnCount = 3;

var paragraphs = LoremNET.Lorem.Paragraphs(20, 8, 3);
foreach (var paragraph in paragraphs)
{
    var text = new TextFragment(paragraph)
    {
        IsFirstParagraphInColumn = true
    };
    box.Paragraphs.Add(text);
}

page.Paragraphs.Add(box);

document.Save("sample.pdf");
```
### Support de fond

Vous pouvez définir la couleur d'arrière-plan souhaitée en utilisant la propriété `BackgroundColor`.

```cs
// Initialiser l'objet document
Document document = new Document();
Page page = document.Pages.Add();
var box = new FloatingBox(400, 60)
{
    IsNeedRepeating = false,
    BackgroundColor = Color.LightGreen,
};
var text = LoremNET.Lorem.Paragraph(20, 6);
box.Paragraphs.Add(new TextFragment(text));
page.Paragraphs.Add(box);
```

### Support de décalage

FloatingBox peut être déplacé vers un autre emplacement en définissant les valeurs `Top` et `Left`.

```cs
Document document = new Document();
Page page = document.Pages.Add();

var box = new FloatingBox()
{
    Top = -45,
    Left = 15,
    Border = new BorderInfo(BorderSide.All, 1.5f, Color.DarkGreen)
};
var text = LoremNET.Lorem.Paragraph(20, 6);
box.Paragraphs.Add(new TextFragment(text));

page.Paragraphs.Add(new TextFragment(LoremNET.Lorem.Paragraph(20, 6)));
page.Paragraphs.Add(box);            
page.Paragraphs.Add(new TextFragment(LoremNET.Lorem.Paragraph(20, 6)));
```

