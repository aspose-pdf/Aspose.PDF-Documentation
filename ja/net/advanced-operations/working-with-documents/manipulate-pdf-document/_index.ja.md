---
title: PDFドキュメントを操作する
linktitle: PDFドキュメントを操作する
type: docs
weight: 20
url: /net/manipulate-pdf-document/
description: この記事には、PDF A標準に対するPDFドキュメントの検証方法、目次の操作方法、PDFの有効期限設定方法などが含まれています。
keywords: "manipulate pdf c#"
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFドキュメントを操作する",
    "alternativeHeadline": "PDFファイルの操作方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, dotnet, manipulate pdf file",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事には、PDF A標準に対するPDFドキュメントの検証方法、目次の操作方法、PDFの有効期限設定方法などが含まれています。"
}
</script>
## **PDFドキュメントをC#で操作する**

## PDFドキュメントをPDF A規格（A 1AおよびA 1B）で検証する

PDF/A-1aまたはPDF/A-1bとの互換性のためにPDFドキュメントを検証するには、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスのValidateメソッドを使用します。このメソッドでは、結果を保存するファイルの名前と必要な検証タイプ [PdfFormat](https://reference.aspose.com/pdf/net/aspose.pdf/pdfformat) 列挙：PDF_A_1AまたはPDF_A_1Bを指定できます。

{{% alert color="primary" %}}

出力XML形式はカスタムAspose形式です。XMLには、Problemという名前のタグのコレクションが含まれており、各タグには特定の問題の詳細が含まれています。ProblemタグのObjectID属性は、この問題に関連する特定のオブジェクトのIDを表します。Clause属性は、PDF仕様の対応するルールを表します。

{{% /alert %}}

このコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリとも連携します。

次のコードスニペットは、PDF/A-1AのPDFドキュメントを検証する方法を示しています。
以下のコードスニペットは、PDFドキュメントをPDF/A-1Aで検証する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// PDFをPDF/A-1aで検証
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);
```

以下のコードスニペットは、PDFドキュメントをPDF/A-1Bで検証する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// PDFをPDF/A-1bで検証
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```
{{% alert color="primary" %}}

Aspose.PDF for .NETは、読み込まれたドキュメントが有効なPDFであるかどうか、また[暗号化されているかどうか](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/)を判断するために使用できます。Documentクラスの機能をさらに拡張するために、入力ファイルがPDF/A準拠であるかどうかを判断する*IsPdfaCompliant*プロパティとPDF/Aフォーマットを識別する*PdfaFormat*プロパティが導入されました。

{{% /alert %}}

## 目次の操作

### 既存のPDFに目次を追加

Aspose.PDF APIを使用すると、PDFを作成する際または既存のファイルに目次を追加することができます。Aspose.Pdf.Generator名前空間のListSectionクラスを使用して、最初からPDFを作成する際に目次を作成できます。目次の要素である見出しを追加するには、Aspose.Pdf.Generator.Headingクラスを使用します。

既存のPDFファイルに目次を追加するには、Aspose.Pdf名前空間のHeadingクラスを使用します。
既存のPDFファイルに目次を追加するには、Aspose.Pdf名前空間のHeadingクラスを使用します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 既存のPDFファイルを読み込む
Document doc = new Document(dataDir + "AddTOC.pdf");

// PDFファイルの最初のページにアクセスする
Page tocPage = doc.Pages.Insert(1);

// TOC情報を表すオブジェクトを作成する
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("目次");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;

// TOCのタイトルを設定する
tocInfo.Title = title;
tocPage.TocInfo = tocInfo;

// TOC要素として使用される文字列オブジェクトを作成する
string[] titles = new string[4];
titles[0] = "最初のページ";
titles[1] = "2番目のページ";
titles[2] = "3番目のページ";
titles[3] = "4番目のページ";
for (int i = 0; i < 2; i++)
{
    // Headingオブジェクトを作成する
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);

    // Headingオブジェクトの目的のページを指定する
    heading2.DestinationPage = doc.Pages[i + 2];

    // 目的のページ
    heading2.Top = doc.Pages[i + 2].Rect.Height;

    // 目的の座標
    segment2.Text = titles[i];

    // TOCを含むページにheadingを追加する
    tocPage.Paragraphs.Add(heading2);
}
dataDir = dataDir + "TOC_out.pdf";
// 更新されたドキュメントを保存する
doc.Save(dataDir);
```
### 異なるTOCレベルに対して異なるTabLeaderTypeを設定する

Aspose.PDFでは、異なるTOCレベルに対して異なるTabLeaderTypeを設定することもできます。以下のようにFormatArrayのLineDashプロパティをTabLeaderType列挙型の適切な値に設定する必要があります。

```csharp
 string outFile = "TOC.pdf";

Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();

