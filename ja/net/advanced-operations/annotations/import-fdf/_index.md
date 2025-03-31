---
title: FDF形式の注釈をC#経由でPDFにインポート
linktitle: FDF形式の注釈をPDFにインポート
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/import-fdf/
description: 既存のForm.ImportFdf()またはPdfAnnotationEditor.ImportAnnotationsFromFdf()メソッドを使用して、Aspose.PDF for .NETを使用してFDF形式の注釈をPDFにインポートします。
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import FDF format annotations to PDF via C#",
    "alternativeHeadline": "Effortlessly Import FDF Annotations to PDF with C#",
    "abstract": "Aspose.PDF for .NETを使用してFDF形式の注釈をPDFファイルにシームレスにインポートし、PDF管理機能を強化します。Form.ImportFdf()およびPdfAnnotationEditor.ImportAnnotationsFromFdf()メソッドを使用すると、軽量のFDFファイルからフォームデータとコメントをPDF文書に簡単に統合でき、データの提出と注釈プロセスを効率化できます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import FDF, FDF format annotations, PDF annotations, Aspose.PDF for .NET, Form.ImportFdf(), PdfAnnotationEditor, import annotations from FDF, lightweight PDF, fill form fields, exchange annotations",
    "wordcount": "350",
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
    "url": "/net/import-fdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-fdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

FDF（Forms Data Format）は、PDF文書内のフォームデータと注釈を保存および送信するファイル形式です。これは、元のPDFファイルの完全な内容を含まず、フォームフィールドの値やコメントのみを含む軽量PDFバージョンです。FDFファイルは、フォームデータをサーバーに送信する際や、PDFファイル全体を送信することなく注釈を交換する際によく使用されます。これらはPDFに再インポートしてフォームフィールドを埋めたり、コメントを適用したりできます。

{{% /alert %}}

[PDFAnnotationEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfannotationeditor/)クラスには、FDFファイルからの注釈のインポートに関するメソッドが含まれています。[PdfAnnotationEditor.ImportAnnotationsFromFdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfannotationeditor/importannotationsfromfdf/)メソッドは、FDFドキュメントからPDFファイルに注釈をインポートする機能を提供します。

また、[Class Form](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/)には、FDFファイルからフィールドの内容をインポートし、新しいPDFに配置する[Form.ImportFdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/importfdf/)メソッドが含まれています。

次のコードスニペットは、Form.ImportFdf()メソッドを使用してFDF形式の注釈をPDFにインポートする方法を示しています：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFDFByForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "input.pdf"))
    {
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }
        // Save PDF document
        form.Save(dataDir + "ImportDataFromPdf_Form_out.pdf");
    }
}
```

次のコードスニペットは、PdfAnnotationEditor.ImportAnnotationsFromFdf()メソッドを使用してFDF形式の注釈をPDFにインポートする方法を示しています：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFdfByPdfAnnotationEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        var editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
        // Bind PDF document
        editor.BindPdf(dataDir + "input.pdf");
        editor.ImportAnnotationsFromFdf(dataDir + "student.fdf");
        // Save PDF document
        editor.Save(dataDir + "ImportDataFromPdf_AnnotationEditor_out.pdf");  
    }
}
```