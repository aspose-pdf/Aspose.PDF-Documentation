---
title: PDFでのアクションの操作
linktitle: アクション
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/actions/
description: このセクションでは、C#でプログラム的にドキュメントやフォームフィールドにアクションを追加する方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Actions in PDF",
    "alternativeHeadline": "Programmatic Actions in PDF with C#",
    "abstract": "「Aspose.PDF for .NETの新機能により、開発者はプログラムでPDFにアクションを追加できるようになり、ドキュメント内のインタラクティブ性が向上します。ユーザーはドキュメント内を移動するためのハイパーリンクや外部URLへのリンクを実装できるほか、PDFが開かれた際の表示方法を制御するためのドキュメントオープンアクションを操作できます。この強力な機能により、C#アプリケーション向けのドキュメント作成とインタラクションが効率化されます」",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "C#, PDF actions, hyperlink creation, LinkAnnotation, LocalHyperlink, FreeTextAnnotation, document open action, XYZExplicitDestination, Aspose.PDF, PDF manipulation",
    "wordcount": "2714",
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
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2025-03-29",
    "description": "このセクションでは、C#を使用してドキュメントやフォームフィールドにアクションをプログラムで追加する方法について説明します。"
}
</script>

以下のコードスニペットは [Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリでも動作します。

## PDFファイルにハイパーリンクを追加する

PDFファイルにハイパーリンクを追加して、読者がPDFの別の部分や外部コンテンツに移動できるようにすることが可能です。

PDFドキュメントにウェブハイパーリンクを追加するには:

1. [Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document) クラスオブジェクトを作成します。
1. リンクを追加したい [Page](https://reference.aspose.com/pdf/ja/net/aspose.pdf/page) クラスを取得します。
1. Pageと [Rectangle](https://reference.aspose.com/pdf/ja/net/aspose.pdf/rectangle) オブジェクトを使用して [LinkAnnotation](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/linkannotation) オブジェクトを作成します。矩形オブジェクトは、リンクを追加するページ上の位置を指定するために使用されます。
1. Actionプロパティを、リモートURIの場所を指定する [GoToURIAction](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/gotouriaction) オブジェクトに設定します。
1. ハイパーリンクテキストを表示するには、[LinkAnnotation](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/linkannotation) オブジェクトが配置されている場所と同様の位置にテキスト文字列を追加します。
1. 自由テキストを追加するには:

- [FreeTextAnnotation](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/freetextannotation) オブジェクトをインスタンス化します。これもPageとRectangleオブジェクトを引数として受け取るため、LinkAnnotationコンストラクタに指定したのと同じ値を提供できます。
- [FreeTextAnnotation](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/freetextannotation) オブジェクトのContentsプロパティを使用して、出力PDFに表示される文字列を指定します。
- オプションで、[LinkAnnotation](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/linkannotation) とFreeTextAnnotationオブジェクトの境界線の幅を0に設定して、PDFドキュメントに表示されないようにします。
- [LinkAnnotation](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/linkannotation) と [FreeTextAnnotation](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/freetextannotation) オブジェクトが定義されたら、これらのリンクを [Page](https://reference.aspose.com/pdf/ja/net/aspose.pdf/page) オブジェクトのAnnotationsコレクションに追加します。
- 最後に、[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document) オブジェクトの [Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save) メソッドを使用して更新されたPDFを保存します。

以下のコードスニペットは、PDFファイルにハイパーリンクを追加する方法を示しています。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf"))
    {
        // Get page
        var page = document.Pages[1];
        // Create Link annotation object
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        // Create border object for LinkAnnotation
        var border = new Aspose.Pdf.Annotations.Border(link);
        // Set the border width value as 0
        border.Width = 0;
        // Set the border for LinkAnnotation
        link.Border = border;
        // Specify the link type as remote URI
        link.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");
        // Add link annotation to annotations collection of first page of PDF file
        page.Annotations.Add(link);

        // Create Free Text annotation
        var textAnnotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
        // String to be added as Free text
        textAnnotation.Contents = "Link to Aspose website";
        // Set the border for Free Text Annotation
        textAnnotation.Border = border;
        // Add FreeText annotation to annotations collection of first page of Document
        document.Pages[1].Annotations.Add(textAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf");
    // Get page
    var page = document.Pages[1];
    // Create Link annotation object
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    // Create border object for LinkAnnotation
    var border = new Aspose.Pdf.Annotations.Border(link);
    // Set the border width value as 0
    border.Width = 0;
    // Set the border for LinkAnnotation
    link.Border = border;
    // Specify the link type as remote URI
    link.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");
    // Add link annotation to annotations collection of first page of PDF file
    page.Annotations.Add(link);

    // Create Free Text annotation
    var textAnnotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
    // String to be added as Free text
    textAnnotation.Contents = "Link to Aspose website";
    // Set the border for Free Text Annotation
    textAnnotation.Border = border;
    // Add FreeText annotation to annotations collection of first page of Document
    document.Pages[1].Annotations.Add(textAnnotation);

    // Save PDF document
    document.Save(dataDir + "AddHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

別の一般的なシナリオは、TextFragmentAbsorberを使用してドキュメント内の特定のテキストを見つけ、その領域をサイトへのハイパーリンクとして設定することです。以下はこれを実装するコードスニペットです。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlinkForExistingText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf"))
    {
        // Get page
        var page = document.Pages[1];

        // The text in the document for which we want to create a link
        string textForLink = "Portable Document Format";

        // Finding the location of text on a page
        var textFragmentAbsosrber = new Aspose.Pdf.Text.TextFragmentAbsorber(textForLink);
        page.Accept(textFragmentAbsosrber);
        foreach(Aspose.Pdf.Text.TextFragment textFragment in textFragmentAbsosrber.TextFragments)
        {
            // Create Link annotation object
            var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, textFragment.Rectangle);
            // Create border object for LinkAnnotation
            var border = new Aspose.Pdf.Annotations.Border(link);
            // Set the border width value as 0
            border.Width = 0;
            // Set the border for LinkAnnotation
            link.Border = border;
            // Specify the link type as remote URI
            link.Action = new Aspose.Pdf.Annotations.GoToURIAction("https://www.pdfa-inc.org/");
            // Add link annotation to annotations collection of first page of PDF file
            page.Annotations.Add(link);
        }

        // Save PDF document
        document.Save(dataDir + "AddHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlinkForExistingText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf");

    // Get page
    var page = document.Pages[1];

    // The text in the document for which we want to create a link
    string textForLink = "Portable Document Format";

    // Finding the location of text on a page
    var textFragmentAbsosrber = new Aspose.Pdf.Text.TextFragmentAbsorber(textForLink);
    page.Accept(textFragmentAbsosrber);
    foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentAbsosrber.TextFragments)
    {
        // Create Link annotation object
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, textFragment.Rectangle);
        // Create border object for LinkAnnotation
        var border = new Aspose.Pdf.Annotations.Border(link);
        // Set the border width value as 0
        border.Width = 0;
        // Set the border for LinkAnnotation
        link.Border = border;
        // Specify the link type as remote URI
        link.Action = new Aspose.Pdf.Annotations.GoToURIAction("https://www.pdfa-inc.org/");
        // Add link annotation to annotations collection of first page of PDF file
        page.Annotations.Add(link);
    }

    // Save PDF document
    document.Save(dataDir + "AddHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 同じPDF内のページへのハイパーリンクを作成する

Aspose.PDF for .NETは、PDFの作成とその操作に優れた機能を提供します。また、PDFページへのリンクを追加する機能も提供しており、リンクは別のPDFファイルのページ、ウェブURL、アプリケーションを起動するリンク、または同じPDFファイル内のページに向けることができます。同じPDFファイル内のページへのローカルハイパーリンクを追加するには、Aspose.PDF名前空間に [LocalHyperlink](https://reference.aspose.com/pdf/ja/net/aspose.pdf/localhyperlink) というクラスが追加されており、このクラスにはTargetPageNumberというプロパティがあり、ハイパーリンクのターゲット/宛先ページを指定するために使用されます。

ローカルハイパーリンクを追加するには、リンクをTextFragmentに関連付けることができるようにTextFragmentを作成する必要があります。[TextFragment](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text/textfragment) クラスにはHyperlinkというプロパティがあり、LocalHyperlinkインスタンスを関連付けるために使用されます。以下のコードスニペットは、この要件を達成するための手順を示しています。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create Text Fragment instance
        var text = new Aspose.Pdf.Text.TextFragment("link page number test to page 7");
        // Create local hyperlink instance
        var link = new Aspose.Pdf.LocalHyperlink();
        // Set target page for link instance
        link.TargetPageNumber = 7;
        // Set TextFragment hyperlink
        text.Hyperlink = link;
        // Add text to paragraphs collection of Page
        page.Paragraphs.Add(text);
        // Create new TextFragment instance
        text = new Aspose.Pdf.Text.TextFragment("link page number test to page 1");
        // TextFragment should be added over new page
        text.IsInNewPage = true;
        // Create another local hyperlink instance
        link = new Aspose.Pdf.LocalHyperlink();
        // Set Target page for second hyperlink
        link.TargetPageNumber = 1;
        // Set link for second TextFragment
        text.Hyperlink = link;
        // Add text to paragraphs collection of page object
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CreateLocalHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    // Add page
    var page = document.Pages.Add();
    // Create Text Fragment instance
    var text = new Aspose.Pdf.Text.TextFragment("link page number test to page 7");
    // Create local hyperlink instance
    var link = new Aspose.Pdf.LocalHyperlink();
    // Set target page for link instance
    link.TargetPageNumber = 7;
    // Set TextFragment hyperlink
    text.Hyperlink = link;
    // Add text to paragraphs collection of Page
    page.Paragraphs.Add(text);
    // Create new TextFragment instance
    text = new Aspose.Pdf.Text.TextFragment("link page number test to page 1");
    // TextFragment should be added over new page
    text.IsInNewPage = true;
    // Create another local hyperlink instance
    link = new Aspose.Pdf.LocalHyperlink();
    // Set Target page for second hyperlink
    link.TargetPageNumber = 1;
    // Set link for second TextFragment
    text.Hyperlink = link;
    // Add text to paragraphs collection of page object
    page.Paragraphs.Add(text);

    // Save PDF document
    document.Save(dataDir + "CreateLocalHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## PDFハイパーリンクの宛先（URL）を取得する

リンクはPDFファイル内で注釈として表現され、追加、更新、または削除することができます。Aspose.PDF for .NETは、PDFファイル内のハイパーリンクの宛先（URL）を取得する機能もサポートしています。

リンクのURLを取得するには:

1. [Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document) オブジェクトを作成します。
1. リンクを抽出したい [Page](https://reference.aspose.com/pdf/ja/net/aspose.pdf/page) を取得します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/annotationselector) クラスを使用して、指定されたページからすべての [LinkAnnotation](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/linkannotation) オブジェクトを抽出します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/annotationselector) オブジェクトを [Page](https://reference.aspose.com/pdf/ja/net/aspose.pdf/page) オブジェクトのAcceptメソッドに渡します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/annotationselector) オブジェクトのSelectedプロパティを使用して、選択されたすべてのリンク注釈をIListオブジェクトに取得します。
1. 最後に、LinkAnnotationのActionをGoToURIActionとして抽出します。

以下のコードスニペットは、PDFファイルからハイパーリンクの宛先（URL）を取得する方法を示しています。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Traverse through all the page of PDF
        foreach (var page in document.Pages)
        {
            // Get the link annotations from particular page
            var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

            page.Accept(selector);

            // Create list holding all the links
            var list = selector.Selected;

            // Iterate through individual item inside list
            foreach (var a in list)
            {
                // Print the destination URL
                Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Traverse through all the page of PDF
    foreach (var page in document.Pages)
    {
        // Get the link annotations from particular page
        var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

        page.Accept(selector);

        // Create list holding all the links
        var list = selector.Selected;

        // Iterate through individual item inside list
        foreach (var a in list)
        {
            // Print the destination URL
            Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## ハイパーリンクのテキストを取得する

ハイパーリンクには2つの部分があります: ドキュメントに表示されるテキストと、宛先URLです。場合によっては、URLではなくテキストが必要になることがあります。

PDFファイル内のテキストと注釈/アクションは、異なるエンティティによって表現されます。ページ上のテキストは単なる単語と文字の集合であり、注釈はハイパーリンクに固有のインタラクティブ性をもたらします。

URLの内容を見つけるには、注釈とテキストの両方を操作する必要があります。[Annotation](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/annotation) オブジェクト自体にはテキストがありませんが、ページ上のテキストの下に配置されます。したがって、テキストを取得するには、注釈はURLの境界を提供し、テキストオブジェクトはURLの内容を提供します。以下のコードスニペットを参照してください。

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShowLinkAnnotationText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through each page of PDF
        foreach (var page in document.Pages)
        {
            // Show link annotation
            ShowLinkAnnotations(page);
        }
    }
}

private static void ShowLinkAnnotations(Aspose.Pdf.Page page)
{
    foreach (var annot in page.Annotations)
    {
        if (annot is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            page.Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShowLinkAnnotationText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Iterate through each page of PDF
    foreach (var page in document.Pages)
    {
        // Show link annotation
        ShowLinkAnnotations(page);
    }
}

private static void ShowLinkAnnotations(Aspose.Pdf.Page page)
{
    foreach (var annot in page.Annotations)
    {
        if (annot is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            page.Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## PDFファイルからドキュメントオープンアクションを削除する

[ドキュメントを表示する際にPDFページを指定する方法](#how-to-specify-pdf-page-when-viewing-document)では、ドキュメントを最初のページ以外で開くように指定する方法を説明しました。複数のドキュメントを結合する際に、1つ以上のドキュメントにGoToアクションが設定されている場合、それらを削除したいことがあります。たとえば、2つのドキュメントを結合し、2番目のドキュメントに2ページ目に移動するGoToアクションがある場合、出力ドキュメントは結合されたドキュメントの最初のページではなく、2番目のドキュメントの2ページ目で開きます。この動作を避けるために、オープンアクションコマンドを削除します。

オープンアクションを削除するには:

1. [Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document) オブジェクトの [OpenAction](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/properties/openaction) プロパティをnullに設定します。
1. Documentオブジェクトの [Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save) メソッドを使用して更新されたPDFを保存します。

以下のコードスニペットは、PDFファイルからドキュメントオープンアクションを削除する方法を示しています。

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveOpenAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveOpenAction.pdf"))
    {
        // Remove document open action
        document.OpenAction = null;

        // Save PDF document
        document.Save(dataDir + "RemoveOpenAction_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveOpenAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "RemoveOpenAction.pdf");

    // Remove document open action
    document.OpenAction = null;

    // Save PDF document
    document.Save(dataDir + "RemoveOpenAction_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## ドキュメントを表示する際にPDFページを指定する方法 {#how-to-specify-pdf-page-when-viewing-document}

Adobe ReaderなどのPDFビューアでPDFファイルを表示する場合、通常は最初のページで開きます。しかし、ファイルを別のページで開くように設定することも可能です。

[XYZExplicitDestination](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/xyzexplicitdestination) クラスを使用すると、開きたいPDFファイル内のページを指定できます。GoToActionオブジェクト値を [Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document) クラスのOpenActionプロパティに渡すと、XYZExplicitDestinationオブジェクトに対して指定されたページでドキュメントが開きます。以下のコードスニペットは、ドキュメントオープンアクションとしてページを指定する方法を示しています。

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SpecifyPageWhenViewing.pdf"))
    {
        // Get the instance of second page of document
        var page2 = document.Pages[2];
        // Create the variable to set the zoom factor of target page
        double zoom = 1;
        // Create GoToAction instance
        var action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[2]);
        // Go to 2 page
        action.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
        // Set the document open action
        document.OpenAction = action;
        // Save PDF document
        document.Save(dataDir + "Goto2page_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "SpecifyPageWhenViewing.pdf");
    // Get the instance of second page of document
    var page2 = document.Pages[2];
    // Create the variable to set the zoom factor of target page
    double zoom = 1;
    // Create GoToAction instance
    var action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[2]);
    // Go to 2 page
    action.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
    // Set the document open action
    document.OpenAction = action;
    // Save PDF document
    document.Save(dataDir + "Goto2page_out.pdf");
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