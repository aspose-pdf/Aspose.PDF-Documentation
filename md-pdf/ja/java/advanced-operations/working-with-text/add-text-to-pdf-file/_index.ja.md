---
title: PDFファイルにテキストを追加する
linktitle: PDFファイルにテキストを追加する
type: docs
weight: 10
url: /java/add-text-to-pdf-file/
description: この記事では、Aspose.PDFでのテキスト操作のさまざまな側面について説明します。PDFにテキストを追加する方法、HTMLフラグメントを追加する方法、またはカスタムOTFフォントを使用する方法を学びます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

既存のPDFファイルにテキストを追加するには：

1. Documentオブジェクトを使用して入力PDFを開きます。
2. テキストを追加したい特定のページを取得します。
3. 入力テキストと他のテキストプロパティを使用してTextFragmentオブジェクトを作成します。その特定のページから作成されたTextBuilderオブジェクトを使用すると、AppendTextメソッドを使用してTextFragmentオブジェクトをページに追加できます。
4. DocumentオブジェクトのSaveメソッドを呼び出し、出力PDFファイルを保存します。

## テキストの追加

次のコードスニペットは、既存のPDFファイルにテキストを追加する方法を示しています。

```java
public static void AddingText() {
    // PDFファイルを読み込む
    Document document = new Document(_dataDir + "sample.pdf");

    // 特定のページを取得
    Page pdfPage = document.getPages().get_Item(1);
    // テキストフラグメントを作成
    TextFragment textFragment = new TextFragment("Aspose.PDF");
    textFragment.setPosition(new Position(80, 700));

    // テキストプロパティを設定
    textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
    textFragment.getTextState().setFontSize(14);
    textFragment.getTextState().setForegroundColor(Color.getBlue());
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());

    // TextBuilderオブジェクトを作成
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // テキストフラグメントをPDFページに追加
    textBuilder.appendText(textFragment);

    // 結果のPDFドキュメントを保存します。
    document.save(_dataDir + "AddText_out.pdf");
}
```


## ストリームからフォントを読み込む

以下のコードスニペットは、PDFドキュメントにテキストを追加するときに、ストリームオブジェクトからフォントを読み込む方法を示しています。

```java
import com.aspose.pdf.*;
import com.aspose.pdf.text.FontTypes;

import java.io.FileInputStream;
import java.io.FileNotFoundException;  
//...
public static void LoadingFontFromStream() throws FileNotFoundException{
    
    String fontFile = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf";

    // 入力PDFファイルを読み込む
    Document doc = new Document(_dataDir + "input.pdf");
    // ドキュメントの最初のページ用のテキストビルダーオブジェクトを作成する
    TextBuilder textBuilder = new TextBuilder(doc.getPages().get_Item(1));
    // サンプル文字列を含むテキストフラグメントを作成する
    TextFragment textFragment = new TextFragment("Hello world");
    
    if (fontFile != "")
    {
        // TrueTypeフォントをストリームオブジェクトに読み込む
        FileInputStream fontStream=new FileInputStream(fontFile);            
        // テキスト文字列のフォント名を設定する
        textFragment.getTextState().setFont (FontRepository.openFont(fontStream, FontTypes.TTF));
        // テキストフラグメントの位置を指定する
        textFragment.setPosition(new Position(10, 10));
        // テキストビルダーにテキストを追加して、PDFファイル上に配置できるようにする
        textBuilder.appendText(textFragment);
        
        _dataDir = _dataDir + "LoadingFontFromStream_out.pdf";
    
        // 結果のPDFドキュメントを保存する。
        doc.save(_dataDir); 
    }       
}
```


## TextParagraphを使用してテキストを追加する

以下のコードスニペットは、[TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph)クラスを使用してPDFドキュメントにテキストを追加する方法を示しています。

```java
public static void AddTextUsingTextParagraph() {
    // ドキュメントを開く
    Document doc = new Document();
    // Documentオブジェクトのpagesコレクションにページを追加
    Page page = doc.getPages().add();
    TextBuilder builder = new TextBuilder(page);
    // テキスト段落を作成
    TextParagraph paragraph = new TextParagraph();
    // 次の行のインデントを設定
    paragraph.setSubsequentLinesIndent(20);
    // TextParagraphを追加する位置を指定
    paragraph.setRectangle(new Rectangle(100, 300, 200, 700));
    // 単語の折り返しモードを指定
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    // テキストフラグメントを作成
    TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
    fragment1.getTextState().setFont(FontRepository.findFont("Times New Roman"));
    fragment1.getTextState().setFontSize(12);
    // フラグメントを段落に追加
    paragraph.appendLine(fragment1);
    // 段落を追加
    builder.appendParagraph(paragraph);

    _dataDir = _dataDir + "AddTextUsingTextParagraph_out.pdf";

    // 結果のPDFドキュメントを保存
    doc.save(_dataDir);        
}
```


