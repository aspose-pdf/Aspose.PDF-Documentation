---
title: PDFファイルの復号化
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/decrypt-pdf-file/
description: Aspose.PDFを使用して、.NETでパスワード保護されたPDFファイルを復号化する方法を探ります。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Decrypt PDF File",
    "alternativeHeadline": "Unlock Encrypted PDFs with Ease Using PdfFileSecurity",
    "abstract": "PdfFileSecurityクラスを使用して新しいPDFファイル復号化機能で、PDFドキュメントを簡単に解除できます。この機能により、ユーザーは暗号化されたPDFからパスワード保護を削除し、ドキュメントへのシームレスなアクセスと操作を可能にします。強力なDecryptFileメソッドを活用して、安全なPDF処理のためのシンプルなドキュメント管理アプローチを体験してください。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "235",
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
    "url": "/net/decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/decrypt-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

パスワードまたは証明書で暗号化されたPDFドキュメントは、他の操作を実行する前に解除する必要があります。暗号化されたPDFドキュメントに対して操作を試みると、例外がスローされます。暗号化されたPDFを解除した後は、1つ以上の操作を実行できます。

## オーナーパスワードを使用してPDFファイルを復号化する

{{% alert color="primary" %}}
オンラインで試す <br>
Aspose.PDFを使用してドキュメントを解除し、次のリンクで結果をオンラインで取得できます：
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

PDFファイルを復号化するには、[PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity)オブジェクトを作成し、次に[DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile)メソッドを呼び出す必要があります。また、[DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile)メソッドにオーナーパスワードを渡す必要があります。以下のコードスニペットは、PDFファイルを復号化する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecryptPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample_encrypted.pdf"))
    {
        if (pdfFileInfo.IsEncrypted)
        {
            using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
            {
                // Bind PDF document
                fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
                // Decrypt PDF document
                fileSecurity.DecryptFile("P@ssw0rd");
                // Save PDF document
                fileSecurity.Save(dataDir + "SampleDecrtypted_out.pdf");
            }
        }
    }
}
```