---
title: PDFドキュメントのフォーマット 
linktitle: PDFドキュメントのフォーマット
type: docs
weight: 20
url: /ja/php-java/formatting-pdf-document/
description: Aspose.PDF for PHP via Javaを使用してPDFドキュメントをフォーマットします。タスクを解決するために次のコードスニペットを使用してください。
lastmod: "2024-06-05"
---

## ドキュメントウィンドウとページ表示プロパティを取得する

このトピックでは、ドキュメントウィンドウのプロパティ、ビューアアプリケーション、およびページの表示方法を理解するのに役立ちます。

これらの異なるプロパティを設定するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスを使用してPDFファイルを開きます。これで、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトのメソッドを取得できます。例えば、

- [isCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – ドキュメントウィンドウを画面の中央に配置します。デフォルト: false。
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – 読み取り順序。
 このオプションは、ページが並べて表示されるときの配置方法を決定します。デフォルト: 左から右。
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – ドキュメントウィンドウのタイトルバーにドキュメントタイトルを表示します。デフォルト: false (タイトルが表示されます)。
- [isHideMenubar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideMenubar--) – ドキュメントがアクティブなときにメニューバーを非表示にするかどうかを指定するフラグを取得します。
- [isHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideToolBar--) – ドキュメントがアクティブなときにツールバーを非表示にするかどうかを指定するフラグを取得します。
- [isHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideWindowUI--) – ドキュメントがアクティブなときにユーザーインターフェース要素を非表示にするかどうかを指定するフラグを取得します。

- [getNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getNonFullScreenPageMode--) – 全画面モードを終了するときにドキュメントを表示する方法を指定するページモードを取得します。- [getPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageLayout--) – ページレイアウト。
- [getPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageMode--) – ページモードを取得し、ドキュメントが開かれたときにどのように表示されるべきかを指定します。

次のコードスニペットは、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用してプロパティを取得する方法を示しています。

```php  

    // ドキュメントを開く
    $document = new Document($inputFile);

    // 異なるドキュメントのプロパティを取得
    // ドキュメントのウィンドウの位置 - デフォルト: false
    $responseData = "CenterWindow : " . $document->isCenterWindow();

    // 主な読み取り順序; ページの位置を決定する
    // 並べて表示されたとき - デフォルト: L2R
    $responseData = $responseData . "Direction : " . $document->getDirection();

    // ウィンドウのタイトルバーにドキュメントのタイトルを表示するかどうか。
    // falseの場合、タイトルバーにはPDFファイル名が表示されます - デフォルト: false
    $responseData = $responseData . "DisplayDocTitle : " . $document->isDisplayDocTitle();

    // ドキュメントのウィンドウサイズを最初に表示されたページのサイズに合わせて変更するかどうか - デフォルト: false
    $responseData = $responseData . "FitWindow : " . $document->isFitWindow();

    // ビューアアプリケーションのメニューバーを非表示にするかどうか - デフォルト: false
    $responseData = $responseData . "HideMenuBar :" . $document->isHideMenubar();

    // ビューアアプリケーションのツールバーを非表示にするかどうか - デフォルト: false
    $responseData = $responseData . "HideToolBar :" . $document->isHideToolBar();

    // スクロールバーのようなUI要素を非表示にして
    // ページ内容のみを表示するかどうか - デフォルト: false
    $responseData = $responseData . "HideWindowUI :" . $document->isHideWindowUI();

    // ドキュメントのページモード。フルスクリーンモードを終了するときに
    // ドキュメントをどのように表示するか。
    $responseData = $responseData . "NonFullScreenPageMode :" . $document->getNonFullScreenPageMode();

    // ページレイアウト、例えば単一ページ、一列
    $responseData = $responseData . "PageLayout :" . $document->getPageLayout();

    // ドキュメントを開いたときにどのように表示するか。
    $responseData = $responseData . "Page Mode :" . $document->getPageMode();
    $document->close();  
```


## ドキュメントウィンドウとページ表示プロパティを設定する

このトピックでは、ドキュメントウィンドウ、ビューアアプリケーション、およびページ表示のプロパティを設定する方法を説明します。

これらの異なるプロパティを設定するには：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用して PDF ファイルを開きます。
1. Document オブジェクトのプロパティを設定します。
1. Save メソッドを使用して更新された PDF ファイルを保存します。

利用可能なメソッドは次のとおりです：

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

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    // 異なるドキュメントプロパティを設定する
    // ドキュメントウィンドウの位置を指定する - デフォルト: false
    $document->setCenterWindow(true);
    // 主な読み取り順序を指定する; ページの位置を決定する
    // 並べて表示する場合 - デフォルト: L2R
    $document->setDirection(Direction::$R2L);
    // ウィンドウのタイトルバーにドキュメントタイトルを表示するかどうかを指定する
    // falseの場合、タイトルバーにはPDFファイル名が表示される - デフォルト: false
    $document->setDisplayDocTitle(true);
    // ドキュメントのウィンドウサイズを
    // 最初に表示されたページのサイズに合わせてリサイズするかどうかを指定する - デフォルト: false
    $document->setFitWindow(true);
    // ビューアアプリケーションのメニューバーを非表示にするかどうかを指定する - デフォルト:
    // false
    $document->setHideMenubar(true);
    // ビューアアプリケーションのツールバーを非表示にするかどうかを指定する - デフォルト:
    // false
    $document->setHideToolBar(true);
    // スクロールバーなどのUI要素を非表示にするかどうかを指定し、
    // ページの内容のみを表示する - デフォルト: false
    $document->setHideWindowUI(true);
    // ドキュメントのページモード。フルスクリーンモードを終了するときに
    // ドキュメントをどのように表示するかを指定する。
    $document->setNonFullScreenPageMode(PageMode::$UseOC);
    // ページレイアウトを指定する、つまり単一ページ、一列
    $document->setPageLayout(PageLayout::$TwoColumnLeft);
    // ドキュメントを開いたときにどのように表示するかを指定する
    // 例：サムネイルを表示、フルスクリーン、添付ファイルパネルを表示
    $document->setPageMode(PageMode::$UseThumbs);
    // 更新されたPDFファイルを保存
    $document->save($outputFile);
    $document->close();

```


## 既存のPDFファイルにフォントを埋め込む

PDFリーダーは[14のコアフォント](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts)をサポートしており、これによりドキュメントが表示されるプラットフォームに関係なく同じ方法で表示できます。PDFにコアフォント以外のフォントが含まれている場合、フォントの代替を防ぐためにフォントを埋め込んでください。

Java経由のAspose.PDF for PHPは、既存のPDFドキュメントへのフォントの埋め込みをサポートしています。フォント全体またはサブセットを埋め込むことができます。フォントを埋め込むには：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用して既存のPDFファイルを開きます。
1. フォントを埋め込むために [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) クラスを使用します。
   1. setEmbedded(true) メソッドは完全なフォントを埋め込みます。
   1. [isSubset(true) メソッド](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/#isSubset--) はフォントのサブセットを埋め込みます。

フォントサブセットは使用される文字のみを埋め込み、短い文やスローガンにフォントが使用される場合に便利です。例えば、企業のロゴにフォントが使用されるが、本文には使用されない場合などです。
 ファイルサイズを削減するためにサブセットを使用します。

しかし、本文にカスタムフォントを使用する場合は、それを全体として埋め込んでください。

以下のコードスニペットは、PDFファイルにフォントを埋め込む方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    $pages = $document->getPages();
    for ($i = 1; $i <= $pages->size(); $i++) {
      $page = $pages->get_Item($i);
      $fonts = $page->getResources()->getFonts();
      if (!is_null($fonts)) {
        for ($fontIndex = 1; $fontIndex <= $fonts->size(); $fontIndex++) {
          $pageFont = $fonts->get_Item($fontIndex);
          // フォントがすでに埋め込まれているか確認
          if (!$pageFont->isEmbedded())
            $pageFont->setEmbedded(true);
        }
      }
      $forms = $page->getResources()->getForms();
      // フォームオブジェクトを確認
      for ($formIndex = 0; $formIndex < -$forms->size(); $formIndex++) {
        $formFonts = $forms->get_Item($formIndex)->getResources()->getFonts();
        if (!is_null($formFonts)) {
          for ($fontIndex = 1; $fontIndex <= $formFonts->size(); $fontIndex++) {
            $pageFont = $formFonts->get_Item($fontIndex);
            // フォントがすでに埋め込まれているか確認
            if (!$pageFont->isEmbedded())
              $pageFont->setEmbedded(true);
          }
        }
      }
      $responseData = "Ok";
    }

    // 更新されたPDFファイルを保存
    $document->save($outputFile);
    $document->close();
```

## PDF作成時にフォントを埋め込む

Adobe Readerがサポートする14のコアフォント以外のフォントを使用する必要がある場合は、PDFファイルを生成する際にフォントの説明を埋め込む必要があります。フォント情報が埋め込まれていない場合、Adobe Readerはオペレーティングシステムからそれを取得します（システムにインストールされている場合）、またはPDFのフォント記述子に従って代替フォントを構築します。埋め込まれるフォントはホストマシンにインストールされている必要があることに注意してください。例えば、以下のコードでは「Univers Condensed」フォントがシステムにインストールされています。

フォント情報をPDFファイルに埋め込むために、[Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) クラスの setEmbedded プロパティを使用します。このプロパティの値を 'true' に設定すると、フォントファイル全体がPDFに埋め込まれますが、PDFファイルサイズが大きくなることを理解しておいてください。以下は、フォント情報をPDFに埋め込むために使用できるコードスニペットです。

```php

    // 空のコンストラクタを呼び出してPDFオブジェクトをインスタンス化します
    $document = new Document();

    // Pdfオブジェクトにセクションを作成します
    $page = $document->getPages()->add();
    $fragment = new TextFragment("");
    $segment = new TextSegment("This is a sample text using Custom font.");

    $fontRepository = new FontRepository();

    $ts = new TextState();
    $ts->setFont($fontRepository->findFont("Univers Condensed"));
    $ts->getFont()->setEmbedded(true);
    $segment->setTextState($ts);
    $fragment->getSegments()->add($segment);
    $page->getParagraphs()->add($fragment);

    // 更新されたPDFファイルを保存します
    $document->save($outputFile);
    $document->close();
```


## PDFを保存する際のデフォルトフォント名の設定

PDFドキュメントに含まれるフォントが、そのドキュメント自体やデバイスに存在しない場合、APIはこれらのフォントをデフォルトフォントに置き換えます。フォントが利用可能な場合（デバイスにインストールされているか、ドキュメントに埋め込まれている場合）、出力PDFは同じフォントを持つべきです（デフォルトフォントに置き換えるべきではありません）。デフォルトフォントの値は、フォントファイルへのパスではなく、フォントの名前を含むべきです。ドキュメントをPDFとして保存する際にデフォルトフォント名を設定する機能を実装しました。デフォルトフォントを設定するために次のコードスニペットを使用できます：

```php

    // 既存のPDFドキュメントをロード
    $document = new Document($inputFile);
    $newName = "Arial";

    // PDF形式の保存オプションを初期化
    $ops = new PdfSaveOptions();

    // デフォルトフォント名を設定
    $ops->setDefaultFontName($newName);

    // PDFファイルを保存
    $document->save($outputFile, $ops);
    // 更新されたPDFファイルを保存
    $document->close();
```

## PDFドキュメントからすべてのフォントを取得

PDFドキュメントからすべてのフォントを取得したい場合は、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスで提供されている**Document.getFontUtilities().getAllFonts()**メソッドを使用できます。
 以下のコードスニペットを確認して、既存のPDFドキュメントからすべてのフォントを取得してください:

```php

    // 既存のPDFドキュメントをロード
    $document = new Document($inputFile);

    // ドキュメントからすべてのフォントを取得
    $fonts = $document->getFontUtilities()->getAllFonts();
    foreach ($fonts as $font) {
      $responseData = $responseData . $f->getFontName() . PHP_EOL;
    }

    // 更新されたPDFファイルを保存
    $document->close();
```

## PDFファイルのズームファクターの取得と設定

時々、PDFドキュメントのズームファクターを設定または取得したいことがあります。この要件はAspose.PDFを使用すると簡単に達成できます。

[GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction)オブジェクトは、PDFファイルに関連付けられたズーム値を取得することを可能にします。同様に、ファイルのズームファクターを設定するためにも使用できます。

```php

    // 既存のPDFドキュメントをロード
    $document = new Document($inputFile);

    // GoToActionオブジェクトを作成
    $action = $document->getOpenAction();

    // PDFファイルのズームファクターを取得
    $responseData = $action->getDestination()->getZoom();

    // 更新されたPDFファイルを保存
    $document->close();  
```

以下のコードスニペットは、PDFファイルのズームファクターを取得する方法を示しています。

```php

    // 既存のPDFドキュメントをロードする
    $document = new Document($inputFile);
    $zoom = 0.5;
    // ドキュメントのズームファクターを設定
    $page = $document->getPages()->get_Item(1);
    $actionzoom = new GoToAction(
      new XYZExplicitDestination($page, $page->getMediaBox()->getWidth(), $page->getMediaBox()->getHeight(), $zoom)
    );

    // ページ幅に合わせてズームするアクションを設定
    $actionFitToWidth = new GoToAction(
      new FitHExplicitDestination($page, $page->getMediaBox()->getWidth())
    );

    // ページ高さに合わせてズームするアクションを設定
    $actionFittoHeight = new GoToAction(
      new FitVExplicitDestination( $page, $page->getMediaBox()->getHeight())
    );

    $document->setOpenAction($actionzoom);
    $document->setOpenAction($actionFittoWidth);
    $document->setOpenAction($actionFittoHeight);

    // 更新されたPDFファイルを保存する
    $document->save($outputFile);
    $document->close();  
```