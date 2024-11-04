---
title: PDFドキュメントを操作する
linktitle: PDFドキュメントを操作する
type: docs
weight: 30
url: /php-java/manipulate-pdf-document/
description: この記事には、PDF A標準に対するPDFドキュメントの検証方法、目次の操作方法、PDFの有効期限の設定方法、PDFファイル生成の進行状況を判断する方法に関する情報が含まれています。
lastmod: "2024-06-05"
---

## PDF A標準 (A 1AおよびA 1B) に対するPDFドキュメントの検証

PDF/A-1aまたはPDF/A-1bの互換性についてPDFドキュメントを検証するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスの [validate(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#validate-java.lang.String-com.aspose.pdf.PdfFormat-) メソッドを使用します。このメソッドでは、結果を保存するファイル名と、必要な検証タイプ [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat) 列挙型: PDF_A_1AまたはPDF_A_1Bを指定できます。

出力XML形式はカスタムAspose形式です。
 The XMLには、Problemという名前のタグのコレクションが含まれています。各タグには、特定の問題の詳細が含まれています。ProblemタグのObjectID属性は、この問題に関連する特定のオブジェクトのIDを表します。Clause属性は、PDF仕様の対応するルールを表します。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    
    $pdfFormat =  (new PdfFormat())->PDF_A_1A;
    // PDF/A-1aのためにPDFを検証
    $document->validate($outputFile, $pdfFormat);
    $document->close();
```

## TOCの操作

### 既存のPDFにTOCを追加

既存のPDFファイルにTOCを追加するには、com.aspose.pdfパッケージ内の[Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading)クラスを使用します。com.aspose.pdfパッケージは、新しいPDFファイルの作成と既存のPDFファイルの操作の両方を行うことができます。既存のPDFにTOCを追加するには、com.aspose.pdfパッケージを使用します。

このPHPコードスニペットは、既存のPDFドキュメントに目次（TOC）を追加するためにAspose.PDFを使用しています：

```php
    // ドキュメントを開く
    $document = new Document($inputFile);

    // PDFファイルの最初のページにアクセス
    $tocPage = $document->getPages()->insert(1);

    // TOC情報を表すオブジェクトを作成
    $tocInfo = new TocInfo();

    $title = new TextFragment("目次");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // TOCのタイトルを設定
    $tocInfo->setTitle($title);
    $tocPage->setTocInfo($tocInfo);

    // TOC要素として使用される文字列オブジェクトを作成
    $titles = ["最初のページ", "2ページ目", "3ページ目", "4ページ目"];

    for ($i = 0; $i < 4; $i++) {
        // Headingオブジェクトを作成
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Headingオブジェクトの宛先ページを指定
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // 宛先ページ
        $heading2->setTop($page->getRect()->getHeight());

        // 宛先座標
        $segment2->setText($titles[$i]);

        // TOCを含むページに見出しを追加
        $tocPage->getParagraphs()->add($heading2);
    }
    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

### 異なるTOCレベルに異なるTabLeaderTypeを設定する

Aspose.PDFは、異なるTOCレベルに異なるTabLeaderTypeを設定することも可能です。FormatArrayのLineDashプロパティを、以下のようにTabLeaderType列挙型の適切な値に設定する必要があります。

```php
    // ドキュメントを開く
    $document = new Document($inputFile);
    $tocPage = $document->getPages()->add();

    $tocInfo = new TocInfo();

    // LeaderTypeを設定
    $tocInfo->setLineDash(TabLeaderType->Solid);

    $title = new TextFragment("目次");
    $title->getTextState()->setFontSize(30);
    $tocInfo->setTitle($title);

    // Pdfドキュメントのセクションコレクションにリストセクションを追加
    $tocPage->setTocInfo($tocInfo);

    // 左マージンと各レベルのテキストフォーマット設定を設定することで、4レベルリストの形式を定義
    $fontStyles = new FontStyles();
    $tabLeaderTypes = new TabLeaderType();

    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setLeft(0);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[0]->setLineDash($tabLeaderTypes->getDot());
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle($fontStyles->getBold() | $fontStyles->getItalic());
    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(10);
    $tocInfo->getFormatArray()[1]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[1]->setLineDash($tabLeaderTypes->getNone());
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);
    $tocInfo->getFormatArray()[2]->getMargin()->setLeft(20);
    $tocInfo->getFormatArray()[2]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle($fontStyles->getBold());
    $tocInfo->getFormatArray()[3]->setLineDash($tabLeaderTypes->getSolid());
    $tocInfo->getFormatArray()[3]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[3]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle($fontStyles->getBold());

    // Pdfドキュメントにセクションを作成
    $page = $document->getPages()->add();

    // セクションに4つの見出しを追加
    for ($Level = 1; $Level <= 4; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();

      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $heading2->setTocPage($tocPage);

      $segment2->setText("サンプル見出し" . $Level);
      $fontRepository = new FontRepository();
      $heading2->getTextState()->setFont($fontRepository->findFont("Arial UnicodeMS"));

      // 見出しを目次に追加
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }

    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();
```


### TOCでページ番号を非表示にする

TOCで見出しと一緒にページ番号を表示したくない場合は、[TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) クラスの [ShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/#setShowPageNumbers-boolean-) プロパティをfalseに設定することができます。以下のコードスニペットを確認して、目次でページ番号を非表示にする方法を示します:

```php
    // ドキュメントを開く
    $document = new Document();
    $tocPage = $document->getPages()->add();
    
    // TOC情報を表すオブジェクトを作成
    $tocInfo = new TocInfo();

    $title = new TextFragment("目次");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // TOCのタイトルを設定
    $tocInfo->setTitle($title);

    // Pdfドキュメントのセクションコレクションにリストセクションを追加
    $tocPage->setTocInfo($tocInfo);

    // 左マージンと各レベルのテキストフォーマット設定を設定することで
    // 4レベルのリストのフォーマットを定義

    $tocInfo->setShowPageNumbers(false);
    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle(FontStyles::$Bold | FontStyles::$Italic);

    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[1]->getTextState()->setUnderline(true);
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);

    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle(FontStyles::$Bold);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle(FontStyles::$Bold);

    $page = $document->getPages()->add();

    // セクションに4つの見出しを追加
    for ($Level = 1; $Level < 5; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();
      $heading2->setTocPage($tocPage);
      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $segment2->setText("これはレベル " + $Level + " の見出しです");
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }
     
    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();
```


### 目次を追加する際のページ番号のカスタマイズ

PDFドキュメントに目次を追加する際に、目次のページ番号をカスタマイズすることは一般的です。例えば、ページ番号の前にP1, P2, P3などのプレフィックスを追加する必要があるかもしれません。このような場合、Aspose.PDF for PHP via Javaは、次のコードサンプルに示すように、ページ番号をカスタマイズするためにTocInfoクラスのPageNumbersPrefixプロパティを提供しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // PDFファイルの最初のページにアクセス
    $tocPage = $document->getPages()->insert(1);

    // 目次情報を表すオブジェクトを作成
    $tocInfo = new TocInfo();

    $title = new TextFragment("目次");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // 目次のタイトルを設定
    $tocInfo->setTitle($title);
    $tocInfo->setPageNumbersPrefix("P");
    $tocPage->setTocInfo($tocInfo);

    // 目次要素として使用される文字列オブジェクトを作成
    $titles = ["最初のページ", "2ページ目", "3ページ目", "4ページ目"];

    for ($i = 0; $i < 4; $i++) {
        // 見出しオブジェクトを作成
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // 見出しオブジェクトの宛先ページを指定
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // 宛先ページ
        $heading2->setTop($page->getRect()->getHeight());

        // 宛先座標
        $segment2->setText($titles[$i]);

        // 目次を含むページに見出しを追加
        $tocPage->getParagraphs()->add($heading2);
    }
    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();
```


## PDFファイルにレイヤーを追加する

レイヤーはPDFドキュメントで多くの方法で使用できます。たとえば、複数言語のファイルを配布したい場合、各言語のテキストを異なるレイヤーに表示し、背景デザインを別のレイヤーに表示することができます。また、アニメーションが別のレイヤーに表示されるドキュメントを作成することもできます。一例として、ライセンス契約をファイルに追加し、ユーザーが契約の条件に同意するまで内容を表示しないようにすることができます。

Aspose.PDF for PHP via Javaは、PDFファイルにレイヤーを追加することをサポートしています。

PDFファイル内のレイヤーを操作するには、以下のAPIメンバーを使用します。

[Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer)クラスはレイヤーを表し、以下のプロパティを含んでいます：

- **Name** – レイヤーの名前。
- **Id** – レイヤーのID。
- **Contents** – レイヤーオペレーターのリスト。

[Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer)オブジェクトが定義されたら、それらを[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)オブジェクトのLayersコレクションに追加します。
 以下のコードは、PDFドキュメントにレイヤーを追加する方法を示しています。

```php
    // ドキュメントを開く
    $document = new Document($inputFile);
    $page = $document->getPages()->add();
    $arrayList = new java("java.util.ArrayList");
    $page->setLayers($arrayList);

    $layer = new $layer("oc1", "赤い線");
    $layer->getContents()->add(new operators_SetRGBColorStroke(1, 0, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 700));
    $layer->getContents()->add(new operators_LineTo(400, 700));
    $layer->getContents()->add(new operators_Stroke());    
    $page->getLayers()->add($layer);

    $layer = new $layer("oc2", "緑の線");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 1, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 750));
    $layer->getContents()->add(new operators_LineTo(400, 750));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);

    $layer = new $layer("oc3", "青い線");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 0, 1));
    $layer->getContents()->add(new operators_MoveTo(500, 800));
    $layer->getContents()->add(new operators_LineTo(400, 800));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);
    
    // 更新したドキュメントを保存する
    $document->save($outputFile);
    $document->close();
