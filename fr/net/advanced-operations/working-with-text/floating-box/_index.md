---
title: Utilisation de FloatingBox pour la génération de texte
linktitle: Utilisation de FloatingBox
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/floating-box/
description: Cette page explique comment formater le texte à l'intérieur de la boîte flottante.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using FloatingBox for text generation",
    "alternativeHeadline": "FloatingBox Enhances PDF Text Layout Options",
    "abstract": "La fonctionnalité FloatingBox améliore le formatage du texte PDF en permettant aux utilisateurs de gérer le placement du texte avec précision, y compris les mises en page à colonnes multiples et les décalages ajustables. Elle prend en charge le découpage de texte, les couleurs de fond et les options pour répéter le contenu sur plusieurs pages, ce qui en fait un outil polyvalent pour créer des documents structurés et visuellement attrayants.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "682",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/floating-box/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/floating-box/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

Cette fonctionnalité fonctionne également dans la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Principes de base de l'utilisation de l'outil FloatingBox

L'outil Floating Box est un outil spécial pour placer du texte et d'autres contenus sur une page PDF. Sa principale caractéristique est le découpage de texte lorsqu'il dépasse la taille de la FloatingBox.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAndAddFloatingBox()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        // Create and fill box
        var box = new Aspose.Pdf.FloatingBox(400, 30)
        {
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1.5f, Aspose.Pdf.Color.DarkGreen),
            IsNeedRepeating = false,
        };
        box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example"));
        // Add box
        page.Paragraphs.Add(box);
    }
}
```  

Dans l'exemple ci-dessus, nous créons une FloatingBox d'une largeur de 400 pt et d'une hauteur de 30 pt. De plus, dans cet exemple, plus de texte a été intentionnellement créé que ce qui pouvait tenir dans la taille donnée. En conséquence, le texte a été coupé.

![Image 1](image01.png)

La propriété `IsNeedRepeating` avec la valeur `false` limite le texte à 1 page.

Si nous définissons cette propriété sur `true`, le texte sera réajusté à la page suivante à la même position.

![Image 2](image02.png)

## Fonctionnalités avancées de FloatingBox

### Support multi-colonnes

#### Mise en page multi-colonnes (cas simple)

`FloatingBox` prend en charge la mise en page à colonnes multiples. Pour créer une telle mise en page, vous devez définir les valeurs des propriétés ColumnInfo.

* `ColumnWidths` est une chaîne avec l'énumération des largeurs en pt.
* `ColumnSpacing` est une chaîne avec la largeur de l'écart entre les colonnes.
* `ColumnCount` est le nombre de colonnes.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MultiColumnLayout()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tooltip();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Set margin settings
        page.PageInfo.Margin = new Aspose.Pdf.MarginInfo(36, 18, 36, 18);
        var columnCount = 3;
        var spacing = 10;
        var width = page.PageInfo.Width
            - page.PageInfo.Margin.Left
            - page.PageInfo.Margin.Right
            - (columnCount - 1) * spacing;
        var columnWidth = width / 3;
        // Create FloatingBox
        var box = new Aspose.Pdf.FloatingBox()
        {
            IsNeedRepeating = true
        };
        box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
        box.ColumnInfo.ColumnSpacing = $"{spacing}";
        box.ColumnInfo.ColumnCount = 3;

        var phrase = "text example";
        var paragraphs = new string[10]
        {
            phrase, phrase, phrase, phrase, phrase,
            phrase, phrase, phrase, phrase, phrase,
        };
        foreach (var paragraph in paragraphs)
        {
            box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment(paragraph));
        }
        // Add a box to a page
        page.Paragraphs.Add(box);
        // Save PDF document
        document.Save(dataDir + "MultiColumnLayout_out.pdf");
    }
}
```

Nous avons utilisé la bibliothèque supplémentaire LoremNET dans l'exemple ci-dessus et créé 20 paragraphes. Ces paragraphes ont été divisés en trois colonnes et ont rempli les pages suivantes jusqu'à ce que le texte soit épuisé.

#### Mise en page multi-colonnes avec début de colonne forcé

Nous allons faire la même chose avec l'exemple suivant que le précédent. La différence est que nous avons créé 3 paragraphes. Nous pouvons forcer FloatingBox à rendre chaque paragraphe dans la nouvelle colonne. Pour ce faire, nous devons définir `IsFirstParagraphInColumn` lorsque nous ajoutons du texte à l'objet FloatingBox.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MultiColumnLayout2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tooltip();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Set margin settings
        page.PageInfo.Margin = new Aspose.Pdf.MarginInfo(36, 18, 36, 18);
        var columnCount = 3;
        var spacing = 10;
        var width = page.PageInfo.Width
            - page.PageInfo.Margin.Left
            - page.PageInfo.Margin.Right
            - (columnCount - 1) * spacing;
        var columnWidth = width / 3;
        // Create the FloatingBox
        var box = new Aspose.Pdf.FloatingBox()
        {
            IsNeedRepeating = true
        };
        box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
        box.ColumnInfo.ColumnSpacing = $"{spacing}";
        box.ColumnInfo.ColumnCount = 3;

        var phrase = "text example";
        var paragraphs = new string[10]
        {
            phrase, phrase, phrase, phrase, phrase,
            phrase, phrase, phrase, phrase, phrase,
        };
        foreach (var paragraph in paragraphs)
        {
            var text = new Aspose.Pdf.Text.TextFragment(paragraph)
            {
                IsFirstParagraphInColumn = true
            };
            box.Paragraphs.Add(text);
        }

        // Add a box to a page
        page.Paragraphs.Add(box);
        // Save PDF document
        document.Save(dataDir + "MultiColumnLayout2_out.pdf");
    }
}
```

### Support de fond

Vous pouvez définir la couleur de fond souhaitée en utilisant la propriété `BackgroundColor`.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void BackgroundSupport()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var box = new Aspose.Pdf.FloatingBox(400, 60)
        {
            IsNeedRepeating = false,
            BackgroundColor = Aspose.Pdf.Color.LightGreen,
        };
        var text = "text example";
        box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment(text));
        page.Paragraphs.Add(box);
    }
}
```

### Support de positionnement

L'emplacement de la FloatingBox sur la page générée est déterminé par les propriétés `PositioningMode`, `Left`, `Top`. Lorsque la valeur de `PositioningMode` est
- `ParagraphPositioningMode.Default` (valeur par défaut)
	L'emplacement est déterminé par les éléments placés précédemment. L'ajout d'un élément est pris en compte lors de la détermination de l'emplacement des éléments suivants. Si la valeur d'au moins une des propriétés Left, Top n'est pas zéro, alors elles sont également prises en compte, mais cela utilise une logique pas entièrement évidente et il est préférable de ne pas l'utiliser.

- `ParagraphPositioningMode.Absolute`
	L'emplacement est spécifié par les valeurs Left et Top, ne dépend pas des éléments précédents et n'affecte pas l'emplacement des suivants.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OffsetSupport()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create FloatingBox
        var box = new Aspose.Pdf.FloatingBox()
        {
            Top = 45,
            Left = 15,
            PositioningMode = Aspose.Pdf.ParagraphPositioningMode.Absolute
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1.5f, Aspose.Pdf.Color.DarkGreen)
        };
        box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example 1"));

        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example 2"));
        // Add the box to the page
        page.Paragraphs.Add(box);
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example 3"));
    }
}
```