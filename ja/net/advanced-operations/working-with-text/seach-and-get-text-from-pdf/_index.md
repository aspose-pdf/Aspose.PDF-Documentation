---
title: PDFのページからテキストを検索して取得
linktitle: テキストを検索して取得
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ja/net/search-and-get-text-from-pdf/
description: Aspose.PDFを使用して.NETでPDFファイルからテキストを検索および取得する方法を発見してください。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Search and Get Text from Pages of PDF",
    "alternativeHeadline": "Search and Extract Text from PDF Pages",
    "abstract": "Aspose.PDF for .NETは、ユーザーがPDFドキュメントのすべてのページから効率的にテキストを検索して抽出できるようにします。この機能は、指定されたフレーズやテキストセグメントを見つけるためにTextFragmentAbsorberクラスを活用し、正規表現の高度なサポートを提供し、正確なテキストの取得と操作を可能にします。開発者に最適なこの機能は、テキスト抽出プロセスを簡素化することでPDFドキュメントの処理能力を向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2762",
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
    "url": "/net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "この記事では、Aspose.PDF for .NETを使用してさまざまなツールを使ってテキストを検索して取得する方法を説明します。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

## PDFドキュメントのすべてのページからテキストを検索して取得

[TextFragmentAbsorber](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text/textfragmentabsorber)クラスを使用すると、PDFドキュメントのすべてのページから特定のフレーズに一致するテキストを見つけることができます。ドキュメント全体からテキストを検索するには、PagesコレクションのAcceptメソッドを呼び出す必要があります。[Accept](https://reference.aspose.com/pdf/ja/net/aspose.pdf.page/accept/methods/3)メソッドはTextFragmentAbsorberオブジェクトをパラメーターとして受け取り、TextFragmentオブジェクトのコレクションを返します。すべてのフラグメントをループして、Text、Position (XIndent, YIndent)、FontName、FontSize、IsAccessible、IsEmbedded、IsSubset、ForegroundColorなどのプロパティを取得できます。

次のコードスニペットは、すべてのページからテキストを検索する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
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
    }
}
```

特定のPDFページ内でテキストを検索する必要がある場合は、ドキュメントインスタンスのページコレクションからページ番号を指定し、そのページに対してAcceptメソッドを呼び出してください（以下のコード行に示されています）。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for a particular page
        document.Pages[2].Accept(textFragmentAbsorber);
    }
}
```

### TextFragmentAbsorber内のフレーズのリストを通じて検索

C#ライブラリはTextFragmentAbsorberに1つのフレーズしか渡せませんが、Aspose.PDFの24.2リリース以降、リスト検索アルゴリズムの新しいアルゴリズムが実装されました。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // Create resular expressions
    var regexes = new Regex[]
    {
        new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)", RegexOptions.IgnoreCase),
        new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:? ", RegexOptions.IgnoreCase),
        new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
        new Regex("Vested in:", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regexes, new Aspose.Pdf.Text.TextSearchOptions(true));
        document.Pages.Accept(absorber);
        // Get result
        var result = absorber.RegexResults;
    }
}
```

このコードスニペットは、正規表現を使用してPDFドキュメント内の特定のパターン（ドキュメント番号、キーワード、ファイル番号など）を検索します。PDFを読み込み、検索を適用し、さらなる処理のために一致する結果を取得します。

## PDFドキュメントのすべてのページからテキストセグメントを検索して取得

すべてのページからテキストセグメントを検索するには、まずドキュメントからTextFragmentオブジェクトを取得する必要があります。TextFragmentAbsorberを使用すると、PDFドキュメントのすべてのページから特定のフレーズに一致するテキストを見つけることができます。ドキュメント全体からテキストを検索するには、PagesコレクションのAcceptメソッドを呼び出す必要があります。AcceptメソッドはTextFragmentAbsorberオブジェクトをパラメーターとして受け取り、TextFragmentオブジェクトのコレクションを返します。ドキュメントからTextFragmentCollectionが取得されたら、このコレクションをループして各TextFragmentオブジェクトのTextSegmentCollectionを取得する必要があります。その後、各TextSegmentオブジェクトのすべてのプロパティを取得できます。次のコードスニペットは、すべてのページからテキストセグメントを検索する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextPage.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Figure");

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            foreach (var textSegment in textFragment.Segments)
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
    }
}
```