## テキストセグメントにハイパーリンクを追加

PDF ページは 1 つ以上の TextFragment オブジェクトで構成される場合があり、それぞれの TextFragment オブジェクトは 1 つ以上の TextSegment インスタンスを持つことができます。TextSegment にハイパーリンクを設定するには、Aspose.Pdf.WebHyperlink インスタンスのオブジェクトを提供しながら、TextSegment クラスの Hyperlink プロパティを使用できます。この要件を達成するために、次のコードスニペットを試してください。

```java
public static void AddHyperlinkToTextSegment() {
    // ドキュメントインスタンスを作成する
    Document doc = new Document();
    // PDFファイルのページコレクションにページを追加する
    Page page1 = doc.getPages().add();

    // TextFragment インスタンスを作成する
    TextFragment tf = new TextFragment("サンプル テキスト フラグメント");
    // TextFragment の横方向の配置を設定する
    tf.setHorizontalAlignment(HorizontalAlignment.Right);

    // サンプルテキストでテキストセグメントを作成する
    TextSegment segment = new TextSegment(" ... テキストセグメント 1...");
    // TextFragment のセグメントコレクションにセグメントを追加する
    tf.getSegments().add(segment);

    // 新しい TextSegment を作成する
    segment = new TextSegment("Google へのリンク");
    // TextFragment のセグメントコレクションにセグメントを追加する

    tf.getSegments().add(segment);

    // TextSegment にハイパーリンクを設定する
    segment.setHyperlink(new com.aspose.pdf.WebHyperlink("www.aspose.com"));

    // テキストセグメントの前景色を設定する
    segment.getTextState().setForegroundColor(com.aspose.pdf.Color.getBlue());

    // テキストの書式をイタリックに設定する
    segment.getTextState().setFontStyle(FontStyles.Italic);

    // 別の TextSegment オブジェクトを作成する
    segment = new TextSegment("ハイパーリンクなしのテキストセグメント");

    // TextFragment のセグメントコレクションにセグメントを追加する
    tf.getSegments().add(segment);

    // TextFragment をページオブジェクトの段落コレクションに追加する
    page1.getParagraphs().add(tf);

    _dataDir = _dataDir + "AddHyperlinkToTextSegment_out.pdf";

    // 結果の PDF ドキュメントを保存する
    doc.save(_dataDir);

}
```


## OTFフォントを使用する

Aspose.PDF for Javaは、PDFファイルの内容を作成/操作する際にカスタム/TrueTypeフォントを使用する機能を提供しており、ファイルの内容がデフォルトのシステムフォント以外のフォントで表示されるようにできます。Aspose.PDF for Java 10.4.0のリリースから、Open Typeフォントのサポートが提供されています。

```java
public static void UseOTFFont() {
    // 新しいドキュメントインスタンスを作成
    Document pdfDocument = new Document();
    // PDFファイルのページコレクションにページを追加
    Page page = pdfDocument.getPages().add();
    // サンプルテキストでTextFragmentインスタンスを作成
    TextFragment fragment = new TextFragment("OTFフォントのサンプルテキスト");
    // または、システムディレクトリ内のOTFフォントのパスを指定することもできます
    fragment.getTextState().setFont(FontRepository.openFont("/home/aspose/.fonts/Montserrat-Black.otf"));
    // PDFファイル内にフォントを埋め込むように指定し、ターゲットマシンに特定のフォントが
    // インストールされていない/存在しない場合でも正しく表示されるようにする
    fragment.getTextState().getFont().setEmbedded(true);
    // ページインスタンスの段落コレクションにTextFragmentを追加
    page.getParagraphs().add(fragment);
    // 結果のPDFドキュメントを保存
    pdfDocument.save(_dataDir + "OTFFont_out.pdf");
}
```


## DOMを使用してHTML文字列を追加

Aspose.Pdf.Generator.Textクラスには、IsHtmlTagSupportedというプロパティがあり、これを使うとPDFファイルにHTMLタグ/コンテンツを追加することが可能です。追加されたコンテンツは、単なるテキスト文字列としてではなく、ネイティブのHTMLタグとしてレンダリングされます。Aspose.Pdf名前空間の新しいドキュメントオブジェクトモデル（DOM）で同様の機能をサポートするために、HtmlFragmentクラスが導入されました。

[HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlFragment)インスタンスは、PDFファイル内に配置されるべきHTMLコンテンツを指定するために使用できます。TextFragmentと同様に、HtmlFragmentは段落レベルのオブジェクトであり、Pageオブジェクトの段落コレクションに追加することができます。以下のコードスニペットは、DOMアプローチを使用してPDFファイル内にHTMLコンテンツを配置する手順を示しています。

