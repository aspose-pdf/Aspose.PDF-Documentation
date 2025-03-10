---
title: PDFへのテキスト注釈の使用
linktitle: テキスト注釈
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/text-annotation/
description: Aspose.PDF for .NETは、PDFドキュメントからテキスト注釈を追加、取得、削除することを可能にします。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Text Annotation for PDF",
    "alternativeHeadline": "Enhance PDFs with Dynamic Text Annotations",
    "abstract": "Aspose.PDF for .NETは、ユーザーがPDFドキュメント内でテキスト注釈を簡単に追加、取得、または削除できる高度なテキスト注釈機能を導入します。この機能は、注釈の正確な配置とカスタマイズを可能にすることで、PDF編集プロセスを向上させ、ドキュメントのインタラクションと使いやすさを改善します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Text Annotation, PDF document generation, Aspose.PDF for .NET, Add Annotation, Delete Annotation, Free Text Annotation, Popup Annotation, StrikeOutAnnotation, AnnotationCollection, Aspose.PDF library",
    "wordcount": "2636",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NETは、PDFドキュメントからテキスト注釈を追加、取得、削除することを可能にします。"
}
</script>

## 既存のPDFファイルにテキスト注釈を追加する方法

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

テキスト注釈は、PDFドキュメント内の特定の位置に添付された注釈です。閉じているとき、注釈はアイコンとして表示され、開くと、読者が選択したフォントとサイズでノートテキストを含むポップアップウィンドウが表示されるべきです。

注釈は特定のページの[Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations)コレクションに含まれています。このコレクションには、その個々のページの注釈のみが含まれています。すべてのページには独自のAnnotationsコレクションがあります。

特定のページに注釈を追加するには、そのページのAnnotationsコレクションに[Add](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add)メソッドを使用して追加します。

1. まず、PDFに追加したい注釈を作成します。
1. 次に、入力PDFを開きます。
1. 注釈を[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトのAnnotationsコレクションに追加します。

次のコードスニペットは、PDFページに注釈を追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextAnnotationToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create text annotation
        var textAnnotation = new Aspose.Pdf.Annotations.TextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
        textAnnotation.Title = "Sample Annotation Title";
        textAnnotation.Subject = "Sample Subject";
        textAnnotation.SetReviewState(Aspose.Pdf.Annotations.AnnotationState.Accepted);
        textAnnotation.Contents = "Sample contents for the annotation";
        textAnnotation.Open = true;
        textAnnotation.Icon = Aspose.Pdf.Annotations.TextIcon.Key;

        // Set border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(textAnnotation);
        border.Width = 5;
        border.Dash = new Aspose.Pdf.Annotations.Dash(1, 1);
        textAnnotation.Border = border;
        textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

        // Add annotation to the annotations collection of the page
        document.Pages[1].Annotations.Add(textAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddAnnotation_out.pdf");
    }
}
```

## ポップアップ注釈を追加する方法

ポップアップ注釈は、入力と編集のためにポップアップウィンドウにテキストを表示します。単独では表示されず、マークアップ注釈、親注釈に関連付けられ、親のテキストを編集するために使用されます。

独自の外観ストリームや関連するアクションを持たず、親の注釈辞書のPopupエントリによって識別されます。

次のコードスニペットは、親の[Line annotation](/pdf/ja/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file)を追加する例を使用して、PDFページに[Popup Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation)を追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments.pdf"))
    {
        // Create Line Annotation
        var lineAnnotation = new Aspose.Pdf.Annotations.LineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(550, 93, 562, 439),
            new Aspose.Pdf.Point(556, 99), new Aspose.Pdf.Point(556, 443))
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Width = 3,
            StartingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 124, 1021, 266))
        };

        // Add annotation to the page
        document.Pages[1].Annotations.Add(lineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddLineAnnotation_out.pdf");
    }
}
```

## 新しいフリーテキスト注釈を追加（または作成）する方法

