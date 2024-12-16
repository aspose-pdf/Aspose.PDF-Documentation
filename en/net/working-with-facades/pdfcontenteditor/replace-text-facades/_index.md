---
title: Replace Text - Facades
type: docs
weight: 40
url: /net/replace-text-facades/
description: This section explains how to work with Text - Facades using PdfContentEditor Class.
lastmod: "2021-06-24"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Replace Text - Facades",
    "alternativeHeadline": "Effortless Text Replacement in PDF Files",
    "abstract": "The Replace Text feature in the PdfContentEditor class allows users to efficiently modify textual content within existing PDF documents. By using simple methods like BindPdf and ReplaceText, users can seamlessly update text, adjust font sizes, and customize text formatting, including bold and color, all while maintaining the integrity of the original document. This functionality enhances PDF editing capabilities, making it easier to manage content dynamically",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "550",
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
    "url": "/net/replace-text-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-facades/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Replace Text in an Existing PDF File

In order to replace text in an existing PDF file, you need to create an object of [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class and bind an input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, you need to call [ReplaceText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index) method. You need to save the updated PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method of [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class. The following code snippet shows you how to replace text in an existing PDF file.

```csharp
public static void ReplaceText01()
{
    PdfContentEditor editor = new PdfContentEditor();
    ditor.BindPdf(dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label");

    // save the output file
    editor.Save(dataDir + "PdfContentEditorDemo01.pdf");
}
```

Check how it's looks in the original document:

![Replace Text](replace_text1.png)

And check the result after replacing the text:

![Result of replacing Text](replace_text2.png)

In the second example, you will see how, in addition to replacing the text, you can also increase or decrease the font size:

```csharp
public static void ReplaceText02()
{
    PdfContentEditor editor = new PdfContentEditor();
    editor.BindPdf(dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label", 12);

    // save the output file
    editor.Save(dataDir + "PdfContentEditorDemo02.pdf");
}
```

For more advanced possibilities for working with our text, we will use the [TextState](https://reference.aspose.com/pdf/net/aspose.pdf.text/textstate) method. With this method, we can make text bold, italic, colored, and so on.

```csharp
public static void ReplaceText03()
{
    PdfContentEditor editor = new PdfContentEditor();
    editor.BindPdf(dataDir + "sample.pdf");
    TextState textState = new TextState
    {
        ForegroundColor = Color.Red,
        FontSize = 12,
    };
    editor.ReplaceText("Value", "Label", textState);

    // save the output file
    editor.Save(dataDir + "PdfContentEditorDemo03.pdf");
}
```

In case you need to replace all the specified text in the document, use the following code snippet. That is, the replacement of the text will take place wherever the text specified for replacement will be encountered, and it will also count the number of such replacements.

```csharp
public static void ReplaceText04()
{
    PdfContentEditor editor = new PdfContentEditor();
    editor.BindPdf(dataDir + "sample.pdf");
    int count = 0;
    while (editor.ReplaceText("Value", "Label"))
    { 
        count++;
    }

    Console.WriteLine($"{count} occurrences have been replaced.");

    // save the output file
    editor.Save(dataDir + "PdfContentEditorDemo04.pdf");
}
```

![Replace all Text](replace_text3.png)

The following code snippet shows how to make all the text replacements but on a specific page of your document.

```csharp
public static void ReplaceText05()
{
    PdfContentEditor editor = new PdfContentEditor();
    editor.BindPdf(dataDir + "sample.pdf");
    int count = 0;
    while (editor.ReplaceText("9999", 2, "ABCDE"))
    {
        count++;
    }
    
    Console.WriteLine($"{count} occurrences have been replaced.");

    // save the output file
    editor.Save(dataDir + "PdfContentEditorDemo05.pdf");
}
```

In the next code snippet, we will show how to replace, for example, a given number with the letters we need.

```csharp
public static void ReplaceText06()
{
    PdfContentEditor editor = new PdfContentEditor
    {
        ReplaceTextStrategy = new ReplaceTextStrategy
        {
            IsRegularExpressionUsed = true,
            ReplaceScope = ReplaceTextStrategy.Scope.ReplaceAll
        }
    };
    editor.BindPdf(dataDir + "sample.pdf");
    editor.ReplaceText("\\d{4}", "ABCDE");
    // save the output file
    editor.Save(dataDir + "PdfContentEditorDemo06.pdf");
}
```