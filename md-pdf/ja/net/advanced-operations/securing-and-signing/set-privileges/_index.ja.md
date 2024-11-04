---
title: 権限を設定し、PDFを暗号化および復号化する
linktitle: PDFファイルの暗号化および復号化
type: docs
weight: 20
url: /net/set-privileges-encrypt-and-decrypt-pdf-file/
description: 異なる暗号化タイプとアルゴリズムを使用してC#でPDFファイルを暗号化します。また、所有者のパスワードを使用してPDFファイルを復号化します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "権限を設定し、PDFを暗号化および復号化する",
    "alternativeHeadline": "PDFファイルの暗号化および復号化方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, PDF暗号化, PDF復号化",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDFドキュメントチーム",
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
    "dateModified": "2022-02-04",
    "description": "異なる暗号化タイプとアルゴリズムを使用してC#でPDFファイルを暗号化します。また、所有者のパスワードを使用してPDFファイルを復号化します。"
}
</script>

次のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

## 既存のPDFファイルに権限を設定する

PDFファイルに権限を設定するには、[DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege)クラスのオブジェクトを作成し、ドキュメントに適用したい権利を指定します。権限が定義されたら、このオブジェクトを [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトの [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) メソッドの引数として渡します。次のコードスニペットは、PDFファイルの権限を設定する方法を示しています。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// ソースPDFファイルを読み込む
using (Document document = new Document(dataDir + "input.pdf"))
{
    // Document Privileges オブジェクトをインスタンス化します
    // すべての権限に制限を適用する
    DocumentPrivilege documentPrivilege = DocumentPrivilege.ForbidAll;
    // スクリーンリーディングのみ許可
    documentPrivilege.AllowScreenReaders = true;
    // ユーザーとオーナーパスワードでファイルを暗号化する。
    // パスワードを設定する必要があります。ユーザーパスワードでファイルを表示すると、
    // スクリーンリーディングオプションのみが有効になります
    document.Encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
    // 更新されたドキュメントを保存する
    document.Save(dataDir + "SetPrivileges_out.pdf");
}
```
## PDFファイルを異なる暗号化タイプとアルゴリズムで暗号化する

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトの[Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1)メソッドを使用して、PDFファイルを暗号化できます。[Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1)メソッドには、ユーザーパスワード、オーナーパスワード、および権限を渡すことができます。さらに、[CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm)列挙型の任意の値を渡すことができます。この列挙型は、異なる暗号化アルゴリズムとキーサイズの組み合わせを提供します。お好みの値を渡してください。最後に、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトの[Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して、暗号化されたPDFファイルを保存します。

>PDFファイルを暗号化する際には、異なるユーザーパスワードとオーナーパスワードを指定してください。

- **ユーザーパスワード**が設定されている場合、PDFを開くために必要となります。
- **ユーザーパスワード**が設定されている場合、PDFを開くために必要です。
- **所有者パスワード**が設定されている場合、印刷、編集、抽出、コメントなどの権限を制御します。Acrobat/Readerは、許可設定に基づいてこれらのことを不許可にします。権限を設定/変更したい場合は、Acrobatがこのパスワードを要求します。

次のコードスニペットは、PDFファイルを暗号化する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// ドキュメントを開く
Document document = new Document(dataDir+ "Encrypt.pdf");
// PDFを暗号化
document.Encrypt("user", "owner", 0, CryptoAlgorithm.RC4x128);
dataDir = dataDir + "Encrypt_out.pdf";
// 更新されたPDFを保存
document.Save(dataDir);
```

## 所有者パスワードを使用してPDFファイルを復号化

ますます多くのユーザーが、印刷/コピー/共有/抽出など、PDFファイルの内容についての情報を無許可でアクセスすることを防ぐために、暗号化されたPDFファイルを交換しています。

ますます多くのユーザーが、PDFファイルの印刷/コピー/共有/抽出情報など、文書への不正アクセスを防ぐために暗号化されたPDFファイルを交換しています。
この点で、暗号化されたPDFファイルにアクセスする必要がありますが、そのようなアクセスは認証されたユーザーによってのみ得られます。また、人々はインターネット上でPDFファイルを復号するさまざまな解決策を探しています。

この問題は、Aspose.PDFライブラリを使用して一度に解決する方がよいでしょう。

PDFファイルの復号化を行うには、まず[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを作成し、所有者のパスワードを使用してPDFを開く必要があります。
```
PDFファイルを復号するには、まず[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを作成し、所有者のパスワードを使用してPDFを開く必要があります。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// ドキュメントを開く
Document document = new Document(dataDir+ "Decrypt.pdf", "password");
// PDFを復号
document.Decrypt();
dataDir = dataDir + "Decrypt_out.pdf";
// 更新されたPDFを保存
document.Save(dataDir);
```

## PDFファイルのパスワードを変更する

PDFファイルのパスワードを変更する場合、まず所有者のパスワードを使用して[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトでPDFファイルを開く必要があります。
PDFファイルのパスワードを変更したい場合、まず[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを使用してオーナーパスワードでPDFファイルを開く必要があります。

>- ユーザーパスワードが設定されている場合、PDFを開くために必要です。Acrobat/Readerはユーザーにユーザーパスワードの入力を求めます。正しくない場合、ドキュメントは開かれません。
>- オーナーパスワードが設定されている場合、印刷、編集、抽出、コメントなどの権限を制御します。Acrobat/Readerはこれらの権限設定に基づいてこれらの操作を禁止します。権限を設定/変更したい場合は、このパスワードが必要になります。

次のコードスニペットは、PDFファイルのパスワードを変更する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

// ドキュメントを開く
Document document = new Document(dataDir+ "ChangePassword.pdf", "owner");
// パスワードを変更
document.ChangePasswords("owner", "newuser", "newowner");
dataDir = dataDir + "ChangePassword_out.pdf";
// 更新されたPDFを保存
document.Save(dataDir);
```
## 方法 - ソースPDFがパスワード保護されているかどうかを判断する

**Aspose.PDF for .NET** はPDFドキュメントを扱う際に優れた機能を提供します。Aspose.PDF名前空間のDocumentクラスを使用してパスワードで保護されたPDFドキュメントを開く場合、Documentコンストラクタにパスワード情報を引数として提供する必要があります。この情報が提供されていない場合、エラーメッセージが生成されます。実際に、DocumentオブジェクトでPDFファイルを開こうとすると、コンストラクタはPDFファイルの内容を読み取ろうとし、正しいパスワードが提供されていない場合はエラーメッセージが生成されます（これは文書の不正アクセスを防ぐためです）。

暗号化されたPDFファイルを扱う場合、PDFにオープンパスワードや編集パスワードが設定されているかどうかを検出するシナリオに遭遇することがあります。
暗号化されたPDFファイルを扱う際に、PDFにオープンパスワードまたは編集パスワードが設定されているかどうかを検出するシナリオに遭遇することがあります。

### PDF文書のセキュリティに関する情報を取得する

PdfFileInfoにはPDF文書のセキュリティに関する情報を取得するための三つのプロパティが含まれています。

1. プロパティ PasswordType は PasswordType 列挙値を返します：
    - PasswordType.None - 文書はパスワード保護されていません
    - PasswordType.User - 文書はユーザー（または文書オープン）パスワードで開かれました
    - PasswordType.Owner - 文書は所有者（または権限、編集）パスワードで開かれました
    - PasswordType.Inaccessible - 文書はパスワード保護されていますが、開くためにはパスワードが必要で、無効なパスワード（またはパスワードなし）が提供されました。
2. boolean プロパティ HasOpenPassword - 入力ファイルを開く際にパスワードが必要かどうかを判断するために使用されます。
3. boolean プロパティ HasEditPassword - 入力ファイルを編集するためにパスワードが必要かどうかを判断するために使用されます。

### 配列から正しいパスワードを決定する
### 配列から正しいパスワードを決定する

時々、パスワードの配列から正しいパスワードを決定し、正しいパスワードでドキュメントを開く必要があります。以下のコードスニペットは、パスワードの配列を反復処理し、正しいパスワードでドキュメントを開く手順を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// ソースPDFファイルをロード
PdfFileInfo info = new PdfFileInfo();
info.BindPdf(dataDir + "IsPasswordProtected.pdf");
// ソースPDFが暗号化されているかどうかを判断
Console.WriteLine("File is password protected " + info.IsEncrypted);
String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
{
    try
    {
        Document doc = new Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
        if (doc.Pages.Count > 0)
            Console.WriteLine("Number of Page in document are = " + doc.Pages.Count);
    }
    catch (InvalidPasswordException)
    {
        Console.WriteLine("Password = " + passwords[passwordcount] + "  is not correct");
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
                "contactType": "販売",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
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
    "applicationCategory": ".NET用PDF操作ライブラリ",
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
```

