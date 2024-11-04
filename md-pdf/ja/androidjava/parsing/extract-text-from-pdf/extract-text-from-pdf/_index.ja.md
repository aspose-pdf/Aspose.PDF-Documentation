---
title: PDFファイルから生のテキストを抽出
linktitle: PDFからテキストを抽出
type: docs
weight: 10
url: /androidjava/extract-text-from-all-pdf/
description: この記事では、Java経由でAndroid向けにAspose.PDFを使用してPDFドキュメントからテキストを抽出するさまざまな方法を説明します。全ページから、一部から、列に基づいて、など。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントのすべてのページからテキストを抽出する

PDFドキュメントからテキストを抽出することは一般的な要件です。この例では、Aspose.PDF for Javaを使用してPDFドキュメントのすべてのページからテキストを抽出する方法を紹介します。
すべてのPDFページからテキストを抽出するには：

1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber)クラスのオブジェクトを作成します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用してPDFを開き、[Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) コレクションの [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) メソッドを呼び出します。  
2. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) クラスは、ドキュメントからテキストを吸収し、**Text** プロパティで返します。

次のコードスニペットは、PDFドキュメントのすべてのページからテキストを抽出する方法を示しています。

```java
public static void ExtractFromAllPages() {
        // ドキュメントディレクトリへのパス。

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // ドキュメントを開く
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // テキストを抽出するためにTextAbsorberオブジェクトを作成
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // すべてのページにアブソーバーを適用
        pdfDocument.getPages().accept(textAbsorber);

        // 抽出されたテキストを取得
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // ファイルにテキストの行を書き込む
            writer.write(extractedText);
            // ストリームを閉じる
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```


## PDFドキュメントからハイライトされたテキストを抽出する

PDFドキュメントからテキストを抽出する様々なシナリオで、PDFドキュメントからハイライトされたテキストのみを抽出する必要があるかもしれません。この機能を実装するために、APIにTextMarkupAnnotation.GetMarkedText()およびTextMarkupAnnotation.GetMarkedTextFragments()メソッドを追加しました。TextMarkupAnnotationをフィルタリングし、指定されたメソッドを使用して、PDFドキュメントからハイライトされたテキストを抽出することができます。以下のコードスニペットは、PDFドキュメントからハイライトされたテキストを抽出する方法を示しています。

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // すべての注釈をループする
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // TextMarkupAnnotationをフィルタリングする
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // ハイライトされたテキストフラグメントを取得する
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // ハイライトされたテキストを表示
                    System.out.println(tf.getText());
                }
            }
        }
    }
```


## XMLからテキストフラグメントおよびセグメント要素にアクセスする

時々、XMLから生成されたPDFドキュメントを処理する際に、TextFragmentまたはTextSegment項目にアクセスする必要があります。Aspose.PDF for Android via Javaは、名前によってそのような項目にアクセスする機能を提供します。以下のコードスニペットは、この機能を使用する方法を示しています。

```java
public static void AccessTextFragmentAndSegmentElements() {
    String inXml = "40014.xml";
    Document doc = new Document();
    doc.bindXml(_dataDir + inXml);

    TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
    segment = (TextSegment) doc.getObjectById("strongHtml");

    System.out.println(segment.getText());
}
```