---
title: PDFの権限を設定する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/set-privileges/
description: Aspose.PDFを使用してPDFファイル内のユーザー権限を変更し、特定のアクションを制限する方法を発見してください。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges on PDF",
    "alternativeHeadline": "Set Custom Permissions for PDF Document Security",
    "abstract": "PdfFileSecurityクラスを使用して既存のPDFファイルに権限を設定する新しい機能を紹介します。これにより、ユーザーは印刷やコピーなどのアクションに対する権限を指定できます。さらに、ユーザーはPDF文書から拡張権を簡単に削除できるようになり、文書の変更とセキュリティに対するより大きな制御を確保します。この機能はPDF管理を効率化し、セキュリティコンプライアンスを強化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "436",
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
    "url": "/net/set-privileges/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 既存のPDFファイルの権限を設定する

PDFファイルの権限を設定するには、[PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity)オブジェクトを作成し、SetPrivilegeメソッドを呼び出します。DocumentPrivilegeオブジェクトを使用して権限を指定し、このオブジェクトをSetPrivilegeメソッドに渡すことができます。以下のコードスニペットは、PDFファイルの権限を設定する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilege1()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Create DocumentPrivileges object and set needed privileges
    var privilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample.pdf");
        // Set privilege
        fileSecurity.SetPrivilege(privilege);
        // Save PDF document
        fileSecurity.Save(dataDir + "SamplePrivileges_out.pdf");
    }
}
```

パスワードを指定する以下のメソッドを参照してください：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilegeWithPassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Create DocumentPrivileges object and set needed privileges
    var privilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample.pdf");
        // Set privilege and passwords
        fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
        // Save PDF document
        fileSecurity.Save(dataDir + "SamplePrivilegesPassword_out.pdf");
    }
}
```

## PDFから拡張権機能を削除する

PDF文書は、Adobe Acrobat Readerを使用してフォームフィールドにデータを入力し、入力されたフォームのコピーを保存できるようにするために、拡張権機能をサポートしています。しかし、これによりPDFファイルが変更されないことが保証され、PDFの構造に変更が加えられると、拡張権機能は失われます。そのような文書を表示すると、文書が変更されたために拡張権が削除されたというエラーメッセージが表示されます。最近、PDF文書から拡張権を削除する要求がありました。

PDFファイルから拡張権を削除するには、PdfFileSignatureクラスにRemoveUsageRights()という新しいメソッドが追加されました。もう一つのメソッドContainsUsageRights()が追加され、ソースPDFが拡張権を含むかどうかを判断します。

{{% alert color="primary" %}}
Aspose.PDF for .NET 9.5.0以降、以下のメソッドの名前が更新されました。以前のメソッドはAPIに残っていますが、非推奨としてマークされ、削除される予定です。したがって、更新されたメソッドを使用することをお勧めします。

- IsContainSignature(.)メソッドはContainsSignature(..)に名前が変更されました。
- IsCoversWholeDocument(..)メソッドはCoversWholeDocument(..)に名前が変更されました。
{{% /alert %}}

以下のコードは、文書から使用権を削除する方法を示しています：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveExtendedRights()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
    
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "DigitallySign.pdf");
        if (pdfSign.ContainsUsageRights())
        {
            pdfSign.RemoveUsageRights();
        }
        // Save PDF document
        pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
    }
}
```