// LeaderTypeを設定
tocInfo.LineDash = TabLeaderType.Solid;
TextFragment title = new TextFragment("目次");
title.TextState.FontSize = 30;
tocInfo.Title = title;

// Pdfドキュメントのセクションコレクションにリストセクションを追加
tocPage.TocInfo = tocInfo;
// 左マージンを設定し、
// 各レベルのテキストフォーマット設定を定義することで、4レベルのリストの形式を定義

tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Left = 0;
tocInfo.FormatArray[0].Margin.Right = 30;
tocInfo.FormatArray[0].LineDash = TabLeaderType.Dot;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 10;
tocInfo.FormatArray[1].Margin.Right = 30;
tocInfo.FormatArray[1].LineDash = TabLeaderType.None;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].Margin.Left = 20;
tocInfo.FormatArray[2].Margin.Right = 30;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].LineDash = TabLeaderType.Solid;
tocInfo.FormatArray[3].Margin.Left = 30;
tocInfo.FormatArray[3].Margin.Right = 30;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;

// Pdfドキュメントにセクションを作成
Page page = doc.Pages.Add();

// セクションに4つの見出しを追加
for (int Level = 1; Level <= 4; Level++)
{

    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(Level);
    TextSegment segment2 = new TextSegment();
    heading2.Segments.Add(segment2);
    heading2.IsAutoSequence = true;
    heading2.TocPage = tocPage;
    segment2.Text = "サンプル見出し" + Level;
    heading2.TextState.Font = FontRepository.FindFont("Arial Unicode MS");

    // 見出しを目次に追加
    heading2.IsInList = true;
    page.Paragraphs.Add(heading2);
}

// Pdfを保存

doc.Save(outFile);
```
### TOCでページ番号を非表示にする

TOCで見出しと一緒にページ番号を表示したくない場合は、[TOCInfo](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo) クラスの [IsShowPageNumbers](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) プロパティをfalseに設定できます。以下のコードスニペットを確認して、目次でページ番号を非表示にしてください：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// 文書ディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "HiddenPageNumbers_out.pdf";
Document doc = new Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("目次");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
tocInfo.Title = title;
// Pdf文書のセクションコレクションにリストセクションを追加します
tocPage.TocInfo = tocInfo;
// 各レベルの左マージンとテキストフォーマット設定を設定することで、4つのレベルリストの形式を定義します

tocInfo.IsShowPageNumbers = false;
tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Right = 0;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 30;
tocInfo.FormatArray[1].TextState.Underline = true;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;
Page page = doc.Pages.Add();
// セクションに4つの見出しを追加します
for (int Level = 1; Level != 5; Level++)

{ Heading heading2 = new Heading(Level); TextSegment segment2 = new TextSegment(); heading2.TocPage = tocPage; heading2.Segments.Add(segment2); heading2.IsAutoSequence = true; segment2.Text = "このレベルの見出し " + Level; heading2.IsInList = true; page.Paragraphs.Add(heading2); }
doc.Save(outFile);
```
### TOCにページ番号をカスタマイズする

