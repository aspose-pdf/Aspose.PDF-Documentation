---
title: PDFでテキストを置換する 
linktitle: PDFでテキストを置換する
type: docs
weight: 40
url: /ja/java/replace-text-in-a-pdf-document/
description: PDFからテキストを置換および削除するさまざまな方法について学びます。Aspose.PDFは、特定の領域内または正規表現でテキストを置換することを可能にします。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントの全ページでテキストを置換する

{{% alert color="primary" %}}

Aspose.PDFを使用してドキュメント内のテキストを検索して置換し、この[リンク](https://products.aspose.app/pdf/redaction)で結果をオンラインで確認できます。

{{% /alert %}}

[Aspose.PDF for Java](https://products.aspose.com/pdf/java)を使用してPDFドキュメントの全ページでテキストを置換するには：

1. まず、[TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber)を使用して、置換される特定のフレーズを見つけます。

1. 次に、すべての[TextFragments](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber#getTextFragments--)を確認し、テキストを置き換えて他の属性を変更します。
1. 最後に、Documentクラスの[save](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--)メソッドを使用して、出力PDFを保存します。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleReplaceText {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void ReplaceTextOnAllPages() {
        Document pdfDocument = new Document(_dataDir+"sample.pdf");

        // 入力された検索フレーズのすべてのインスタンスを見つけるためにTextAbsorberオブジェクトを作成
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Web");
        
        // ドキュメントの最初のページにアブソーバーを適用
        pdfDocument.getPages().accept(textFragmentAbsorber);
        
        // 抽出されたテキストフラグメントをコレクションに取得
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
        
        // フラグメントをループ処理
        for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
            // テキストとその他のプロパティを更新
            textFragment.setText("World Wide Web");
            textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getBlue());
            textFragment.getTextState().setBackgroundColor(Color.getGray());
        }
        // 更新されたPDFファイルを保存
        pdfDocument.save(_dataDir+"Updated_Text.pdf");
    }
}
```


## 特定のページ領域のテキストを置換する

特定のページ領域のテキストを置換するためには、まず `TextFragmentAbsorber` オブジェクトをインスタンス化し、[TextSearchOptions.setRectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions#setRectangle-com.aspose.pdf.Rectangle-) を使用してページ領域を指定し、すべての `TextFragment` を反復してテキストを置換する必要があります。これらの操作が完了したら、Document オブジェクトの `save` メソッドを使用して出力 PDF を保存するだけです。

以下のコードスニペットは、PDF ドキュメントのすべてのページのテキストを置換する方法を示しています。

```java
public static void ReplaceTextInParticularRegion(){
    // PDFファイルをロード
    Document pdfDocument = new Document(_dataDir+"sample.pdf");

    // TextFragmentAbsorberオブジェクトをインスタンス化
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("PDF");

    // ページ境界内でテキストを検索
    textFragmentAbsorber.getTextSearchOptions().setLimitToPageBounds(true);

    // TextSearchOptionsのページ領域を指定
    textFragmentAbsorber.getTextSearchOptions().setRectangle(new Rectangle(100, 700, 400, 770));

    // PDFファイルの最初のページからテキストを検索
    pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);

    // 個々のTextFragmentを反復
    for(TextFragment tf : textFragmentAbsorber.getTextFragments())
    {
        // テキストを "---" に置換
        tf.setText("---");
    }

    // 更新されたPDFファイルを保存
    pdfDocument.save(_dataDir+"Updated_Text.pdf");
}
```


## 正規表現に基づいてテキストを置換する

正規表現に基づいていくつかのフレーズを置換したい場合、まず特定の正規表現に一致するすべてのフレーズをTextFragmentAbsorberを使用して見つける必要があります。TextFragmentAbsorberのコンストラクタに正規表現をパラメータとして渡す必要があります。また、正規表現が使用されているかどうかを指定するTextSearchOptionsオブジェクトを作成する必要があります。TextFragmentsで一致するフレーズを取得したら、それらをすべてループして必要に応じて更新する必要があります。最後に、DocumentオブジェクトのSaveメソッドを使用して更新されたPDFを保存する必要があります。

以下のコードスニペットは、正規表現に基づいてテキストを置換する方法を示しています。

```java
public static void ReplaceTextWithRegularExpression() {
    // PDFファイルを読み込む
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // 入力された検索フレーズのすべてのインスタンスを見つけるためにTextAbsorberオブジェクトを作成
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); 
    // 例: 1999-2000

    // 正規表現の使用を指定するためにテキスト検索オプションを設定
    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

    // ドキュメントの最初のページに対してアブソーバーを適用
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // 抽出されたテキストフラグメントをコレクションに取得
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // フラグメントをループ
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // テキストとその他のプロパティを更新
        textFragment.setText("ABCD-EFGH");
        textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }

    // 更新されたPDFファイルを保存
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


