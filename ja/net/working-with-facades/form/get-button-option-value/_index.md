---
title: ボタンオプション値の取得
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/get-button-option-value/
description: このセクションでは、Formクラスを使用してAspose.PDF Facadesからボタンオプション値を取得する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Button Option Value",
    "alternativeHeadline": "Retrieve Button Option Values from PDF Efficiently",
    "abstract": "Aspose.PDF Facadesを使用して既存のPDFファイルからボタンオプション値を効率的に取得する方法を発見してください。FormクラスのGetButtonOptionValuesおよびGetButtonOptionCurrentValueメソッドを使用すると、ラジオボタンのすべての利用可能なオプションと現在選択されている値を簡単に取得でき、PDFフォーム管理機能が向上します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "275",
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
    "url": "/net/get-button-option-value/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-button-option-value/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 既存のPDFファイルからボタンオプション値を取得する

ラジオボタンは、異なるオプションを表示する方法を提供します。[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form)クラスを使用すると、特定のラジオボタンのすべてのボタンオプション値を取得できます。これらの値は、[GetButtonOptionValues](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues)メソッドを使用して取得できます。このメソッドは、ラジオボタンの名前を入力パラメータとして要求し、Hashtableを返します。このHashtableを反復処理してオプション値を取得できます。以下のコードスニペットは、既存のPDFファイルからボタンオプション値を取得する方法を示しています。
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetButtonOptions()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        var optionValues = pdfForm.GetButtonOptionValues("Gender");

        IDictionaryEnumerator optionValueEnumerator = optionValues.GetEnumerator();

        while (optionValueEnumerator.MoveNext())
        {
            Console.WriteLine("Key : {0} , Value : {1} ", optionValueEnumerator.Key, optionValueEnumerator.Value);
        }
    }
}
```

## 既存のPDFファイルから現在のボタンオプション値を取得する

ラジオボタンはオプション値を設定する方法を提供しますが、一度に1つだけ選択できます。現在選択されているオプション値を取得したい場合は、[GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue)メソッドを使用できます。[Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form)クラスはこのメソッドを提供します。このメソッドは、ラジオボタンの名前を入力パラメータとして要求し、値を文字列として返します。以下のコードスニペットは、既存のPDFファイルから現在のボタンオプション値を取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetCurremtButtonOptionValue()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        string optionValue = pdfForm.GetButtonOptionCurrentValue("Gender");

        Console.WriteLine("Current Value : {0} ", optionValue);
    }
}
```