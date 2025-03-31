---
title: PDFファイルの暗号化
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/encrypt-pdf-file/
description: このトピックでは、PdfFileSecurityクラスを使用してPDFファイルを暗号化する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Encrypt PDF File",
    "alternativeHeadline": "Secure PDF Encryption with C#",
    "abstract": "PdfFileSecurityクラスを使用して、機密文書のセキュリティを強化する新しいPDF暗号化機能を発見してください。この機能により、PDFファイルをパスワードで保護し、認可されたユーザーのみがアクセスできるようにします。ファイル共有やアーカイブ中の堅牢な保護のために、最大256ビットのキー長を持つAESを含むさまざまな暗号化タイプとアルゴリズムを探求してください。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "273",
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
    "url": "/net/encrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/encrypt-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

PDF文書を暗号化することで、その内容を外部からの不正アクセスから保護し、特にファイル共有やアーカイブ中に安全性を確保します。

機密PDF文書は暗号化され、パスワードで保護されることがあります。パスワードを知っているユーザーのみが、これらの文書を復号化し、開いて表示することができます。

Aspose.PDFライブラリを使用してPDF暗号化がどのように機能するかを見てみましょう。

## 異なる暗号化タイプとアルゴリズムを使用してPDFファイルを暗号化する

PDFファイルを暗号化するには、[PdfFileSecurity](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilesecurity)オブジェクトを作成し、次に[EncryptFile](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile)メソッドを呼び出す必要があります。ユーザーパスワード、オーナーパスワード、および権限を[EncryptFile](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile)メソッドに渡すことができます。また、このメソッドにKeySizeとAlgorithmの値を渡す必要があります。

以下は、可能な[CryptoAlgorithm](https://reference.aspose.com/pdf/ja/net/aspose.pdf/cryptoalgorithm)のリストです：

|**メンバー名**|**値**|**説明**|
| :- | :- | :- |
|RC4x40|0|キー長40のRC4。|
|RC4x128|1|キー長128のRC4。|
|AESx128|2|キー長128のAES。|
|AESx256|3|キー長256のAES。|

以下のコードスニペットは、PDFファイルを暗号化する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "input.pdf");
        // Encrypt file using 256-bit encryption
        fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256,
            Aspose.Pdf.Facades.Algorithm.AES);
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleEncrypted_out.pdf");
    }
}
```