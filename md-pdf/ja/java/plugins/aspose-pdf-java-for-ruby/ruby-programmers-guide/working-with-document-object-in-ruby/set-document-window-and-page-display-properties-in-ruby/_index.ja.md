---
title: Rubyでドキュメントウィンドウとページ表示プロパティを設定する
type: docs
weight: 100
url: /java/set-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - ドキュメントウィンドウとページ表示プロパティを設定する

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントのウィンドウとページ表示プロパティを設定するには、単に**SetDocumentWindow**モジュールを呼び出します。

Ruby コード

```java
# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDFドキュメントを開く。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 異なるドキュメントプロパティを設定する

# ドキュメントウィンドウの位置 - デフォルト: false

doc.setCenterWindow(true)

# 主な読み取り順序; ページの位置を決定する

# 並べて表示されたとき - デフォルト: L2R

#doc.setDirection(Rjb::import('com.aspose.pdf.Direction.L2R'))

# ウィンドウのタイトルバーにドキュメントタイトルを表示するかどうか。

# falseの場合、タイトルバーにはPDFファイル名が表示されます - デフォルト: false

doc.setDisplayDocTitle(true)

# ドキュメントのウィンドウを最初に表示されたページのサイズに合わせてリサイズするかどうか - デフォルト: false

doc.setFitWindow(true)

# ビューアアプリケーションのメニューバーを隠すかどうか - デフォルト: false

doc.setHideMenubar(true)

# ビューアアプリケーションのツールバーを隠すかどうか - デフォルト: false

doc.setHideToolBar(true)

# スクロールバーのようなUI要素を隠し

# ページコンテンツのみを表示する - デフォルト: false

doc.setHideWindowUI(true)

# ドキュメントのページモード。フルスクリーンモードを終了したときにドキュメントをどのように表示するか。

doc.setNonFullScreenPageMode(Rjb::import('com.aspose.pdf.PageMode.UseOC'))

# ページレイアウト、例えばシングルページ、1カラム

doc.setPageLayout(Rjb::import('com.aspose.pdf.PageLayout.TwoColumnLeft'))

# ドキュメントを開いたときにどのように表示するか。

doc.setPageMode()

# 更新されたPDFファイルを保存する

doc.save(data_dir + "Set Document Window.pdf")
```


## コードのダウンロード

**ドキュメントウィンドウとページ表示プロパティの設定 (Aspose.PDF)** を以下のいずれかのソーシャルコーディングサイトからダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)