特定のPDFページからTextSegmentsを検索して取得するには、Accept(..)メソッドを呼び出すときに特定のページインデックスを指定する必要があります。以下のコード行を参照してください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for a particular page
        document.Pages[2].Accept(textFragmentAbsorber);
    }
}
```

## 正規表現を使用してすべてのページからテキストを検索して取得

TextFragmentAbsorberは、正規表現に基づいてすべてのページからテキストを検索して取得するのに役立ちます。まず、正規表現をTextFragmentAbsorberコンストラクターにフレーズとして渡す必要があります。その後、TextFragmentAbsorberオブジェクトのTextSearchOptionsプロパティを設定する必要があります。このプロパティにはTextSearchOptionsオブジェクトが必要で、新しいオブジェクトを作成する際にそのコンストラクターにtrueをパラメーターとして渡す必要があります。すべてのページから一致するテキストを取得するには、PagesコレクションのAcceptメソッドを呼び出す必要があります。TextFragmentAbsorberは、正規表現によって指定された基準に一致するすべてのフラグメントを含むTextFragmentCollectionを返します。次のコードスニペットは、正規表現に基づいてすべてのページからテキストを検索して取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all the phrases matching the regular expression
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}"); // Like 1999-2000

        // Set text search option to specify regular expression usage
        var textSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

        textFragmentAbsorber.TextSearchOptions = textSearchOptions;

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
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
    }
}
```

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextFragmentAbsorberCtor()
{
    Aspose.Pdf.Text.TextFragmentAbsorber textFragmentAbsorber;
    // In order to search exact match of a word, you may consider using regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"\bWord\b", new Aspose.Pdf.Text.TextSearchOptions(true));

    // In order to search a string in either upper case or lowercase, you may consider using regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("(?i)Line", new Aspose.Pdf.Text.TextSearchOptions(true));

    // In order to search all the strings (parse all strings) inside PDF document, please try using following regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"[\S]+");

    // Find match of search string and get anything after the string till line break
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(?i)the ((.)*)");

    // Please use following regular expression to find text following to the regex match
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(?<=word).*");

    // In order to search Hyperlink/URL's inside PDF document, please try using following regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
}
```

## Regexに基づいてテキストを検索し、ハイパーリンクを追加

正規表現に基づいてテキストフレーズにハイパーリンクを追加したい場合は、まずTextFragmentAbsorberを使用してその特定の正規表現に一致するすべてのフレーズを見つけ、これらのフレーズにハイパーリンクを追加します。

フレーズを見つけてハイパーリンクを追加するには：

1. 正規表現をTextFragmentAbsorberコンストラクターにパラメーターとして渡します。
2. 正規表現が使用されているかどうかを指定するTextSearchOptionsオブジェクトを作成します。
3. 一致するフレーズをTextFragmentsに取得します。
4. 一致をループして、その矩形の寸法を取得し、前景色を青に変更します（オプション - ハイパーリンクのように見えるようにし、PdfContentEditorクラスのCreateWebLink(..)メソッドを使用してリンクを作成します）。
5. DocumentオブジェクトのSaveメソッドを使用して更新されたPDFを保存します。
次のコードスニペットは、正規表現を使用してPDFファイル内のテキストを検索し、一致にハイパーリンクを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create absorber object to find all instances of the input search phrase
    var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}");

    // Enable regular expression search
    absorber.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

    // Create the editor
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");

        // Accept the absorber for the page
        editor.Document.Pages[1].Accept(absorber);

        int[] dashArray = { };
        String[] LEArray = { };
        System.Drawing.Color blue = System.Drawing.Color.Blue;

        // Loop through the fragments
        foreach (var textFragment in absorber.TextFragments)
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

        // Save PDF document
        editor.Save(dataDir + "SearchTextAndAddHyperlink_out.pdf");
    }
}
```

## 各TextFragmentの周りに矩形を描画して検索する

Aspose.PDF for .NETは、各文字またはテキストフラグメントの座標を検索して取得する機能をサポートしています。したがって、各文字に対して返される座標が確実であることを確認するために、各文字の周りにハイライト（矩形を追加）することを検討できます。

