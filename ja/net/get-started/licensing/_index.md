---
title: Aspose PDF ライセンス
linktitle: ライセンスと制限
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /ja/net/licensing/
description: Aspose.PDF for .NET は、顧客にクラシックライセンスとメーターライセンスを取得するよう招待します。また、製品をよりよく探索するために制限付きライセンスを使用することもできます。
lastmod: "2025-02-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose PDF for .NET License",
    "alternativeHeadline": "Licensing Options for Aspose.PDF for .NET Users",
    "abstract": "Aspose PDF for .NET は、固定価格と使用量に基づく請求オプションの間でユーザーが選択できる、クラシックライセンスとメーターライセンスの両方を含む堅牢なライセンスフレームワークを導入します。クラシックライセンスはファイルまたはストリームから簡単に読み込むことができ、革新的なメーターライセンスはAPIの使用に基づいて柔軟なメーターを提供し、多様なユーザーのニーズに応えます。この二重ライセンス戦略は、開発者向けのPDFソリューションのアクセス性とスケーラビリティを向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "869",
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
    "url": "/net/licensing/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/licensing/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF は、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 評価版の制限

私たちは顧客が購入前にコンポーネントを十分にテストしていただきたいと考えているため、評価版では通常通り使用することができます。

- **評価用の透かしが入ったPDF。** Aspose.PDF for .NET の評価版は、製品の全機能を提供しますが、生成されたPDFドキュメントのすべてのページには「Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd.」というテキストの透かしが上部に表示されます。

- **処理できるページ数の制限。**
評価版では、ドキュメントの最初の4ページのみを処理できます。

