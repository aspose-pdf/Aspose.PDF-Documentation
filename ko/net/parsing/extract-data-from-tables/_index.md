---
title: PDF에서 C#으로 테이블 데이터 추출
linktitle: 테이블 데이터 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/extract-data-from-table-in-pdf/
description: C#을 사용하여 PDF에서 표 형식 데이터를 추출하는 방법을 배우십시오.
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
    "abstract": "C#에서 Aspose.PDF for .NET을 사용하여 PDF 문서에서 표 형식 데이터를 추출하는 강력한 기능을 발견하십시오. 이 기능은 사용자가 개별 셀에 원활하게 접근하고 추출된 데이터를 CSV 및 Excel과 같은 형식으로 저장할 수 있도록 하여 테이블 검색 및 조작 프로세스를 단순화하여 데이터 접근성과 사용성을 향상시킵니다.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## PDF에서 프로그래밍 방식으로 테이블 추출

PDF에서 테이블을 추출하는 것은 간단한 작업이 아닙니다. 테이블은 다양한 방식으로 생성될 수 있기 때문입니다.

Aspose.PDF for .NET은 테이블을 쉽게 검색할 수 있는 도구를 제공합니다. 테이블 데이터를 추출하려면 다음 단계를 수행해야 합니다:

1. 문서 열기 - [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 인스턴스화합니다.
1. [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) 객체를 생성합니다.
1. 분석할 페이지를 결정하고 원하는 페이지에 [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/visit)를 적용합니다. 표 형식 데이터가 스캔되고 결과는 [TableList](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/properties/tablelist)에 저장됩니다.
1. `TableList`는 [AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable)의 목록입니다. 데이터를 가져오려면 `TableList`를 반복하고 [RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist) 및 [CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist)를 처리합니다.
1. 각 [AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell)에는 [TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments) 컬렉션이 포함되어 있습니다. 이를 자신의 목적에 맞게 처리할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

다음 예제는 모든 페이지에서 테이블을 추출하는 방법을 보여줍니다:

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

## PDF 페이지의 특정 영역에서 테이블 추출

각 흡수된 테이블에는 페이지에서 테이블의 위치를 설명하는 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle) 속성이 있습니다.

특정 지역에 위치한 테이블을 추출해야 하는 경우 특정 좌표로 작업해야 합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

다음 예제는 사각형 주석으로 표시된 테이블을 추출하는 방법을 보여줍니다:

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

## PDF에서 테이블 데이터 추출 및 CSV 파일에 저장

다음 예제는 테이블을 추출하고 CSV 파일로 저장하는 방법을 보여줍니다.
PDF를 Excel 스프레드시트로 변환하는 방법에 대한 내용은 [PDF를 Excel로 변환](/pdf/net/convert-pdf-to-excel/) 기사를 참조하십시오.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

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