---
title: PDF内のテキストを置き換える
linktitle: PDF内のテキストを置き換える
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/replace-text-in-pdf/
description: Aspose.PDF for .NETライブラリからテキストを置き換えたり削除したりするさまざまな方法について学びます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Replace Text in PDF",
    "alternativeHeadline": "Efficiently Modify Text Across PDF Pages with Ease",
    "abstract": "Aspose.PDF for .NETのPDF内のテキストを置き換える機能により、ユーザーはPDFドキュメント全体または特定のページ領域内のテキストを効率的に検索して置き換えることができます。正規表現に基づくテキスト置き換え、置き換え後のページコンテンツの自動再配置、未使用フォントの削除機能など、高度な機能をサポートしており、ドキュメント編集体験を向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2744",
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
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NETライブラリからテキストを置き換えたり削除したりするさまざまな方法について学びます。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

## PDFドキュメントのすべてのページでテキストを置き換える

{{% alert color="primary" %}}

Aspose.PDFを使用してドキュメント内のテキストを検索して置き換え、結果をこの[リンク](https://products.aspose.app/pdf/redaction)でオンラインで取得できます。

{{% /alert %}}

PDFドキュメントのすべてのページでテキストを置き換えるには、まずTextFragmentAbsorberを使用して置き換えたい特定のフレーズを見つける必要があります。その後、すべてのTextFragmentsを通過してテキストを置き換え、他の属性を変更する必要があります。それが完了したら、DocumentオブジェクトのSaveメソッドを使用して出力PDFを保存するだけです。次のコードスニペットは、PDFドキュメントのすべてのページでテキストを置き換える方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextInAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for all the pages
        document.Pages.Accept(absorber);

        // Get the extracted text fragments
        var textFragmentCollection = absorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            // Update text and other properties
            textFragment.Text = "TEXT";
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");
            textFragment.TextState.FontSize = 22;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
            textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextInAllPages_out.pdf");
    }
}
```

## 特定のページ領域でテキストを置き換える

特定のページ領域でテキストを置き換えるには、まずTextFragmentAbsorberオブジェクトをインスタンス化し、TextSearchOptions.Rectangleプロパティを使用してページ領域を指定し、その後すべてのTextFragmentsを通過してテキストを置き換える必要があります。これらの操作が完了したら、DocumentオブジェクトのSaveメソッドを使用して出力PDFを保存するだけです。次のコードスニペットは、PDFドキュメントのすべてのページでテキストを置き換える方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextInParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "programaticallyproducedpdf.pdf"))
    {
        // instantiate TextFragment Absorber object
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // search text within page bound
        absorber.TextSearchOptions.LimitToPageBounds = true;

        // specify the page region for TextSearch Options
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 100, 200, 200);

        // search text from first page of PDF file
        document.Pages[1].Accept(absorber);

        // iterate through individual TextFragment
        foreach (var textFragment in absorber.TextFragments)
        {
            // update text to blank characters
            textFragment.Text = "";
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextInParticularPageRegion_out.pdf");
    }
}
```

## 正規表現に基づいてテキストを置き換える

