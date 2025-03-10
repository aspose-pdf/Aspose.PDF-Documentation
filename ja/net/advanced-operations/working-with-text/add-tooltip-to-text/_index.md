---
title: C#を使用したPDFツールチップ
linktitle: PDFツールチップ
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/pdf-tooltip/
description: C#とAspose.PDFを使用してPDFのテキストフラグメントにツールチップを追加する方法を学びます
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip using C#",
    "alternativeHeadline": "Add Interactive Tooltips to PDF Text in C#",
    "abstract": "C#を使用して新しいPDFツールチップ機能でPDFドキュメントを強化します。この機能により、PDFファイルのテキストフラグメントにツールチップをシームレスに追加でき、ユーザーはマウスをテキストの上に置くことで追加情報を得ることができます。目に見えないボタンと隠れたテキストブロックを利用して、Aspose.PDFを使用した動的でインタラクティブな読書体験を作成します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1072",
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
    "url": "/net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-tooltip/"
    },
    "dateModified": "2024-11-26",
    "description": "C#とAspose.PDFを使用してPDFのテキストフラグメントにツールチップを追加する方法を学びます"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

## 見えないボタンを追加して検索されたテキストにツールチップを追加する

PDFドキュメント内のフレーズや特定の単語にツールチップとして詳細を追加することがしばしば必要です。これにより、ユーザーがテキストの上にマウスカーソルを置いたときにポップアップします。Aspose.PDF for .NETは、検索されたテキストの上に見えないボタンを追加することでツールチップを作成するこの機能を提供します。次のコードスニペットは、この機能を実現する方法を示します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTooltipToSearchedText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add().Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Move the mouse cursor here to display a tooltip"));
        document.Pages[1].Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Move the mouse cursor here to display a very long tooltip"));
        // Save PDF document
        document.Save(dataDir + "Tooltip_out.pdf");
    }

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Tooltip_out.pdf"))
    {
        // Create TextAbsorber object to find all the phrases matching the regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Move the mouse cursor here to display a tooltip");
        // Accept the absorber for the document pages
        document.Pages.Accept(absorber);
        // Get the extracted text fragments
        var textFragments = absorber.TextFragments;

        // Loop through the fragments
        foreach (var fragment in textFragments)
        {
            // Create invisible button on text fragment position
            var field = new Aspose.Pdf.Forms.ButtonField(fragment.Page, fragment.Rectangle);
            // AlternateName value will be displayed as tooltip by a viewer application
            field.AlternateName = "Tooltip for text.";
            // Add button field to the document
            document.Form.Add(field);
        }

        absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Move the mouse cursor here to display a very long tooltip");
        document.Pages.Accept(absorber);
        textFragments = absorber.TextFragments;

        foreach (var fragment in textFragments)
        {
            var field = new Aspose.Pdf.Forms.ButtonField(fragment.Page, fragment.Rectangle);
            // Set very long text
            field.AlternateName = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.";
            document.Form.Add(field);
        }

        // Save PDF document
        document.Save(dataDir + "Tooltip_out.pdf");
    }
}
```

{{% alert color="primary" %}}

ツールチップの長さに関して、ツールチップテキストはPDFドキュメント内にPDF文字列タイプとして含まれており、コンテンツストリームの外にあります。このような文字列に対する効果的な制限はPDFファイルにはありません（PDFリファレンス付録Cを参照）。ただし、特定のプロセッサおよび特定のオペレーティング環境で動作する準拠リーダー（例：Adobe Acrobat）には、そのような制限があります。PDFリーダーアプリケーションのドキュメントを参照してください。

{{% /alert %}}

## 隠れたテキストブロックを作成し、マウスオーバーで表示する

Aspose.PDFでは、アクションを隠す機能が実装されており、目に見えないボタンの上でマウスが入る/出るとテキストボックスフィールド（または他のタイプの注釈）を表示/非表示にすることができます。この目的のために、Aspose.Pdf.Annotations.HideActionクラスを使用して、テキストブロックの表示/非表示のアクションを割り当てます。次のコードスニペットを使用して、マウスの入出に応じてテキストブロックを表示/非表示にしてください。

また、ドキュメント内のPDFアクションは準拠リーダー（例：Adobe Reader）では正常に動作しますが、他のPDFリーダー（例：ウェブブラウザプラグイン）には保証がありません。簡単な調査を行い、次のことがわかりました：

- PDFドキュメント内の隠すアクションのすべての実装は、Internet Explorer v.11.0で正常に動作します。
- 隠すアクションのすべての実装もOpera v.12.14で動作しますが、ドキュメントを最初に開くときに応答の遅延が見られます。
- Google Chrome v.61.0でドキュメントを閲覧する場合、フィールド名を受け入れるHideActionコンストラクタを使用した実装のみが機能します。Google Chromeでの閲覧が重要な場合は、対応するコンストラクタを使用してください：

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateHiddenTextBlock()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add paragraph with text
        document.Pages.Add().Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Move the mouse cursor here to display floating text"));
        // Save PDF document
        document.Save(dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf");
    }

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf"))
    {
        // Create TextAbsorber object to find all the phrases matching the regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Move the mouse cursor here to display floating text");
        // Accept the absorber for the document pages
        document.Pages.Accept(absorber);
        // Get the first extracted text fragment
        var textFragments = absorber.TextFragments;
        var fragment = textFragments[1];

        // Create hidden text field for floating text in the specified rectangle of the page
        var floatingField = new Aspose.Pdf.Forms.TextBoxField(fragment.Page, new Aspose.Pdf.Rectangle(100, 700, 220, 740));
        // Set text to be displayed as field value
        floatingField.Value = "This is the \"floating text field\".";
        // We recommend to make field 'readonly' for this scenario
        floatingField.ReadOnly = true;
        // Set 'hidden' flag to make field invisible on document opening
        floatingField.Flags |= Aspose.Pdf.Annotations.AnnotationFlags.Hidden;

        // Setting a unique field name isn't necessary but allowed
        floatingField.PartialName = "FloatingField_1";

        // Setting characteristics of field appearance isn't necessary but makes it better
        floatingField.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
        floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
        floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
        floatingField.Border = new Aspose.Pdf.Annotations.Border(floatingField);
        floatingField.Border.Width = 1;
        floatingField.Multiline = true;

        // Add text field to the document
        document.Form.Add(floatingField);

        // Create invisible button on text fragment position
        var buttonField = new Aspose.Pdf.Forms.ButtonField(fragment.Page, fragment.Rectangle);
        // Create new hide action for specified field (annotation) and invisibility flag
        // (You also may reffer floating field by the name if you specified it above)
        // Add actions on mouse enter/exit at the invisible button field
        buttonField.Actions.OnEnter = new Aspose.Pdf.Annotations.HideAction(floatingField, false);
        buttonField.Actions.OnExit = new Aspose.Pdf.Annotations.HideAction(floatingField);

        // Add button field to the document
        document.Form.Add(buttonField);

        // Save PDF document
        document.Save(dataDir + "CreateHiddenTextBlock_out.pdf");
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