---
title: Извлечение данных из таблицы в PDF с помощью C#
linktitle: Извлечение данных из таблицы
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ru/net/extract-data-from-table-in-pdf/
description: Узнайте, как извлечь данные из таблицы в формате PDF с помощью Aspose.PDF for .NET на C#.
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
    "abstract": "Откройте для себя мощную возможность извлекать табличные данные из PDF-документов с помощью Aspose.PDF для .NET на C#. Эта функция упрощает процесс извлечения и обработки таблиц, позволяя пользователям легко получать доступ к отдельным ячейкам и сохранять извлечённые данные в таких форматах, как CSV и Excel, повышая доступность и удобство использования данных",
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
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

## Извлечение таблиц из PDF программным способом

Извлечение таблиц из PDF — нетривиальная задача, поскольку таблицы могут быть созданы различными способами.

У Aspose.PDF for .NET есть инструмент, который упрощает извлечение табличных данных. Чтобы извлечь данные таблицы, выполните следующие действия:

1. Откройте документ — создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Создайте объект [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber).
1. Решите, какие страницы нужно проанализировать, и примените [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/visit) к нужным страницам. Табличные данные будут отсканированы, а результат будет сохранён в [TableList](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/properties/tablelist).
1. `TableList` — это список [AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable). Чтобы получить данные, переберите `TableList` и обработайте [RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist) и [CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist).
1. Каждый [AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell) содержит коллекцию [TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments). Вы можете обработать её для своих целей.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Приведённый ниже пример показывает извлечение таблицы со всех страниц:

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

## Извлечение таблицы в определённой области страницы PDF

Каждая поглощённая таблица имеет свойство [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle), которое описывает положение таблицы на странице.

Если вам нужно извлечь таблицы, расположенные в определённой области, вам придётся работать с конкретными координатами.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

В приведённом ниже примере показано, как извлечь таблицу, отмеченную квадратной аннотацией:

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

## Извлечение табличных данных из PDF и сохранение их в CSV-файл

В следующем примере показано, как извлечь таблицу и сохранить её в виде CSV-файла.
Чтобы узнать, как преобразовать PDF в электронную таблицу Excel, обратитесь к статье [Преобразование PDF в Excel](/pdf/ru/net/convert-pdf-to-excel/).

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

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