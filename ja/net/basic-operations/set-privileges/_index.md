---
title: 権限の設定、PDFの暗号化と復号化
linktitle: PDFファイルの暗号化と復号化
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ja/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: C#を使用して異なる暗号化タイプとアルゴリズムでPDFファイルを暗号化します。また、オーナーパスワードを使用してPDFファイルを復号化します。
lastmod: "2024-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges, Encrypt and Decrypt PDF",
    "alternativeHeadline": "Set PDF Privileges and Secure with Encryption with C#",
    "abstract": "この新機能により、ユーザーはC#を使用してさまざまな暗号化タイプとアルゴリズムでPDFファイルを効率的に暗号化および復号化できます。ユーザーおよびオーナーパスワードを利用することで、文書へのアクセスと権限を強力に制御し、PDFコンテンツの機密性と整合性を確保しながら、開発者のセキュリティ管理を簡素化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1586",
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
    "url": "/net/set-privileges-encrypt-and-decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges-encrypt-and-decrypt-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "C#を使用して異なる暗号化タイプとアルゴリズムでPDFファイルを暗号化します。また、オーナーパスワードを使用してPDFファイルを復号化します。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも機能します。

## 既存のPDFファイルに権限を設定する

PDFファイルに権限を設定するには、[DocumentPrivilege](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/documentprivilege)クラスのオブジェクトを作成し、文書に適用したい権利を指定します。権限が定義されたら、このオブジェクトを[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)オブジェクトの[Encrypt](https://reference.aspose.com/pdf/ja/net/aspose.pdf.document/encrypt/methods/1)メソッドに引数として渡します。次のコードスニペットは、PDFファイルの権限を設定する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilegesOnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate Document Privileges object
        // Apply restrictions on all privileges
        var documentPrivilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
        // Only allow screen reading
        documentPrivilege.AllowScreenReaders = true;
        // Encrypt the file with User and Owner password
        // Need to set the password, so that once the user views the file with user password
        // Only screen reading option is enabled
        document.Encrypt("user", "owner", documentPrivilege, Aspose.Pdf.CryptoAlgorithm.AESx128, false);
        // Save PDF document
        document.Save(dataDir + "SetPrivileges_out.pdf");
    }
}
```

## 異なる暗号化タイプとアルゴリズムを使用してPDFファイルを暗号化する

[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)オブジェクトの[Encrypt](https://reference.aspose.com/pdf/ja/net/aspose.pdf.document/encrypt/methods/1)メソッドを使用してPDFファイルを暗号化できます。ユーザーパスワード、オーナーパスワード、および権限を[Encrypt](https://reference.aspose.com/pdf/ja/net/aspose.pdf.document/encrypt/methods/1)メソッドに渡すことができます。さらに、[CryptoAlgorithm](https://reference.aspose.com/pdf/ja/net/aspose.pdf/cryptoalgorithm)列挙体の任意の値を渡すことができます。この列挙体は、暗号化アルゴリズムとキーサイズのさまざまな組み合わせを提供します。選択した値を渡すことができます。最後に、[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)オブジェクトの[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf.document/save/methods/4)メソッドを使用して暗号化されたPDFファイルを保存します。

>PDFファイルを暗号化する際には、異なるユーザーおよびオーナーパスワードを指定してください。

- **ユーザーパスワード**が設定されている場合、PDFを開くために必要です。Acrobat/Readerはユーザーにユーザーパスワードの入力を促します。正しくない場合、文書は開きません。
- **オーナーパスワード**が設定されている場合、印刷、編集、抽出、コメントなどの権限を制御します。Acrobat/Readerは、権限設定に基づいてこれらの操作を禁止します。権限を設定/変更する場合、このパスワードが必要です。

次のコードスニペットは、PDFファイルを暗号化する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Encrypt.pdf"))
    {
        // Encrypt PDF
        document.Encrypt("user", "owner", 0, Aspose.Pdf.CryptoAlgorithm.RC4x128);
        // Save PDF document
        document.Save(dataDir + "Encrypt_out.pdf");
    }
}
```

## オーナーパスワードを使用してPDFファイルを復号化する

ユーザーは、文書への不正アクセスを防ぐために暗号化されたPDFファイルを交換することが増えています。たとえば、印刷、コピー、共有、PDFファイルの内容に関する情報の抽出などです。今日、PDFファイルを暗号化する最良の選択肢は、コンテンツの機密性と整合性を維持することです。この点において、暗号化されたPDFファイルにアクセスする必要があります。このアクセスは、認可されたユーザーのみが取得できます。また、人々はインターネット上でPDFファイルを復号化するさまざまなソリューションを探しています。

この問題は、Aspose.PDFライブラリを使用して一度で解決するのが最善です。

