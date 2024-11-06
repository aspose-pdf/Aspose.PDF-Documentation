---
title: Rubyでのドキュメントウィンドウおよびページ表示プロパティの取得
type: docs
weight: 40
url: ja/java/get-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - ドキュメントウィンドウおよびページ表示プロパティの取得

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントのウィンドウおよびページ表示プロパティを取得するには、単に**GetDocumentWindow**モジュールを呼び出します。

Rubyコード

```java
# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDFドキュメントを開く。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 異なるドキュメントプロパティを取得

# ドキュメントウィンドウの位置 - デフォルト: false

puts "CenterWindow :- " + doc.getCenterWindow().to_s

# 主な読み順; ページの位置を決定する

# 横に並べて表示されるとき - デフォルト: L2R

puts "Direction :- " + doc.getDirection().to_s

# ウィンドウのタイトルバーがドキュメントタイトルを表示するかどうか。

# falseの場合、タイトルバーにはPDFファイル名が表示される - デフォルト: false

puts "DisplayDocTitle :- " + doc.getDisplayDocTitle().to_s

# ドキュメントのウィンドウをリサイズして

# 最初に表示されるページのサイズに合わせるかどうか - デフォルト: false

puts "FitWindow :- " + doc.getFitWindow().to_s

# ビューアアプリケーションのメニューバーを非表示にするかどうか - デフォルト: false

puts "HideMenuBar :-" + doc.getHideMenubar().to_s

# ビューアアプリケーションのツールバーを非表示にするかどうか - デフォルト: false

puts "HideToolBar :-" + doc.getHideToolBar().to_s

# スクロールバーのようなUI要素を非表示にするかどうか

# ページの内容のみを表示 - デフォルト: false

puts "HideWindowUI :-" + doc.getHideWindowUI().to_s

# ドキュメントのページモード。フルスクリーンモードを終了したときの表示方法。

puts "NonFullScreenPageMode :-" + doc.getNonFullScreenPageMode().to_s

# ページレイアウト、つまり単一ページ、1列

puts "PageLayout :-" + doc.getPageLayout().to_s

# ドキュメントを開いたときの表示方法。

puts "pageMode :-" + doc.getPageMode().to_s
```


## Download Running Code

以下のいずれかのソーシャルコーディングサイトから **Get Document Window and Page Display Properties (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getdocumentwindow.rb)