> Aspose.PDF for .NET を評価版の制限なしでテストしたい場合は、30日間の一時ライセンスをリクエストすることもできます。詳細は [一時ライセンスの取得方法](https://purchase.aspose.com/temporary-license) を参照してください。

## クラシックライセンス

ライセンスはファイルまたはストリームオブジェクトから読み込むことができます。ライセンスを設定する最も簡単な方法は、ライセンスファイルをAspose.PDF.dllファイルと同じフォルダーに置き、パスなしでファイル名を指定することです。以下の例に示すように。

Aspose.PDF for .NET と一緒に他のAspose for .NETコンポーネントを使用する場合は、ライセンスの名前空間を [Aspose.Pdf.License](https://reference.aspose.com/pdf/ja/net/aspose.pdf/license) のように指定してください。

### ファイルからライセンスを読み込む

ライセンスを適用する最も簡単な方法は、ライセンスファイルをAspose.PDF.dllファイルと同じフォルダーに置き、パスなしでファイル名を指定することです。

[SetLicense](https://reference.aspose.com/pdf/ja/net/aspose.pdf/license/methods/setlicense/index) メソッドを呼び出すとき、渡すライセンス名はライセンスファイルの名前である必要があります。たとえば、ライセンスファイル名を「Aspose.PDF.lic.xml」に変更した場合、そのファイル名をPdf.SetLicense(…)メソッドに渡します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseExample()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    try
    {
        // Set license
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // Something went wrong
        throw;
    }
    Console.WriteLine("License set successfully.");
}
```
### ストリームオブジェクトからライセンスを読み込む

以下の例は、ストリームからライセンスを読み込む方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    // Load license from the file stream
    var myStream = new FileStream(
            "Aspose.Pdf.lic",
            FileMode.Open);
    // Set license
    license.SetLicense(myStream);
    Console.WriteLine("License set successfully.");
}
```
## メーターライセンス

Aspose.PDF は、開発者がメーターキーを適用できるようにします。メーターライセンスメカニズムは、既存のライセンス方法とともに使用されます。API機能の使用に基づいて請求されることを希望する顧客は、メーターライセンスを使用できます。詳細については、メーターライセンスのFAQセクションを参照してください。
このガイドは、スムーズな実装のためのベストプラクティスを提供し、ライセンスの状態変更による中断を防ぎます。

「Metered」クラスは、メーターキーを適用するために使用されます。以下は、メーターの公開キーと秘密キーを設定する方法を示すサンプルコードです。

詳細については、[メーターライセンスのFAQ](https://purchase.aspose.com/faqs/licensing/metered) セクションを参照してください。

__メーターライセンスの方法__

メーターライセンスを適用するには、`SetMeteredKey` メソッドを使用して、公開キーと秘密キーを提供してメーターライセンスをアクティブにします。これは、適切なライセンスを確保するために、アプリケーションの初期化中に一度行う必要があります。

例:

```csharp
 var metered = new Aspose.Pdf.Metered();
 metered.SetMeteredKey("your-public-key", "your-private-key");
 ```
ライセンスの状態を確認するには、`IsMeteredLicensed()` を使用してメーターライセンスがアクティブかどうかを確認します。

例:

```csharp
bool isLicensed = Aspose.Pdf.License.IsMeteredLicensed();
if (!isLicensed) 
{
    metered.SetMeteredKey("your-public-key", "your-private-key");
}
 ```
`Metered.GetConsumptionCredit()` メソッドは、消費クレジットに関する情報を取得するために使用されます。
`Metered.GetConsumptionQuantity()` メソッドは、消費ファイルサイズに関する情報を取得するために使用されます。

例:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMeteredLicense()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    // Set metered public and private keys
    var metered = new Aspose.Pdf.Metered();
    // Access the setMeteredKey property and pass public and private keys as parameters
    metered.SetMeteredKey("your public key", "your private key");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
       // Add five pages
       AddPages(document, 5);
       // Save the document
       document.Save(dataDir + "output.pdf")
    }
}

private static void AddPages(Document document, int n)
{
    for(int i = 0; i < n; i++)
    {
        document.Pages.Add();
    }
}   
```

__メーターライセンスのベストプラクティス__

✅ 推奨アプローチ: シングルトンパターン
安定したライセンス設定を確保するために：

- アプリケーションの起動時に一度ライセンスを適用します。
- シングルトンパターン（または類似のアプローチ）を使用して、メーターライセンスインスタンスを作成し再利用します。
- 定期的に `IsMeteredLicensed()` を使用してライセンスの状態を確認します。無効になった場合のみライセンスを再適用します。
- 正しく実装されていれば、ライセンスサーバーが一時的に利用できなくても、ライセンスは24時間有効です。

例: シングルトン実装

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public class AsposeLicenseManager
{
    private static AsposeLicenseManager _instance;
    private static readonly object _lock = new object();
    private Aspose.Pdf.Metered _metered;

    private AsposeLicenseManager()
    {
        _metered = new Aspose.Pdf.Metered();
        _metered.SetMeteredKey("your-public-key", "your-private-key");
    }

    public static AsposeLicenseManager Instance
    {
        get
        {
            lock (_lock)
            {
                if (_instance == null)
                {
                    _instance = new AsposeLicenseManager();
                }
                return _instance;
            }
        }
    }

    public void ValidateLicense()
    {
        if (!Aspose.Pdf.License.IsMeteredLicensed())
        {
        _metered.SetMeteredKey("your-public-key", "your-private-key");
        }
    }
}
```

❌ 避けるべき一般的な間違い：

- 頻繁なライセンスの適用
- 各操作のために新しいメーターライセンスインスタンスを作成しないでください。
- 初期化中にライセンスサーバーに接続できない場合、ライセンスは評価モードに戻る可能性があります。
- 各操作のためにライセンスを繰り返し適用しないでください。
- 頻繁なライセンスの適用は、ライセンスサーバーが一時的に利用できない場合にトライアルモードにフォールバックする原因となる可能性があります。

__要約：__

✅ アプリケーションの起動時に一度メーターライセンスを設定します。
✅ シングルトンパターンを使用して単一インスタンスを管理します。
✅ 定期的にライセンスを確認し、必要に応じて再適用します。
❌ トライアルモードへのフォールバックを防ぐために頻繁なライセンスの適用を避けます。
これらのベストプラクティスに従うことで、メーターライセンスを使用したAspose.PDFのスムーズで中断のない使用を確保できます。

ライセンスが初期化されている場合、このオブジェクトが「生きている」限り、ライセンスサーバーへの接続が何らかの理由で失われても、ライセンスはさらに7日間アクティブと見なされます。何かをする必要があるたびにライセンスを初期化し、その時点でサーバーへの接続がない場合、ライセンスはEvalモードに入ります。
ユーザーがライセンスを初期化した場合、このオブジェクトが「生きている」限り、ライセンスサーバーへの接続が何らかの理由で失われても、ライセンスはさらに24時間アクティブと見なされます。何かをする必要があるたびにライセンスを初期化し、その時点でサーバーへの接続がない場合、ライセンスはEvalモードに入ります。

**Aspose.PDF for .NET** と連携して動作するCOMアプリケーションもライセンスクラスを使用する必要があることに注意してください。

考慮すべきポイント：
埋め込まれたリソースは、追加された方法でアセンブリに含まれます。つまり、アプリケーションにテキストファイルを埋め込まれたリソースとして追加し、結果として得られたEXEをメモ帳で開くと、テキストファイルの正確な内容が表示されます。したがって、ライセンスファイルを埋め込まれたリソースとして使用する場合、誰でもEXEファイルを簡単なテキストエディタで開いて埋め込まれたライセンスの内容を確認/抽出できます。

したがって、アプリケーションにライセンスを埋め込む際に追加のセキュリティ層を設けるために、ライセンスを圧縮/暗号化し、その後アセンブリに埋め込むことができます。たとえば、Aspose.PDF.licライセンスファイルがあると仮定すると、パスワードtestでAspose.PDF.zipを作成し、このzipファイルをソリューションに埋め込みます。ライセンスを初期化するために以下のコードスニペットを使用できます：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    var license = new Aspose.Pdf.License();
    license.SetLicense(GetSecureLicenseFromStream());
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the page count of document
        Console.WriteLine(document.Pages.Count);
    }
}

private static Stream GetSecureLicenseFromStream()
{
    var assembly = Assembly.GetExecutingAssembly();
    var memoryStream = new MemoryStream();
    using (var zipToOpen = assembly.GetManifestResourceStream("Aspose.Pdf.Examples.License.Aspose.PDF.zip"))
    {
        using (ZipArchive archive = new ZipArchive(zipToOpen ?? throw new InvalidOperationException(), ZipArchiveMode.Read))
        {
            var unpackedLicense  = archive.GetEntry("Aspose.PDF.lic");
            unpackedLicense?.Open().CopyTo(memoryStream);
        }
    }

    memoryStream.Position = 0;
    return memoryStream;
}
```