```java
public static void AddingHtmlString() {
    // Documentオブジェクトをインスタンス化
    Document doc = new Document();
    // PDFファイルのページコレクションにページを追加
    Page page = doc.getPages().add();
    // HTMLコンテンツでHtmlFragmentをインスタンス化
    HtmlFragment title = new HtmlFragment("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");
    // マージン詳細のためにMarginInfoを設定
    MarginInfo Margin = new MarginInfo();
    Margin.setBottom(10);
    Margin.setTop(200);
    // マージン情報を設定
    title.setMargin(Margin);
    // ページの段落コレクションにHTMLフラグメントを追加
    page.getParagraphs().add(title);
    // PDFファイルを保存
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


次のコードスニペットは、HTMLの順序付きリストをドキュメントに追加する手順を示しています：

```java
public static void AddHTMLOrderedListIntoDocuments() {
    // Documentオブジェクトをインスタンス化
    Document doc = new Document();
    // 対応するHTMLフラグメントでHtmlFragmentオブジェクトをインスタンス化
    HtmlFragment t = new HtmlFragment(
            "<div style=\"font-family: sans-serif\"><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul><p>リストの後のテキスト。</p><p>次の行<br/>最後の行</p></div>");
    // Pagesコレクションにページを追加
    Page page = doc.getPages().add();
    // ページ内にHtmlFragmentを追加
    page.getParagraphs().add(t);
    // 結果のPDFファイルを保存
    doc.save(_dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
}
```

TextStateオブジェクトを使用して、次のようにHTML文字列のフォーマットを設定することもできます：

```java
public static void AddHTMLStringFormatting() {
    // Documentオブジェクトをインスタンス化
    Document doc = new Document();
    // PDFファイルのページコレクションにページを追加
    Page page = doc.getPages().add();
    // HTMLコンテンツでHtmlFragmentをインスタンス化
    HtmlFragment title = new HtmlFragment("<h1><strong>HTML文字列のデモ</strong></h1>");
    TextState textState = new TextState(12);
    textState.setFont(FontRepository.findFont("Calibri"));
    textState.setForegroundColor(Color.getGreen());
    textState.setBackgroundColor(Color.getCoral());
    title.setTextState(textState);

    // ページの段落コレクションにHTMLフラグメントを追加
    page.getParagraphs().add(title);
    // PDFファイルを保存
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


以下のコードスニペットは、説明された動作を示しています。

```java
public static void AddHTMLUsingDOMAndOverwrite() {
    // Documentオブジェクトをインスタンス化する
    Document doc = new Document();
    // PDFファイルのページコレクションにページを追加する
    Page page = doc.getPages().add();
    // HTMLコンテンツでHtmlFragmentをインスタンス化する
    HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>表にはテキストが含まれています</i></b></p>");
    // 'Verdana'からフォントファミリーが'Arial'にリセットされます
    title.setTextState(new TextState("Arial Black"));
    title.setTextState(new TextState(20));
    // 下マージン情報を設定する
    title.getMargin().setBottom(10);
    // 上マージン情報を設定する
    title.getMargin().setTop(400);
    // ページの段落コレクションにHTMLフラグメントを追加する
    page.getParagraphs().add(title);
    // PDFファイルを保存する
    doc.save(_dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
}
```


## フットノートとエンドノート (DOM)

フットノートは、連続した上付き番号を使用して論文のテキスト内に注を示します。実際の注はインデントされ、ページの下部にフットノートとして表示されることがあります。

### フットノートの追加

フットノート参照システムでは、参照を次のように示します：

- ソース資料に直接続く行の上に小さな番号を置きます。この番号はノート識別子と呼ばれ、テキスト行の少し上に位置します。
- 同じ番号を、ソースの引用とともにページの下部に置きます。フットノートは数値的かつ年代順に行うべきです：最初の参照は1、2番目は2、という具合です。

フットノートの利点は、読者が関心のある参照の出典を簡単にページの下部で確認できることです。

フットノートを作成するために以下の手順に従ってください：

- Documentインスタンスを作成
- Pageオブジェクトを作成
- TextFragmentオブジェクトを作成

- Noteインスタンスを作成し、その値をTextFragment.FootNoteプロパティに渡す
- ページインスタンスの段落コレクションにTextFragmentを追加

### フットノートのカスタムラインスタイル

次の例は、PDFページの下部にフットノートを追加し、カスタムラインスタイルを定義する方法を示しています。

```java
public static void AddFootNote() {
    // Documentインスタンスを作成
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("デモ");
    t.setFootNote(note);

    // TextFragmentインスタンスを作成
    TextFragment text = new TextFragment("こんにちは世界");
    // TextFragmentにフットノートの値を設定
    text.setFootNote(new Note("テストテキスト1のフットノート"));
    // ドキュメントの最初のページの段落コレクションにTextFragmentを追加
    page.getParagraphs().add(text);
    // 2つ目のTextFragmentを作成
    text = new TextFragment("Aspose.Pdf for Java");
    // 2つ目のテキストフラグメントにフットノートを設定
    text.setFootNote(new Note("テストテキスト2のフットノート"));
    // PDFファイルの段落コレクションに2つ目のテキストフラグメントを追加
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


以下のようにTextStateオブジェクトを使用して脚注ラベル（ノート識別子）のフォーマットを設定できます：

```java
public static void AddCustomFootNoteLabel() {
    // Documentインスタンスを作成
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("デモ");
    t.setFootNote(note);

    // TextFragmentインスタンスを作成
    TextFragment text = new TextFragment("Hello World");
    // TextFragmentに脚注値を設定
    text.setFootNote(new Note("テストテキスト1の脚注"));
    text.getFootNote().setText("21");
    TextState ts = new TextState();
    ts.setForegroundColor(Color.getBlue());
    ts.setFontStyle(FontStyles.Italic);
    text.getFootNote().setTextState(ts);

    // 文書の最初のページの段落コレクションにTextFragmentを追加
    page.getParagraphs().add(text);
    // 2番目のTextFragmentを作成
    text = new TextFragment("Aspose.Pdf for Java");
    // 2番目のテキストフラグメントに脚注を設定
    text.setFootNote(new Note("テストテキスト2の脚注"));
    // PDFファイルの段落コレクションに2番目のテキストフラグメントを追加
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


### フットノートラベルのカスタマイズ

デフォルトでは、フットノート番号は1から始まる増分です。しかし、カスタムのフットノートラベルを設定する必要がある場合があります。この要件を達成するために、以下のコードスニペットを試してください

```java
public static void CustomFootNote_Label() {
    // Documentインスタンスを作成
    Document document = new Document();
    // ページをPDFのページコレクションに追加
    Page page = document.getPages().add();
    // GraphInfoオブジェクトを作成
    GraphInfo graph = new GraphInfo();
    // 線幅を2に設定
    graph.setLineWidth(2);
    // グラフオブジェクトの色を設定
    graph.setColor(Color.getRed());
    // ダッシュ配列の値を3に設定
    graph.setDashArray(new int[] { 3 });
    // ダッシュフェーズの値を1に設定
    graph.setDashPhase(1);
    // ページのフットノートの線スタイルをグラフとして設定
    page.setNoteLineStyle(graph);

    // TextFragmentインスタンスを作成
    TextFragment text = new TextFragment("Hello World");
    // TextFragmentにフットノートの値を設定
    text.setFootNote(new Note("foot note for test text 1"));
    // フットノートのカスタムラベルを指定
    text.getFootNote().setText(" Aspose(2021)");
    // TextFragmentをドキュメントの最初のページの段落コレクションに追加
    page.getParagraphs().add(text);

    document.save(_dataDir + "CustomizeFootNoteLabel_out.pdf");
}
```


## 画像と表を脚注に追加

以前のリリースバージョンでは、脚注のサポートは提供されていましたが、TextFragmentオブジェクトにのみ適用されていました。しかし、Aspose.PDF for Java 10.7.0のリリースから、PDFドキュメント内のテーブル、セルなど他のオブジェクトにも脚注を追加できるようになりました。以下のコードスニペットは、TextFragmentオブジェクトに脚注を追加し、その後、脚注セクションの段落コレクションに画像と表オブジェクトを追加する手順を示しています。

```java
public static void AddingImageAndTableToFootnote() {
    // Documentインスタンスを作成
    Document document = new Document();
    // PDFのページコレクションにページを追加
    Page page = document.getPages().add();
    // TextFragmentインスタンスを作成
    TextFragment text = new TextFragment("Hello World");

    page.getParagraphs().add(text);

    text.setFootNote(new Note());
    Image image = new Image();
    image.setFile(_dataDir + "aspose-logo.jpg");
    image.setFixHeight(20);
    text.getFootNote().getParagraphs().add(image);
    TextFragment footNote = new TextFragment("footnote text");
    footNote.getTextState().setFontSize(20);
    footNote.setInLineParagraph(true);
    text.getFootNote().getParagraphs().add(footNote);
    Table table = new Table();
    table.getRows().add().getCells().add().getParagraphs().add(new TextFragment("Row 1 Cell 1"));
    text.getFootNote().getParagraphs().add(table);

    page.getParagraphs().add(text);

    document.save(_dataDir + "AddImageAndTable_out.pdf");
}
```


## エンドノートの作成方法

エンドノートは、読者が論文の最後の特定の場所を参照して、引用された情報や言葉の出典を確認できるようにするための出典引用です。エンドノートを使用する場合、引用または要約された文や資料の後に上付き数字が付きます。

次の例は、PDFページにエンドノートを追加する方法を示しています。

```java
public static void HowToCreateEndNotes() {
    Document doc = new Document();
    // PDFのページコレクションにページを追加
    Page page = doc.getPages().add();
    // TextFragmentインスタンスを作成
    TextFragment text = new TextFragment("Hello World");
    // TextFragmentに対してFootNoteの値を設定
    text.setEndNote(new Note("サンプルエンドノート"));
    // FootNoteのカスタムラベルを指定
    text.getEndNote().setText(" Aspose(2021)");
    // ドキュメントの最初のページの段落コレクションにTextFragmentを追加
    page.getParagraphs().add(text);
    // PDFファイルを保存
    doc.save(_dataDir + "EndNote.pdf");
}
```


## テキストと画像をインライン段落として

PDF ファイルのデフォルトのレイアウトはフロー レイアウト (左上から右下) です。したがって、PDF ファイルに追加される新しい要素はすべて右下のフローに追加されます。ただし、画像やテキストなど、さまざまなページ要素を同じレベル (次々に) に表示する必要がある場合があります。一つのアプローチとしては、テーブル インスタンスを作成し、両方の要素を個々のセル オブジェクトに追加することができます。ただし、別のアプローチとしてインライン段落を使用することができます。画像とテキストの IsInLineParagraph プロパティを true に設定すると、これらの段落は他のページ要素とインラインで表示されます。

次のコード スニペットは、PDF ファイルにテキストと画像をインライン段落として追加する方法を示しています。

```java
 public static void TextAndImageAsInLineParagraph() {
    // Document インスタンスをインスタンス化
    Document doc = new Document();
    // Document インスタンスのページ コレクションにページを追加
    Page page = doc.getPages().add();
    // TextFragmnet を作成
    TextFragment text = new TextFragment("Hello World.. ");
    // テキスト フラグメントをページ オブジェクトの段落コレクションに追加
    page.getParagraphs().add(text);
    // 画像インスタンスを作成
    Image image = new Image();
    // 画像をインライン段落として設定し、前の段落オブジェクト (TextFragment) の直後に表示されるようにする
    image.setInLineParagraph (true);
    // 画像ファイルのパスを指定
    image.setFile(_dataDir + "aspose-logo.jpg");
    // 画像の高さを設定 (オプション)
    image.setFixHeight(30);
    // 画像の幅を設定 (オプション)
    image.setFixWidth(100);
    // ページ オブジェクトの段落コレクションに画像を追加
    page.getParagraphs().add(image);
    // 異なる内容で TextFragment オブジェクトを再初期化
    text = new TextFragment(" Hello Again..");
    // TextFragment をインライン段落として設定
    text.setInLineParagraph (true);
    // 新しく作成した TextFragment をページの段落コレクションに追加
    page.getParagraphs().add(text);
    
    doc.save(_dataDir+"TextAndImageAsParagraph_out.pdf");
}
```


## テキストを追加する際の文字間隔の指定

テキストは、TextFragmentインスタンスを使用するか、TextParagraphオブジェクトを使用してPDFファイルの段落コレクション内に追加することができます。また、TextStampクラスを使用してPDF内にテキストをスタンプすることもできます。テキストを追加する際、テキストオブジェクトの文字間隔を指定する必要がある場合があります。この要件を達成するために、CharacterSpacingという新しいプロパティが導入されました。この要件を満たすための次のアプローチをご覧ください。

以下のアプローチは、PDFドキュメント内にテキストを追加する際の文字間隔を指定する手順を示しています。

## TextBuilderとTextFragmentを使用

```java
 public static void CharacterSpacing_TextFragment(){
    // Documentインスタンスを作成
    Document pdfDocument = new Document();
    // ページをDocumentのページコレクションに追加
    Page page = pdfDocument.getPages().add();
    // TextBuilderインスタンスを作成
    TextBuilder builder = new TextBuilder(page);
    // サンプルコンテンツでテキストフラグメントインスタンスを作成
    TextFragment wideFragment = new TextFragment("文字間隔が広がったテキスト");
    wideFragment.getTextState().applyChangesFrom(new TextState("Arial", 12));
    // TextFragmentの文字間隔を指定
    wideFragment.getTextState().setCharacterSpacing(2.0f);
    // TextFragmentの位置を指定
    wideFragment.setPosition(new Position(100, 650));
    // TextBuilderインスタンスにTextFragmentを追加
    builder.appendText(wideFragment);        
    // 結果のPDFドキュメントを保存
    pdfDocument.save(_dataDir+ "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
}
```


## TextBuilderとTextParagraphの使用

```java
public static void CharacterSpacing_TextParagraph() {
    // Documentインスタンスを作成
    Document pdfDocument = new Document();
    // ページをDocumentのページコレクションに追加
    Page page = pdfDocument.getPages().add();
    // TextBuilderインスタンスを作成
    TextBuilder builder = new TextBuilder(page);
    // TextParagraphインスタンスをインスタンス化
    TextParagraph paragraph = new TextParagraph();
    // フォント名とサイズを指定するためにTextStateインスタンスを作成
    TextState state = new TextState("Arial", 12);
    // 文字間隔を指定
    state.setCharacterSpacing (1.5f);
    // テキストをTextParagraphオブジェクトに追加
    paragraph.appendLine("これは文字間隔を持つ段落です", state);
    // TextParagraphの位置を指定
    paragraph.setPosition (new Position(100, 550));
    // TextParagraphをTextBuilderインスタンスに追加
    builder.appendParagraph(paragraph);
    // 結果のPDFドキュメントを保存
    pdfDocument.save(_dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
}
```


## テキストスタンプの使用

```java
public static void CharacterSpacing_TextStamp() {
    // Documentインスタンスを作成
    Document pdfDocument = new Document();
    // Documentのページコレクションにページを追加
    Page page = pdfDocument.getPages().add();
    // サンプルテキストでTextStampインスタンスを作成
    TextStamp stamp = new TextStamp("これは文字間隔があるテキストスタンプです");
    // Stampオブジェクトのフォント名を指定
    stamp.getTextState().setFont(FontRepository.findFont("Arial"));
    // TextStampのフォントサイズを指定
    stamp.getTextState().setFontSize(12);
    // 文字間隔を1fとして指定
    stamp.getTextState().setCharacterSpacing (1f);
    // StampのXインデントを設定
    stamp.setXIndent(100);
    // StampのYインデントを設定
    stamp.setYIndent(500);
    // ページインスタンスにテキストスタンプを追加
    stamp.put(page);        
    // 結果のPDFドキュメントを保存
    pdfDocument.save(_dataDir+"CharacterSpacingUsingTextStamp_out.pdf");        
}
```

## マルチカラムPDF文書の作成

雑誌や新聞では、多くの場合、ニュースが単一ページに複数のカラムで表示されており、テキスト段落が左から右に全ページにわたって印刷されている本とは異なります。
 多くのドキュメント処理アプリケーション、例えばMicrosoft WordやAdobe Acrobat Writerは、ユーザーが1つのページに複数の列を作成し、それにデータを追加できるようにします。

Aspose.PDF for Javaも、PDFドキュメントのページ内に複数の列を作成する機能を提供しています。マルチカラムのPDFファイルを作成するために、Aspose.Pdf.FloatingBoxクラスを使用することができます。このクラスは、FloatingBox内の列の数を指定するためのColumnInfo.ColumnCountプロパティを提供しています。また、ColumnInfo.ColumnSpacingおよびColumnInfo.ColumnWidthsプロパティを使用して、列間の間隔や列の幅を指定することもできます。FloatingBoxはドキュメントオブジェクトモデル内の要素であり、相対的な位置指定（例えば、テキスト、グラフ、画像など）と比較して、配置があいまいである可能性があることに注意してください。
列間隔とは、列間のスペースを指し、デフォルトの列間隔は1.25cmです。列の幅が指定されていない場合、Aspose.PDF for Javaはページサイズと列間隔に従って各列の幅を自動的に計算します。

以下の例は、Graphsオブジェクト（Line）を使用して2列を作成し、それらをFloatingBoxの段落コレクションに追加し、さらにPageインスタンスの段落コレクションに追加する方法を示しています。

```java
public static void CreateMultiColumn() {
    Document doc = new Document();
    // PDFファイルの左マージン情報を指定
    doc.getPageInfo().getMargin().setLeft(40);
    
    // PDFファイルの右マージン情報を指定
    doc.getPageInfo().getMargin().setRight(40);
    
    Page page = doc.getPages().add();

    com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500, 2);
    
    // 線をセクションオブジェクトの段落コレクションに追加
    page.getParagraphs().add(graph1);

    // 線の座標を指定
    float[] posArr = new float[] { 1, 2, 500, 2 };
    com.aspose.pdf.drawing.Line l1 = new com.aspose.pdf.drawing.Line(posArr);
    graph1.getShapes().add(l1);
    
    // HTMLタグを含むテキストで文字列変数を作成
    String s = "<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">"
                +"<strong> How to Steer Clear of money scams</<strong> </span>";
    
    // HTMLテキストを含むテキスト段落を作成

    HtmlFragment heading_text = new HtmlFragment(s);
    page.getParagraphs().add(heading_text);

    FloatingBox box = new FloatingBox();
    
    // セクションに4つの列を追加
    box.getColumnInfo().setColumnCount(2);
    // 列間の間隔を設定
    box.getColumnInfo().setColumnSpacing("5");

    box.getColumnInfo().setColumnWidths("105 105");
    TextFragment text1 = new TextFragment("By A Googler (The Official Google Blog)");
    text1.getTextState().setFontSize (8);
    text1.getTextState().setLineSpacing (2);
    text1.getTextState().setFontSize (10);
    text1.getTextState().setFontStyle (FontStyles.Italic);

    box.getParagraphs().add(text1);
    
    // 線を描くためのグラフオブジェクトを作成
    com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50, 10);
    // 線の座標を指定
    float[] posArr2 = new float[] { 1, 10, 100, 10 };
    com.aspose.pdf.drawing.Line l2 = new com.aspose.pdf.drawing.Line(posArr2);
    graph2.getShapes().add(l2);

    // 線をセクションオブジェクトの段落コレクションに追加
    box.getParagraphs().add(graph2);

    TextFragment text2 = new TextFragment("Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. "
    +"Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue."
    +"Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur "
    +"ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean "
    +"posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. "
    +"Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, "
    +"risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam "
    +"luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, "
    +"sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, "
    +"pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,"
    +"iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus "
    +"mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla."
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,"
    +"iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique"
    +"ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
    +"Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. "
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box.getParagraphs().add(text2);

    page.getParagraphs().add(box);

    // PDFファイルを保存
    doc.save(_dataDir + "CreateMultiColumnPdf_out.pdf");        
}
```


## カスタムタブストップの使用

タブストップは、タブの停止点です。ワードプロセッシングでは、各行に一定間隔で配置された複数のタブストップがあります（例えば、半インチごと）。しかし、ほとんどのワードプロセッサはタブストップを任意の場所に設定できるため、変更することができます。Tabキーを押すと、カーソルまたは挿入ポイントが次のタブストップにジャンプしますが、それ自体は見えません。タブストップはテキストファイルには存在しませんが、ワードプロセッサはそれらを追跡し、Tabキーに正しく反応できるようにしています。

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) は、開発者がPDFドキュメントでカスタムタブストップを使用できるようにします。Aspose.Pdf.Text.TabStopクラスは、[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) クラスでカスタムタブストップを設定するために使用されます。

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) には、列挙体としていくつかの事前定義されたタブリーダータイプも用意されています。TabLeaderTypeの事前定義された値とその説明は以下の通りです。

|**タブリーダータイプ**|**説明**|
| :- | :- |
|None|タブリーダーなし|
|Solid|ソリッドタブリーダー|
|Dash|ダッシュタブリーダー|
|Dot|ドットタブリーダー|

ここでは、カスタムTABストップを設定する方法の例を示します。

```java
public static void CustomTabStops() {
    Document pdfdocument = new Document();
    Page page = pdfdocument.getPages().add();

    com.aspose.pdf.TabStops ts = new com.aspose.pdf.TabStops();
    com.aspose.pdf.TabStop ts1 = ts.add(100);
    ts1.setAlignmentType(TabAlignmentType.Right);
    ts1.setLeaderType (TabLeaderType.Solid);
    
    com.aspose.pdf.TabStop ts2 = ts.add(200);
    ts2.setAlignmentType(TabAlignmentType.Center);
    ts2.setLeaderType (TabLeaderType.Dash);

    com.aspose.pdf.TabStop ts3 = ts.add(300);
    ts3.setAlignmentType(TabAlignmentType.Left);
    ts3.setLeaderType (TabLeaderType.Dot);

    TextFragment header = new TextFragment("これはTABストップでテーブルを形成する例です", ts);
    TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data22 "));
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data23"));

    page.getParagraphs().add(header);
    page.getParagraphs().add(text0);
    page.getParagraphs().add(text1);
    page.getParagraphs().add(text2);
    
    pdfdocument.save(_dataDir + "CustomTabStops_out.pdf"); 
}
```


## PDFに透過テキストを追加する方法

PDFファイルには、画像、テキスト、グラフ、添付ファイル、注釈オブジェクトが含まれ、TextFragmentを作成する際に、前景色、背景色の情報やテキストの書式設定を設定できます。Aspose.PDF for Javaは、アルファカラーチャネルを使ったテキストの追加をサポートしています。以下のコードスニペットは、透過色でテキストを追加する方法を示しています。

```java
  public static void AddTransparentText() {
    // Documentインスタンスを作成
    Document pdfdocument = new Document();
    // PDFファイルのページコレクションにページを作成
    Page page = pdfdocument.getPages().add();

    // Graphオブジェクトを作成
    Graph canvas = new Graph(100, 400);
    // 特定の寸法でRectangleインスタンスを作成
    com.aspose.pdf.drawing.Rectangle rect = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
    // アルファカラーチャネルからColorオブジェクトを作成
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;
    Color alphaColor = Color.fromArgb(alpha, red, green, blue);
    rect.getGraphInfo().setFillColor(alphaColor);
    // Graphオブジェクトのshapesコレクションに長方形を追加
    canvas.getShapes().add(rect);
    // ページオブジェクトのparagraphsコレクションにgraphオブジェクトを追加
    page.getParagraphs().add(canvas);
    // Graphオブジェクトの位置を変更しないように設定
    canvas.setChangePosition(false);

    // サンプル値でTextFragmentインスタンスを作成
    TextFragment text = new TextFragment(
            "透明テキスト 透明テキスト 透明テキスト 透明テキスト 透明テキスト 透明テキスト 透明テキスト 透明テキスト 透明テキスト 透明テキスト 透明テキスト 透明テキスト 透明テキスト 透明テキスト 透明テキスト 透明テキスト ");
    // アルファチャネルからColorオブジェクトを作成
    alpha = 30;
    alphaColor = Color.fromArgb(alpha, red, green, blue);
    // テキストインスタンスのカラー情報を設定
    text.getTextState().setForegroundColor (alphaColor);
    // ページインスタンスのparagraphsコレクションにテキストを追加
    page.getParagraphs().add(text);
    
    pdfdocument.save(_dataDir + "AddTransparentText_out.pdf");
}
```


## フォントの行間を指定する

すべてのフォントには抽象的な四角形があり、その高さは同じフォントサイズでの行間距離を意図しています。この四角形は `em square` と呼ばれ、グリフのアウトラインが定義されるデザイングリッドです。入力フォントの多くの文字には、フォントの `em square` の境界外に配置されたポイントがあります。そのため、フォントを正しく表示するには、特別な設定の使用が必要です。オブジェクト TextFragment は、[TextState.getFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#getFormattingOptions--) メソッドを介してアクセス可能なテキストフォーマットオプションのセットを持っています。このメソッドは [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) クラスを返します。
 このクラスには、特定のフォント（例：入力フォント "HPSimplified.ttf"）用に設計された列挙 [LineSpacingMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions.LineSpacingMode) があります。また、クラス [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) には、LineSpacingMode 型のメソッド [setLineSpacing](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions#setLineSpacing-int-) があります。単に LineSpacing を LineSpacingMode.FullSize に設定する必要があります。フォントを正しく表示するためのコードスニペットは次のようになります:

```java
public static void SpecifyLineSpacingForFonts() {
    String fontFile = _dataDir + "hp-simplified.ttf";
    // 入力PDFファイルを読み込む
    Document doc = new Document();
    // LineSpacingMode.FullSizeでTextFormattingOptionsを作成
    TextFormattingOptions formattingOptions = new TextFormattingOptions();
    formattingOptions.setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);

    // ドキュメントの最初のページ用にテキストビルダーオブジェクトを作成
    // TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
    // サンプル文字列でテキストフラグメントを作成
    TextFragment textFragment = new TextFragment("Hello world");

    // TrueType フォントをストリームオブジェクトに読み込む
    FileInputStream fontStream;
    try {
        fontStream = new FileInputStream(fontFile);
    } catch (FileNotFoundException e) {
        e.printStackTrace();
        return;
    }

    // テキスト文字列にフォント名を設定
    textFragment.getTextState().setFont(FontRepository.openFont(fontStream, FontTypes.TTF));
    // テキストフラグメントの位置を指定
    textFragment.setPosition(new Position(100, 600));
    // 現在のフラグメントのTextFormattingOptionsを事前定義されたものに設定
    // （LineSpacingMode.FullSizeを指す）
    textFragment.getTextState().setFormattingOptions(formattingOptions);
    // PDFファイル上に配置できるようにテキストをTextBuilderに追加
    // textBuilder.AppendText(textFragment);
    Page page = doc.getPages().add();
    page.getParagraphs().add(textFragment);

    // 結果のPDFドキュメントを保存
    doc.save(_dataDir + "SpecifyLineSpacing_out.pdf");
}
```

## テキスト幅を動的に取得する

時には、テキスト幅を動的に取得する必要があります。Aspose.PDF for Java には、文字列の幅を測定するための2つのメソッドが含まれています。com.aspose.pdf.Font または com.aspose.pdf.TextState クラス（またはその両方）の [MeasureString](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState#measureString--) メソッドを呼び出すことができます。以下のコードスニペットは、この機能の使用方法を示しています。

```java
public static void GetTextWidthDynamicaly() {
    Font font = FontRepository.findFont("Arial");
    TextState ts = new TextState();
        ts.setFont(font);
        ts.setFontSize(14);
        if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001)
            System.out.println("予期しないフォント文字列測定!");

        if (Math.abs(ts.measureString("z") - 7.0) > 0.001)
        System.out.println("予期しないフォント文字列測定!");

        for (char c = 'A'; c <= 'z'; c++)
        {
            double fnMeasure = font.measureString(String.valueOf(c), 14);
            double tsMeasure = ts.measureString(String.valueOf(c));

            if (Math.abs(fnMeasure - tsMeasure) > 0.001)
                System.out.println("フォントと状態の文字列測定が一致しません!");
        }
}
```