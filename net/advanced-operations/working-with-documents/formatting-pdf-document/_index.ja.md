---
title: C#を使用してPDFドキュメントをフォーマットする
linktitle: PDFドキュメントのフォーマット
type: docs
weight: 11
url: /net/formatting-pdf-document/
description: Aspose.PDF for .NETを使用してPDFドキュメントを作成およびフォーマットします。次のコードスニペットを使用してタスクを解決してください。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#を使用してPDFドキュメントをフォーマットする",
    "alternativeHeadline": ".NETでPDFドキュメントをフォーマットする方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, dotnet, PDFドキュメントをフォーマット",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETを使用してPDFドキュメントを作成およびフォーマットします。次のコードスニペットを使用してタスクを解決してください。"
}
</script>
## PDFドキュメントのフォーマット

### ドキュメントウィンドウとページ表示プロパティの取得

このトピックでは、ドキュメントウィンドウ、ビューアアプリケーションのプロパティ、およびページの表示方法を取得する方法について説明します。これらのプロパティを設定するには：

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスを使用してPDFファイルを開きます。これで、Documentオブジェクトのプロパティを設定できます。例えば

- CenterWindow – ドキュメントウィンドウを画面の中央に表示します。デフォルト：false。
- Direction – 読み取り順序。これは、ページが並べて表示されるときのレイアウトを決定します。デフォルト：左から右。
- DisplayDocTitle – ドキュメントウィンドウのタイトルバーにドキュメントのタイトルを表示します。デフォルト：false（タイトルが表示されます）。
- HideMenuBar – ドキュメントウィンドウのメニューバーを非表示または表示します。デフォルト：false（メニューバーが表示されます）。
- HideToolBar – ドキュメントウィンドウのツールバーを非表示または表示します。デフォルト：false（ツールバーが表示されます）。
- HideWindowUI – ドキュメントウィンドウの要素（スクロールバーなど）を非表示または表示します。デフォルト：false（ウィンドウUIが表示されます）。
- HideWindowUI – スクロールバーやその他のドキュメントウィンドウ要素を非表示または表示します。
- NonFullScreenPageMode – フルページモードで表示されていないときのドキュメントの状態です。
- PageLayout – ページレイアウト。
- PageMode – 最初に開かれたときにドキュメントがどのように表示されるか。オプションにはサムネイルを表示、フルスクリーン、添付ファイルパネルを表示があります。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも動作します。

次のコードスニペットは、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスを使用してプロパティを取得する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "GetDocumentWindow.pdf");

// 異なるドキュメントプロパティを取得します
// ドキュメントのウィンドウの位置 - デフォルト：false
Console.WriteLine("CenterWindow : {0}", pdfDocument.CenterWindow);
  
// 支配的な読み取り順序；ページの位置を決定します
// 横に並べて表示されるとき - デフォルト：L2R
Console.WriteLine("Direction : {0}", pdfDocument.Direction);

// ウィンドウのタイトルバーがドキュメントのタイトルを表示するかどうか
// falseの場合、タイトルバーはPDFファイル名を表示します - デフォルト：false
Console.WriteLine("DisplayDocTitle : {0}", pdfDocument.DisplayDocTitle);

// ドキュメントのウィンドウを、最初に表示されたページのサイズに合わせてリサイズするかどうか - デフォルト：false
Console.WriteLine("FitWindow : {0}", pdfDocument.FitWindow);

// ビューアアプリケーションのメニューバーを隠すかどうか - デフォルト：false
Console.WriteLine("HideMenuBar : {0}", pdfDocument.HideMenubar);

// ビューアアプリケーションのツールバーを隠すかどうか - デフォルト：false
Console.WriteLine("HideToolBar : {0}", pdfDocument.HideToolBar);

// スクロールバーなどのUI要素を隠し
// ページの内容のみを表示するかどうか - デフォルト：false
Console.WriteLine("HideWindowUI : {0}", pdfDocument.HideWindowUI);

// ドキュメントのページモード。フルスクリーンモードを終了するときにドキュメントをどのように表示するか。
Console.WriteLine("NonFullScreenPageMode : {0}", pdfDocument.NonFullScreenPageMode);

// ページレイアウト。例：単一ページ、一列
Console.WriteLine("PageLayout : {0}", pdfDocument.PageLayout);

