---
title: AcroFormの抽出 - C#でPDFからフォームデータを抽出
linktitle: AcroFormの抽出
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ja/net/extract-form/
description: Aspose.PDF for .NETライブラリを使用してPDFドキュメントからフォームを抽出します。PDFファイルの個々のフィールドから値を取得します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract AcroForm - Extract Form Data from PDF in C#",
    "alternativeHeadline": "Effortlessly Extract PDF Form Data Using C#",
    "abstract": "Aspose.PDF for .NETの新しいAcroForm抽出機能により、開発者はPDFドキュメントからフォームデータを簡単に抽出できます。この機能により、ユーザーはPDF内の個々のフィールドまたはすべてのフィールドから値を取得でき、C#アプリケーションにおけるデータ管理と操作能力が向上します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "extract form data, PDF in C#, Aspose.PDF for .NET, AcroForm extraction, get field values PDF, PDF form fields, individual field value, get fields in region, manipulate PDF forms, C# PDF library",
    "wordcount": "673",
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
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NETライブラリを使用してPDFドキュメントからフォームを抽出します。PDFファイルの個々のフィールドから値を取得します。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

## フォームからデータを抽出

### PDFドキュメントのすべてのフィールドから値を取得

PDFドキュメントのすべてのフィールドから値を取得するには、すべてのフォームフィールドをナビゲートし、次にValueプロパティを使用して値を取得する必要があります。Formコレクションから各フィールドを取得し、基本フィールドタイプであるFieldにアクセスして、そのValueプロパティにアクセスします。

次のC#コードスニペットは、PDFドキュメントからすべてのフィールドの値を取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetValuesFromFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValuesFromAllFields.pdf"))
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

### PDFドキュメントの個々のフィールドから値を取得

フォームフィールドのValueプロパティを使用すると、特定のフィールドの値を取得できます。値を取得するには、DocumentオブジェクトのFormコレクションからフォームフィールドを取得します。このC#の例では、[TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield)を選択し、そのValueプロパティを使用して値を取得します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetValueFromField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValueFromField.pdf"))
    {
        // Get a field
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.TextBoxField textBoxField)
        {
            // Get field value
            Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
            Console.WriteLine("Value : {0} ", textBoxField.Value);
        }
    }
}
```

送信ボタンのURLを取得するには、次のコード行を使用します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetSubmitFormActionUrl()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValueFromField.pdf"))
    {
        // Get the SubmitFormAction from the form field
        if (document.Form[1].OnActivated is Aspose.Pdf.Annotations.SubmitFormAction act)
        {
            // Output the URL of the SubmitFormAction
            Console.WriteLine(act.Url.Name);
        }
    }
}
```

### PDFファイルの特定の領域からフォームフィールドを取得

場合によっては、ドキュメント内のフォームフィールドの位置を知っているが、その名前を知らないことがあります。たとえば、印刷されたフォームのスキーマしかない場合です。Aspose.PDF for .NETを使用すれば、これは問題ではありません。PDFファイルの特定の領域にどのフィールドがあるかを確認できます。特定の領域からフォームフィールドを取得するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを使用してPDFファイルを開きます。
1. ドキュメントのFormsコレクションからフォームを取得します。
1. 矩形領域を指定し、それをFormオブジェクトのGetFieldsInRectメソッドに渡します。Fieldsコレクションが返されます。
1. これを使用してフィールドを操作します。

次のC#コードスニペットは、PDFファイルの特定の矩形領域にあるフォームフィールドを取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldsFromRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf"))
    {
        // Create rectangle object to get fields in that area
        var rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

        // Get the PDF form
        var form = document.Form;

        // Get fields in the rectangular area
        var fields = form.GetFieldsInRect(rectangle);

        // Display Field names and values
        foreach (var field in fields)
        {
            // Display image placement properties for all placements
            Console.Out.WriteLine("Field Name: " + field.FullName + "-" + "Field Value: " + field.Value);
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>