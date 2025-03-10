---
title: Usando o FloatingBox para geração de texto
linktitle: Usando o FloatingBox
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/floating-box/
description: Esta página explica como formatar texto dentro de uma caixa flutuante.
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
    "abstract": "O recurso FloatingBox melhora a formatação de texto em PDF ao permitir que os usuários gerenciem a colocação do texto com precisão, incluindo layouts de várias colunas e deslocamentos ajustáveis. Ele suporta recorte de texto, cores de fundo e opções para repetir conteúdo em várias páginas, tornando-se uma ferramenta versátil para criar documentos estruturados e visualmente atraentes.",
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
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

Este recurso também funciona na biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Noções básicas sobre o uso da ferramenta FloatingBox

A ferramenta Floating Box é uma ferramenta especial para colocar texto e outros conteúdos em uma página PDF. Sua principal característica é o recorte de texto quando ele ultrapassa o tamanho da FloatingBox.

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

No exemplo acima, estamos criando uma FloatingBox com uma largura de 400 pt e uma altura de 30 pt. 
Além disso, neste exemplo, mais texto foi intencionalmente criado do que poderia caber no tamanho dado. 
Como resultado, o texto foi cortado.

![Imagem 1](image01.png)

A propriedade `IsNeedRepeating` com valor `false` limita o texto a 1 página.

Se definirmos essa propriedade como `true`, o texto será redistribuído para a próxima página na mesma posição.

![Imagem 2](image02.png)

## Recursos avançados do FloatingBox

### Suporte a várias colunas

#### Layout de várias colunas (caso simples)

`FloatingBox` suporta layout de várias colunas. Para criar tal layout, você deve definir os valores das propriedades ColumnInfo.

* `ColumnWidths` é uma string com enumeração de largura em pt.
* `ColumnSpacing` é uma string com a largura do espaço entre colunas.
* `ColumnCount` é o número de colunas.

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

Usamos a biblioteca adicional LoremNET no exemplo acima e criamos 20 parágrafos. Esses parágrafos foram divididos em três colunas e preencheram as páginas seguintes até que o texto acabasse.

#### Layout de várias colunas com início de coluna forçado

Faremos o mesmo com o exemplo a seguir como o anterior. A diferença é que criamos 3 parágrafos. Podemos forçar o FloatingBox a renderizar cada parágrafo em uma nova coluna. Para fazer isso, precisamos definir `IsFirstParagraphInColumn` ao adicionar texto ao objeto FloatingBox.

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

### Suporte a fundo

Você pode definir a cor de fundo desejada usando a propriedade `BackgroundColor`.

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

### Suporte a posicionamento

A localização da FloatingBox na página gerada é determinada pelos valores `PositioningMode`, `Left`, `Top`. 
Quando o valor de `PositioningMode` é
- `ParagraphPositioningMode.Default` (valor padrão)
	A localização é determinada pelos elementos previamente colocados. 
	A adição de um elemento é levada em conta ao determinar a localização dos elementos subsequentes. 
	Se o valor de pelo menos uma das propriedades Left, Top não for zero, então elas também são levadas em conta, mas isso usa uma lógica não totalmente óbvia e é melhor não usar isso.

- `ParagraphPositioningMode.Absolute`
	A localização é especificada pelos valores Left e Top, não depende de elementos anteriores e não afeta a localização dos subsequentes.

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