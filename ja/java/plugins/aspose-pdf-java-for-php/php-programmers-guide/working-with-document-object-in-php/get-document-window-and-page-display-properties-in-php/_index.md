---
title: PHPでのドキュメントウィンドウとページ表示プロパティの取得
type: docs
weight: 30
url: /ja/java/get-document-window-and-page-display-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - ドキュメントウィンドウとページ表示プロパティの取得

**Aspose.PDF Java for PHP**を使用してPDFドキュメントのウィンドウとページ表示プロパティを取得するには、単に**GetDocumentWindow**クラスを呼び出します。

PHPコード

```php

# PDFドキュメントを開く。
$doc = new Document($dataDir . "input1.pdf");

# 異なるドキュメントプロパティを取得
# ドキュメントウィンドウの位置 - デフォルト: false
print "CenterWindow :- " . $doc->getCenterWindow() . PHP_EOL;

# 主な読み順; ページの位置を決定する
# 並べて表示されるとき - デフォルト: L2R
print "Direction :- " . $doc->getDirection() . PHP_EOL;

# ウィンドウのタイトルバーにドキュメントタイトルを表示するかどうか。
# falseの場合、タイトルバーにはPDFファイル名が表示される - デフォルト: false
print "DisplayDocTitle :- " . $doc->getDisplayDocTitle() . PHP_EOL;

# ドキュメントウィンドウのサイズを
# 最初に表示されたページのサイズに合わせてリサイズするかどうか - デフォルト: false
print "FitWindow :- " . $doc->getFitWindow() . PHP_EOL;

# ビューアアプリケーションのメニューバーを隠すかどうか - デフォルト: false
print "HideMenuBar :-" . $doc->getHideMenubar() . PHP_EOL;

# ビューアアプリケーションのツールバーを隠すかどうか - デフォルト: false
print "HideToolBar :-" . $doc->getHideToolBar() . PHP_EOL;

# スクロールバーなどのUI要素を隠すかどうか
# ページの内容のみを表示する - デフォルト: false
print "HideWindowUI :-" . $doc->getHideWindowUI() . PHP_EOL;

# ドキュメントのページモード。全画面モードを終了するときにドキュメントを表示する方法。
print "NonFullScreenPageMode :-" . $doc->getNonFullScreenPageMode() . PHP_EOL;

# ページレイアウト、つまり単一ページ、1列
print "PageLayout :-" . $doc->getPageLayout() . PHP_EOL;

# ドキュメントを開いたときにどのように表示するか。
print "pageMode :-" . $doc->getPageMode() . PHP_EOL;
```


**コードの実行をダウンロードする**

**ドキュメントウィンドウとページ表示プロパティを取得する (Aspose.PDF)** を以下のいずれかのソーシャルコーディングサイトからダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)