テキスト段落の場合、段落の区切りを決定するためにいくつかの正規表現を使用し、その周りに矩形を描画することを検討できます。次のコードスニペットを参照してください。次のコードスニペットは、各文字の座標を取得し、各文字の周りに矩形を作成します。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SearchAndDraw()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {

        // Create TextAbsorber object to find all the phrases matching the regular expression
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(".");

        var textSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);
        textAbsorber.TextSearchOptions = textSearchOptions;

        document.Pages.Accept(textAbsorber);

        foreach (var textFragment in textAbsorber.TextFragments)
        {
            DrawRectangleOnPage(textFragment.Rectangle, textFragment.Page, new Aspose.Pdf.Operators.SetRGBColorStroke(System.Drawing.Color.Red));
        }   
        // Save PDF document
        document.Save(dataDir + "SearchTextAndDrawRectangle_out.pdf");
    }
}

 private static void DrawRectangleOnPage(Aspose.Pdf.Rectangle rectangle, Aspose.Pdf.Page page, Aspose.Pdf.Operators.SetRGBColorStroke colorStroke = null)
 {
     if (colorStroke == null)
     {
         colorStroke = new Aspose.Pdf.Operators.SetRGBColorStroke(0.7, 0, 0);
     }

     page.Contents.Add(new Aspose.Pdf.Operators.GSave());
     page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
     page.Contents.Add(colorStroke);
     page.Contents.Add(
         new Re(rectangle.LLX,
             rectangle.LLY,
             rectangle.Width,
             rectangle.Height));
     page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
     page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
 }
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SearchAndDraw()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf");
    
    // Create TextAbsorber object to find all the phrases matching the regular expression
    var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(".");

    var textSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);
    textAbsorber.TextSearchOptions = textSearchOptions;

    document.Pages.Accept(textAbsorber);

    foreach (var textFragment in textAbsorber.TextFragments)
    {
        DrawRectangleOnPage(textFragment.Rectangle, textFragment.Page, new Aspose.Pdf.Operators.SetRGBColorStroke(System.Drawing.Color.Red));
    }   
    // Save PDF document
    document.Save(dataDir + "SearchTextAndDrawRectangle_out.pdf");
}

 private static void DrawRectangleOnPage(Aspose.Pdf.Rectangle rectangle, Aspose.Pdf.Page page, Aspose.Pdf.Operators.SetRGBColorStroke colorStroke = null)
 {
     if (colorStroke == null)
     {
         colorStroke = new Aspose.Pdf.Operators.SetRGBColorStroke(0.7, 0, 0);
     }

     page.Contents.Add(new Aspose.Pdf.Operators.GSave());
     page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
     page.Contents.Add(colorStroke);
     page.Contents.Add(
         new Re(rectangle.LLX,
             rectangle.LLY,
             rectangle.Width,
             rectangle.Height));
     page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
     page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
 }
```
{{< /tab >}}
{{< /tabs >}}

## PDFドキュメント内の各文字をハイライト

{{% alert color="primary" %}}

Aspose.PDFを使用してドキュメント内のテキストを検索し、結果をオンラインでこの[リンク](https://products.aspose.app/pdf/search)で取得することを試してみてください。

{{% /alert %}}

Aspose.PDF for .NETは、各文字またはテキストフラグメントの座標を検索して取得する機能をサポートしています。したがって、各文字に対して返される座標が確実であることを確認するために、各文字の周りにハイライト（矩形を追加）することを検討できます。次のコードスニペットは、各文字の座標を取得し、各文字の周りに矩形を作成します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SearchAndHighlight()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    int resolution = 150;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {

        using (MemoryStream stream = new MemoryStream())
        {
            var conv = new Aspose.Pdf.Facades.PdfConverter(document);
            conv.Resolution = new Aspose.Pdf.Devices.Resolution(resolution, resolution);
            conv.GetNextImage(stream, System.Drawing.Imaging.ImageFormat.Png);

            using (var bmp = System.Drawing.Bitmap.FromStream(stream))
            {

                using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
                {
                    float scale = resolution / 72f;
                    gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

                    for (int i = 0; i < document.Pages.Count; i++)
                    {
                        var page = document.Pages[1];
                        // Create TextAbsorber object to find all words
                        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"[\S]+");
                        textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
                        page.Accept(textFragmentAbsorber);
                        // Get the extracted text fragments
                        var textFragmentCollection = textFragmentAbsorber.TextFragments;
                        // Loop through the fragments
                        foreach (var textFragment in textFragmentCollection)
                        {
                            if (i == 0)
                            {
                                gr.DrawRectangle(
                                    System.Drawing.Pens.Yellow,
                                    (float)textFragment.Position.XIndent,
                                    (float)textFragment.Position.YIndent,
                                    (float)textFragment.Rectangle.Width,
                                    (float)textFragment.Rectangle.Height);

                                for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
                                {
                                    var segment = textFragment.Segments[segNum];

                                    for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
                                    {
                                        var characterInfo = segment.Characters[charNum];

                                        Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
                                        Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
                                            "   TextFragment URY = " + textFragment.Rectangle.URY);

                                        gr.DrawRectangle(
                                            System.Drawing.Pens.Black,
                                            (float)characterInfo.Rectangle.LLX,
                                            (float)characterInfo.Rectangle.LLY,
                                            (float)characterInfo.Rectangle.Width,
                                            (float)characterInfo.Rectangle.Height);
                                    }

                                    gr.DrawRectangle(
                                        System.Drawing.Pens.Green,
                                        (float)segment.Rectangle.LLX,
                                        (float)segment.Rectangle.LLY,
                                        (float)segment.Rectangle.Width,
                                        (float)segment.Rectangle.Height);
                                }
                            }
                        }
                    }
                }
                
                // Save result
                bmp.Save(dataDir + "HighlightCharacterInPDF_out.png", System.Drawing.Imaging.ImageFormat.Png);
            }
        }
    }
}
```

