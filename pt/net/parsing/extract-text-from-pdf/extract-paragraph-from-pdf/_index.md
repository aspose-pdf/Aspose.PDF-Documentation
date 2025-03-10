---
title: Extrair Parágrafo de PDF C#
linktitle: Extrair Parágrafo de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/extract-paragraph-from-pdf/
description: Aprenda como extrair parágrafos de documentos PDF em .NET usando Aspose.PDF para recuperação de texto estruturado.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Paragraph from PDF C#",
    "alternativeHeadline": "Extract Text from PDF as Paragraphs Efficiently",
    "abstract": "O novo recurso ParagraphAbsorber no Aspose.PDF permite que os desenvolvedores extraiam e manipulem parágrafos de documentos PDF de forma eficiente. Com essa ferramenta, os usuários podem não apenas recuperar texto em um formato de parágrafo organizado, mas também visualizar seções através de bordas personalizáveis, aumentando a precisão da extração de texto em PDF. Essa funcionalidade simplifica o trabalho com dados PDF estruturados, tornando-se inestimável para aplicações que requerem análise de texto aprofundada.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "590",
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
    "url": "/net/extract-paragraph-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-paragraph-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Extrair Texto de documento PDF em forma de Parágrafos

Podemos obter texto de um documento PDF pesquisando um texto específico (usando "texto simples" ou "expressões regulares") de uma única página ou do documento inteiro, ou podemos obter o texto completo de uma única página, intervalo de páginas ou documento completo. No entanto, em alguns casos, você precisa extrair parágrafos de um documento PDF ou texto na forma de Parágrafos. Implementamos funcionalidade para pesquisar seções e parágrafos no texto das páginas do documento PDF. Introduzimos a Classe ParagraphAbsorber (como TextFragmentAbsorber e TextAbsorber), que pode ser usada para extrair parágrafos de documentos PDF. Existem duas maneiras a seguir nas quais você pode usar o ParagraphAbsorber:

**Desenhando a borda das seções e parágrafos de texto na página PDF:**

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractParagraphWithDrawingTheBorder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentForExtract.pdf"))
    {
        var page = document.Pages[2];

        var absorber = new Aspose.Pdf.Text.ParagraphAbsorber();
        absorber.Visit(page);

        Aspose.Pdf.Text.PageMarkup markup = absorber.PageMarkups[0];

        foreach (Aspose.Pdf.Text.MarkupSection section in markup.Sections)
        {
            DrawRectangleOnPage(section.Rectangle, page);
            foreach (Aspose.Pdf.Text.MarkupParagraph paragraph in section.Paragraphs)
            {
                DrawPolygonOnPage(paragraph.Points, page);
            }
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithBorder_out.pdf");
    }
}

private static void DrawRectangleOnPage(Aspose.Pdf.Rectangle rectangle, Aspose.Pdf.Page page)
{
    page.Contents.Add(new Aspose.Pdf.Operators.GSave());
    page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetRGBColorStroke(0, 1, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetLineWidth(2));
    page.Contents.Add(
        new Aspose.Pdf.Operators.Re(rectangle.LLX,
            rectangle.LLY,
            rectangle.Width,
            rectangle.Height));
    page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
    page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
}

private static void DrawPolygonOnPage(Aspose.Pdf.Point[] polygon, Aspose.Pdf.Page page)
{
    page.Contents.Add(new Aspose.Pdf.Operators.GSave());
    page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetRGBColorStroke(0, 0, 1));
    page.Contents.Add(new Aspose.Pdf.Operators.SetLineWidth(1));
    page.Contents.Add(new Aspose.Pdf.Operators.MoveTo(polygon[0].X, polygon[0].Y));
    for (int i = 1; i < polygon.Length; i++)
    {
        page.Contents.Add(new Aspose.Pdf.Operators.LineTo(polygon[i].X, polygon[i].Y));
    }
    page.Contents.Add(new Aspose.Pdf.Operators.LineTo(polygon[0].X, polygon[0].Y));
    page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
    page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
}
```

**Iterando pela coleção de parágrafos e obtendo o texto deles:**

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractParagraphByIteratingThroughParagraphsCollection()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentForExtract.pdf"))
    {
        // Instantiate ParagraphAbsorber
        var absorber = new Aspose.Pdf.Text.ParagraphAbsorber();
        absorber.Visit(document);

        foreach (Aspose.Pdf.Text.PageMarkup markup in absorber.PageMarkups)
        {
            int i = 1;
            foreach (Aspose.Pdf.Text.MarkupSection section in markup.Sections)
            {
                int j = 1;
                foreach (Aspose.Pdf.Text.MarkupParagraph paragraph in section.Paragraphs)
                {
                    StringBuilder paragraphText = new StringBuilder();
                    foreach (List<Aspose.Pdf.Text.TextFragment> line in paragraph.Lines)
                    {
                        foreach (Aspose.Pdf.Text.TextFragment fragment in line)
                        {
                            paragraphText.Append(fragment.Text);
                        }
                        paragraphText.Append("\r\n");
                    }
                    paragraphText.Append("\r\n");

                    Console.WriteLine("Paragraph {0} of section {1} on page {2}:", j, i, markup.Number);
                    Console.WriteLine(paragraphText.ToString());

                    j++;
                }
                i++;
            }
        }
    }
}
```