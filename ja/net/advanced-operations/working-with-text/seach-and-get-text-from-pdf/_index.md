---
title: PDFページからテキストを検索して取得
linktitle: テキストを検索して取得
type: docs
weight: 60
url: ja/net/search-and-get-text-from-pdf/
description: この記事では、Aspose.PDF for .NETを使用してテキストを検索し取得する方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFページからテキストを検索して取得",
    "alternativeHeadline": "PDFページからテキストを検索し取得するツール",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, テキスト検索, PDFからテキストを取得",
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
    "url": "/net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDF for .NETを使用してテキストを検索し取得する方法について説明します。"
}
</script>
次のコードスニペットも[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリで動作します。

## PDFドキュメントのすべてのページからテキストを検索して取得する

[TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber)クラスを使用すると、PDFドキュメントのすべてのページから特定のフレーズに一致するテキストを見つけることができます。ドキュメント全体からテキストを検索するには、PagesコレクションのAcceptメソッドを呼び出す必要があります。[Accept](https://reference.aspose.com/pdf/net/aspose.pdf.page/accept/methods/3)メソッドはTextFragmentAbsorberオブジェクトをパラメータとして受け取り、TextFragmentオブジェクトのコレクションを返します。すべてのフラグメントをループし、Text、Position（XIndent、YIndent）、FontName、FontSize、IsAccessible、IsEmbedded、IsSubset、ForegroundColorなどのプロパティを取得することができます。

次のコードスニペットは、すべてのページからテキストを検索する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// 入力検索フレーズのすべてのインスタンスを見つけるためのTextAbsorberオブジェクトを作成する
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// すべてのページに対して吸収体を受け入れる
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 抽出されたテキストフラグメントを取得する
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// フラグメントをループする
foreach (TextFragment textFragment in textFragmentCollection)
{

    Console.WriteLine("テキスト : {0} ", textFragment.Text);
    Console.WriteLine("位置 : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("フォント - 名前 : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("フォント - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("フォント - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("フォント - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("フォントサイズ : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("前景色 : {0} ", textFragment.TextState.ForegroundColor);
}
```
PDFドキュメントの特定のページ内でテキストを検索する必要がある場合は、Documentインスタンスのpagesコレクションからページ番号を指定し、そのページに対してAcceptメソッドを呼び出してください（以下のコード行に示すように）。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// 特定のページに対して吸収器を受け入れる
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## PDFドキュメントのすべてのページからテキストセグメントを検索して取得する

すべてのページからテキストセグメントを検索するためには、まずドキュメントからTextFragmentオブジェクトを取得する必要があります。
すべてのページからテキストセグメントを検索するには、まずドキュメントからTextFragmentオブジェクトを取得する必要があります。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// 入力検索フレーズのすべてのインスタンスを見つけるためのTextAbsorberオブジェクトを作成
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// すべてのページに対してアブソーバーを受け入れる
pdfDocument.Pages.Accept(textFragmentAbsorber);
// 抽出されたテキストフラグメントを取得
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// フラグメントをループする
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
PDFの特定のページからTextSegmentsを検索して取得するためには、Accept(..) メソッドを呼び出すときに特定のページインデックスを指定する必要があります。以下のコード行をご覧ください。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// すべてのページに対して吸収器を受け入れる
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## 正規表現を使用してすべてのページからテキストを検索して取得する

TextFragmentAbsorberは、正規表現に基づいて、すべてのページからテキストを検索して取得するのに役立ちます。
TextFragmentAbsorberは、正規表現に基づいて全てのページからテキストを検索し、取得するのに役立ちます。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// 正規表現に一致する全てのフレーズを見つけるためのTextAbsorberオブジェクトを作成する
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // 例：1999-2000

// 正規表現の使用を指定するためにテキスト検索オプションを設定する
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// 全てのページで吸収器を受け入れる
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 抽出されたテキストフラグメントを取得する
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
```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET を参照してください。
TextFragmentAbsorber textFragmentAbsorber;
// 単語の完全一致を検索する場合、正規表現の使用を検討してください。
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// 大文字または小文字の文字列を検索する場合、正規表現の使用を検討してください。
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// PDF文書内のすべての文字列を検索（すべての文字列を解析する）するには、次の正規表現を使用してみてください。
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// 検索文字列の一致を見つけ、その文字列から行末までの任意の文字を取得します。
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// 正規表現に続くテキストを検索するには、以下の正規表現を使用してください。
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// PDF文書内のハイパーリンク/URLを検索するには、以下の正規表現を使用して試してください。
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```
## 正規表現を使用してテキストを検索し、ハイパーリンクを追加する

テキストフレーズに正規表現に基づいたハイパーリンクを追加したい場合は、まずその特定の正規表現に一致するフレーズをすべて見つけるためにTextFragmentAbsorberを使用し、これらのフレーズにハイパーリンクを追加します。

フレーズを見つけてそれにハイパーリンクを追加するには：

1. 正規表現をTextFragmentAbsorberコンストラクターのパラメータとして渡します。
2. 正規表現が使用されているかどうかを指定するTextSearchOptionsオブジェクトを作成します。
3. TextFragmentsに一致するフレーズを取得します。
4. マッチをループしてそれらの矩形の寸法を取得し、前景色を青に変更します（オプション - ハイパーリンクのように見せるため）し、PdfContentEditorクラスのCreateWebLink(..)メソッドを使用してリンクを作成します。
5. DocumentオブジェクトのSaveメソッドを使用して更新されたPDFを保存します。
以下のコードスニペットは、PDFファイル内で正規表現を使用してテキストを検索し、一致したものにハイパーリンクを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 入力検索フレーズのすべてのインスタンスを見つけるための吸収体オブジェクトを作成します。
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// 正規表現検索を有効にします。
absorber.TextSearchOptions = new TextSearchOptions(true);
// ドキュメントを開く
PdfContentEditor editor = new PdfContentEditor();
// ソースPDFファイルをバインドします。
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// ページに吸収体を受け入れます。
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// フラグメントをループします。
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
## 各TextFragmentを検索して四角を描く

Aspose.PDF for .NETでは、各文字またはテキストフラグメントの座標を検索して取得する機能がサポートされています。したがって、各文字に対して返される座標を確認するために、各文字の周囲に四角を追加する（ハイライトする）ことを検討するかもしれません。

テキスト段落の場合、段落の区切りを判断するために正規表現を使用することを検討し、それを囲む四角を描画することができます。次のコードスニペットをご覧ください。このコードスニペットは、各文字の座標を取得し、各文字の周囲に四角を作成します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// 文書ディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 文書を開く
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// すべてのフレーズを見つけるためのTextAbsorberオブジェクトを作成
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
## PDFドキュメント内の各文字を強調表示

{{% alert color="primary" %}}

Aspose.PDFを使用してドキュメント内のテキストを検索し、この[リンク](https://products.aspose.app/pdf/search)でオンラインで結果を取得することができます。

{{% /alert %}}

Aspose.PDF for .NETは、各文字またはテキスト断片を検索して座標を取得する機能をサポートしています。したがって、各文字の返される座標が確実であることを確認するために、各文字の周りに矩形（ハイライト）を追加することを検討するかもしれません。次のコードスニペットは、各文字の座標を取得し、各文字の周りに矩形を作成します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
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
            // 全ての単語を見つけるためのTextAbsorberオブジェクトを作成
            TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
            textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
            page.Accept(textFragmentAbsorber);
            // 抽出されたテキスト断片を取得
            TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
            // 断片をループ処理
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
## 隠されたテキストの追加と検索

PDFドキュメントに隠されたテキストを追加してから、隠されたテキストを検索し、その位置を後処理に使用することがあります。便宜のために、Aspose.PDF for .NETはこれらの機能を提供します。ドキュメント生成中に隠されたテキストを追加できます。また、TextFragmentAbsorberを使用して隠されたテキストを見つけることができます。隠されたテキストを追加するには、追加されたテキストのTextState.Invisibleを「true」に設定します。TextFragmentAbsorberは、指定された場合にパターンと一致するすべてのテキストを見つけます。これは変更できないデフォルトの動作です。見つかったテキストが実際に不可視であるかどうかを確認するために、TextState.Invisibleプロパティを使用できます。以下のコードスニペットは、この機能の使用方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 隠されたテキストを含むドキュメントを作成
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("これは一般的なテキストです。");
TextFragment frag2 = new TextFragment("これは見えないテキストです。");

// テキストプロパティを設定 - 不可視
frag2.TextState.Invisible = true;

page.Paragraphs.Add(frag1);
page.Paragraphs.Add(frag2);
doc.Save(dataDir + "39400_out.pdf");
doc.Dispose();

// ドキュメント内のテキストを検索
doc = new Aspose.Pdf.Document(dataDir + "39400_out.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.Visit(doc.Pages[1]);

foreach (TextFragment fragment in absorber.TextFragments)
{
    // フラグメントを何かで処理
    Console.WriteLine("テキスト '{0}' の位置 {1} の不可視性: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```
## .NET Regexを使用したテキスト検索

Aspose.PDF for .NETは、標準の.NET Regexオプションを使用してドキュメントを検索する機能を提供します。以下のコードサンプルに示されているように、この目的のためにTextFragmentAbsorberを使用できます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// すべての単語を見つけるためのRegexオブジェクトを作成
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// ドキュメントを開く
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// 特定のページを取得
Page page = document.Pages[1];

// 入力されたregexのすべてのインスタンスを見つけるためのTextAbsorberオブジェクトを作成
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// ページに対してabsorberを受け入れる
page.Accept(textFragmentAbsorber);

// 抽出されたテキストフラグメントを取得
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// フラグメントを通してループ
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine(textFragment.Text);
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
                "contactType": "営業",
                "areaServed": "US",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
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

