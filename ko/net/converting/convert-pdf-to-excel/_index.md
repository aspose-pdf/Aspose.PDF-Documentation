---
title: PDF를 Excel로 변환하기 (.NET)
linktitle: PDF를 Excel로 변환하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
description: Aspose.PDF for .NET 라이브러리를 사용하여 C#로 PDF를 Excel 형식으로 변환할 수 있습니다. 이러한 형식에는 XLS, XLSX, XML 2003 스프레드시트, CSV, ODS가 포함됩니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Excel in .NET",
    "alternativeHeadline": "Convert PDF Files to Excel Formats with C#",
    "abstract": "Aspose.PDF for .NET의 강력한 기능을 통해 PDF 문서를 XLS, XLSX, CSV 및 ODS를 포함한 다양한 Excel 형식으로 손쉽게 변환할 수 있습니다. 이 기능은 개별 PDF 페이지를 별도의 Excel 워크시트로 변환할 수 있을 뿐만 아니라, 결합된 시트 옵션도 제공하여 사용자가 PDF 데이터를 효율적으로 관리할 수 있도록 합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1311",
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
    "url": "/net/convert-pdf-to-excel/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-excel/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 개요

이 문서에서는 **C#를 사용하여 PDF를 Excel 형식으로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

- [PDF를 XLS로 변환하기](#csharp-pdf-to-xls)
- [PDF를 XLSX로 변환하기](#csharp-pdf-to-xlsx)
- [PDF를 Excel로 변환하기](#csharp-pdf-to-xlsx)
- [단일 워크시트를 가진 PDF를 XLS로 변환하기](#csharp-pdf-to-excel-single)
- [단일 워크시트를 가진 PDF를 XLSX로 변환하기](#csharp-pdf-to-excel-single)
- [PDF를 XML Excel로 변환하기](#csharp-pdf-to-excel-xml-2003)
- [PDF를 CSV로 변환하기](#csharp-pdf-to-csv)
- [PDF를 ODS로 변환하기](#csharp-pdf-to-ods)
- [PDF를 XLSM으로 변환하기](#csharp-pdf-to-xlsm)

## C# PDF를 Excel로 변환하기

**Aspose.PDF for .NET**는 PDF 파일을 Excel 2007, CSV 및 SpreadsheetML 형식으로 변환하는 기능을 지원합니다.

Aspose.PDF for .NET는 PDF 조작 구성 요소로, PDF 파일을 Excel 통합 문서(XLSX 파일)로 렌더링하는 기능을 도입했습니다. 이 변환 과정에서 PDF 파일의 개별 페이지가 Excel 워크시트로 변환됩니다.

{{% alert color="success" %}}
**PDF를 Excel로 온라인 변환해 보세요**

Aspose.PDF for .NET는 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)라는 온라인 무료 애플리케이션을 제공하여 기능과 품질을 확인할 수 있습니다.

[![Aspose.PDF PDF를 Excel로 변환하는 무료 앱](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

PDF 파일을 <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr> 형식으로 변환하기 위해 Aspose.PDF에는 [ExcelSaveOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/excelsaveoptions)라는 클래스가 있습니다. ExcelSaveOptions 클래스의 객체는 Document.Save(..) 생성자의 두 번째 인수로 전달됩니다.

다음 코드 스니펫은 Aspose.PDF for .NET를 사용하여 PDF 파일을 XLS 또는 XLSX 형식으로 변환하는 과정을 보여줍니다.

<a name="csharp-pdf-to-xls" id="cshart-pdf-to-xls"><strong>PDF를 XLS로 변환하기</strong></a>

1. 소스 PDF 문서로 **Document** 객체의 인스턴스를 생성합니다.
2. **ExcelSaveOptions**의 인스턴스를 생성합니다.
3. **Document.Save()** 메서드를 호출하고 **ExcelSaveOptions**를 전달하여 **.xls 확장자**를 지정하여 **XLS** 형식으로 저장합니다.

<a name="csharp-pdf-to-xlsx" id="cshart-pdf-to-xlsx"><strong>PDF를 XLSX로 변환하기</strong></a>

1. 소스 PDF 문서로 **Document** 객체의 인스턴스를 생성합니다.
2. **ExcelSaveOptions**의 인스턴스를 생성합니다.
3. **Document.Save()** 메서드를 호출하고 **ExcelSaveOptions**를 전달하여 **.xlsx 확장자**를 지정하여 **XLSX** 형식으로 저장합니다.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcel()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions();

         // Save the file in XLSX format
         document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
     }
 }
```

## 제어 열이 있는 PDF를 XLS로 변환하기

PDF를 XLS 형식으로 변환할 때 출력 파일의 첫 번째 열로 빈 열이 추가됩니다. ExcelSaveOptions 클래스의 InsertBlankColumnAtFirst 옵션을 사용하여 이 열을 제어할 수 있습니다. 기본값은 `false`로, 빈 열이 삽입되지 않음을 의미합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            InsertBlankColumnAtFirst = false
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## 단일 Excel 워크시트로 PDF 변환하기

페이지가 많은 PDF 파일을 XLS로 내보낼 때 각 페이지는 Excel 파일의 다른 시트로 내보내집니다. 이는 MinimizeTheNumberOfWorksheets 속성이 기본적으로 false로 설정되어 있기 때문입니다. 출력 Excel 파일에서 모든 페이지가 하나의 시트로 내보내지도록 하려면 MinimizeTheNumberOfWorksheets 속성을 true로 설정합니다.

<a name="csharp-pdf-to-excel-single" id="cshart-pdf-to-excel-single"><strong>PDF를 XLS 또는 XLSX 단일 워크시트로 변환하기</strong></a>

1. 소스 PDF 문서로 **Document** 객체의 인스턴스를 생성합니다.
2. **MinimizeTheNumberOfWorksheets = true**로 **ExcelSaveOptions**의 인스턴스를 생성합니다.
3. **Document.Save()** 메서드를 호출하고 **ExcelSaveOptions**를 전달하여 단일 워크시트를 가진 **XLS** 또는 **XLSX** 형식으로 저장합니다.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            MinimizeTheNumberOfWorksheets = true
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## 다른 스프레드시트 형식으로 변환하기

### XML 스프레드시트 2003 형식으로 변환하기

버전 20.8부터 Aspose.PDF는 데이터를 저장하기 위한 기본 형식으로 Microsoft Excel Open XML Spreadsheet 2007 파일 형식을 사용합니다. PDF 파일을 XML 스프레드시트 2003 형식으로 변환하기 위해 Aspose.PDF에는 [ExcelSaveOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/excelsaveoptions) 클래스가 있으며, [Format](https://reference.aspose.com/pdf/ko/net/aspose.pdf/excelsaveoptions/properties/format) 속성이 있습니다. [ExcelSaveOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf/excelsaveoptions) 클래스의 객체는 [Document.Save(..)](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/methods/save/index) 메서드의 두 번째 인수로 전달됩니다.

다음 코드 스니펫은 PDF 파일을 XLS Excel 2003 XML 형식으로 변환하는 과정을 보여줍니다.

<a name="csharp-pdf-to-excel-xml-2003" id="cshart-pdf-to-excel-xml-2003"><strong>PDF를 Excel 2003 XML 형식으로 변환하기</strong></a>

1. 소스 PDF 문서로 **Document** 객체의 인스턴스를 생성합니다.
2. **Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003**로 **ExcelSaveOptions**의 인스턴스를 생성합니다.
3. **Document.Save()** 메서드를 호출하고 **ExcelSaveOptions**를 전달하여 **XLS - Excel 2003 XML 형식**으로 저장합니다.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions
         {
             Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
         };

         // Save the file in XLS format
         document.Save(dataDir + "PDFToXLS_out.xls", saveOptions);
     }
 }
```

### CSV로 변환하기

CSV 형식으로의 변환은 위와 동일한 방식으로 수행됩니다. 필요한 것은 적절한 형식을 설정하는 것입니다.

<a name="csharp-pdf-to-csv"  id="cshart-pdf-to-csv"><strong>PDF를 CSV로 변환하기</strong></a>

1. 소스 PDF 문서로 **Document** 객체의 인스턴스를 생성합니다.
2. **Format = ExcelSaveOptions.ExcelFormat.CSV**로 **ExcelSaveOptions**의 인스턴스를 생성합니다.
3. **Document.Save()** 메서드를 호출하고 **ExcelSaveOptions**를 전달하여 **CSV** 형식으로 저장합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToCSV()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.CSV
        };
        
        // Save the file in CSV format
        document.Save(dataDir + "PDFToXLS_out.csv", saveOptions);
    }
}
```

### ODS로 변환하기

<a name="csharp-pdf-to-ods"  id="cshart-pdf-to-ods"><strong>PDF를 ODS로 변환하기</strong></a>

1. 소스 PDF 문서로 **Document** 객체의 인스턴스를 생성합니다.
2. **Format = ExcelSaveOptions.ExcelFormat.ODS**로 **ExcelSaveOptions**의 인스턴스를 생성합니다.
3. **Document.Save()** 메서드를 호출하고 **ExcelSaveOptions**를 전달하여 **ODS** 형식으로 저장합니다.

ODS 형식으로의 변환은 다른 모든 형식과 동일한 방식으로 수행됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToODS()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.ODS
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.ods", saveOptions);
    }
}
```

### XLSM으로 변환하기

<a name="csharp-pdf-to-xlsm" id="cshart-pdf-to-xlsm"><strong>PDF를 XLSM으로 변환하기</strong></a>

1. 소스 PDF 문서로 **Document** 객체의 인스턴스를 생성합니다.
2. **Format = ExcelSaveOptions.ExcelFormat.XLSM**로 **ExcelSaveOptions**의 인스턴스를 생성합니다.
3. **Document.Save()** 메서드를 호출하고 **ExcelSaveOptions**를 전달하여 **XLSM** 형식으로 저장합니다.

XLSM 형식으로의 변환은 다른 모든 형식과 동일한 방식으로 수행됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToXLSM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XLSM
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.xlsm", saveOptions);
    }
}
```