---
title: PDFのページからテキストを検索して取得する
linktitle: 検索とテキスト取得
type: docs
weight: 60
url: ja/python-net/search-and-get-text-from-pdf/
description: この記事では、Aspose.PDF for .NETからテキストを検索して取得するためのさまざまなツールの使用方法を説明します。
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFのページからテキストを検索して取得する",
    "alternativeHeadline": "PDFのページからテキストを検索して取得するためのツール",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, search text, get text from pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "この記事では、Aspose.PDF for .NETからテキストを検索して取得するためのさまざまなツールの使用方法を説明します。"
}
</script>


## PDFドキュメントのすべてのページからテキストを検索して取得する

[TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber) クラスを使用すると、PDFドキュメントのすべてのページから特定のフレーズに一致するテキストを見つけることができます。ドキュメント全体からテキストを検索するには、PagesコレクションのAcceptメソッドを呼び出す必要があります。[Accept](https://reference.aspose.com/pdf/python-net/aspose.pdf.page/accept/methods/3) メソッドはTextFragmentAbsorberオブジェクトをパラメータとして受け取り、TextFragmentオブジェクトのコレクションを返します。すべてのフラグメントをループして、そのプロパティ（テキスト、位置（XIndent、YIndent）、フォント名、フォントサイズ、IsAccessible、IsEmbedded、IsSubset、前景色など）を取得できます。

以下のコードスニペットは、すべてのページからテキストを検索する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください
// ドキュメントディレクトリへのパス
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// 入力検索フレーズのすべてのインスタンスを見つけるためにTextAbsorberオブジェクトを作成
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// すべてのページに対してアブソーバーを受け入れる
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 抽出されたテキストフラグメントを取得
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// フラグメントをループする
foreach (TextFragment textFragment in textFragmentCollection)
{

    Console.WriteLine("Text : {0} ", textFragment.Text);
    Console.WriteLine("Position : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
}
```


特定のPDFページ内のテキストを検索する必要がある場合は、Documentインスタンスのページコレクションからページ番号を指定し、そのページに対してAcceptメソッドを呼び出してください（以下のコード行に示すように）。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// 特定のページに対してアブソーバーを受け入れる
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## PDFドキュメントのすべてのページからテキストセグメントを検索して取得する

すべてのページからテキストセグメントを検索するには、まずドキュメントからTextFragmentオブジェクトを取得する必要があります。
 TextFragmentAbsorberを使用すると、特定のフレーズに一致するテキストをPDFドキュメントのすべてのページから検索できます。ドキュメント全体からテキストを検索するには、PagesコレクションのAcceptメソッドを呼び出す必要があります。AcceptメソッドはTextFragmentAbsorberオブジェクトをパラメータとして受け取り、TextFragmentオブジェクトのコレクションを返します。ドキュメントからTextFragmentCollectionを取得したら、このコレクションをループして各TextFragmentオブジェクトのTextSegmentCollectionを取得する必要があります。その後、個々のTextSegmentオブジェクトのすべてのプロパティを取得できます。次のコードスニペットは、すべてのページからテキストセグメントを検索する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET を参照してください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// 入力検索フレーズのすべてのインスタンスを見つけるためにTextAbsorberオブジェクトを作成
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// すべてのページに対してアブソーバーを適用
pdfDocument.Pages.Accept(textFragmentAbsorber);
// 抽出されたテキストフラグメントを取得
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// フラグメントをループ
foreach (TextFragment textFragment in textFragmentCollection)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        Console.WriteLine("Text : {0} ", textSegment.Text);
        Console.WriteLine("Position : {0} ", textSegment.Position);
        Console.WriteLine("XIndent : {0} ", textSegment.Position.XIndent);
        Console.WriteLine("YIndent : {0} ", textSegment.Position.YIndent);
        Console.WriteLine("Font - Name : {0}", textSegment.TextState.Font.FontName);
        Console.WriteLine("Font - IsAccessible : {0} ", textSegment.TextState.Font.IsAccessible);
        Console.WriteLine("Font - IsEmbedded : {0} ", textSegment.TextState.Font.IsEmbedded);
        Console.WriteLine("Font - IsSubset : {0} ", textSegment.TextState.Font.IsSubset);
        Console.WriteLine("Font Size : {0} ", textSegment.TextState.FontSize);
        Console.WriteLine("Foreground Color : {0} ", textSegment.TextState.ForegroundColor);
    }
}
```

特定のPDFページからTextSegmentsを検索して取得するには、Accept(..)メソッドを呼び出す際に特定のページインデックスを指定する必要があります。以下のコード行をご覧ください。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// すべてのページに対してアブソーバーを受け入れます
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## 正規表現を使用してすべてのページからテキストを検索して取得する

TextFragmentAbsorberを使用すると、正規表現に基づいてすべてのページからテキストを検索し、取得することができます。
 最初に、正規表現をTextFragmentAbsorberコンストラクタにフレーズとして渡す必要があります。その後、TextFragmentAbsorberオブジェクトのTextSearchOptionsプロパティを設定する必要があります。このプロパティにはTextSearchOptionsオブジェクトが必要で、新しいオブジェクトを作成する際にそのコンストラクタにtrueをパラメータとして渡す必要があります。全ページから一致するテキストを取得したい場合、PagesコレクションのAcceptメソッドを呼び出す必要があります。TextFragmentAbsorberは、正規表現で指定された条件に一致するすべてのフラグメントを含むTextFragmentCollectionを返します。以下のコードスニペットは、正規表現に基づいてすべてのページからテキストを検索して取得する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// 正規表現に一致するすべてのフレーズを見つけるためにTextAbsorberオブジェクトを作成
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // 例: 1999-2000

// 正規表現の使用を指定するためにテキスト検索オプションを設定
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// すべてのページに対してアブソーバを受け入れる
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 抽出されたテキストフラグメントを取得
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// フラグメントをループ
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Text : {0} ", textFragment.Text);
    Console.WriteLine("Position : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
}
```

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
TextFragmentAbsorber textFragmentAbsorber;
// 単語の正確な一致を検索するには、正規表現を使用することを検討してください。
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// 大文字または小文字で文字列を検索するには、正規表現を使用することを検討してください。
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// PDFドキュメント内のすべての文字列を検索（すべての文字列を解析）するには、次の正規表現を使用してください。
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// 検索文字列の一致を見つけ、文字列の後の改行までのすべてを取得します。
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// 正規表現の一致に続くテキストを見つけるには、次の正規表現を使用してください。
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// PDFドキュメント内のハイパーリンク/URLを検索するには、次の正規表現を使用してください。
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```


## 正規表現に基づいたテキストの検索とハイパーリンクの追加

正規表現に基づいてテキストフレーズにハイパーリンクを追加したい場合は、まず特定の正規表現に一致するすべてのフレーズをTextFragmentAbsorberを使用して見つけ、これらのフレーズにハイパーリンクを追加します。

フレーズを見つけてそれにハイパーリンクを追加するには:

1. 正規表現をTextFragmentAbsorberのコンストラクタにパラメータとして渡します。
2. 正規表現が使用されるかどうかを指定するTextSearchOptionsオブジェクトを作成します。
3. 一致するフレーズをTextFragmentsに取得します。
4. 一致をループしてその長方形の寸法を取得し、前景色を青に変更します（オプション - ハイパーリンクのように見せるため）。そしてPdfContentEditorクラスのCreateWebLink(..)メソッドを使用してリンクを作成します。
5. ドキュメントオブジェクトのSaveメソッドを使用して更新されたPDFを保存します。
以下のコードスニペットは、正規表現を使用してPDFファイル内のテキストを検索し、一致する部分にハイパーリンクを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 入力された検索フレーズのすべてのインスタンスを見つけるために吸収オブジェクトを作成
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// 正規表現検索を有効にする
absorber.TextSearchOptions = new TextSearchOptions(true);
// ドキュメントを開く
PdfContentEditor editor = new PdfContentEditor();
// ソースPDFファイルをバインド
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// ページのために吸収オブジェクトを受け入れる
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// フラグメントをループする
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle((int)textFragment.Rectangle.LLX,
        (int)Math.Round(textFragment.Rectangle.LLY), (int)Math.Round(textFragment.Rectangle.Width + 2),
        (int)Math.Round(textFragment.Rectangle.Height + 1));
    Enum[] actionName = new Enum[2] { Aspose.Pdf.Annotations.PredefinedAction.Document_AttachFile, Aspose.Pdf.Annotations.PredefinedAction.Document_ExtractPages };
    editor.CreateWebLink(rect, "http:// Www.aspose.com", 1, blue, actionName);
    editor.CreateLine(rect, "", (float)textFragment.Rectangle.LLX + 1, (float)textFragment.Rectangle.LLY - 1,
        (float)textFragment.Rectangle.URX, (float)textFragment.Rectangle.LLY - 1, 1, 1, blue, "S", dashArray, LEArray);
}

dataDir = dataDir + "SearchTextAndAddHyperlink_out.pdf";
editor.Save(dataDir);
editor.Close();
```


## 各TextFragmentの周りに四角形を検索して描画

Aspose.PDF for .NETは、各文字またはテキストフラグメントの座標を検索して取得する機能をサポートしています。したがって、各文字に対して返される座標が正確であることを確認するために、各文字の周りに四角形を追加して強調表示することを検討できます。

テキストの段落の場合、正規表現を使用して段落の区切りを判断し、その周りに四角形を描画することを検討できます。以下のコードスニペットをご覧ください。次のコードスニペットは、各文字の座標を取得し、各文字の周りに四角形を作成します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NETをご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// 正規表現に一致するすべてのフレーズを見つけるためにTextAbsorberオブジェクトを作成

TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber(@"[\S]+");

TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textAbsorber.TextSearchOptions = textSearchOptions;

document.Pages.Accept(textAbsorber);

var editor = new PdfContentEditor(document);

foreach (TextFragment textFragment in textAbsorber.TextFragments)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        DrawBox(editor, textFragment.Page.Number, textSegment, System.Drawing.Color.Red);
    }

}
dataDir = dataDir + "SearchTextAndDrawRectangle_out.pdf";
document.Save(dataDir);
```


## PDFドキュメントの各文字を強調表示する

{{% alert color="primary" %}}

Aspose.PDFを使用してドキュメント内のテキストを検索し、[このリンク](https://products.aspose.app/pdf/search)でオンラインで結果を取得することができます。

{{% /alert %}}

Aspose.PDF for .NETは、各文字またはテキストフラグメントの座標を検索して取得する機能をサポートしています。したがって、各文字に対して返される座標を確実にするために、各文字の周りに矩形を追加して強調表示することを考慮することができます。以下のコードスニペットは、各文字の座標を取得し、各文字の周りに矩形を作成します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

int resolution = 150;

Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "input.pdf");

using (MemoryStream ms = new MemoryStream())
{
    PdfConverter conv = new PdfConverter(pdfDocument);
    conv.Resolution = new Resolution(resolution, resolution);
    conv.GetNextImage(ms, System.Drawing.Imaging.ImageFormat.Png);

    Bitmap bmp = (Bitmap)Bitmap.FromStream(ms);

    using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
    {
        float scale = resolution / 72f;
        gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

        for (int i = 0; i < pdfDocument.Pages.Count; i++)
        {
Page page = pdfDocument.Pages[1];
// すべての単語を見つけるためのTextAbsorberオブジェクトを作成
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
page.Accept(textFragmentAbsorber);
// 抽出されたテキストフラグメントを取得
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// フラグメントをループする
foreach (TextFragment textFragment in textFragmentCollection)
{
    if (i == 0)
    {
        gr.DrawRectangle(
        Pens.Yellow,
        (float)textFragment.Position.XIndent,
        (float)textFragment.Position.YIndent,
        (float)textFragment.Rectangle.Width,
        (float)textFragment.Rectangle.Height);

        for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
        {
TextSegment segment = textFragment.Segments[segNum];

for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
{
    CharInfo characterInfo = segment.Characters[charNum];

    Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
    Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
          "   TextFragment URY = " + textFragment.Rectangle.URY);

    gr.DrawRectangle(
    Pens.Black,
    (float)characterInfo.Rectangle.LLX,
    (float)characterInfo.Rectangle.LLY,
    (float)characterInfo.Rectangle.Width,
    (float)characterInfo.Rectangle.Height);
}

gr.DrawRectangle(
Pens.Green,
(float)segment.Rectangle.LLX,
(float)segment.Rectangle.LLY,
(float)segment.Rectangle.Width,
(float)segment.Rectangle.Height);
        }
    }
}
        }
    }
    dataDir = dataDir + "HighlightCharacterInPDF_out.png";
    bmp.Save(dataDir, System.Drawing.Imaging.ImageFormat.Png);
}
```


## 隠しテキストを追加して検索

時々、PDFドキュメントに隠しテキストを追加し、その隠しテキストを検索して、その位置を後処理に利用したいことがあります。あなたの利便性のために、Aspose.PDF for .NET はこれらの機能を提供します。ドキュメント生成中に隠しテキストを追加することができます。また、TextFragmentAbsorber を使用して隠しテキストを見つけることもできます。隠しテキストを追加するには、追加されたテキストに対して TextState.Invisible を ‘true’ に設定します。TextFragmentAbsorber は、パターンに一致するすべてのテキストを見つけます（指定されている場合）。これは変更できないデフォルトの動作です。見つかったテキストが実際に見えないかどうかを確認するために、TextState.Invisible プロパティを使用することができます。以下のコードスニペットは、この機能を使用する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//隠しテキストを含むドキュメントを作成
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("This is common text.");
TextFragment frag2 = new TextFragment("This is invisible text.");

//テキストプロパティを設定 - 非表示
frag2.TextState.Invisible = true;

page.Paragraphs.Add(frag1);
page.Paragraphs.Add(frag2);
doc.Save(dataDir + "39400_out.pdf");
doc.Dispose();

//ドキュメント内のテキストを検索
doc = new Aspose.Pdf.Document(dataDir + "39400_out.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.Visit(doc.Pages[1]);

foreach (TextFragment fragment in absorber.TextFragments)
{
    //断片で何かをする
    Console.WriteLine("Text '{0}' on pos {1} invisibility: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```


## .NET Regexによるテキスト検索

Aspose.PDF for .NETは、標準の.NET Regexオプションを使用してドキュメントを検索する機能を提供します。この目的のためにTextFragmentAbsorberを使用できます。以下のコードサンプルに示すように。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NETをご覧ください。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// すべての単語を見つけるためのRegexオブジェクトを作成
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// ドキュメントを開く
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// 特定のページを取得
Page page = document.Pages[1];

// 入力された正規表現のすべてのインスタンスを見つけるためのTextAbsorberオブジェクトを作成
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// ページに対してabsorberを受け入れる
page.Accept(textFragmentAbsorber);

// 抽出されたテキストフラグメントを取得
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// フラグメントをループする
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine(textFragment.Text);
}
```


{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "PDF操作ライブラリ for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}