正規表現に基づいていくつかのフレーズを置き換えたい場合は、まずTextFragmentAbsorberを使用してその特定の正規表現に一致するすべてのフレーズを見つける必要があります。正規表現をTextFragmentAbsorberコンストラクタのパラメータとして渡す必要があります。また、正規表現が使用されているかどうかを指定するTextSearchOptionsオブジェクトを作成する必要があります。一度TextFragments内で一致するフレーズを取得したら、それらすべてをループして必要に応じて更新する必要があります。最後に、DocumentオブジェクトのSaveメソッドを使用して更新されたPDFを保存する必要があります。次のコードスニペットは、正規表現に基づいてテキストを置き換える方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextBasedOnARegularExpression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionPage.pdf"))
    {

        // Create TextAbsorber object to find all the phrases matching the regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}"); // Like 1999-2000

        // Set text search option to specify regular expression usage
        absorber.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

        // Accept the absorber for a single page
        document.Pages[1].Accept(absorber);

        // Get the extracted text fragments
        var collection = absorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in collection)
        {
            // Update text and other properties
            textFragment.Text = "New Phrase";
            // Set to an instance of an object.
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");
            textFragment.TextState.FontSize = 22;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
            textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextonRegularExpression_out.pdf");
    }
}
```

## 既存のPDFファイル内のフォントを置き換える

Aspose.PDF for .NETは、PDFドキュメント内のテキストを置き換える機能をサポートしています。ただし、時にはPDFドキュメント内で使用されているフォントのみを置き換える必要がある場合があります。したがって、テキストを置き換えるのではなく、使用されているフォントのみが置き換えられます。TextFragmentAbsorberコンストラクタのオーバーロードの1つは、TextEditOptionsオブジェクトを引数として受け入れ、TextEditOptions.FontReplace列挙型のRemoveUnusedFonts値を使用して要件を達成できます。次のコードスニペットは、PDFドキュメント内のフォントを置き換える方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextPage.pdf"))
    {
        // Create text edit options
        var options = new Aspose.Pdf.Text.TextEditOptions(Aspose.Pdf.Text.TextEditOptions.FontReplace.RemoveUnusedFonts);

        // Search text fragments and set edit option as remove unused fonts
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(options);

        // Accept the absorber for all the pages
        document.Pages.Accept(absorber);

        // Traverse through all the TextFragments
        foreach (var textFragment in absorber.TextFragments)
        {
            // If the font name is ArialMT, replace font name with Arial
            if (textFragment.TextState.Font.FontName == "Arial,Bold")
            {
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceFonts_out.pdf");
    }
}
```

## テキストの置き換えは自動的にページコンテンツを再配置する必要があります

Aspose.PDF for .NETは、PDFファイル内のテキストを検索して置き換える機能をサポートしています。ただし、最近、一部の顧客は、特定のTextFragmentが小さいコンテンツに置き換えられたときに問題が発生し、結果のPDFに余分なスペースが表示されたり、TextFragmentが長い文字列に置き換えられた場合に単語が既存のページコンテンツと重なったりする問題に直面しました。したがって、PDFドキュメント内のテキストが置き換えられた後にコンテンツが再配置されるメカニズムを導入する必要がありました。

上記のシナリオに対応するために、Aspose.PDF for .NETは、PDFファイル内のテキストを置き換える際にそのような問題が発生しないように強化されました。次のコードスニペットは、PDFファイル内のテキストを置き換える方法を示しており、ページコンテンツが自動的に再配置される必要があります。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutomaticallyReArrangePageContents()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // Create TextFragment Absorber object with regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
        document.Pages.Accept(absorber);

        // Replace each TextFragment
        foreach (var textFragment in absorber.TextFragments)
        {
            // Set font of text fragment being replaced
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            // Set font size
            textFragment.TextState.FontSize = 12;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
            // Replace the text with larger string than placeholder
            textFragment.Text = "This is a Larger String for the Testing of this issue";
        }

        // Save PDF document
        document.Save(dataDir + "AutomaticallyReArrangePageContents_out.pdf");
    }
}
```

## PDF作成中の置き換え可能なシンボルのレンダリング

置き換え可能なシンボルは、テキスト文字列内の特別なシンボルで、実行時に対応するコンテンツに置き換えることができます。現在、Aspose.PDF名前空間の新しいドキュメントオブジェクトモデルでサポートされている置き換え可能なシンボルは、`$P`、`$p`、`\n`、`\r`です。`$p`と`$P`は、実行時のページ番号処理に使用されます。`$p`は、現在のParagraphクラスが存在するページの番号に置き換えられます。`$P`は、ドキュメント内のページの総数に置き換えられます。PDFドキュメントの段落コレクションに`TextFragment`を追加する際、テキスト内の改行はサポートされていません。ただし、改行を含むテキストを追加するには、`TextParagraph`を使用した`TextFragment`を使用してください：

- `TextFragment`内で単一の`\n`の代わりに`\r\n`または`Environment.NewLine`を使用します。
- `TextParagraph`オブジェクトを作成します。これにより、テキストが行分割されて追加されます。
- `TextParagraph.AppendLine`で`TextFragment`を追加します。
- `TextBuilder.AppendParagraph`で`TextParagraph`を追加します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RenderingReplaceableSymbols()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Initialize new TextFragment with text containing required newline markers
        Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

        // Set text fragment properties if necessary
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

        // Create TextParagraph object
        var par = new Aspose.Pdf.Text.TextParagraph();

        // Add new TextFragment to paragraph
        par.AppendLine(textFragment);

        // Set paragraph position
        par.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);

        // Add the TextParagraph using TextBuilder
        textBuilder.AppendParagraph(par);

        // Save PDF document
        document.Save(dataDir + "RenderingReplaceableSymbols_out.pdf");
    }
}
```