// ドキュメントを開いたときの表示方法
// 例：サムネイルを表示、フルスクリーン、添付ファイルパネルを表示
Console.WriteLine("pageMode : {0}", pdfDocument.PageMode);
```
### ドキュメントウィンドウとページ表示プロパティの設定

このトピックでは、ドキュメントウィンドウ、ビューアアプリケーション、およびページ表示のプロパティを設定する方法について説明します。これらの異なるプロパティを設定するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスを使用してPDFファイルを開きます。
1. Documentオブジェクトのプロパティを設定します。
1. Saveメソッドを使用して更新されたPDFファイルを保存します。

利用可能なプロパティは次のとおりです：

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

以下のコードスニペットは、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスを使用してプロパティを設定する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "SetDocumentWindow.pdf");

// 異なるドキュメントプロパティを設定
// ドキュメントのウィンドウの位置を指定 - デフォルト：false
pdfDocument.CenterWindow = true;

// ページが横に並べて表示されるときの優勢な読み取り順序 - デフォルト：L2R
pdfDocument.Direction = Direction.R2L;

// ウィンドウのタイトルバーがドキュメントのタイトルを表示するかどうかを指定
// falseの場合、タイトルバーはPDFファイル名を表示 - デフォルト：false
pdfDocument.DisplayDocTitle = true;

// 最初に表示されるページのサイズにドキュメントのウィンドウをリサイズするかどうかを指定 - デフォルト：false
pdfDocument.FitWindow = true;

// ビューアアプリケーションのメニューバーを隠すかどうかを指定 - デフォルト：false
pdfDocument.HideMenubar = true;

// ビューアアプリケーションのツールバーを隠すかどうかを指定 - デフォルト：false
pdfDocument.HideToolBar = true;

// スクロールバーなどのUI要素を隠し
// ページ内容のみを表示するかどうかを指定 - デフォルト：false
pdfDocument.HideWindowUI = true;

// ドキュメントのページモード。フルスクリーンモードを終了するときにドキュメントをどのように表示するかを指定します。
pdfDocument.NonFullScreenPageMode = PageMode.UseOC;

// ページレイアウトを指定します。例：シングルページ、1カラム
pdfDocument.PageLayout = PageLayout.TwoColumnLeft;

// ドキュメントを開いたときにどのように表示するかを指定します。
// 例：サムネイルを表示、フルスクリーン、添付ファイルパネルを表示
pdfDocument.PageMode = PageMode.UseThumbs;

dataDir = dataDir + "SetDocumentWindow_out.pdf";
// 更新されたPDFファイルを保存
pdfDocument.Save(dataDir);
```
### 既存のPDFファイルにフォントを埋め込む