## 既存のPDFファイルのフォントを置き換える

Aspose.PDF for Javaは、PDF文書内のテキストを置き換える機能をサポートしています。しかし、PDF文書内で使用されているフォントのみを置き換える必要がある場合もあります。この場合、テキストを置き換えるのではなく、使用されているフォントのみが置き換えられます。TextFragmentAbsorberコンストラクタのオーバーロードの1つは、TextEditOptionsオブジェクトを引数として受け取り、TextEditOptions.FontReplace列挙のRemoveUnusedFonts値を使用して要件を達成できます。

次のコードスニペットは、PDF文書内のフォントを置き換える方法を示しています。

```java
public static void ReplaceFonts() {
    // Documentオブジェクトをインスタンス化
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // テキストフラグメントを検索し、編集オプションとして未使用のフォントを削除するように設定
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(
            new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

    // 文書のすべてのページに対してアブソーバーを適用
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // すべてのTextFragmentをトラバース
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection)
    {
        String fontName = textFragment.getTextState().getFont().getFontName();
        // フォント名がArialMTの場合、フォント名をArialに置き換え
        if (fontName.equals("ArialMT")) {
            textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        }
    }

    // 更新されたPDFファイルを保存
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


### 非英語（日本語）のフォントを使用してテキストを置換する

以下のコードスニペットは、日本語の文字でテキストを置換する方法を示しています。日本語のテキストを追加するには、日本語の文字をサポートするフォントを使用する必要があることに注意してください（例：MSGothic）。

```java
public static void UseNonEnglishFontWhenReplacingText() {

    // Documentオブジェクトをインスタンス化
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // "page"という単語を日本語の特定のフォントで置き換える
    // OSにインストールされている可能性のあるTakaoMincho
    // または、他の象形文字をサポートするフォントでも良い
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("page");

    // Text Searchオプションのインスタンスを作成
    TextSearchOptions searchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(searchOptions);

    // ドキュメントのすべてのページに対してアブソーバーを受け入れる
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // 抽出されたテキストフラグメントをコレクションに取得
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    
    // フラグメントをループ処理
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // テキストとその他のプロパティを更新
        textFragment.setText("ファイル");
        textFragment.getTextState().setFont(FontRepository.findFont("MSGothic"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }
    // 更新されたドキュメントを保存
    pdfDocument.save(_dataDir + "Japanese_Text.pdf");
}
```


## テキストの置換によりページコンテンツが自動的に再配置されるべき

Aspose.PDF for Javaは、PDFファイル内のテキストを検索して置換する機能をサポートしています。しかし、最近では、特定のTextFragmentがより小さい内容で置換された場合に、生成されたPDFに余分なスペースが表示されたり、TextFragmentがより長い文字列で置換された場合に、既存のページ内容に重なったりする問題に遭遇したお客様がいました。そのため、PDFドキュメント内のテキストが置換された後に内容が再配置されるメカニズムを導入する必要がありました。

上記のシナリオに対応するために、Aspose.PDF for Javaは強化され、PDFファイル内のテキストを置換する際にそのような問題が発生しないようになりました。以下のコードスニペットは、PDFファイル内のテキストを置換し、ページコンテンツが自動的に再配置される方法を示しています。

```java
public static void RearrangeContent() {
    // ソースPDFファイルを読み込む
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 正規表現を使用してTextFragment Absorberオブジェクトを作成
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[PDF,Web]");

    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
    
    // 現在の行が置換後に長すぎたり短すぎたりする場合、次の行または現在の行にテキストを折り返すためにReplaceAdjustment.WholeWordsHyphenationオプションを指定することもできます:
    // textFragmentAbsorber.getTextReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.WholeWordsHyphenation);

    // ドキュメントのすべてのページに対してアブソーバーを受け入れる
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // 抽出されたテキストフラグメントをコレクションに取得
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // 各TextFragmentを置換
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // 置換されるテキストフラグメントのフォントを設定
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        // フォントサイズを設定
        textFragment.getTextState().setFontSize(10);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
        // プレースホルダーよりも大きな文字列でテキストを置換
        textFragment.setText("This is a larger string for the testing of this feature");
    }
    // 結果のPDFを保存
    pdfDocument.save(_dataDir + "RearrangeContentsUsingTextReplacement_out.pdf");
}
```


## PDF 作成中の置換可能なシンボルのレンダリング

置換可能なシンボルは、実行時に対応するコンテンツに置き換えることができるテキスト文字列内の特別なシンボルです。現在、Aspose.PDF 名前空間の新しいドキュメントオブジェクトモデルでサポートされている置換可能なシンボルは、`$P`、`$p`、`\n`、`\r` です。`$p` と `$P` は、実行時のページ番号処理に使用されます。`$p` は現在の Paragraph クラスが存在するページの番号に置き換えられます。`$P` はドキュメント内の総ページ数に置き換えられます。PDF ドキュメントのパラグラフコレクションに [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) を追加する場合、テキスト内の改行をサポートしていません。ただし、改行を含むテキストを追加するには、[TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph) を使用した [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) を使用してください。

- 単一の "\n" の代わりに TextFragment で "\r\n" または Environment.NewLine を使用します。
- TextParagraph オブジェクトを作成します。
 それは行分割でテキストを追加します。
- TextParagraph.AppendLineでTextFragmentを追加します。
- TextBuilder.AppendParagraphでTextParagraphを追加します。

```java
public static void RenderingReplaceableSymbols() {
    // PDFファイルをロード
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    Page page = pdfDocument.getPages().add();

    // 必要な改行マーカーを含むテキストで新しいTextFragmentを初期化
    TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");

    // 必要に応じてテキストフラグメントのプロパティを設定
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());

    // TextParagraphオブジェクトを作成
    TextParagraph par = new TextParagraph();

    // 新しいTextFragmentを段落に追加
    par.appendLine(textFragment);

    // 段落の位置を設定
    par.setPosition (new Position(100, 600));

    // TextBuilderオブジェクトを作成
    TextBuilder textBuilder = new TextBuilder(page);
    // TextBuilderを使用してTextParagraphを追加
    textBuilder.appendParagraph(par);

    _dataDir = _dataDir + "RenderingReplaceableSymbols_out.pdf";
    pdfDocument.save(_dataDir);
}
```

## ヘッダー/フッター領域の置換可能なシンボル

置換可能なシンボルは、PDFファイルのヘッダー/フッターセクション内にも配置できます。フッターセクションに置換可能なシンボルを追加する方法の詳細については、次のコードスニペットを参照してください。

```java
public static void ReplaceableSymbolsInHeaderFooterArea() {
    Document doc = new Document();
    Page page = doc.getPages().add();

    MarginInfo marginInfo = new MarginInfo();
    marginInfo.setTop(90);
    marginInfo.setBottom(50);
    marginInfo.setLeft(50);
    marginInfo.setRight(50);

    // マージン情報インスタンスをsec1.PageInfoのMarginプロパティに割り当てる
    page.getPageInfo().setMargin(marginInfo);

    HeaderFooter hfFirst = new HeaderFooter();
    page.setHeader(hfFirst);
    hfFirst.getMargin().setLeft(50);
    hfFirst.getMargin().setRight(50);

    // ヘッダーとして表示するコンテンツを格納するテキスト段落をインスタンス化する
    TextFragment t1 = new TextFragment("レポートタイトル");
    t1.getTextState().setFont(FontRepository.findFont("Arial"));
    t1.getTextState().setFontSize(16);
    t1.getTextState().setForegroundColor(Color.getBlack());
    t1.getTextState().setFontStyle(FontStyles.Bold);
    t1.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t1.getTextState().setLineSpacing(5f);
    hfFirst.getParagraphs().add(t1);

    TextFragment t2 = new TextFragment("レポート名");
    t2.getTextState().setFont(FontRepository.findFont("Arial"));
    t2.getTextState().setForegroundColor(Color.getBlack());
    t2.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t2.getTextState().setLineSpacing(5f);
    t2.getTextState().setFontSize(12);
    hfFirst.getParagraphs().add(t2);

    // セクションのHeaderFooterオブジェクトを作成する
    HeaderFooter hfFoot = new HeaderFooter();

    // HeaderFooterオブジェクトを奇数および偶数のフッターに設定する
    page.setFooter(hfFoot);
    hfFoot.getMargin().setLeft(50);
    hfFoot.getMargin().setRight(50);

    // 現在のページ番号と総ページ数を含むテキスト段落を追加する
    TextFragment t3 = new TextFragment("テスト日付に生成");
    TextFragment t4 = new TextFragment("レポート名");
    TextFragment t5 = new TextFragment("ページ $p / $P");

    // テーブルオブジェクトをインスタンス化する
    Table tab2 = new Table();

    // テーブルを目的のセクションの段落コレクションに追加する
    hfFoot.getParagraphs().add(tab2);

    // テーブルの列幅を設定する
    tab2.setColumnWidths("165 172 165");

    // テーブルに行を作成し、その行にセルを作成する
    Row row3 = tab2.getRows().add();

    row3.getCells().add();
    row3.getCells().add();
    row3.getCells().add();

    // テキストの垂直方向の配置を中央揃えに設定する
    row3.getCells().get_Item(0).setAlignment(HorizontalAlignment.Left);
    row3.getCells().get_Item(1).setAlignment(HorizontalAlignment.Center);
    row3.getCells().get_Item(2).setAlignment(HorizontalAlignment.Right);

    row3.getCells().get_Item(0).getParagraphs().add(t3);
    row3.getCells().get_Item(1).getParagraphs().add(t4);
    row3.getCells().get_Item(2).getParagraphs().add(t5);

    Table table = new Table();

    table.setColumnWidths("33% 33% 34%");
    table.setDefaultCellPadding(new MarginInfo());
    table.getDefaultCellPadding().setTop(10);
    table.getDefaultCellPadding().setBottom(10);

    // テーブルを目的のセクションの段落コレクションに追加する
    page.getParagraphs().add(table);

    // BorderInfoオブジェクトを使用してデフォルトのセルボーダーを設定する
    table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));

    // 別のカスタマイズされたBorderInfoオブジェクトを使用してテーブルボーダーを設定する
    table.setBorder(new BorderInfo(BorderSide.All, 1f));

    table.setRepeatingRowsCount(1);

    // テーブルに行を作成し、その行にセルを作成する
    Row row1 = table.getRows().add();

    row1.getCells().add("col1");
    row1.getCells().add("col2");
    row1.getCells().add("col3");
    String CRLF = "\r\n";

    for (int i = 0; i <= 10; i++) {
        Row row = table.getRows().add();
        row.setRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            Cell c1;
            if (c == 2)
                c1 = row.getCells().add(
                        "Aspose.Total for Javaは、Asposeが提供するすべてのJavaコンポーネントを集めたものです。"
                                + CRLF
                                + "最新バージョンが含まれていることを保証するために、日々コンパイルされています。"
                                + CRLF
                                + "最新バージョンが含まれていることを保証するために、日々コンパイルされています。"
                                + CRLF
                                + "Aspose.Total for Javaを使用することで、開発者はさまざまなアプリケーションを作成できます。");
            else
                c1 = row.getCells().add("アイテム1" + c);
            c1.setMargin(new MarginInfo());
            c1.getMargin().setLeft(30);
            c1.getMargin().setTop(10);
            c1.getMargin().setBottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```


## PDFドキュメントからすべてのテキストを削除

### 演算子を使用してすべてのテキストを削除

テキスト操作の中には、PDFドキュメントからすべてのテキストを削除する必要がある場合があり、そのためには通常、見つかったテキストを空の文字列値として設定します。多くのテキスト断片のテキストを変更することは、多くのチェックとテキスト位置調整操作を引き起こします。これらはテキスト編集のシナリオでは不可欠です。問題は、ループで処理されるシナリオで、削除されるテキスト断片がいくつあるかを判断できないことです。

したがって、PDFページからすべてのテキストを削除するシナリオには、別のアプローチを使用することをお勧めします。非常に高速に動作する次のコードスニペットを考慮してください。

```java
public static void RemoveAllTextUsingOperators() {
    // ドキュメントを開く
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // PDFドキュメントのすべてのページをループする
    for (int i = 1; i <= pdfDocument.getPages().size(); i++) {
        Page page = pdfDocument.getPages().get_Item(i);
        OperatorSelector operatorSelector = new OperatorSelector(new com.aspose.pdf.operators.TextShowOperator());
        // ページ上のすべてのテキストを選択
        page.getContents().accept(operatorSelector);
        // すべてのテキストを削除
        page.getContents().delete(operatorSelector.getSelected());
    }
    // ドキュメントを保存
    pdfDocument.save(_dataDir + "RemoveAllText_out.pdf");
}
```