## ヘッダー/フッター領域内の置き換え可能なシンボル

置き換え可能なシンボルは、PDFファイルのヘッダー/フッターセクション内にも配置できます。フッターセクションに置き換え可能なシンボルを追加する方法については、次のコードスニペットを参照してください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceableSymbolsInHeaderOrFooterArea()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Create margin info
        var marginInfo = new Aspose.Pdf.MarginInfo();
        marginInfo.Top = 90;
        marginInfo.Bottom = 50;
        marginInfo.Left = 50;
        marginInfo.Right = 50;
        // Assign the marginInfo instance to Margin property of sec1.PageInfo
        page.PageInfo.Margin = marginInfo;

        var headerFooterFirst = new Aspose.Pdf.HeaderFooter();
        page.Header = headerFooterFirst;
        headerFooterFirst.Margin.Left = 50;
        headerFooterFirst.Margin.Right = 50;

        // Instantiate a Text paragraph that will store the content to show as header
        var fragment1 = new Aspose.Pdf.Text.TextFragment("report title");
        fragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment1.TextState.FontSize = 16;
        fragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
        fragment1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        fragment1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        fragment1.TextState.LineSpacing = 5f;
        headerFooterFirst.Paragraphs.Add(fragment1);

        var fragment2 = new Aspose.Pdf.Text.TextFragment("Report_Name");
        fragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
        fragment2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        fragment2.TextState.LineSpacing = 5f;
        fragment2.TextState.FontSize = 12;
        headerFooterFirst.Paragraphs.Add(fragment2);

        // Create a HeaderFooter object for the section
        var headerFooterFoot = new Aspose.Pdf.HeaderFooter();

        // Set the HeaderFooter object to odd & even footer
        page.Footer = headerFooterFoot;
        headerFooterFoot.Margin.Left = 50;
        headerFooterFoot.Margin.Right = 50;

        // Add a text paragraph containing current page number of total number of pages
        var fragment3 = new Aspose.Pdf.Text.TextFragment("Generated on test date");
        var fragment4 = new Aspose.Pdf.Text.TextFragment("report name ");
        var fragment5 = new Aspose.Pdf.Text.TextFragment("Page $p of $P");

        // Instantiate a table object
        var table2 = new Aspose.Pdf.Table();

        // Add the table in paragraphs collection of the desired section
        headerFooterFoot.Paragraphs.Add(table2);

        // Set with column widths of the table
        table2.ColumnWidths = "165 172 165";

        // Create rows in the table and then cells in the rows
        var row3 = table2.Rows.Add();

        row3.Cells.Add();
        row3.Cells.Add();
        row3.Cells.Add();

        // Set the vertical allignment of the text as center alligned
        row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
        row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
        row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

        row3.Cells[0].Paragraphs.Add(fragment3);
        row3.Cells[1].Paragraphs.Add(fragment4);
        row3.Cells[2].Paragraphs.Add(fragment5);

        // Sec1.Paragraphs.Add(New Text("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL"))
        var table = new Aspose.Pdf.Table();

        table.ColumnWidths = "33% 33% 34%";
        table.DefaultCellPadding = new Aspose.Pdf.MarginInfo();
        table.DefaultCellPadding.Top = 10;
        table.DefaultCellPadding.Bottom = 10;

        // Add the table in paragraphs collection of the desired section
        page.Paragraphs.Add(table);

        // Set default cell border using BorderInfo object
        table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1f);

        // Set table border using another customized BorderInfo object
        table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1f);

        table.RepeatingRowsCount = 1;

        // Create rows in the table and then cells in the rows
        var row1 = table.Rows.Add();

        row1.Cells.Add("col1");
        row1.Cells.Add("col2");
        row1.Cells.Add("col3");
        const string CRLF = "\r\n";
        for (int i = 0; i <= 10; i++)
        {
            var row = table.Rows.Add();
            row.IsRowBroken = true;
            for (int c = 0; c <= 2; c++)
            {
                Aspose.Pdf.Cell c1;
                if (c == 2)
                {
                    c1 = row.Cells.Add("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a" + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "Using Aspose.Total for Java developers can create a wide range of applications.");
                }
                else
                {
                    c1 = row.Cells.Add("item1" + c);
                }
                c1.Margin = new Aspose.Pdf.MarginInfo();
                c1.Margin.Left = 30;
                c1.Margin.Top = 10;
                c1.Margin.Bottom = 10;
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf");
    }
}
```

## PDFファイルから未使用フォントを削除する

Aspose.PDF for .NETは、PDFドキュメントを作成する際にフォントを埋め込む機能をサポートしており、既存のPDFファイルにフォントを埋め込む機能もサポートしています。Aspose.PDF for .NET 7.3.0以降、PDFドキュメントから重複または未使用のフォントを削除することもできます。

フォントを置き換えるには、次のアプローチを使用します：

1. [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber)クラスを呼び出します。
1. TextFragmentAbsorberクラスのTextEditOptions.FontReplace.RemoveUnusedFontsパラメータを呼び出します。（これにより、フォント置き換え中に未使用になったフォントが削除されます）。
1. 各テキストフラグメントに対して個別にフォントを設定します。

次のコードスニペットは、すべてのドキュメントページのすべてのテキストフラグメントのフォントを置き換え、未使用のフォントを削除します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveUnusedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextPage.pdf"))
    {
        var options = new Aspose.Pdf.Text.TextEditOptions(Aspose.Pdf.Text.TextEditOptions.FontReplace.RemoveUnusedFonts);
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages.Accept(absorber);

        // Iterate through all the TextFragments
        foreach (var textFragment in absorber.TextFragments)
        {
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial, Bold");
        }

        // Save PDF document
        document.Save(dataDir + "RemoveUnusedFonts_out.pdf");
    }
}
```

## PDFドキュメントからすべてのテキストを削除する

### 演算子を使用してすべてのテキストを削除する

いくつかのテキスト操作では、PDFドキュメントからすべてのテキストを削除する必要があり、そのためには通常、見つかったテキストを空の文字列値として設定する必要があります。ポイントは、多数のテキストフラグメントのテキストを変更することが、いくつかのチェックおよびテキスト位置調整操作を呼び出すことを引き起こすことです。これらはテキスト編集シナリオでは不可欠です。問題は、ループ内で処理されるシナリオで削除されるテキストフラグメントの数を決定できないことです。

したがって、PDFページからすべてのテキストを削除するシナリオには別のアプローチを使用することをお勧めします。非常に高速に動作する次のコードスニペットを考慮してください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveAllTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveAllText.pdf"))
    {
        // Loop through all pages of PDF Document
        for (int i = 1; i <= document.Pages.Count; i++)
        {
            var page = document.Pages[i];
            var operatorSelector = new Aspose.Pdf.OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
            // Select all text on the page
            page.Contents.Accept(operatorSelector);
            // Delete all text
            page.Contents.Delete(operatorSelector.Selected);
        }
        // Save PDF document
        document.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
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