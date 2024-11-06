---
title: PDFドキュメントを操作する
linktitle: PDFドキュメントを操作する
type: docs
weight: 30
url: ja/java/manipulate-pdf-document/
description: 本記事には、PDF A規格に対するPDFドキュメントの検証方法、目次の操作方法、PDFの有効期限の設定方法、およびPDFファイル生成の進捗を確認する方法に関する情報が含まれています。
lastmod: "2021-06-05"
---

## PDF A規格 (A 1AおよびA 1B) に対するPDFドキュメントの検証

PDF/A-1aまたはPDF/A-1bの互換性を検証するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスの [validate(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#validate-java.io.OutputStream-int-) メソッドを使用します。このメソッドでは、結果を保存するファイル名と、必要な検証タイプ [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat) 列挙: PDF_A_1A または PDF_A_1B を指定することができます。

出力XMLフォーマットはカスタムAsposeフォーマットです。
 XMLには、Problemという名前のタグのコレクションが含まれています。各タグには特定の問題の詳細が含まれています。ProblemタグのObjectID属性は、この問題が関連する特定のオブジェクトのIDを表します。Clause属性はPDF仕様の対応するルールを表します。

```java
  public static void ValidatePDFDocumentForPDF_A_Standard() {
    // ドキュメントを開く
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // PDFをPDF/A-1aに対して検証する
    pdfDocument.validate(_dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);

    // 更新されたPDFファイルを保存する
    // document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```
## 目次の操作

### 既存のPDFに目次を追加する

aspose.pdfパッケージのListSectionクラスを使用すると、PDFドキュメントをゼロから作成するときに目次を作成できます。目次の要素である見出しを追加するには、[aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading)クラスを使用します。

既存のPDFファイルに目次を追加するには、com.aspose.pdfパッケージの[Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading)クラスを使用します。 com.aspose.pdf パッケージは、新しいPDFファイルの作成と既存のPDFファイルの操作の両方が可能です。既存のPDFに目次を追加するには、com.aspose.pdf パッケージを使用します。

次のコードスニペットは、既存のPDFファイル内に目次を作成する方法を示しています。

```java
public static void AddTOCtoExistingPDF() {
    // 既存のPDFファイルをロード
    Document document = new Document(_dataDir + "sample.pdf");

    // PDFファイルの最初のページにアクセス
    Page tocPage = document.getPages().insert(1);

    // 目次情報を表すオブジェクトを作成
    com.aspose.pdf.TocInfo tocInfo = new com.aspose.pdf.TocInfo();
    com.aspose.pdf.TextFragment title = new com.aspose.pdf.TextFragment("目次");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(com.aspose.pdf.FontStyles.Bold);

    // 目次のタイトルを設定
    tocInfo.setTitle(title);
    tocPage.setTocInfo(tocInfo);

    // 目次要素として使用される文字列オブジェクトを作成
    String[] titles = new String[4];
    titles[0] = "最初のページ";
    titles[1] = "2ページ目";
    titles[2] = "3ページ目";
    titles[3] = "4ページ目";
    for (int i = 0; i < 4; i++) {
      // 見出しオブジェクトを作成
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(1);

      com.aspose.pdf.TextSegment segment2 = new com.aspose.pdf.TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);

      // 見出しオブジェクトの対象ページを指定
      heading2.setDestinationPage(document.getPages().get_Item(i + 2));

      // 対象ページ
      heading2.setTop(document.getPages().get_Item(i + 2).getRect().getHeight());

      // 対象座標
      segment2.setText(titles[i]);

      // 目次を含むページに見出しを追加
      tocPage.getParagraphs().add(heading2);
    }
    // 更新されたドキュメントを保存
    document.save("TOC_Output_Java.pdf");
  }
```
### 異なるTOCレベルに異なるTabLeaderTypeを設定する

Aspose.PDFは、異なるTOCレベルに異なるTabLeaderTypeを設定することも可能です。以下のように、FormatArrayのLineDashプロパティにTabLeaderType列挙の適切な値を設定する必要があります。

```java
  public static void SetDifferentTabLeaderTypeForTOCLevels() {

    String outFile = "TOC.pdf";

    Document document = new Document();
    Page tocPage = document.getPages().add();

    TocInfo tocInfo = new TocInfo();

    // リーダータイプを設定

    tocInfo.setLineDash(TabLeaderType.Solid);

    TextFragment title = new TextFragment("目次");
    title.getTextState().setFontSize(30);
    tocInfo.setTitle(title);

    // Pdfドキュメントのセクションコレクションにリストセクションを追加

    tocPage.setTocInfo(tocInfo);

    // 各レベルの左マージンとテキストフォーマット設定を設定することにより4レベルリストの形式を定義

    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setLeft(0);
    tocInfo.getFormatArray()[0].getMargin().setRight(30);
    tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
    tocInfo.getFormatArray()[1].getMargin().setLeft(10);
    tocInfo.getFormatArray()[1].getMargin().setRight(30);
    tocInfo.getFormatArray()[1].setLineDash(TabLeaderType.None);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
    tocInfo.getFormatArray()[2].getMargin().setLeft(20);
    tocInfo.getFormatArray()[2].getMargin().setRight(0);
    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
    tocInfo.getFormatArray()[3].getMargin().setLeft(30);
    tocInfo.getFormatArray()[3].getMargin().setRight(30);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    // Pdfドキュメントにセクションを作成
    Page page = document.getPages().add();

    // セクションに4つの見出しを追加
    for (int Level = 1; Level <= 4; Level++) {
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(Level);
      TextSegment segment2 = new TextSegment();

      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      heading2.setTocPage(tocPage);

      segment2.setText("サンプル見出し" + Level);
      heading2.getTextState().setFont(FontRepository.findFont("Arial UnicodeMS"));

      // 目次に見出しを追加。
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }

    // PDFを保存
    document.save(outFile);
  }
```

### 目次のページ番号を非表示にする

目次に見出しと一緒にページ番号を表示したくない場合は、[TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) クラスの [IsShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/TocInfo) プロパティを false に設定することができます。次のコードスニペットを確認して、目次のページ番号を非表示にする方法を確認してください:

```java
public static void HidePageNumbersInTOC() {
    String outFile = _dataDir + "HiddenPageNumbers_out.pdf";
    Document doc = new Document();
    Page tocPage = doc.getPages().add();
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("目次");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.setTitle(title);

    // Pdf ドキュメントのセクションコレクションにリストセクションを追加する
    tocPage.setTocInfo(tocInfo);

    // 各レベルの左マージンとテキストフォーマット設定を設定して、4レベルのリストの形式を定義する

    tocInfo.setShowPageNumbers(false);
    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setRight(0);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);

    tocInfo.getFormatArray()[1].getMargin().setLeft(30);
    tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);

    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    Page page = doc.getPages().add();

    // セクションに4つの見出しを追加する
    for (int Level = 1; Level != 5; Level++) {
      Heading heading2 = new Heading(Level);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      segment2.setText("これはレベル " + Level + " の見出しです");
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }
    doc.save(_dataDir + outFile);
  }
```


### TOCを追加する際のページ番号のカスタマイズ

PDFドキュメントにTOCを追加する際、TOC内のページ番号をカスタマイズすることは一般的です。例えば、ページ番号の前にP1、P2、P3などのプレフィックスを追加する必要があるかもしれません。そのような場合、Aspose.PDF for JavaはTocInfoクラスのPageNumbersPrefixプロパティを提供しており、以下のコードサンプルに示すようにページ番号をカスタマイズできます。

```java
  public static void CustomizePageNumbersWhileAddingTOC() {

    String inFile = _dataDir + "sample.pdf";
    String outFile = _dataDir + "42824_out.pdf";

    // 既存のPDFファイルを読み込む
    Document doc = new Document(inFile);
    // PDFファイルの最初のページにアクセス
    Page tocPage = doc.getPages().insert(1);
    // TOC情報を表すオブジェクトを作成
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("目次");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);

    // TOCのタイトルを設定
    tocInfo.setTitle(title);
    tocInfo.setPageNumbersPrefix("P");
    tocPage.setTocInfo(tocInfo);

    for (int i = 1; i < doc.getPages().size(); i++) {
      // 見出しオブジェクトを作成
      Heading heading2 = new Heading(1);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      // 見出しオブジェクトの宛先ページを指定
      heading2.setDestinationPage(doc.getPages().get_Item(i + 1));
      // 宛先ページ
      heading2.setTop(doc.getPages().get_Item(i + 1).getRect().getHeight());
      // 宛先座標
      segment2.setText("ページ " + i);
      // TOCを含むページに見出しを追加
      tocPage.getParagraphs().add(heading2);
    }

    // 更新されたドキュメントを保存
    doc.save(outFile);
  }
```


## PDFファイルにレイヤーを追加する

レイヤーはPDFドキュメントでさまざまな方法で使用できます。多言語ファイルを配布したい場合、各言語のテキストを異なるレイヤーに表示させ、背景デザインを別のレイヤーに表示させることができます。また、アニメーションを別のレイヤーに表示させるドキュメントを作成することもできます。例として、ファイルに使用許諾契約書を追加し、ユーザーが契約条件に同意するまでコンテンツを表示したくない場合があります。

Aspose.PDF for Javaは、PDFファイルにレイヤーを追加することをサポートしています。

PDFファイルでレイヤーを操作するには、次のAPIメンバーを使用します。

[Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) クラスはレイヤーを表し、次のプロパティを含みます：

- **Name** – レイヤーの名前。
- **Id** – レイヤーのID。
- **Contents** – レイヤーオペレーターのリスト。

[Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) オブジェクトが定義されたら、それらを[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) オブジェクトのLayersコレクションに追加します。
 以下のコードは、PDFドキュメントにレイヤーを追加する方法を示しています。

```java
public static void AddLayersToPDFFile() {
    Document doc = new Document();
    Page page = doc.getPages().add();
    Layer layer = new Layer("oc1", "赤い線");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(1, 0, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 700));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 700));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.setLayers(new ArrayList<Layer>());
    page.getLayers().add(layer);
    layer = new Layer("oc2", "緑の線");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 1, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 750));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 750));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    layer = new Layer("oc3", "青い線");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 0, 1));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 800));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 800));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    doc.save("output.pdf");
  
```
## PDFの有効期限を設定する

PDFの有効期限機能は、PDFファイルがどれだけの期間有効であるかを設定します。特定の日付に誰かがアクセスしようとすると、ファイルが期限切れであり、新しいものが必要であることを説明するポップアップが表示されます。

Aspose.PDFを使用すると、PDFファイルの作成と編集時に有効期限を設定できます。

以下のコードスニペットは、PDFファイルの有効期限を設定する方法を示しています。サードパーティコンポーネント（例: OwnerGuard）によって保存されたファイルは、そのユーティリティなしでは他のワークステーションで表示できないため、JavaScriptを使用する必要があります。

PDFファイルは、既存のファイルと有効期限を使用してPDF OwnerGuardを使用して作成できます。ただし、新しいファイルはPDF OwnerGuardがインストールされているワークステーションでのみ開くことができます。PDF OwnerGuardがインストールされていないワークステーションでは、ExpirationFeatureErrorが発生します。例えば、OwnerGuardがインストールされている場合はPDF Readerがファイルを開きますが、Adobe Acrobatはエラーを返します。

```java
  public static void SetPDFExpiration() {
    Document document = new Document(_dataDir+"sample.pdf");    
    JavascriptAction javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" + 
      "expiry = new Date(year, month);" + 
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('The file is expired. You need a new one.');"
      );
    document.setOpenAction(javaScript);
    document.save(_dataDir + "JavaScript-Added.pdf");
  }
```