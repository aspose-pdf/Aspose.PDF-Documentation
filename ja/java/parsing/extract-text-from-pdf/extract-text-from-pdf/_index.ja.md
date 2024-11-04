---
title: PDFファイルから生のテキストを抽出する
linktitle: PDFからテキストを抽出する
type: docs
weight: 10
url: /java/extract-text-from-all-pdf/
description: この記事では、Aspose.PDF for Javaを使用してPDFドキュメントからテキストを抽出するさまざまな方法について説明します。全ページから、特定の部分から、列に基づいて、など。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントのすべてのページからテキストを抽出する

PDFドキュメントからテキストを抽出することは一般的な要件です。この例では、Aspose.PDF for JavaがPDFドキュメントのすべてのページからテキストを抽出する方法を示します。
すべてのPDFページからテキストを抽出するには:

1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) クラスのオブジェクトを作成します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用してPDFを開き、[Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) コレクションの [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) メソッドを呼び出します。
1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) クラスはドキュメントからテキストを吸収し、**Text** プロパティで返します。

以下のコードスニペットは、PDFドキュメントのすべてのページからテキストを抽出する方法を示しています。

```java
public static void ExtractFromAllPages(){
    // ドキュメントディレクトリへのパス
    String _dataDir = "/home/admin1/pdf-examples/Samples/";
    String filePath = _dataDir + "ExtractTextAll.pdf";

    // ドキュメントを開く
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // テキストを抽出するためにTextAbsorberオブジェクトを作成
    com.aspose.pdf.TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();
    
    // すべてのページに対してアブソーバーを受け入れる
    pdfDocument.getPages().accept(textAbsorber);
    
    // 抽出されたテキストを取得
    String extractedText = textAbsorber.getText();                
    try {
        java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
        // ファイルにテキストの行を書き込み
        writer.write(extractedText);            
        // ストリームを閉じる
        writer.close();
    } catch (java.io.IOException e) {
        e.printStackTrace();
    }

}
```


## ページからテキストを抽出する方法（テキストデバイスを使用）

**TextDevice** クラスを使用して、PDFファイルからテキストを抽出できます。TextDeviceは、その実装において [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) を使用しています。したがって、実際には同じことを行いますが、TextDeviceはページから何かを抽出するための「デバイス」アプローチを統一するために実装されています（ImageDevice、PageDeviceなど）。TextAbsorberはページ、PDF全体、またはXFormからテキストを抽出することができ、このTextAbsorberはより汎用的です。

### すべてのページからテキストを抽出する

次の手順とコードスニペットは、テキストデバイスを使用してPDFからテキストを抽出する方法を示しています。

1. 入力PDFファイルを指定してDocumentクラスのオブジェクトを作成する
2. TextDeviceクラスのオブジェクトを作成する
3. TextExtractOptionsクラスのオブジェクトを使用して抽出オプションを指定する
4. TextDeviceクラスのProcessメソッドを使用して内容をテキストに変換する
5. テキストを出力ファイルに保存する

```java
public static void extractTextFromAllPagesOfPDF() throws IOException {
    // ドキュメントを開く
    Document pdfDocument = new Document("input.pdf");
    // 抽出されたテキストが保存されるテキストファイル
    java.io.OutputStream text_stream = new java.io.FileOutputStream("ExtractedText.txt", false);
    // PDFファイルのすべてのページを反復処理する
    for (Page page : (Iterable<Page>) pdfDocument.getPages()) {
        // テキストデバイスを作成する
        TextDevice textDevice = new TextDevice();
        // テキスト抽出オプションを設定する - テキスト抽出モードを設定する（RawまたはPure）
        TextExtractionOptions textExtOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Raw);
        textDevice.setExtractionOptions(textExtOptions);
        // PDFのページからテキストを取得し、それをOutputStreamオブジェクトに保存する
        textDevice.process(page, text_stream);
    }
    // ストリームオブジェクトを閉じる
    text_stream.close();
}
```


## 特定のページ領域からテキストを抽出

[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) クラスは、PDFドキュメントの特定のページまたはすべてのページからテキストを抽出する機能を提供します。このクラスは抽出されたテキストを**Text**プロパティに返します。しかし、特定のページ領域からテキストを抽出する必要がある場合は、[TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions) の**Rectangle**プロパティを使用することができます。Rectangleプロパティは値としてRectangleオブジェクトを取り、このプロパティを使用して、テキストを抽出する必要があるページの領域を指定できます。

ページの[Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) メソッドは、テキストを抽出するために呼び出されます。
 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) と [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) クラスのオブジェクトを作成します。**Document** オブジェクトの個々のページ、**Page** インデックスに対して [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) メソッドを呼び出します。**Index** はテキストを抽出する必要がある特定のページ番号です。[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) クラスの **Text** プロパティからテキストを取得できます。以下のコードスニペットは、個々のページからテキストを抽出する方法を示しています。

```java
public static void ExtractTextFromParticularPageRegion(String[] args) throws IOException {
    // ドキュメントを開く
    Document doc = new Document("page_0001.pdf");
    // テキストを抽出するための TextAbsorber オブジェクトを作成
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // 最初のページに対してアブソーバーを受け入れる
    doc.getPages().get_Item(1).accept(absorber);
    // 抽出されたテキストを取得
    String extractedText = absorber.getText();
    // ライターを作成してファイルを開く
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // 抽出された内容を書き込む
    writer.write(extractedText);
    // ライターを閉じる
    writer.close();
}
```

## カラムに基づいてテキストを抽出

