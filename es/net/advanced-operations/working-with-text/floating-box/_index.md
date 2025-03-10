---
title: Usando FloatingBox para la generación de texto
linktitle: Usando FloatingBox
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/floating-box/
description: Esta página explica cómo formatear texto dentro de un cuadro flotante.
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
    "abstract": "La función FloatingBox mejora el formato de texto en PDF al permitir a los usuarios gestionar la colocación del texto con precisión, incluyendo diseños de múltiples columnas y desplazamientos ajustables. Soporta recortes de texto, colores de fondo y opciones para repetir contenido a través de páginas, lo que lo convierte en una herramienta versátil para crear documentos estructurados y visualmente atractivos.",
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
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

Esta función también funciona en la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Conceptos básicos del uso de la herramienta FloatingBox

La herramienta Floating Box es una herramienta especial para colocar texto y otro contenido en una página PDF. Su característica principal es el recorte de texto cuando se superpone al tamaño del FloatingBox.

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

En el ejemplo anterior, estamos creando un FloatingBox con un ancho de 400 pt y una altura de 30 pt. 
Además, en este ejemplo, se creó intencionalmente más texto del que podría caber en el tamaño dado. 
Como resultado, el texto fue cortado.

![Image 1](image01.png)

La propiedad `IsNeedRepeating` con el valor `false` limita el texto a 1 página.

Si establecemos esta propiedad en `true`, el texto se refluye a la siguiente página en la misma posición.

![Image 2](image02.png)

## Características avanzadas de FloatingBox

### Soporte para múltiples columnas

#### Diseño de múltiples columnas (caso simple)

`FloatingBox` soporta diseño de múltiples columnas. Para crear tal diseño, debes definir los valores de las propiedades ColumnInfo.

* `ColumnWidths` es una cadena con enumeración de ancho en pt.
* `ColumnSpacing` es una cadena con el ancho del espacio entre columnas.
* `ColumnCount` es el número de columnas.

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

Usamos la biblioteca adicional LoremNET en el ejemplo anterior y creamos 20 párrafos. Estos párrafos se dividieron en tres columnas y llenaron las siguientes páginas hasta que se acabó el texto.

#### Diseño de múltiples columnas con inicio de columna forzado

Haremos lo mismo con el siguiente ejemplo que con el anterior. La diferencia es que creamos 3 párrafos. Podemos forzar a FloatingBox a renderizar cada párrafo en la nueva columna. Para hacer eso, necesitamos establecer `IsFirstParagraphInColumn` al agregar texto al objeto FloatingBox.

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

### Soporte de fondo

Puedes establecer el color de fondo deseado utilizando la propiedad `BackgroundColor`.

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

### Soporte de posicionamiento

La ubicación del FloatingBox en la página generada está determinada por las propiedades `PositioningMode`, `Left`, `Top`. 
Cuando el valor de `PositioningMode` es
- `ParagraphPositioningMode.Default` (valor predeterminado)
    La ubicación está determinada por los elementos colocados previamente. 
    La adición de un elemento se tiene en cuenta al determinar la ubicación de los elementos posteriores. 
    Si el valor de al menos una de las propiedades Left, Top no es cero, entonces también se tienen en cuenta, pero esto utiliza una lógica no del todo obvia y es mejor no usar esto.

- `ParagraphPositioningMode.Absolute`
    La ubicación se especifica por los valores Left y Top, no depende de elementos anteriores y no afecta la ubicación de los posteriores.

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