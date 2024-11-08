---
title: PDF内のテキストフォーマット 
linktitle: PDF内のテキストフォーマット 
type: docs
weight: 30
url: /ja/java/text-formatting-inside-pdf/
description: このページでは、PDFファイル内のテキストをフォーマットする方法を説明します。行インデントの追加、テキスト境界線の追加、下線付きテキストの追加、追加されたテキストの周囲に境界線を追加、フローティングボックス内容のテキスト配置などがあります。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFに行インデントを追加する方法

Aspose.PDF for Javaは、[TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) クラスにSubsequentLinesIndentプロパティを提供しています。このプロパティを使用して、TextFragmentとParagraphsコレクションを使用したPDF生成シナリオで行インデントを指定できます。

次のコードスニペットを使用してプロパティを使用してください:

```java
public static void AddLineIndentToPDF() {
        // 新しいドキュメントオブジェクトを作成
        Document document = new Document();
        Page page = document.getPages().add();

        TextFragment text = new TextFragment(
                "A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

        // テキストフラグメントのTextFormattingOptionsを初期化し、
        // SubsequentLinesIndent値を指定
        TextFormattingOptions textOptions = new TextFormattingOptions();
        textOptions.setSubsequentLinesIndent(20);
        text.getTextState().setFormattingOptions(textOptions);

        page.getParagraphs().add(text);

        text = new TextFragment("Line2");
        page.getParagraphs().add(text);

        text = new TextFragment("Line3");
        page.getParagraphs().add(text);

        text = new TextFragment("Line4");
        page.getParagraphs().add(text);

        text = new TextFragment("Line5");
        page.getParagraphs().add(text);

        document.save(_dataDir + "SubsequentIndent_out.pdf");
    }
```


## テキストボーダーの追加方法

次のコードスニペットは、TextBuilderを使用してテキストにボーダーを追加し、TextStateのDrawTextRectangleBorderメソッドを設定する方法を示しています：

```java
public static void AddTextBorder() {
    // 新しいドキュメントオブジェクトを作成
    Document pdfDocument = new Document();
    // 特定のページを取得
    Page pdfPage = pdfDocument.getPages().add();
    // テキストフラグメントを作成
    TextFragment textFragment = new TextFragment("main text");
    textFragment.setPosition(new Position(100, 600));
    // テキストのプロパティを設定
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());
    // テキストの矩形の周囲にボーダー（ストローク）を描画するためにsetStrokingColorを使用
    textFragment.getTextState().setStrokingColor (Color.getDarkRed());
    // setDrawTextRectangleBorderメソッドを使用して値をtrueに設定
    textFragment.getTextState().setDrawTextRectangleBorder(true);
    TextBuilder tb = new TextBuilder(pdfPage);
    tb.appendText(textFragment);
    // ドキュメントを保存
    pdfDocument.save(_dataDir + "PDFWithTextBorder_out.pdf");
}
```


## テキストに下線を追加する方法

次のコードスニペットは、新しいPDFファイルを作成する際にテキストに下線を追加する方法を示しています。

```java
public static void AddUnderlineText(){
    // ドキュメントオブジェクトの作成
    Document pdfDocument = new Document();
    // PDFドキュメントにページを追加
    Page page = pdfDocument.getPages().add();
    // 最初のページのためのTextBuilderの作成
    TextBuilder tb = new TextBuilder(page);
    // サンプルテキストを含むTextFragment
    TextFragment fragment = new TextFragment("Text with underline decoration");
    // TextFragmentのフォントを設定
    fragment.getTextState().setFont (FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize (10);
    // テキストの書式を下線として設定
    fragment.getTextState().setUnderline(true);
    // TextFragmentを配置する位置を指定
    fragment.setPosition (new Position(10, 800));
    // TextFragmentをPDFファイルに追加
    tb.appendText(fragment);

    // 生成されたPDFドキュメントを保存
    pdfDocument.save(_dataDir + "AddUnderlineText_out.pdf");
}
```


## 追加したテキストの周りに枠線を追加する方法

追加したテキストの外観を制御できます。以下の例は、追加したテキストの周りに長方形を描くことによって枠線を追加する方法を示しています。[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) クラスについて詳しく知る。

```java
public static void AddBorderAroundAddedText() {
    PdfContentEditor editor = new PdfContentEditor();
    editor.bindPdf(_dataDir + "input.pdf");
    LineInfo lineInfo = new LineInfo();
    lineInfo.setLineWidth(2);
    lineInfo.setVerticeCoordinate (new float[] { 0, 0, 100, 100, 50, 100 });
    lineInfo.setVisibility(true);
    editor.createPolygon(lineInfo, 1, new java.awt.Rectangle(0, 0, 0, 0), "");

    // 結果のPDF文書を保存します。
    editor.save(_dataDir + "AddingBorderAroundAddedText_out.pdf");
}
```

## 改行を追加する方法

TextFragmentはテキスト内での改行をサポートしていません。
 しかし、改行付きのテキストを追加するには、TextParagraphを使用してTextFragmentを使用してください：