PDFファイルを復号化するには、まず[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)オブジェクトを作成し、オーナーパスワードを使用してPDFを開く必要があります。その後、[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)オブジェクトの[Decrypt](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/decrypt)メソッドを呼び出す必要があります。最後に、[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)オブジェクトの[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf.document/save/methods/4)メソッドを使用して更新されたPDFファイルを保存します。次のコードスニペットは、PDFファイルを復号化する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecryptPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document with password
    using (var document = new Aspose.Pdf.Document(dataDir + "Decrypt.pdf", "password"))
    {
        // Decrypt PDF
        document.Decrypt();
        // Save PDF document
        document.Save(dataDir + "Decrypt_out.pdf");
    }
}
```

## PDFファイルのパスワードを変更する

PDFファイルのパスワードを変更するには、まず[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)オブジェクトを使用してオーナーパスワードでPDFファイルを開く必要があります。その後、[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)オブジェクトの[ChangePasswords](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/changepasswords)メソッドを呼び出す必要があります。このメソッドには、現在のオーナーパスワードと新しいユーザーパスワード、新しいオーナーパスワードを渡す必要があります。最後に、[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)オブジェクトの[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf.document/save/methods/4)メソッドを使用して更新されたPDFファイルを保存します。

>- ユーザーパスワードが設定されている場合、PDFを開くために必要です。Acrobat/Readerはユーザーにユーザーパスワードの入力を促します。正しくない場合、文書は開きません。
>- オーナーパスワードが設定されている場合、印刷、編集、抽出、コメントなどの権限を制御します。Acrobat/Readerは、権限設定に基づいてこれらの操作を禁止します。権限を設定/変更する場合、このパスワードが必要です。

次のコードスニペットは、PDFファイルのパスワードを変更する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document with password
    using (var document = new Aspose.Pdf.Document(dataDir + "ChangePassword.pdf", "owner"))
    {
        // Change password
        document.ChangePasswords("owner", "newuser", "newowner");
        // Save PDF document
        document.Save(dataDir + "ChangePassword_out.pdf");
    }
}
```

## ソースPDFがパスワード保護されているかどうかを判断する方法

**Aspose.PDF for .NET**は、PDF文書を扱うための優れた機能を提供します。Aspose.PDF名前空間のDocumentクラスを使用してパスワード保護されたPDF文書を開く場合、パスワード情報をDocumentコンストラクタに引数として提供する必要があります。この情報が提供されない場合、エラーメッセージが生成されます。実際、DocumentオブジェクトでPDFファイルを開こうとすると、コンストラクタはPDFファイルの内容を読み取ろうとし、正しいパスワードが提供されない場合、エラーメッセージが生成されます（これは文書への不正アクセスを防ぐために行われます）。

暗号化されたPDFファイルを扱う際には、PDFにオープンパスワードおよび/または編集パスワードがあるかどうかを検出したいシナリオに遭遇することがあります。時には、開く際にパスワード情報を必要としない文書もありますが、ファイルの内容を編集するためには情報が必要です。したがって、上記の要件を満たすために、Aspose.PDF.FacadesのPdfFileInfoクラスは、必要な情報を判断するのに役立つプロパティを提供します。

### PDF文書のセキュリティに関する情報を取得する

PdfFileInfoには、PDF文書のセキュリティに関する情報を取得するための3つのプロパティがあります。

1. プロパティPasswordTypeは、PasswordType列挙体の値を返します：
    - PasswordType.None - 文書はパスワード保護されていません。
    - PasswordType.User - 文書はユーザー（または文書オープン）パスワードで開かれました。
    - PasswordType.Owner - 文書はオーナー（または権限、編集）パスワードで開かれました。
    - PasswordType.Inaccessible - 文書はパスワード保護されていますが、無効なパスワード（またはパスワードなし）を提供したため、開くためのパスワードが必要です。
2. booleanプロパティHasOpenPassword - 入力ファイルを開く際にパスワードが必要かどうかを判断するために使用されます。
3. booleanプロパティHasEditPassword - 入力ファイルの内容を編集するためにパスワードが必要かどうかを判断するために使用されます。

### 配列から正しいパスワードを判断する

時には、パスワードの配列から正しいパスワードを判断し、正しいパスワードで文書を開く必要があります。次のコードスニペットは、パスワードの配列を反復処理し、正しいパスワードで文書を開く手順を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineCorrectPasswordFromArray()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var info = new  Aspose.Pdf.Facades.PdfFileInfo())
    {
        // Bind PDF document
        info.BindPdf(dataDir + "IsPasswordProtected.pdf");
        // Determine if the source PDF is encrypted
        Console.WriteLine("File is password protected " + info.IsEncrypted);
    
        String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
    
        for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
        {
            try
            {
                using (var document = new Aspose.Pdf.Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]))
                {
                    if (document.Pages.Count > 0)
                    {
                        Console.WriteLine("Number of Page in document are = " + document.Pages.Count);
                    }
                }
            }
            catch (Aspose.Pdf.InvalidPasswordException)
            {
                Console.WriteLine("Password = " + passwords[passwordcount] + "  is not correct");
            }
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