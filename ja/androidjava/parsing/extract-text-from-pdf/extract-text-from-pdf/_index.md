---
title: PDF ファイルから生のテキストを抽出する
linktitle: PDF からテキストを抽出する
type: docs
weight: 10
url: /ja/androidjava/extract-text-from-all-pdf/
description: この記事では、Aspose.PDF for Android via Java を使用して PDF ドキュメントからテキストを抽出するさまざまな方法について説明します。ページ全体、特定の部分、列に基づく抽出などがあります。
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF ドキュメントのすべてのページからテキストを抽出する

PDF ドキュメントからテキストを抽出することは一般的な要件です。この例では、Aspose.PDF for Java が PDF ドキュメントのすべてのページからテキストを抽出できる方法を示します。
すべての PDF ページからテキストを抽出するには:

1. オブジェクトを作成します [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) クラス。
1. PDF を開くには [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用し、呼び出します [受け入れる](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) メソッドの [ページ](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) コレクション。
1. この [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) クラスはドキュメントからテキストを吸収し、**Text** プロパティで返します。

次のコードスニペットは、PDFドキュメントのすべてのページからテキストを抽出する方法を示しています。

```java
public static void ExtractFromAllPages() {
        // The path to the documents directory.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // Open document
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // Create TextAbsorber object to extract text
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // Accept the absorber for all the pages
        pdfDocument.getPages().accept(textAbsorber);

        // Get the extracted text
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // Write a line of text to the file
            writer.write(extractedText);
            // Close the stream
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```

## PDFドキュメントからハイライトされたテキストを抽出する

PDFドキュメントからテキストを抽出するさまざまなシナリオにおいて、ハイライトされたテキストのみを抽出するという要件が出てくることがあります。その機能を実装するために、APIに TextMarkupAnnotation.GetMarkedText() と TextMarkupAnnotation.GetMarkedTextFragments() メソッドを追加しました。TextMarkupAnnotation をフィルタリングし、前述のメソッドを使用することで、PDFドキュメントからハイライトされたテキストを抽出できます。以下のコードスニペットは、PDFドキュメントからハイライトされたテキストを抽出する方法を示しています。

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // Loop through all the annotations
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // Filter TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // Retrieve highlighted text fragments
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // Display highlighted text
                    System.out.println(tf.getText());
                }
            }
        }
    }
```

## XML からテキストフラグメントとセグメント要素にアクセスする

XML から生成された PDF 文書を処理する際に、TextFragement または TextSegment アイテムへのアクセスが必要になることがあります。Aspose.PDF for Android via Java は、名前でこれらのアイテムにアクセスする機能を提供します。以下のコードスニペットは、この機能の使用方法を示しています。

  public static void AccessTextFragmentAndSegmentElements() {
        String inXml = "40014.xml";
        Document doc = new Document();
        doc.bindXml(_dataDir + inXml);

        TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
        segment = (TextSegment) doc.getObjectById("strongHtml");

        System.out.println(segment.getText());
        
    }
```