## 隠しテキストを追加して検索

時々、PDFドキュメントに隠しテキストを追加し、その後隠しテキストを検索してその位置を後処理に使用したいことがあります。ご便利のために、Aspose.PDF for .NETはこれらの機能を提供します。ドキュメント生成中に隠しテキストを追加できます。また、TextFragmentAbsorberを使用して隠しテキストを見つけることができます。隠しテキストを追加するには、追加されたテキストに対してTextState.Invisibleを‘true’に設定します。TextFragmentAbsorberは、パターンに一致するすべてのテキストを見つけます（指定されている場合）。これは変更できないデフォルトの動作です。見つかったテキストが実際に見えないかどうかを確認するには、TextState.Invisibleプロパティを使用できます。以下のコードスニペットは、この機能の使用方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAndSearchText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var frag1 = new Aspose.Pdf.Text.TextFragment("This is common text.");
        var frag2 = new Aspose.Pdf.Text.TextFragment("This is invisible text.");

        //Set text property - invisible
        frag2.TextState.Invisible = true;

        page.Paragraphs.Add(frag1);
        page.Paragraphs.Add(frag2);
        // Save PDF document
        document.Save(dataDir + "CreateAndSearchText_out.pdf");
    }

    // Search text in the document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateAndSearchText_out.pdf"))
    {
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        foreach (var fragment in absorber.TextFragments)
        {
            //Do something with fragments
            Console.WriteLine("Text '{0}' on pos {1} invisibility: {2} ",
            fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
        }
    }
}
```

## .NET Regexを使用してテキストを検索

Aspose.PDF for .NETは、標準の.NET Regexオプションを使用してドキュメントを検索する機能を提供します。TextFragmentAbsorberは、この目的のために使用できます。以下のコードサンプルに示されています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create Regex object to find all words
    var regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf"))
    {

        // Get a particular page
        var page = document.Pages[1];

        // Create TextAbsorber object to find all instances of the input regex
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regex);
        textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

        // Accept the absorber for the page
        page.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            Console.WriteLine(textFragment.Text);
        }
    }
}
```

## 太字テキストを検索する

Aspose.PDF for .NETは、フォントスタイルプロパティを使用してドキュメントを検索することを許可します。TextFragmentAbsorberは、この目的のために使用できます。以下のコードサンプルに示されています。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractBoldText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractBoldText.pdf"))
    {
        // Create TextFragmentAbsorber object to extract text
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // Accept the absorber for all document
        textFragmentAbsorber.Visit(document);

        // Loop through the fragments
        foreach (var textFragment in textFragmentAbsorber.TextFragments)
        {
            // Get the text properties of the text fragment
            var textState = textFragment.TextState;
            // Check if text is bold
            if (textState.FontStyle == FontStyles.Bold)
            {
                // Print the text from the text fragment
                Console.WriteLine("Text :- " + textFragment.Text);
            }
        }
    }
}
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractBoldText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "ExtractBoldText.pdf");
    
    // Create TextFragmentAbsorber object to extract text
    var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

    // Accept the absorber for all document
    textFragmentAbsorber.Visit(document);

    // Loop through the fragments
    foreach (var textFragment in textFragmentAbsorber.TextFragments)
    {
        // Get the text properties of the text fragment
        var textState = textFragment.TextState;
        // Check if text is bold
        if (textState.FontStyle == FontStyles.Bold)
        {
            // Print the text from the text fragment
            Console.WriteLine("Text :- " + textFragment.Text);
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

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