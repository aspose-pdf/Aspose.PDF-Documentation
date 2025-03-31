---
title: PDFファイルのパスワードを変更する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/change-password/
description: Aspose.PDFを使用して、.NETでPDFドキュメントのパスワードを変更してファイルのセキュリティを向上させる方法を探ります。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Change Password of PDF File",
    "alternativeHeadline": "Securely Change PDF Passwords with Ease",
    "abstract": "PdfFileSecurityクラスを使用して、PDFのセキュリティを簡単に強化できます。この機能により、ユーザーとオーナーのパスワードの両方を変更でき、不正アクセスに対する強力な保護を確保しながら、権限を効果的に管理できます。シンプルな実装でドキュメントのセキュリティ設定を簡単に最適化できます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "250",
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
    "url": "/net/change-password/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-password/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDFファイルのパスワードを変更する

PDFファイルのパスワードを変更するには、[PdfFileSecurity](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilesecurity)オブジェクトを作成し、次に[ChangePassword](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2)メソッドを呼び出す必要があります。既存のオーナーパスワードと新しいユーザーパスワードおよびオーナーパスワードを[ChangePassword](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2)メソッドに渡す必要があります。

{{% alert color="primary" %}}

- **ユーザーパスワード**が設定されている場合、PDFを開くために提供する必要があります。Acrobat/Readerはユーザーにユーザーパスワードの入力を促します。正しくない場合、ドキュメントは開きません。
- **オーナーパスワード**が設定されている場合、印刷、編集、抽出、コメントなどの権限を制御します。Acrobat/Readerは、権限設定に基づいてこれらの操作を許可しません。権限を設定/変更したい場合は、このパスワードが必要です。

{{% /alert %}}

次のコードスニペットは、PDFファイルのパスワードを変更する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdfFileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample_encrypted.pdf"))
    {
        // Create PdfFileSecurity object if the document is encrypted
        if (pdfFileInfo.IsEncrypted)    
        {
            using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
            {
                // Bind PDF document
                fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256);
                // Save PDF document
                fileSecurity.Save(dataDir + "sample_encrtypted1.pdf");
            }
        }
    }
}
```