PDFドキュメントにTOCを追加する際、TOCのページ番号をカスタマイズすることは一般的です。例えば、ページ番号の前に「P1」「P2」「P3」などの接頭辞を付ける必要がある場合があります。このような場合には、Aspose.PDF for .NET の TocInfo クラスの PageNumbersPrefix プロパティを使用してページ番号をカスタマイズできます。以下のコードサンプルに示されています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET を参照してください。
string inFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824.pdf";
string outFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824_out.pdf";
// 既存のPDFファイルを読み込む
Document doc = new Document(inFile);
// PDFファイルの最初のページにアクセスする
Aspose.Pdf.Page tocPage = doc.Pages.Insert(1);
// TOC情報を表すオブジェクトを作成する
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("目次");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
// TOCのタイトルを設定する
tocInfo.Title = title;
tocInfo.PageNumbersPrefix = "P";
tocPage.TocInfo = tocInfo;
for (int i = 1; i<doc.Pages.Count; i++)
{
    // Headingオブジェクトを作成する
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);
    // headingオブジェクトの目的のページを指定する
    heading2.DestinationPage = doc.Pages[i + 1];
    // 目的のページ
    heading2.Top = doc.Pages[i + 1].Rect.Height;
    // 目的の座標
    segment2.Text = "ページ " + i.ToString();
    // TOCを含むページにheadingを追加する
    tocPage.Paragraphs.Add(heading2);
}

// 更新されたドキュメントを保存する
doc.Save(outFile);
```
## PDF有効期限の設定方法

PDFファイルにアクセス権限を適用して、特定のユーザーグループがPDFドキュメントの特定の機能/オブジェクトにアクセスできるようにします。PDFファイルのアクセスを制限するために、通常は暗号化を適用し、PDFファイルの有効期限を設定する必要がある場合があります。これにより、ドキュメントをアクセス/閲覧するユーザーにPDFファイルの有効期限に関する有効なプロンプトが表示されます。

上記の要件を達成するために、*JavascriptAction* オブジェクトを使用できます。以下のコードスニペットをご覧ください。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Documentオブジェクトをインスタンス化
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
// PDFファイルのページコレクションにページを追加
doc.Pages.Add();
// ページオブジェクトのパラグラフコレクションにテキストフラグメントを追加
doc.Pages[1].Paragraphs.Add(new TextFragment("Hello World..."));
// PDF有効期限を設定するJavaScriptオブジェクトを作成
JavascriptAction javaScript = new JavascriptAction(
"var year=2017;"
+ "var month=5;"
+ "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
+ "expiry = new Date(year, month);"
+ "if (today.getTime() > expiry.getTime())"
+ "app.alert('The file is expired. You need a new one.');");
// JavaScriptをPDFオープンアクションとして設定
doc.OpenAction = javaScript;

dataDir = dataDir + "SetExpiryDate_out.pdf";
// PDFドキュメントを保存
doc.Save(dataDir);
```
## PDFファイル生成の進行状況を決定する

顧客がPDFファイル生成の進行状況を確認できる機能を追加するよう依頼しました。以下がそのリクエストに対する回答です。

[DocSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) クラスの [CustomerProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) フィールドを使用すると、PDF生成の進行状況を把握できます。ハンドラには以下のタイプがあります:

- DocSaveOptions.ConversionProgessEventHandler
- DocSaveOptions.ProgressEventHandlerInfo
- DocSaveOptions.ProgressEventType

以下のコードスニペットは、CustomerProgressHandlerの使用方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "AddTOC.pdf");
DocSaveOptions saveOptions = new DocSaveOptions();
saveOptions.CustomProgressHandler = new UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

dataDir = dataDir + "DetermineProgress_out.pdf";
pdfDocument.Save(dataDir, saveOptions);
Console.ReadLine();
```
```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
public static void ShowProgressOnConsole(DocSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case DocSaveOptions.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - 変換の進行状況 : {1}% 。", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.SourcePageAnalized:
            Console.WriteLine(String.Format("{0}  - ソースページ {1}の{2}が分析されました。", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - 結果ページの{1}の{2}のレイアウトが作成されました。", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - 結果ページ{1}の{2}がエクスポートされました。", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }

}
```
## C#で入力可能なPDFをフラット化する

PDFドキュメントには、ラジオボタン、チェックボックス、テキストボックス、リストなどのインタラクティブな入力可能ウィジェットが含まれていることがよくあります。さまざまなアプリケーションの目的で編集不可にするために、PDFファイルをフラット化する必要があります。
Aspose.PDFは、C#で数行のコードだけでPDFをフラット化する機能を提供します：

```csharp

// Load source PDF form
Document doc = new Document(dataDir + "input.pdf");

// Flatten Fillable PDF 
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// Save the updated document
doc.Save(dataDir);
```

