---
title: AcroFormからC#を使用してデータを抽出
linktitle: AcroFormからデータを抽出
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/extract-data-from-acroform/
description: Aspose.PDFは、PDFファイルからフォームフィールドデータを簡単に抽出できます。AcroFormsからデータを抽出し、JSON、XML、またはFDF形式で保存する方法を学びましょう。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Data from AcroForm using C#",
    "alternativeHeadline": "Effortlessly Extract Acrobat Form Data with C#",
    "abstract": "PDF文書のAcroFormsからフォームフィールドデータを抽出するための新しい機能を発見してください。JSON、XML、FDF、およびXFDF形式にデータをエクスポートする機能により、ユーザーはアプリケーションへのシームレスな統合のための簡潔なコード例を活用しながら、フォームデータを効率的に管理できます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "826",
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
    "url": "/net/extract-data-from-acroform/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-data-from-acroform/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDF文書からフォームフィールドを抽出

Aspose.PDF for .NETは、フォームフィールドを生成し、フォームフィールドを入力するだけでなく、PDFファイルからフォームフィールドデータやフォームフィールドに関する情報を簡単に抽出できます。

以下のサンプルコードでは、PDF内のすべてのAcroFormに関する情報とフォームフィールドの値を抽出するために、PDFの各ページを反復処理する方法を示します。このサンプルコードは、事前にフォームフィールドの名前を知らないことを前提としています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {
        // Get values from all fields
        foreach (Aspose.Pdf.Forms.Field formField in document.Form)
        {
            Console.WriteLine("Field Name : {0} ", formField.PartialName);
            Console.WriteLine("Value : {0} ", formField.Value);
        }
    }
}
```

抽出したいフォームフィールドの名前がわかっている場合は、Documents.Formコレクションのインデクサを使用して、このデータを迅速に取得できます。その機能の使用方法については、この記事の下部にあるサンプルコードを参照してください。

## タイトルによるフォームフィールド値の取得

フォームフィールドのValueプロパティを使用すると、特定のフィールドの値を取得できます。値を取得するには、DocumentオブジェクトのFormコレクションからフォームフィールドを取得します。この例では、TextBoxFieldを選択し、その値をValueプロパティを使用して取得します。

## PDF文書からJSONにフォームフィールドを抽出

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFieldsToJson()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {
        // Extract form fields and convert to JSON
        var formData = document.Form.Cast<Aspose.Pdf.Forms.Field>().Select(f => new { Name = f.PartialName, f.Value });
        string jsonString = System.Text.Json.JsonSerializer.Serialize(formData);

        // Output the JSON string
        Console.WriteLine(jsonString);
    }
}
```

## PDFファイルからXMLにデータを抽出

Formクラスを使用すると、ExportXmlメソッドを使用してPDFファイルからXMLファイルにデータをエクスポートできます。データをXMLにエクスポートするには、Formクラスのオブジェクトを作成し、FileStreamオブジェクトを使用してExportXmlメソッドを呼び出す必要があります。最後に、FileStreamオブジェクトを閉じてFormオブジェクトを破棄できます。以下のコードスニペットは、データをXMLファイルにエクスポートする方法を示しています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFormDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            form.ExportXml(xmlOutputStream);
        }
    }
}
```

## PDFファイルからFDFにデータをエクスポート

Formクラスを使用すると、ExportFdfメソッドを使用してPDFファイルからFDFファイルにデータをエクスポートできます。データをFDFにエクスポートするには、Formクラスのオブジェクトを作成し、FileStreamオブジェクトを使用してExportFdfメソッドを呼び出す必要があります。最後に、FormクラスのSaveメソッドを使用してPDFファイルを保存できます。以下のコードスニペットは、データをFDFファイルにエクスポートする方法を示しています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create fdf file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            form.ExportFdf(fdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToPdf_out.pdf");
    }
}
```

## PDFファイルからXFDFにデータをエクスポート

Formクラスを使用すると、ExportXfdfメソッドを使用してPDFファイルからXFDFファイルにデータをエクスポートできます。データをXFDFにエクスポートするには、Formクラスのオブジェクトを作成し、FileStreamオブジェクトを使用してExportXfdfメソッドを呼び出す必要があります。最後に、FormクラスのSaveメソッドを使用してPDFファイルを保存できます。以下のコードスニペットは、データをXFDFファイルにエクスポートする方法を示しています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create xfdf file
        using (var xfdfOutputStream = new FileStream(dataDir + "student1.xfdf", FileMode.Create))
        {
            // Export data
            form.ExportXfdf(xfdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToXFDF_out.pdf");
    }
}
```