- 単一の「\n」の代わりに、TextFragmentで「\r\n」またはEnvironment.NewLineを使用します。
- TextParagraphオブジェクトを作成します。これにより、テキストが行分割されて追加されます。
- TextParagraph.AppendLineでTextFragmentを追加します。
- TextBuilder.AppendParagraphでTextParagraphを追加します。
以下のコードスニペットを使用してください。

```java
public static void AddNewLineFeed() {        
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    // 新しいTextFragmentを、必要な改行マーカーを含むテキストで初期化
    TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");

    // 必要に応じてテキストフラグメントのプロパティを設定
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());

    // TextParagraphオブジェクトを作成
    TextParagraph par = new TextParagraph();

    // 新しいTextFragmentを段落に追加
    par.appendLine(textFragment);

    // 段落の位置を設定
    par.setPosition(new Position(100, 600));

    // TextBuilderオブジェクトを作成
    TextBuilder textBuilder = new TextBuilder(page);
    // TextBuilderを使用してTextParagraphを追加
    textBuilder.appendParagraph(par);

    // 結果のPDFドキュメントを保存
    pdfDocument.save(_dataDir + "AddNewLineFeed_out.pdf");
}
```

## StrikeOutテキストの追加方法

TextStateクラスは、PDFドキュメント内に配置されるTextFragmentsの書式設定を行う機能を提供します。このクラスを使用して、テキストの書式を太字、イタリック、下線に設定することができ、このリリースから、APIはテキストの書式を打ち消し線としてマークする機能を提供しています。以下のコードスニペットを使用して、打ち消し線の書式設定を持つTextFragmentを追加してみてください。

完全なコードスニペットを使用してください：

```java
public static void AddStrikeOutText(){
    // ドキュメントを開く
    Document pdfDocument = new Document();
    // 特定のページを取得
    Page pdfPage = (Page)pdfDocument.getPages().add();

    // テキストフラグメントを作成
    TextFragment textFragment = new TextFragment("main text");
    textFragment.setPosition (new Position(100, 600));

    // テキストのプロパティを設定
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());
    // setStrikeOutメソッドを使用して打ち消し線を有効にする
    textFragment.getTextState().setStrikeOut(true);
    // テキストを太字としてマーク
    textFragment.getTextState().setFontStyle(FontStyles.Bold);

    // TextBuilderオブジェクトを作成
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // テキストフラグメントをPDFページに追加
    textBuilder.appendText(textFragment);

    // 結果のPDFドキュメントを保存
    pdfDocument.save(_dataDir + "AddStrikeOutText_out.pdf");        
}
```


## テキストにグラデーションシェーディングを適用する

テキストフォーマットは、テキスト編集シナリオのためにAPIでさらに強化され、PDFドキュメント内でパターンカラースペースを持つテキストを追加できるようになりました。`com.aspose.pdf.Color` クラスは、新しいメソッド `setPatternColorSpace` を導入することでさらに強化されており、テキストのシェーディングカラーを指定するために使用できます。この新しいメソッドは、以下のコードスニペットに示されているように、テキストに異なるグラデーションシェーディング（例えば、軸方向シェーディング、放射状（タイプ3）シェーディング）を追加します。

```java
public static void ApplyGradientShading() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("always print correctly");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));

    // パターンカラースペースを持つ新しいカラーを作成
    textFragment.getTextState().setForegroundColor(foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```


ラジアルグラデーションを適用するには、上記のコードスニペットで `setPatternColorSpace` メソッドを `GradientRadialShading(startingColor, endingColor)` と等しく設定します。

```java
public static void ApplyGradientShadingRadial() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("常に正しく印刷されます");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));

    // パターンカラースペースを持つ新しい色を作成
    textFragment.getTextState().setForegroundColor(foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```

## テキストをフロートコンテンツに整列させる方法

Aspose.PDF は、Floating Box 要素内のコンテンツのテキスト整列を設定することをサポートしています。
 Aspose.Pdf.FloatingBox インスタンスの配置プロパティを使用して、次のコードサンプルに示すようにこれを達成できます。

```java
public static void AlignTextToFloatContent() {
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    FloatingBox floatBox = new FloatingBox(100, 100);
    floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
    floatBox.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
    floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
    
    page.getParagraphs().add(floatBox);

    FloatingBox floatBox1 = new FloatingBox(100, 100);
    floatBox1.setVerticalAlignment(VerticalAlignment.Center);
    floatBox1.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox1.getParagraphs().add(new TextFragment("FloatingBox_center"));
    floatBox1.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox1);

    FloatingBox floatBox2 = new FloatingBox(100, 100);
    floatBox2.setVerticalAlignment(VerticalAlignment.Top);
    floatBox2.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox2.getParagraphs().add(new TextFragment("FloatingBox_top"));
    floatBox2.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox2);

    pdfDocument.save(_dataDir + "FloatingBox_alignment_review_out.pdf");        
}
```