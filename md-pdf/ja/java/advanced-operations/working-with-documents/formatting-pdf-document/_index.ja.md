---

title: PDFドキュメントのフォーマット  
linktitle: PDFドキュメントのフォーマット  
type: docs  
weight: 20  
url: /java/formatting-pdf-document/  
description: Aspose.PDF for JavaでPDFドキュメントをフォーマットします。次のコードスニペットを使用してタスクを解決してください。  
lastmod: "2021-06-05"  

## ドキュメントウィンドウとページ表示プロパティを取得する

このトピックでは、ドキュメントウィンドウ、ビューアアプリケーションのプロパティ、およびページがどのように表示されるかを理解するのに役立ちます。

これらの異なるプロパティを設定するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスを使用してPDFファイルを開きます。これで、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトのメソッドを取得できます。例えば、

- [IsCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – ドキュメントウィンドウを画面の中央に配置します。デフォルト: false。
- [SetDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – 読み順。
 この機能は、ページが並べて表示されるときのレイアウト方法を決定します。デフォルト: 左から右。

- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – ドキュメントのタイトルをドキュメントウィンドウのタイトルバーに表示します。デフォルト: false (タイトルが表示されます)。
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-) – ドキュメントウィンドウのメニューバーを非表示または表示します。デフォルト: false (メニューバーが表示されます)。
- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-) – ドキュメントウィンドウのツールバーを非表示または表示します。デフォルト: false (ツールバーが表示されます)。
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-) – スクロールバーなどのドキュメントウィンドウの要素を非表示または表示します。デフォルト: false (UI要素が表示されます)。

- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-) – ドキュメントが全ページモードで表示されないときにどのように表示されるかを決定します。- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-) – ページレイアウト。
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-) – ドキュメントが最初に開かれたときの表示方法。オプションはサムネイルを表示、全画面、添付ファイルパネルを表示。