PDFリーダーは[14種類の基本フォント](https://en.wikipedia.org/wiki/PDF#Text)をサポートしているため、ドキュメントが表示されるプラットフォームに関わらず、ドキュメントが同じ方法で表示されるようになっています。PDFに14種類の基本フォントに含まれないフォントが含まれている場合は、フォント置換を避けるためにPDFファイルにフォントを埋め込む必要があります。

Aspose.PDF for .NETは、既存のPDFファイルにフォントを埋め込むことをサポートしています。完全なフォントまたはフォントのサブセットを埋め込むことができます。フォントを埋め込むには、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスを使用してPDFファイルを開きます。その後、[Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text) クラスを使用してPDFファイルにフォントを埋め込みます。完全なフォントを埋め込むには、FontクラスのIsEmbededプロパティを使用し、フォントのサブセットを使用するにはIsSubsetプロパティを使用します。

{{% alert color="primary" %}}

フォントのサブセットは使用される文字のみを埋め込み、短い文やスローガン、例えば企業のフォントがロゴ用には使用されるが本文には使用されない場合などに役立ちます。
フォントのサブセットは使用される文字のみを埋め込み、フォントが短い文やスローガンに使用される場合に便利です。たとえば、企業のフォントがロゴには使用されるが、本文には使用されない場合などです。

{{% /alert %}}

次のコードスニペットは、PDFファイルにフォントを埋め込む方法を示しています。

### 標準タイプ1フォントの埋め込み

一部のPDFドキュメントには、特別なAdobeフォントセットからのフォントが含まれています。このセットのフォントは「標準タイプ1フォント」と呼ばれます。このセットには14のフォントが含まれており、このタイプのフォントを埋め込むには特別なフラグを使用する必要があります。例えば [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts) があります。以下は、標準タイプ1フォントを含むすべてのフォントが埋め込まれたドキュメントを取得するために使用できるコードスニペットです：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 既存のPDFドキュメントをロードする
Document pdfDocument = new Document(dataDir + "input.pdf");
// ドキュメントのEmbedStandardFontsプロパティを設定する
pdfDocument.EmbedStandardFonts = true;
foreach (Aspose.Pdf.Page page in pdfDocument.Pages)
{
    if (page.Resources.Fonts != null)
    {
        foreach (Aspose.Pdf.Text.Font pageFont in page.Resources.Fonts)
        {
// フォントが既に埋め込まれているかを確認する
if (!pageFont.IsEmbedded)
{
    pageFont.IsEmbedded = true;
}
        }
    }
}
pdfDocument.Save(dataDir + "EmbeddedFonts-updated_out.pdf");
```
### PDF作成時のフォント埋め込み

Adobe Readerがサポートする14のコアフォント以外のフォントを使用する必要がある場合、PDFファイルを生成する際にフォントの説明を埋め込む必要があります。フォント情報が埋め込まれていない場合、Adobe Readerはシステムにインストールされている場合はオペレーティングシステムからフォントを取得し、インストールされていない場合はPDFのフォント記述子に従って代替フォントを構築します。

>埋め込まれたフォントはホストマシンにインストールされている必要があります。例えば、以下のコードではシステムに「Univers Condensed」フォントがインストールされています。

Pdfファイルにフォント情報を埋め込むために、FontクラスのIsEmbeddedプロパティを使用します。このプロパティの値を「True」に設定すると、完全なフォントファイルがPdfに埋め込まれ、Pdfファイルのサイズが増加することを知っておく必要があります。以下は、Pdfにフォント情報を埋め込むために使用できるコードスニペットです。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 空のコンストラクタを呼び出すことによってPdfオブジェクトをインスタンス化します
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();

// Pdfオブジェクトにセクションを作成します
Aspose.Pdf.Page page = doc.Pages.Add();

Aspose.Pdf.Text.TextFragment fragment = new Aspose.Pdf.Text.TextFragment("");

Aspose.Pdf.Text.TextSegment segment = new Aspose.Pdf.Text.TextSegment(" これはカスタムフォントを使用したサンプルテキストです。");
Aspose.Pdf.Text.TextState ts = new Aspose.Pdf.Text.TextState();
ts.Font = FontRepository.FindFont("Arial");
ts.Font.IsEmbedded = true;
segment.TextState = ts;
fragment.Segments.Add(segment);
page.Paragraphs.Add(fragment);

dataDir = dataDir + "EmbedFontWhileDocCreation_out.pdf";
// PDFドキュメントを保存します
doc.Save(dataDir);
```
### PDF保存時のデフォルトフォント名の設定

PDFドキュメントにドキュメント自体やデバイスに存在しないフォントが含まれている場合、APIはこれらのフォントをデフォルトフォントに置き換えます。フォントが利用可能（デバイスにインストールされているかドキュメントに埋め込まれている場合）、出力PDFは同じフォントを保持するべきです（デフォルトフォントに置き換えられるべきではありません）。デフォルトフォントの値はフォントの名前を含むべきです（フォントファイルへのパスではない）。ドキュメントをPDFとして保存する際にデフォルトフォント名を設定する機能を実装しました。以下のコードスニペットを使用してデフォルトフォントを設定できます：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// 不足しているフォントを持つ既存のPDFドキュメントをロードします
string documentName = dataDir + "input.pdf";
string newName = "Arial";
using (System.IO.FileStream fs = new System.IO.FileStream(documentName, System.IO.FileMode.Open))
using (Document document = new Document(fs))
{
    PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();
    // デフォルトフォント名を指定
    pdfSaveOptions.DefaultFontName = newName;
    document.Save(dataDir + "output_out.pdf", pdfSaveOptions);
}
```
### PDFドキュメントからすべてのフォントを取得する

PDFドキュメントからすべてのフォントを取得したい場合は、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスで提供されているFontUtilities.GetAllFonts()メソッドを使用できます。以下のコードスニペットを確認して、既存のPDFドキュメントからすべてのフォントを取得してください：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

### フォント置換の警告を取得する

Aspose.PDF for .NETは、フォント置換のケースを処理するためにフォント置換に関する通知を取得するメソッドを提供しています。以下のコードスニペットは、対応する機能を使用する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

Document doc = new Document(dataDir + "input.pdf");

doc.FontSubstitution += new Document.FontSubstitutionHandler(OnFontSubstitution);
```
**OnFontSubstitution** メソッドは以下の通りです。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
Console.WriteLine(string.Format("フォント '{0}' が別のフォント '{1}' に置換されました",
oldFont.FontName, newFont.FontName));
```

### フォントの埋め込みを改善するための FontSubsetStrategy の使用

フォントをサブセットとして埋め込む機能は IsSubset プロパティを使用して達成できますが、時にはドキュメントで使用されているサブセットのみに完全に埋め込まれたフォントセットを削減したい場合があります。Aspose.Pdf.Document には FontUtilities プロパティがあり、SubsetFonts(FontSubsetStrategy subsetStrategy) メソッドを含んでいます。SubsetFonts() メソッドでは、パラメータ subsetStrategy がサブセット戦略を調整するのに役立ちます。FontSubsetStrategy は、フォントサブセットの以下の二つのバリアントをサポートします。

- SubsetAllFonts - これは、ドキュメントで使用されているすべてのフォントをサブセットします。
- SubsetEmbeddedFontsOnly - これは、ドキュメントに完全に埋め込まれているフォントのみをサブセットします。

次のコードスニペットは、FontSubsetStrategy を設定する方法を示しています：
以下のコードスニペットは、FontSubsetStrategyを設定する方法を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
// SubsetAllFontsの場合、すべてのフォントがドキュメントにサブセットとして埋め込まれます。
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetAllFonts);
// 完全に埋め込まれたフォントのフォントサブセットが埋め込まれますが、ドキュメントに埋め込まれていないフォントは影響を受けません。
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
doc.Save(dataDir + "Output_out.pdf");
```

### PDFファイルのズームファクターの取得と設定

時々、PDFドキュメントの現在のズームファクターを知りたい場合があります。Aspose.Pdfを使用すると、現在の値を見つけたり、設定したりすることができます。

[GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) クラスのDestinationプロパティを使用して、PDFファイルに関連付けられたズーム値を取得できます。
[GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) クラスの Destination プロパティを使用すると、PDFファイルに関連付けられたズーム値を取得できます。

#### ズーム係数を設定する

次のコードスニペットは、PDFファイルのズーム係数を設定する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 新しいDocumentオブジェクトをインスタンス化
Document doc = new Document(dataDir + "SetZoomFactor.pdf");

GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0, 0, .5));
doc.OpenAction = action;
dataDir = dataDir + "Zoomed_pdf_out.pdf";
// ドキュメントを保存
doc.Save(dataDir);
```

#### ズーム係数を取得する

次のコードスニペットは、PDFファイルのズーム係数を取得する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 新しいDocumentオブジェクトをインスタンス化
Document doc = new Document(dataDir + "Zoomed_pdf.pdf");

// GoToActionオブジェクトを作成
GoToAction action = doc.OpenAction as GoToAction;

// PDFファイルのズーム係数を取得
System.Console.WriteLine((action.Destination as XYZExplicitDestination).Zoom); // ドキュメントのズーム値;
```
### プリントダイアログプリセットプロパティの設定

Aspoose.PDFはPDFドキュメントのプリントダイアログプリセットプロパティを設定することができます。これにより、デフォルトでシンプレックスに設定されているPDFドキュメントのDuplexModeプロパティを変更することができます。これは以下に示す2つの異なる方法で達成できます。

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

using (Document doc = new Document())
{
    doc.Pages.Add();
    doc.Duplex = PrintDuplex.DuplexFlipLongEdge;
    doc.Save(dataDir + "35297_out.pdf", SaveFormat.Pdf);
}
```

### PDFコンテンツエディタを使用してプリントダイアログプリセットプロパティを設定する

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

string outputFile = dataDir + "input.pdf";
using (PdfContentEditor ed = new PdfContentEditor())
{
    ed.BindPdf(outputFile);
    if ((ed.GetViewerPreference() & ViewerPreference.DuplexFlipShortEdge) > 0)
    {
        Console.WriteLine("The file has duplex flip short edge");
    }

    ed.ChangeViewerPreference(ViewerPreference.DuplexFlipShortEdge);
    ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
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
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
                "areaServed": "AU",
                "availableLanguage": "英語"
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