PDFファイルは、テキスト、画像、注釈、添付ファイル、グラフなどの要素で構成される場合があり、Aspose.PDF for .NETはこれらすべての要素を追加および操作する機能を提供します。このAPIはPDFドキュメントからのテキストの追加と抽出において非常に優れており、PDFドキュメントが複数のカラム（マルチカラム）で構成されている場合に、そのレイアウトを維持しながらページ内容を抽出する必要があるというシナリオに遭遇することがあります。その場合、Aspose.PDF for .NETはこの要件を達成するための適切な選択です。一つのアプローチは、PDFドキュメント内の内容のフォントサイズを縮小し、それからテキスト抽出を実行することです。以下のコードスニペットは、テキストサイズを縮小し、それからPDFドキュメントからテキストを抽出しようとする手順を示しています。

```java
public static void ExtractTextBasedOnColumns() throws IOException {
    // ドキュメントを開く
    Document doc = new Document("page_0001.pdf");
    // テキストを抽出するためにTextAbsorberオブジェクトを作成
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // 最初のページにアブソーバーを受け入れる
    doc.getPages().get_Item(1).accept(absorber);
    // 抽出されたテキストを取得
    String extractedText = absorber.getText();
    // ライターを作成し、ファイルを開く
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // 抽出された内容を書き込む
    writer.write(extractedText);
    // ライターを閉じる
    writer.close();
}
```


### セカンドアプローチ - スケールファクターの使用

この新しいリリースでは、TextAbsorberと内部テキストフォーマットメカニズムにいくつかの改善を導入しました。そのため、‘Pure’モードを使用したテキスト抽出中に、ScaleFactorオプションを指定することができ、これは上記のアプローチに加えて、マルチカラムPDFドキュメントからテキストを抽出する別の方法となります。このスケールファクターは、テキスト抽出中の内部テキストフォーマットメカニズムに使用するグリッドを調整するために設定することができます。ScaleFactorの値を1から0.1（0.1を含む）の間で指定すると、フォント縮小と同じ効果があります。

ScaleFactor の値を 0.1 から -0.1 の間に指定すると、ゼロ値として扱われますが、これによりテキスト抽出時に必要なスケールファクターを自動で計算するアルゴリズムが作動します。この計算は、ページ上で最も一般的なフォントの平均グリフ幅に基づいていますが、抽出されたテキストで列の文字列が次の列の開始に達しないことを保証することはできません。ScaleFactor の値が指定されていない場合、デフォルト値の 1.0 が使用されます。これは、スケーリングが行われないことを意味します。指定された ScaleFactor の値が 10 を超えるか -0.1 未満の場合、デフォルト値の 1.0 が使用されます。

We propose the usage of auto-scaling (ScaleFactor = 0) when processing a large number of PDF files for text content extraction. Or manually set redundant reducing of grid width ( about ScaleFactor = 0.5). However, you must not determine whether scaling is necessary for concrete documents or not. If You set redundant reducing of grid width for the document (that doesn't need in it), the extracted text content will remain fully adequate. Please take a look at the following code snippet.

大規模なPDFファイルを処理する際のテキストコンテンツ抽出には、オートスケーリング（ScaleFactor = 0）の使用を提案します。または、グリッド幅を冗長に削減する（ScaleFactor = 0.5程度）を手動で設定します。ただし、具体的なドキュメントに対してスケーリングが必要かどうかを判断してはいけません。ドキュメントに対してグリッド幅の冗長な削減を設定した場合（それが必要でない場合）、抽出されたテキストコンテンツは完全に適切なままです。次のコードスニペットをご覧ください。

```java
public static void usingSetScaleFactorMethod() {
    Document pdfDocument = new Document("inputFile.pdf");
    TextAbsorber textAbsorber = new TextAbsorber();
    textAbsorber.setExtractionOptions(new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure));
    // Setting scale factor to 0.5 is enough to split columns in the majority of documents
    // Setting of zero allows to algorithm choose scale factor automatically
    textAbsorber.getExtractionOptions().setScaleFactor((double) 0.5);
    pdfDocument.getPages().accept(textAbsorber);
    String extractedText = textAbsorber.getText();
}
```


{{% alert color="primary" %}}

新しいScaleFactorと手動でフォントを縮小した以前の係数の間に直接対応はありません。ただし、デフォルトでは、内部的な理由で既に縮小されたフォントサイズの値が考慮されます。例えば、フォントサイズを10から7に縮小することは、スケールファクターを5/8（= 0.625）に設定するのと同じ効果があります。

{{% /alert %}}

## PDFドキュメントからハイライトされたテキストを抽出

PDFドキュメントからテキストを抽出するさまざまなシナリオで、PDFドキュメントからハイライトされたテキストのみを抽出する必要が出てくることがあります。この機能を実装するために、APIにTextMarkupAnnotation.GetMarkedText()とTextMarkupAnnotation.GetMarkedTextFragments()メソッドを追加しました。TextMarkupAnnotationをフィルタリングし、これらのメソッドを使用してPDFドキュメントからハイライトされたテキストを抽出することができます。以下のコードスニペットは、PDFドキュメントからハイライトされたテキストを抽出する方法を示しています。

```java
public static void ExtractHighlightedText() {
    Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
    // すべての注釈をループする
    for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations())
    {
        // TextMarkupAnnotationをフィルタリングする
        if (annotation.getAnnotationType()==AnnotationType.Highlight)
        {
            HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
            // ハイライトされたテキストフラグメントを取得する
            TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
            for (TextFragment tf : collection)
            {
                // ハイライトされたテキストを表示する
                System.out.println(tf.getText());
            }
        }
    }        
}
```


## XMLからテキストフラグメントとセグメント要素にアクセスする

時々、XMLから生成されたPDFドキュメントを処理する際に、TextFragementまたはTextSegmentアイテムにアクセスする必要があります。Aspose.PDF for .NETは、このようなアイテムに名前でアクセスできるようにします。以下のコードスニペットは、この機能を使用する方法を示しています。

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