次のコードスニペットは、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用してプロパティを取得する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleFormatting {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void GetDocumentWindowAndPageDisplayProperties() {

    // ドキュメントを開く
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 異なるドキュメントプロパティを取得する
    // ドキュメントウィンドウの位置 - デフォルト: false
    System.out.printf("CenterWindow : " + pdfDocument.isCenterWindow());

    // 主な読み取り順序; ページの位置を決定する
    // 並べて表示したとき - デフォルト: L2R
    System.out.printf("Direction :- " + pdfDocument.getDirection());

    // ウィンドウのタイトルバーにドキュメントタイトルを表示するかどうか。
    // falseの場合、タイトルバーはPDFファイル名を表示する - デフォルト: false
    System.out.printf("DisplayDocTitle :- " + pdfDocument.isDisplayDocTitle());

    // ドキュメントウィンドウのサイズを
    // 最初に表示されたページのサイズに合わせてリサイズするかどうか - デフォルト: false
    System.out.printf("FitWindow :- " + pdfDocument.isFitWindow());

    // ビューアアプリケーションのメニューバーを非表示にするかどうか - デフォルト: false
    System.out.printf("HideMenuBar :-" + pdfDocument.isHideMenubar());

    // ビューアアプリケーションのツールバーを非表示にするかどうか - デフォルト: false
    System.out.printf("HideToolBar :-" + pdfDocument.isHideToolBar());

    // スクロールバーのようなUI要素を非表示にして
    // ページの内容のみを表示するかどうか - デフォルト: false
    System.out.printf("HideWindowUI :-" + pdfDocument.isHideWindowUI());

    // ドキュメントのページモード。全画面モードを終了するときの表示方法。
    System.out.printf("NonFullScreenPageMode :-" + pdfDocument.getNonFullScreenPageMode());

    // ページレイアウト、つまりシングルページ、1列
    System.out.printf("PageLayout :-" + pdfDocument.getPageLayout());

    // ドキュメントを開いたときの表示方法。
    System.out.printf("pageMode :-" + pdfDocument.getPageMode());

  }

```

## ドキュメントウィンドウとページ表示プロパティを設定する

このトピックでは、ドキュメントウィンドウ、ビューアアプリケーション、およびページ表示のプロパティを設定する方法を説明します。

これらの異なるプロパティを設定するには:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用してPDFファイルを開きます。
1. Documentオブジェクトのプロパティを設定します。
1. Saveメソッドを使用して更新されたPDFファイルを保存します。

利用可能なプロパティは次のとおりです:

- [setCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setCenterWindow-boolean-)
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-)
- [setDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDisplayDocTitle-boolean-)
- [setFitWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setFitWindow-boolean-)
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-)

- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-)
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-)
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-)
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-)
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-)

次のコードスニペットは、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用してプロパティを設定する方法を示しています。

```java
  public static void SetDocumentWindowAndPageDisplayProperties() {

    // ドキュメントを開く
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    
    // 異なるドキュメントプロパティを設定する
    // ドキュメントウィンドウの位置を指定する - デフォルト: false
    pdfDocument.setCenterWindow(true);
    
    // 主な読み取り順序を指定する; ページの位置を決定する
    // 並べて表示する場合 - デフォルト: L2R
    pdfDocument.setDirection(com.aspose.pdf.Direction.R2L);
    
    // ウィンドウのタイトルバーにドキュメントタイトルを表示するかどうかを指定する
    // falseの場合、タイトルバーにはPDFファイル名が表示される - デフォルト: false
    pdfDocument.setDisplayDocTitle(true);
    
    // ドキュメントウィンドウのサイズを最初に表示されたページのサイズに合わせて
    // リサイズするかどうかを指定する - デフォルト: false
    pdfDocument.setFitWindow(true);
    
    // ビューアアプリケーションのメニューバーを非表示にするかどうかを指定する - デフォルト:
    // false
    pdfDocument.setHideMenubar(true);
    
    // ビューアアプリケーションのツールバーを非表示にするかどうかを指定する - デフォルト:
    // false
    pdfDocument.setHideToolBar(true);
    
    // UI要素（スクロールバーなど）を非表示にして
    // ページの内容だけを表示するかどうかを指定する - デフォルト: false
    pdfDocument.setHideWindowUI(true);
    
    // ドキュメントのページモード。全画面モードを終了したときに
    // ドキュメントをどのように表示するかを指定する
    pdfDocument.setNonFullScreenPageMode(com.aspose.pdf.PageMode.UseOC);
    
    // ページレイアウトを指定する 例: シングルページ、1カラム
    pdfDocument.setPageLayout(com.aspose.pdf.PageLayout.TwoColumnLeft);
    
    // ドキュメントを開くときにどのように表示するかを指定する
    // 例: サムネイルを表示、全画面表示、添付ファイルパネルを表示
    pdfDocument.setPageMode(com.aspose.pdf.PageMode.UseThumbs);
    
    // 更新されたPDFファイルを保存する
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");

  }
```

## 既存のPDFファイルへのフォントの埋め込み

PDFリーダーは、ドキュメントが表示されるプラットフォームに関わらず同じ方法で表示できるように、[14のコアフォント](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts)をサポートしています。PDFにコアフォント以外のフォントが含まれている場合、フォントの置換を避けるためにフォントを埋め込む必要があります。

Aspose.PDF for Javaは、既存のPDFドキュメントへのフォントの埋め込みをサポートしています。完全なフォントまたはサブセットを埋め込むことができます。フォントを埋め込むには：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用して、既存のPDFファイルを開きます。
1. [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) クラスを使用してフォントを埋め込みます。
   1. setEmbedded(true) メソッドは完全なフォントを埋め込みます。
   1. pageFont.isSubset(true) メソッドはフォントのサブセットを埋め込みます。

フォントのサブセットは、使用される文字のみを埋め込み、短い文やスローガンでフォントが使用される場合に便利です。例えば、企業のフォントがロゴに使用されるが、本文には使用されない場合などです。
 ファイルサイズを削減するために、サブセットを使用します。

しかし、本文にカスタムフォントを使用する場合、フォント全体を埋め込んでください。

以下のコードスニペットは、PDFファイルにフォントを埋め込む方法を示しています。
```java
public static void EmbeddingFontsInAnExistingPDFFile() {
    // ドキュメントを開く
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // すべてのページを反復処理
    for (com.aspose.pdf.Page page : (Iterable<com.aspose.pdf.Page>) pdfDocument.getPages()) {
      if (page.getResources().getFonts() != null) {
        for (com.aspose.pdf.Font pageFont : (Iterable<com.aspose.pdf.Font>) page.getResources().getFonts()) {
          // フォントが既に埋め込まれているか確認
          if (!pageFont.isEmbedded())
            pageFont.setEmbedded(true);
        }
      }

      // フォームオブジェクトを確認
      for (com.aspose.pdf.XForm form : (Iterable<com.aspose.pdf.XForm>) page.getResources().getForms()) {
        if (form.getResources().getFonts() != null) {
          for (com.aspose.pdf.Font formFont : (Iterable<com.aspose.pdf.Font>) form.getResources().getFonts()) {
            // フォントが埋め込まれているか確認
            if (!formFont.isEmbedded())
              formFont.setEmbedded(true);
          }
        }
      }
    }
    // 更新されたPDFファイルを保存
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## PDF作成時のフォントの埋め込み

Adobe Readerがサポートする14のコアフォント以外のフォントを使用する必要がある場合、PDFファイルを生成する際にフォントの説明を埋め込む必要があります。フォント情報が埋め込まれていない場合、Adobe Readerはオペレーティングシステムからそれを取得します（システムにインストールされている場合）、またはPDFのフォント記述子に従って代用フォントを構成します。埋め込まれたフォントはホストマシンにインストールされている必要があることに注意してください。以下のコードの場合、「Univers Condensed」フォントがシステムにインストールされています。

フォント情報をPDFファイルに埋め込むために、[Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font)クラスのsetEmbeddedプロパティを使用します。このプロパティの値を‘true’に設定すると、PDFに完全なフォントファイルが埋め込まれ、PDFファイルのサイズが増加することがわかっています。以下はフォント情報をPDFに埋め込むために使用できるコードスニペットです。

```java
public static void EmbeddingFontsWhileCreatingPDF() {

    // 空のコンストラクタを呼び出してPDFオブジェクトをインスタンス化
    com.aspose.pdf.Document document = new com.aspose.pdf.Document();

    // Pdfオブジェクトにセクションを作成
    com.aspose.pdf.Page page = document.getPages().add();

    com.aspose.pdf.TextFragment fragment = new com.aspose.pdf.TextFragment("");

    com.aspose.pdf.TextSegment segment = new com.aspose.pdf.TextSegment(" This is a sample text using Custom font.");
    com.aspose.pdf.TextState ts = new com.aspose.pdf.TextState();
    ts.setFont(FontRepository.findFont("Univers Condensed"));
    ts.getFont().setEmbedded(true);
    segment.setTextState(ts);
    fragment.getSegments().add(segment);
    page.getParagraphs().add(fragment);

    // 更新されたPDFファイルを保存
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## PDFを保存するときのデフォルトフォント名を設定する

PDFドキュメントにフォントが含まれており、そのフォントがドキュメント自体やデバイスに存在しない場合、APIはこれらのフォントをデフォルトフォントに置き換えます。フォントが利用可能な場合（デバイスにインストールされているか、ドキュメントに埋め込まれている場合）、出力PDFは同じフォントを持つべきです（デフォルトフォントに置き換えられるべきではありません）。デフォルトフォントの値にはフォントの名前が含まれている必要があります（フォントファイルへのパスではありません）。PDFとしてドキュメントを保存する際にデフォルトフォント名を設定する機能を実装しました。以下のコードスニペットは、デフォルトフォントを設定するために使用できます。

```java
public static void SetDefaultFontNameWhileSavingPDF() {

    // 既存のPDFドキュメントをロードする
    Document document = new Document("input.pdf");

    String newName = "Arial";

    // PDF形式の保存オプションを初期化する
    PdfSaveOptions ops = new PdfSaveOptions();

    // デフォルトフォント名を設定する
    ops.setDefaultFontName(newName);

    // PDFファイルを保存する
    document.save(_dataDir + "output_out.pdf", ops);
  }
```


## PDFドキュメントからすべてのフォントを取得する

PDFドキュメントからすべてのフォントを取得したい場合、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスで提供されている**Document.getFontUtilities().getAllFonts()**メソッドを使用することができます。既存のPDFドキュメントからすべてのフォントを取得するための次のコードスニペットを確認してください:

```java
public static void GetAllFontsFromPDFDocument() {

    // 既存のPDFドキュメントをロードする
    Document document = new Document(_dataDir + "sample.pdf");

    // ドキュメントからすべてのフォントを取得する
    com.aspose.pdf.Font[] fonts = document.getFontUtilities().getAllFonts();
    for (com.aspose.pdf.Font f : fonts) {
      System.out.println(f.getFontName());
    }
  }
```

## PDFファイルのズーム倍率を取得・設定する

場合によっては、PDFドキュメントのズーム倍率を設定または取得したいことがあります。Aspose.PDFを使用すると、この要件を簡単に達成できます。

[GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction)オブジェクトを使用すると、PDFファイルに関連付けられたズーム値を取得することができます。
 Similarly, it can be used to set a file's Zoom factor.  
同様に、ファイルのズーム係数を設定するために使用できます。

```java
  public static void GetSetZoomFactorOfPDFFile() {
    // 既存のPDFドキュメントをロードする
    Document document = new Document(_dataDir + "sample.pdf");
    double zoom = .5;
    // ドキュメントのズーム係数を設定する
    GoToAction actionzoom = new GoToAction(new XYZExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth(),
        document.getPages().get_Item(1).getMediaBox().getHeight(), zoom));

    // ページ幅に合わせてズームするアクションを設定する
    GoToAction actionFittoWidth = new GoToAction(new FitHExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth()));

    // ページの高さに合わせてズームするアクションを設定する
    GoToAction actionFittoHeight = new GoToAction(new FitVExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getHeight()));

    document.setOpenAction(actionzoom);
    document.setOpenAction(actionFittoWidth);
    document.setOpenAction(actionFittoHeight);
```

以下のコードスニペットは、PDFファイルのズーム係数を取得する方法を示しています。

```java
    // 新しいDocumentオブジェクトをインスタンス化
    Document doc1 = new Document(_dataDir + "Zoomed_actionzoom.pdf");
    // GoToActionオブジェクトを作成
    GoToAction action = (GoToAction) doc1.getOpenAction();
    // PDFファイルのズーム係数を取得
    System.out.println(((XYZExplicitDestination) action.getDestination()).getZoom());

    // 更新されたPDFファイルを保存
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
}
```