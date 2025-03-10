---
title: JavaScriptの操作
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /ja/net/working-with-javascript/
description: Aspose.PDF for .NETを使用してPDF文書にJavaScriptを追加、変更、実行する方法を学びます。インタラクティブ性と自動化を強化します。
lastmod: "2025-02-07"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with JavaScript",
    "alternativeHeadline": "Enhance PDF with Custom JavaScript Actions",
    "abstract": "Aspose.PDF for .NETを通じてPDF文書内にJavaScriptを統合する強化された機能を発見してください。この新機能により、開発者は文書およびページレベルでJavaScriptアクションを追加および管理でき、ユーザーエンゲージメントと機能性を向上させるインタラクティブで動的なPDF体験を実現します。Webのような動作を模倣する洗練されたPDFフォームを作成するためにJavaScriptの可能性を解き放ち、文書生成ワークフローを向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "JavaScript, Acrobat JavaScript, PDF document generation, JavaScript collection, document level JavaScript, JavaScript Action, interactive PDF forms, manipulate PDF files, HTML JavaScript, Aspose.PDF for .NET",
    "wordcount": "423",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## JavaScriptの追加 (DOM)

### Acrobat JavaScriptとは？

Acrobat JavaScriptは、ISO-16262のJavaScriptバージョン1.5を基にした言語で、以前はECMAScriptとして知られていた、Netscape Communicationsによって開発されたオブジェクト指向スクリプト言語です。JavaScriptは、Webベースのアプリケーションにおいて、Webページ処理をサーバーからクライアントにオフロードするために作成されました。Acrobat JavaScriptは、JavaScript言語に新しいオブジェクトとそれに伴うメソッドおよびプロパティの形で拡張機能を実装します。これらのAcrobat特有のオブジェクトにより、開発者は文書のセキュリティを管理し、データベースと通信し、ファイル添付を処理し、PDFファイルをインタラクティブでWeb対応のフォームのように操作することができます。Acrobat特有のオブジェクトはコアJavaScriptの上に追加されるため、Math、String、Date、Array、RegExpなどの標準クラスにもアクセスできます。

### Acrobat JavaScriptとHTML (Web) JavaScriptの違い

PDF文書は、Acrobatソフトウェア内およびWebブラウザ内の両方で表示できるため、Acrobat JavaScriptとWebブラウザで使用されるJavaScript（HTML JavaScriptとも呼ばれる）の違いを理解することが重要です：

- Acrobat JavaScriptは、HTMLページ内のオブジェクトにアクセスできません。同様に、HTML JavaScriptはPDFファイル内のオブジェクトにアクセスできません。
- HTML JavaScriptは、Windowなどのオブジェクトを操作できます。Acrobat JavaScriptはこの特定のオブジェクトにアクセスできませんが、PDF特有のオブジェクトを操作できます。

[Aspose.PDF for .NET](/pdf/ja/net/)を使用して、文書およびページレベルの両方でJavaScriptを追加できます。JavaScriptを追加するには：

### 文書またはページアクションにJavaScriptを追加する

1. 希望するJavaScript文をコンストラクタ引数として持つJavascriptActionオブジェクトを宣言し、インスタンス化します。
1. JavascriptActionオブジェクトをPDF文書またはページの希望するアクションに割り当てます。