```

## PDFの有効期限を設定する

PDFの有効期限機能は、PDFファイルがどのくらいの期間有効であるかを設定します。特定の日付に、誰かがそれにアクセスしようとすると、ファイルが期限切れであり、新しいものが必要であることを説明するポップアップが表示されます。

Aspose.PDFを使用すると、PDFファイルの作成および編集時に有効期限を設定することができます。

以下のコードスニペットは、PDFファイルの有効期限を設定する方法を示しています。サードパーティのコンポーネント（例えばOwnerGuard）によって保存されたファイルは、そのユーティリティなしでは他の作業ステーションで表示できないため、JavaScriptを使用する必要があります。

PDFファイルは、既存のファイルを使用して有効期限を設定することで、PDF OwnerGuardを使用して作成できます。ただし、新しいファイルはPDF OwnerGuardがインストールされた作業ステーションでのみ開くことができます。PDF OwnerGuardがない作業ステーションではExpirationFeatureErrorが発生します。例えば、PDF ReaderはOwnerGuardがインストールされていればファイルを開きますが、Adobe Acrobatはエラーを返します。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
       
    $javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "var today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
      "var expiry = new Date(year, month);" +
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('ファイルは期限切れです。新しいものが必要です。');"
      );
    $document->setOpenAction($javaScript);
    $document->save($outputFile);
    $document->close();
```