フリーテキスト注釈は、ページ上に直接テキストを表示します。[PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext)メソッドを使用して、このタイプの注釈を作成できます。次のスニペットでは、文字列の最初の出現の上にフリーテキスト注釈を追加します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextAnnotationDemo()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "pdf-sample.pdf"))
    {
        var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        // Assuming tfa is an instance of TextFragmentAbsorber or similar
        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber();
        tfa.Visit(document.Pages[1]);

        if (tfa.TextFragments.Count <= 0)
        {
            return;
        }

        // Define the rectangle for the free text annotation
        var rect = new System.Drawing.Rectangle
        {
            X = (int)tfa.TextFragments[1].Rectangle.LLX,
            Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
            Height = 18,
            Width = 100
        };

        // Create free text annotation
        pdfContentEditor.CreateFreeText(rect, "Free Text Demo", 1); // Last param is the page number

        // Save PDF document
        pdfContentEditor.Save(dataDir + "pdf-sample-0.pdf");
    }
}
```

### FreeTextAnnotationのコールアウトプロパティを設定する

PDFドキュメント内の注釈のより柔軟な構成のために、Aspose.PDF for .NETは、コールアウトラインのポイントの配列を指定できる[FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation)クラスの[Callout](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout)プロパティを提供します。次のコードスニペットは、この機能を使用する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextCalloutAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create default appearance for the annotation
        var da = new Aspose.Pdf.Annotations.DefaultAppearance();
        da.TextColor = System.Drawing.Color.Red;
        da.FontSize = 10;

        // Create free text annotation with callout
        var fta = new Aspose.Pdf.Annotations.FreeTextAnnotation(page, new Aspose.Pdf.Rectangle(422.25, 645.75, 583.5, 702.75), da);
        fta.Intent = Aspose.Pdf.Annotations.FreeTextIntent.FreeTextCallout;
        fta.EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow;
        fta.Callout = new Aspose.Pdf.Point[]
        {
            new Aspose.Pdf.Point(428.25, 651.75),
            new Aspose.Pdf.Point(462.75, 681.375),
            new Aspose.Pdf.Point(474, 681.375)
        };

        // Add the annotation to the page
        page.Annotations.Add(fta);

        // Set rich text for the annotation
        fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">This is a sample</span></p></body>";

        // Save PDF document
        document.Save(dataDir + "SetCalloutProperty_out.pdf");
    }
}
```

### XFDFファイルのコールアウトプロパティを設定する

XFDFファイルからインポートする場合は、Calloutの代わりにコールアウトライン名を使用してください。次のコードスニペットは、この機能を使用する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationsFromXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create an XFDF string builder
        var xfdf = new StringBuilder();
        xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");

        // Call the method to create XFDF content
        CreateXfdf(ref xfdf);

        xfdf.AppendLine("</annots></xfdf>");

        // Import annotations from the XFDF string
        document.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(xfdf.ToString())));

        // Save PDF document
        document.Save(dataDir + "SetCalloutPropertyXfdf_out.pdf");
    }
}
```

次のメソッドがCreateXfdfに使用されます：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">This is a sample</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```

### フリーテキスト注釈を非表示にする

