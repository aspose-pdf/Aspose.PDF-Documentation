---
title: 데이터 가져오기 및 내보내기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ko/net/import-and-export-data/
description: 이 섹션에서는 Form 클래스를 사용하여 Aspose.PDF Facades로 데이터를 가져오고 내보내는 방법을 설명합니다.
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data",
    "alternativeHeadline": "Effortless Data Import and Export for PDF Forms",
    "abstract": "Aspose.PDF for .NET의 데이터 가져오기 및 내보내기 기능은 사용자가 XML, FDF, XFDF 및 JSON 형식을 활용하여 PDF 양식 데이터를 가져오고 내보낼 수 있도록 하여 문서 데이터 관리의 원활한 통합을 가능하게 합니다. 이 기능은 데이터 처리 능력을 향상시켜 워크플로우 자동화 및 PDF 문서에서 직접 정확한 기록을 유지하는 것을 쉽게 만듭니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1085",
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
    "url": "/net/import-and-export-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-and-export-data/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스는 [ImportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.form/importxml/methods/1) 메서드를 사용하여 XML 파일에서 PDF 파일로 데이터를 가져올 수 있게 해줍니다. XML에서 데이터를 가져오려면 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 [ImportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importxml/index) 메서드를 호출해야 합니다. 마지막으로 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 메서드를 사용하여 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 XML 파일에서 데이터를 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open xml file
        using (var xmlInputStream = new FileStream(dataDir + "input.xml", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXml(xmlInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXML_out.pdf");
        }
    }
}
```

## PDF 파일에서 XML로 데이터 내보내기

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스는 [ExportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxml) 메서드를 사용하여 PDF 파일에서 XML 파일로 데이터를 내보낼 수 있게 해줍니다. XML로 데이터를 내보내려면 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 [ExportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxml) 메서드를 호출해야 합니다. 마지막으로 FileStream 객체를 닫고 Form 객체를 해제할 수 있습니다. 다음 코드 스니펫은 XML 파일로 데이터를 내보내는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXml(xmlOutputStream);
        }
    }
}
```

## FDF에서 PDF 파일로 데이터 가져오기

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스는 [ImportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importfdf) 메서드를 사용하여 FDF 파일에서 PDF 파일로 데이터를 가져올 수 있게 해줍니다. FDF에서 데이터를 가져오려면 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 [ImportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importfdf) 메서드를 호출해야 합니다. 마지막으로 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 메서드를 사용하여 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 FDF 파일에서 데이터를 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromPdfIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");
        
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportFdf(fdfInputStream);         

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromPdf_out.pdf");
        }
    }
}
```

## PDF 파일에서 FDF로 데이터 내보내기

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스는 [ExportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportfdf) 메서드를 사용하여 PDF 파일에서 FDF 파일로 데이터를 내보낼 수 있게 해줍니다. FDF로 데이터를 내보내려면 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 [ExportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportfdf) 메서드를 호출해야 합니다. 마지막으로 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 메서드를 사용하여 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 FDF 파일로 데이터를 내보내는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdfFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create FDF file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportFdf(fdfOutputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToPdf_out.pdf"); 
        }
    }
}
```

## XFDF에서 PDF 파일로 데이터 가져오기

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스는 [ImportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importxfdf) 메서드를 사용하여 XFDF 파일에서 PDF 파일로 데이터를 가져올 수 있게 해줍니다. XFDF에서 데이터를 가져오려면 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 [ImportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importxfdf) 메서드를 호출해야 합니다. 마지막으로 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 메서드를 사용하여 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 XFDF 파일에서 데이터를 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXFDIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open XFDF file
        using (var xfdfInputStream = new FileStream(dataDir + "test2.xfdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXfdf(xfdfInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXFDF_out.pdf");
        }
    }
}
```

## PDF 파일에서 XFDF로 데이터 내보내기

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스는 [ExportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxfdf) 메서드를 사용하여 PDF 파일에서 XFDF 파일로 데이터를 내보낼 수 있게 해줍니다. XFDF로 데이터를 내보내려면 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 [ExportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxfdf) 메서드를 호출해야 합니다. 마지막으로 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 메서드를 사용하여 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 XFDF 파일로 데이터를 내보내는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDFFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XFDF file
        using (var xfdfOutputStream = new FileStream(dataDir + "out.xfdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXfdf(xfdfOutputStream);

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToXFDF_out.pdf");
        }
    }
}
```

## 필드에서 JSON 파일로 값 내보내기

Aspose.Pdf.Facades는 양식 필드 작업을 위한 대체 API를 제공합니다. 이 스니펫은 이 API를 사용하여 필드 값을 내보내고 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportValuesFromFieldsToJSON()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    
    using (var form = new Aspose.Pdf.Facades.Form())
    {       
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Create JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Create))
        {
            // Export data
            form.ExportJson(jsonStream);
        }
    }
}
```

## JSON 파일에서 필드로 값 가져오기

이 코드 스니펫은 Aspose.Pdf.Facades API를 사용하여 JSON 파일에서 PDF 문서의 양식 필드로 값을 가져오는 방법을 보여줍니다. FileStream은 JSON 파일을 처리하는 데 사용됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportValuesFromJsonToForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {        
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Import from JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Open))
        {
            // Export data
            form.ImportJson(jsonStream);
        }
    }
}
```