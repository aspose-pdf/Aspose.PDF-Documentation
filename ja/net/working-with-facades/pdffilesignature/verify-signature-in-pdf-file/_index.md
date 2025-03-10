---
title: PDFファイルの署名を確認する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ja/net/verify-signature-in-pdf/
description: このセクションでは、PdfFileSignatureクラスを使用してPDFファイルの署名を確認する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Verify Signature in PDF File",
    "alternativeHeadline": "Verify Signatures in PDF Files Efficiently",
    "abstract": "この機能により、ユーザーはPdfFileSignatureクラスを使用してPDFファイル内の署名を効率的に確認できます。署名の存在とその有効性を確認するためのメソッドを備えたこの機能は、文書の真正性と整合性を確保するプロセスを簡素化します。PDFのセキュリティをシームレスに確認することで、文書管理を最適化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
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
    "url": "/net/verify-signature-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/verify-signature-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDFファイルが署名されているかどうかを確認する

特定の署名を使用してPDFファイルが署名されているかどうかを確認するには、[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)クラスのVerifySignedメソッドを使用します。このメソッドは署名名を必要とし、その署名名を使用してPDFが署名されている場合はtrueを返します。また、どの署名で署名されているかを確認せずに[PDFが署名されているか](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)を確認することも可能です。

### 特定の署名でPDFが署名されていることを確認する

以下のコードスニペットは、特定の署名を使用してPDFが署名されているかどうかを確認する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IsPdfSigned()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {      
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.ContainsSignature())
        {
            Console.WriteLine("Document Signed");
        }
    }
}
```

### PDFが署名されているかどうかを確認する

署名名を提供せずにファイルが署名されているかどうかを判断するには、以下のコードを使用します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IsPdfSignedWithGivenSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.VerifySignature("Signature1"))
        {
            Console.WriteLine("PDF Signed");
        }
    }
}
```

## 署名が有効かどうかを確認する

[VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature)メソッドは、[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)クラスの特定の署名を検証するために使用されます。このメソッドは署名名を入力として必要とし、署名が有効な場合はtrueを返します。以下のコードスニペットは、署名を検証する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IsPdfSignatureValid()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.VerifySignature("Signature1"))
        {
            Console.WriteLine("Signature Verified");
        }
    }
}
```