時には、文書を表示しているときには見えないが、文書を印刷するときには見える透かしを作成する必要があります。この目的のために注釈フラグを使用します。次のコードスニペットは、その方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInvisibleAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create a free text annotation
        var annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(50, 600, 250, 650),
            new Aspose.Pdf.Annotations.DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red)
        );

        annotation.Contents = "ABCDEFG";
        annotation.Characteristics.Border = System.Drawing.Color.Red;
        annotation.Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print | Aspose.Pdf.Annotations.AnnotationFlags.NoView;

        // Add the annotation to the page
        document.Pages[1].Annotations.Add(annotation);

        // Save PDF document
        document.Save(dataDir + "InvisibleAnnotation_out.pdf");
    }
}
```

### FreeTextAnnotationのフォーマットを設定する

この部分では、フリーテキスト注釈内のテキストをフォーマットする方法を見ていきます。

注釈は[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトの[AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection)コレクションに含まれています。[FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation)をPDFドキュメントに追加する際に、フォント、サイズ、色などのフォーマット情報を[DefaultAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index)クラスを使用して指定できます。また、TextStyleプロパティを使用してフォーマット情報を指定することも可能です。さらに、PDFドキュメント内の既存のFreeTextAnnotationのフォーマットを更新することもできます。

[TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle)クラスは、デフォルトスタイルエントリでの作業をサポートします。このクラスを使用すると、色、フォントサイズ、フォント名を設定できます：

- FontNameプロパティは、フォント名（文字列）を取得または設定します。
- FontSizeプロパティは、デフォルトのテキストサイズ（ダブル）を取得または設定します。
- System.Drawing.Colorプロパティは、テキストの色（色）を取得または設定します。
- TextAlignmentプロパティは、注釈のテキストの配置（配置）を取得または設定します。

次のコードスニペットは、特定のテキストフォーマットでFreeTextAnnotationを追加する方法を示しています。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFreeTextAnnotationFormatting.pdf"))
    {
        // Instantiate DefaultAppearance object
        var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Arial", 28, System.Drawing.Color.Red);

        // Create annotation
        var freetext = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600), defaultAppearance);

        // Specify the contents of annotation
        freetext.Contents = "Free Text";

        // Add annotation to annotations collection of page
        document.Pages[1].Annotations.Add(freetext);

        // Save PDF document
        document.Save(dataDir + "SetFreeTextAnnotationFormatting_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeAnnotation(string fontName = "Arial", float fontSize = 28)
{
     // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
	
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFreeTextAnnotationFormatting.pdf"))
    {
        // Set default values
        var textColor = System.Drawing.Color.Red;
        var position = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

        // Instantiate DefaultAppearance object
        Aspose.Pdf.Annotations.DefaultAppearance defaultAppearance = new(fontName, fontSize, textColor);
        // Create annotation
        var freetext = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], position, defaultAppearance)
        {
            // Specify the contents of annotation
            Contents = "Free Text"
        };
        // Add anootation to annotations collection of page
        document.Pages[1].Annotations.Add(freetext);

        // Save PDF document
        document.Save(dataDir + "SetFreeTextAnnotationFormatting_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

{{% alert color="primary" %}}

フリーテキスト注釈の内容やテキストスタイルを変更すると、注釈の外観が変更を反映するように再生成されます。

{{% /alert %}}

### StrikeOutAnnotationを使用して単語を打ち消す

Aspose.PDF for .NETは、PDFドキュメントに注釈を追加、削除、更新することを可能にします。クラスの1つは、打ち消し線注釈を追加することもできます。これは、文書内の1つまたは複数のテキストフラグメントを打ち消したいときに便利です。注釈は[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトの[AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection)コレクションに保持されます。[StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation)というクラスを使用して、PDFドキュメントに打ち消し線注釈を追加できます。

特定のTextFragmentを打ち消すには：

1. PDFファイル内でTextFragmentを検索します。
1. TextFragmentオブジェクトの座標を取得します。
1. 座標を使用してStrikeOutAnnotationオブジェクトをインスタンス化します。

次のコードスニペットは、特定のTextFragmentを検索し、そのオブジェクトにStrikeOutAnnotationを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void StrikeOutTextInDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "pdf-sample.pdf"))
    {
        // Create TextFragment Absorber instance to search for a particular text fragment
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Estoque");

        // Iterate through pages of PDF document
        foreach (var page in document.Pages)
        {
            // Accept the absorber for the current page
            page.Accept(textFragmentAbsorber);
        }

        // Get the collection of absorbed text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Iterate through the collection of text fragments
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Get rectangular dimensions of the TextFragment object
            var rect = new Aspose.Pdf.Rectangle(
                (float)textFragment.Position.XIndent,
                (float)textFragment.Position.YIndent,
                (float)textFragment.Position.XIndent + (float)textFragment.Rectangle.Width,
                (float)textFragment.Position.YIndent + (float)textFragment.Rectangle.Height);

            // Instantiate StrikeOut Annotation instance
            var strikeOut = new Aspose.Pdf.Annotations.StrikeOutAnnotation(textFragment.Page, rect)
            {
                // Set opacity for annotation
                Opacity = 0.80f,

                // Set the color of annotation
                Color = Aspose.Pdf.Color.Red
            };

            // Set the border for annotation instance
            strikeOut.Border = new Aspose.Pdf.Annotations.Border(strikeOut);

            // Add annotation to the annotations collection of the TextFragment's page
            textFragment.Page.Annotations.Add(strikeOut);
        }

        // Save PDF document
        document.Save(dataDir + "StrikeOutWords_out.pdf");
    }
}
```

## PDFファイルのページからすべての注釈を削除する

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトの[AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection)コレクションには、その特定のページのすべての注釈が含まれています。ページからすべての注釈を削除するには、AnnotationCollectoinコレクションの*Delete*メソッドを呼び出します。

