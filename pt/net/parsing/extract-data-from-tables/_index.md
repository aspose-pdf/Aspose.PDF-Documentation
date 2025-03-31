---
title: Extrair Dados de Tabela em PDF com C#
linktitle: Extrair Dados de Tabela
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /pt/net/extract-data-from-table-in-pdf/
description: Aprenda como extrair dados tabulares de PDF usando Aspose.PDF for .NET em C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Data from Table in PDF with C#",
    "alternativeHeadline": "Effortlessly Extract Tables from PDFs Using C#",
    "abstract": "Descubra a poderosa capacidade de extrair dados tabulares de documentos PDF usando Aspose.PDF for .NET em C#. Este recurso simplifica o processo de recuperação e manipulação de tabelas, permitindo que os usuários acessem facilmente células individuais e armazenem os dados extraídos em formatos como CSV e Excel, melhorando a acessibilidade e usabilidade dos dados.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "695",
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
    "url": "/net/extract-data-from-table-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-data-from-table-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Extrair Tabelas de PDF programaticamente

Extrair tabelas de PDFs não é uma tarefa trivial porque as tabelas podem ser criadas de várias maneiras.

Aspose.PDF for .NET possui uma ferramenta para facilitar a recuperação de tabelas. Para extrair dados de tabela, você deve realizar os seguintes passos:

1. Abrir documento - instanciar um objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document).
1. Criar um objeto [TableAbsorber](https://reference.aspose.com/pdf/pt/net/aspose.pdf.text/tableabsorber).
1. Decidir quais páginas devem ser analisadas e aplicar [Visit](https://reference.aspose.com/pdf/pt/net/aspose.pdf.text/tableabsorber/methods/visit) nas páginas desejadas. Os dados tabulares serão escaneados e o resultado será armazenado em [TableList](https://reference.aspose.com/pdf/pt/net/aspose.pdf.text/tableabsorber/properties/tablelist).
1. `TableList` é uma lista de [AbsorbedTable](https://reference.aspose.com/pdf/pt/net/aspose.pdf.text/absorbedtable). Para obter os dados, itere através de `TableList` e manipule [RowList](https://reference.aspose.com/pdf/pt/net/aspose.pdf.text/absorbedtable/properties/rowlist) e [CellList](https://reference.aspose.com/pdf/pt/net/aspose.pdf.text/absorbedrow/properties/celllist).
1. Cada [AbsorbedCell](https://reference.aspose.com/pdf/pt/net/aspose.pdf.text/absorbedcell) contém uma coleção de [TextFragments](https://reference.aspose.com/pdf/pt/net/aspose.pdf.text/absorbedcell/properties/textfragments). Você pode processá-la para seus próprios fins.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

O seguinte exemplo mostra a extração de tabela de todas as páginas:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {                    
        foreach (var page in document.Pages)
        {
            Aspose.Pdf.TableAbsorber absorber = new Aspose.Pdf.TableAbsorber();
            absorber.Visit(page);
            foreach (var table in absorber.TableList)
            {
                Console.WriteLine("Table");
                foreach (var row in table.RowList)
                {
                    foreach (var cell in row.CellList)
                    {                                 
                        foreach (var fragment in cell.TextFragments)
                        {
                            var sb = new StringBuilder();
                            foreach (var seg in fragment.Segments)
                            {
                                sb.Append(seg.Text);
                            }
                            Console.Write($"{sb.ToString()}|");
                        }                           
                    }
                    Console.WriteLine();
                }
            }
        }
    }
}
```

## Extrair tabela em área específica da página PDF

Cada tabela absorvida tem a propriedade [Rectangle](https://reference.aspose.com/pdf/pt/net/aspose.pdf.text/absorbedtable/properties/rectangle) que descreve a posição da tabela na página.

Se você precisar extrair tabelas localizadas em uma região específica, deve trabalhar com coordenadas específicas.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

O seguinte exemplo mostra como extrair uma tabela marcada com Anotação Quadrada:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractMarkedTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    { 
        var page = document.Pages[1];
        var squareAnnotation =
            page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
            as Aspose.Pdf.Annotations.SquareAnnotation;


        var absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);

        foreach (var table in absorber.TableList)
        {
            var isInRegion = (squareAnnotation.Rect.LLX < table.Rectangle.LLX) &&
            (squareAnnotation.Rect.LLY < table.Rectangle.LLY) &&
            (squareAnnotation.Rect.URX > table.Rectangle.URX) &&
            (squareAnnotation.Rect.URY > table.Rectangle.URY);

            if (isInRegion)
            {
                foreach (var row in table.RowList)
                {
                    foreach (var cell in row.CellList)
                    {
                        foreach (var fragment in cell.TextFragments)
                        {
                            var sb = new StringBuilder();
                            foreach (var seg in fragment.Segments)
                            {
                                sb.Append(seg.Text);
                            }
                            var text = sb.ToString();
                            Console.Write($"{text}|");
                        }
                    }
                    Console.WriteLine();
                }
            }
        }
    }
}
```

## Extrair Dados da Tabela de PDF e armazená-los em arquivo CSV

O seguinte exemplo mostra como extrair uma tabela e armazená-la como arquivo CSV.
Para ver como converter PDF para Planilha Excel, consulte o artigo [Converter PDF para Excel](/pdf/pt/net/convert-pdf-to-excel/).

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTableSaveExcel()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSave Option object
        Aspose.Pdf.ExcelSaveOptions excelSave = new Aspose.Pdf.ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

        // Save the output in XLS format
        document.Save(dataDir + "ExtractTableSaveXLS_out.xlsx", excelSave);
    }
}
```