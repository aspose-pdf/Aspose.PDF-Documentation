---
title: データのインポートとエクスポート
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ja/net/import-and-export-data/
description: このセクションでは、Formクラスを使用してAspose.PDF Facadesでデータをインポートおよびエクスポートする方法を説明します。
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data",
    "alternativeHeadline": "Effortless Data Import and Export for PDF Forms",
    "abstract": "Aspose.PDF for .NETのデータのインポートとエクスポート機能は、ユーザーがXML、FDF、XFDF、およびJSON形式を利用してPDFフォームデータをインポートおよびエクスポートできるようにすることで、文書データ管理のシームレスな統合を可能にします。この機能はデータ処理能力を向上させ、ワークフローの自動化やPDF文書からの正確な記録の維持を容易にします。",
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
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスを使用すると、[ImportXml](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.form/importxml/methods/1)メソッドを使用してXMLファイルからPDFファイルにデータをインポートできます。XMLからデータをインポートするには、[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスのオブジェクトを作成し、FileStreamオブジェクトを使用して[ImportXml](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/importxml/index)メソッドを呼び出す必要があります。最後に、[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスの[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/save)メソッドを使用してPDFファイルを保存できます。以下のコードスニペットは、XMLファイルからデータをインポートする方法を示しています。

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

## PDFファイルからXMLにデータをエクスポート

[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスを使用すると、[ExportXml](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/exportxml)メソッドを使用してPDFファイルからXMLファイルにデータをエクスポートできます。XMLにデータをエクスポートするには、[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスのオブジェクトを作成し、FileStreamオブジェクトを使用して[ExportXml](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/exportxml)メソッドを呼び出す必要があります。最後に、FileStreamオブジェクトを閉じて、Formオブジェクトを破棄できます。以下のコードスニペットは、XMLファイルにデータをエクスポートする方法を示しています。

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

## FDFからPDFファイルにデータをインポート

[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスを使用すると、[ImportFdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/importfdf)メソッドを使用してFDFファイルからPDFファイルにデータをインポートできます。FDFからデータをインポートするには、[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスのオブジェクトを作成し、FileStreamオブジェクトを使用して[ImportFdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/importfdf)メソッドを呼び出す必要があります。最後に、[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスの[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/save)メソッドを使用してPDFファイルを保存できます。以下のコードスニペットは、FDFファイルからデータをインポートする方法を示しています。

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

## PDFファイルからFDFにデータをエクスポート

[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスを使用すると、[ExportFdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/exportfdf)メソッドを使用してPDFファイルからFDFファイルにデータをエクスポートできます。FDFにデータをエクスポートするには、[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスのオブジェクトを作成し、FileStreamオブジェクトを使用して[ExportFdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/exportfdf)メソッドを呼び出す必要があります。最後に、[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスの[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/save)メソッドを使用してPDFファイルを保存できます。以下のコードスニペットは、FDFファイルにデータをエクスポートする方法を示しています。

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

## XFDFからPDFファイルにデータをインポート

[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスを使用すると、[ImportXfdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/importxfdf)メソッドを使用してXFDFファイルからPDFファイルにデータをインポートできます。XFDFからデータをインポートするには、[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスのオブジェクトを作成し、FileStreamオブジェクトを使用して[ImportXfdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/importxfdf)メソッドを呼び出す必要があります。最後に、[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスの[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/save)メソッドを使用してPDFファイルを保存できます。以下のコードスニペットは、XFDFファイルからデータをインポートする方法を示しています。

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

## PDFファイルからXFDFにデータをエクスポート

[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスを使用すると、[ExportXfdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/exportxfdf)メソッドを使用してPDFファイルからXFDFファイルにデータをエクスポートできます。XFDFにデータをエクスポートするには、[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスのオブジェクトを作成し、FileStreamオブジェクトを使用して[ExportXfdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/exportxfdf)メソッドを呼び出す必要があります。最後に、[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/form)クラスの[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/save)メソッドを使用してPDFファイルを保存できます。以下のコードスニペットは、XFDFファイルにデータをエクスポートする方法を示しています。

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

## フィールドの値をJSONファイルにエクスポート

Aspose.Pdf.Facadesは、フォームフィールドを操作するための代替APIを提供します。このスニペットは、このAPIを使用してフィールド値をエクスポートおよびインポートする方法を示しています。

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

## JSONファイルからフィールドに値をインポート

このコードスニペットは、Aspose.Pdf.Facades APIを使用してJSONファイルからPDF文書のフォームフィールドに値をインポートする方法を示しています。FileStreamはJSONファイルを処理するために使用されます。

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