次のコードスニペットは、特定のページからすべての注釈を削除する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAnnotationsFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotationsFromPage.pdf"))
    {
        // Delete all annotations from the first page
        document.Pages[1].Annotations.Delete();

        // Save PDF document
        document.Save(dataDir + "DeleteAllAnnotationsFromPage_out.pdf");
    }
}
```

## PDFファイルから特定の注釈を削除する

{{% alert color="primary" %}}

Aspose.PDFの品質を確認し、オンラインで結果を得るには、次のリンクを参照してください：
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDFは、PDFファイルから特定の注釈を削除することを可能にします。このトピックでは、その方法を説明します。

PDFから特定の注釈を削除するには、[AnnotationCollectionコレクションのDeleteメソッド](https://reference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1)を呼び出します。このコレクションは[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトに属しています。Deleteメソッドには、削除したい注釈のインデックスが必要です。その後、更新されたPDFファイルを保存します。次のコードスニペットは、特定の注釈を削除する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteParticularAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteParticularAnnotation.pdf"))
    {
        // Delete a particular annotation by index (e.g., the first annotation on the first page)
        document.Pages[1].Annotations.Delete(1);

        // Save PDF document
        document.Save(dataDir + "DeleteParticularAnnotation_out.pdf");
    }
}
```

## PDFドキュメントのページからすべての注釈を取得する

Aspose.PDFは、ドキュメント全体または特定のページから注釈を取得することを可能にします。PDFドキュメントのページからすべての注釈を取得するには、希望するページリソースの[AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection)コレクションをループします。次のコードスニペットは、ページのすべての注釈を取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllAnnotationsFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAllAnnotationsFromPage.pdf"))
    {
        // Loop through all the annotations on the first page
        foreach (Aspose.Pdf.Annotations.MarkupAnnotation annotation in document.Pages[1].Annotations)
        {
            // Get annotation properties
            Console.WriteLine("Title : {0} ", annotation.Title);
            Console.WriteLine("Subject : {0} ", annotation.Subject);
            Console.WriteLine("Contents : {0} ", annotation.Contents);
        }
    }
}
```

PDF全体からすべての注釈を取得するには、AnnotationCollectionクラスコレクションをナビゲートする前に、ドキュメントのPageCollectionクラスコレクションをループする必要があることに注意してください。コレクション内の各注釈をMarkupAnnotationクラスという基本注釈タイプで取得し、そのプロパティを表示できます。

## PDFファイルから特定の注釈を取得する

注釈は個々のページに関連付けられ、[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトの[AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection)コレクションに保存されます。特定の注釈を取得するには、そのインデックスを指定します。これにより、特定の注釈タイプ、例えば[TextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textannotation)にキャストする必要がある[Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation)オブジェクトが返されます。次のコードスニペットは、特定の注釈とそのプロパティを取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetParticularAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetParticularAnnotation.pdf"))
    {
        // Get a particular annotation by index (e.g., the first annotation on the first page)
        var textAnnotation = (Aspose.Pdf.Annotations.TextAnnotation)document.Pages[1].Annotations[1];

        // Get annotation properties
        Console.WriteLine("Title : {0} ", textAnnotation.Title);
        Console.WriteLine("Subject : {0} ", textAnnotation.Subject);
        Console.WriteLine("Contents : {0} ", textAnnotation.Contents);
    }
}
```

## 注釈のリソースを取得する

Aspose.PDFは、ドキュメント全体または特定のページから注釈のリソースを取得することを可能にします。次のコードスニペットは、入力PDFファイルの[FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification)オブジェクトとして注釈のリソースを取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAndGetResourceOfAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create a screen annotation with a SWF file
        var sa = new Aspose.Pdf.Annotations.ScreenAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
        document.Pages[1].Annotations.Add(sa);

        // Save PDF document with the new annotation
        document.Save(dataDir + "GetResourceOfAnnotation_out.pdf");

        // Open the updated document
        var document1 = new Aspose.Pdf.Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

        // Get the action of the annotation
        var action = (document1.Pages[1].Annotations[1] as Aspose.Pdf.Annotations.ScreenAnnotation).Action as Aspose.Pdf.Annotations.RenditionAction;

        // Get the rendition of the rendition action
        var rendition = action.Rendition;

        // Get the media clip
        var clip = (rendition as Aspose.Pdf.Annotations.MediaRendition).MediaClip;
        var data = (clip as Aspose.Pdf.Annotations.MediaClipData).Data;

        // Read the media data
        using (var ms = new MemoryStream())
        {
            byte[] buffer = new byte[1024];
            int read = 0;

            // Data of media are accessible in FileSpecification.Contents
            using (var source = data.Contents)
            {
                while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
                {
                    ms.Write(buffer, 0, read);
                }
            }

            Console.WriteLine(rendition.Name);
            Console.WriteLine(action.RenditionOperation);
        }
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