以下の例は、特定の文書にOpenActionを適用します。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Adding JavaScript at Document Level
        // Instantiate JavascriptAction with desired JavaScript statement
        var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

        // Assign JavascriptAction object to desired action of Document
        document.OpenAction = javaScript;

        // Adding JavaScript at Page Level
        document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
        document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

        // Save PDF Document
        document.Save(dataDir + "JavaScriptAdded_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Adding JavaScript at Document Level
    // Instantiate JavascriptAction with desired JavaScript statement
    var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    // Assign JavascriptAction object to desired action of Document
    document.OpenAction = javaScript;

    // Adding JavaScript at Page Level
    document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
    document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

    // Save PDF Document
    document.Save(dataDir + "JavaScriptAdded_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### 文書レベルにJavaScriptを追加/削除する

DocumentクラスにJavaScriptという新しいプロパティが追加され、JavaScriptコレクションタイプを持ち、そのキーによってJavaScriptシナリオにアクセスできます。このプロパティは、文書レベルのJavaScriptを追加するために使用されます。JavaScriptコレクションには、以下のプロパティとメソッドがあります：

- string this(string key)– 名前によってJavaScriptを取得または設定します。
- IList Keys – JavaScriptコレクション内の既存のキーのリストを提供します。
- bool Remove(string key) – キーによってJavaScriptを削除します。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();
        document.JavaScript["func1"] = "function func1() { hello(); }";
        document.JavaScript["func2"] = "function func2() { hello(); }";
        document.Save(dataDir + "AddJavascript.pdf");
    }

    // Remove Document level JavaScript
    using (var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf"))
    {
        var keys = (IList)document1.JavaScript.Keys;

        Console.WriteLine("=============================== ");

        foreach (string key in keys)
        {
            Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
        }

        document1.JavaScript.Remove("func1");

        Console.WriteLine("Key 'func1' removed ");
        Console.WriteLine("=============================== ");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();
    document.JavaScript["func1"] = "function func1() { hello(); }";
    document.JavaScript["func2"] = "function func2() { hello(); }";
    document.Save(dataDir + "AddJavascript.pdf");

    // Remove Document level JavaScript
    using var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf");
    IList keys = (IList)document1.JavaScript.Keys;

    Console.WriteLine("=============================== ");

    foreach (string key in keys)
    {
        Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
    }

    document1.JavaScript.Remove("func1");

    Console.WriteLine("Key 'func1' removed ");
    Console.WriteLine("=============================== ");
}
```
{{< /tab >}}
{{< /tabs >}}

### JavaScriptアクションを使用してPDF文書の有効期限を設定する

Aspose.PDFを使用すると、JavaScriptアクションを埋め込むことによってPDF文書の有効期限を設定できます。この機能により、指定された日時以降にPDFがアクセスできなくなり、文書のセキュリティと制御が強化されます。JavaScriptアクションを活用することで、秒単位で正確な有効期限条件を定義でき、文書のアクセス可能性が厳密に制御されます。

**これを達成するには、以下の手順に従ってください**

1. **文書の初期化:** 新しいPDF文書を作成し、空白のページを追加するか、既存のPDF文書を開きます。
2. **有効期限の日付と時間を定義:** 文書が期限切れになる日時を設定します。
3. **JavaScriptコードの準備:** 
    - 現在の日付と時間を取得します。
    - 有効期限の日付と時間を正確に定義します。JavaScriptでは月がゼロベースであることを考慮してください。
    - 現在の日付と時間を有効期限の日付と時間と比較します。
    - 現在の日付と時間が有効期限の日付と時間を超えた場合、アラートを表示し、文書を閉じます。
4. **オープンアクションの設定:** JavaScriptアクションを文書のオープンアクションに関連付けます。
5. **文書の保存:** 有効期限条件を強制する埋め込まれたJavaScriptを持つPDFを保存します。

以下は、C# (.NET)およびJavaの両方でこの機能を示すコードスニペットです。

以下のC#コードスニペットは、Aspose.PDFを使用してPDF文書の有効期限の日付と時間を設定する方法を示しています。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();

        // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
        DateTime expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

        // Create JavaScript code to enforce the expiry date and time
        string jsCode =
            // Get the current date and time
            "var rightNow = new Date();\n" +
            // Set the expiry date and time
            "var endDate = new Date(" +
            $"{expiryDateTime.Year}," +
            $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
            $"{expiryDateTime.Day}," +
            $"{expiryDateTime.Hour}," +
            $"{expiryDateTime.Minute}," +
            $"{expiryDateTime.Second}" +
            ");\n" +
            "if(rightNow > endDate)\n" +
            "{\n" +
            "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
            "    this.closeDoc();\n" +
            "}";

        // Create a JavascriptAction with the defined JavaScript code
        var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

        // Set the JavaScript action to execute when the document is opened
        document.OpenAction = javaScript;

        // Save PDF document
        document.Save(dataDir + "PDFExpiry_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();

    // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
    var expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

    // Create JavaScript code to enforce the expiry date and time
    string jsCode =
        // Get the current date and time
        "var rightNow = new Date();\n" +
        // Set the expiry date and time
        "var endDate = new Date(" +
        $"{expiryDateTime.Year}," +
        $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
        $"{expiryDateTime.Day}," +
        $"{expiryDateTime.Hour}," +
        $"{expiryDateTime.Minute}," +
        $"{expiryDateTime.Second}" +
        ");\n" +
        "if(rightNow > endDate)\n" +
        "{\n" +
        "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
        "    this.closeDoc();\n" +
        "}";

    // Create a JavascriptAction with the defined JavaScript code
    var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

    // Set the JavaScript action to execute when the document is opened
    document.OpenAction = javaScript;

    // Save PDF document
    document.Save(dataDir + "PDFExpiry_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

- **JavaScript日付オブジェクト:** JavaScriptでは、月のインデックスは1月が`0`、12月が`11`で始まります。有効期限の日付と時間を設定する際に、月の値が適切に調整されていることを確認してください。
  
- **セキュリティに関する考慮事項:** JavaScriptアクションはPDF文書の動作を制御できますが、PDFビューアのJavaScriptサポートに依存します。すべてのPDFビューアがこれらのスクリプトを尊重するわけではなく、ユーザーがセキュリティ上の理由からJavaScriptの実行を無効にしている可能性があります。

- **カスタマイズ:** 有効期限が切れた際に、特定の機能を無効にしたり、特定のページにリダイレクトしたり、イベントをログに記録したりするなど、追加のアクションを実行するためにJavaScriptコードを修正します。また、必要に応じて、時間を指定せずに有効期限の日付のみを確認することもできます。

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