---
title: ドキュメントウィンドウとページ表示プロパティをPythonで取得する
type: docs
weight: 30
url: /python-java/get-document-window-and-page-display-properties-in-python/
---

<ins>**Aspose.PDF Java for Python**を使用してPDFドキュメントのウィンドウとページ表示プロパティを取得するには、**GetDocumentWindow**クラスを呼び出します。

**Pythonコード**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# ドキュメントのさまざまなプロパティを取得
# ドキュメントウィンドウの位置 - デフォルト: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# 主な読み取り順序; ページの位置を決定
# 並べて表示されたとき - デフォルト: L2R
print "Direction :- " + str(doc.getDirection())

# ウィンドウのタイトルバーがドキュメントタイトルを表示するかどうか。
# falseの場合、タイトルバーはPDFファイル名を表示します - デフォルト: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

# ドキュメントのウィンドウを
# 最初に表示されたページのサイズに合わせてリサイズするかどうか - デフォルト: false

print "FitWindow :- " + str(doc.getFitWindow())

# ビューアアプリケーションのメニューバーを非表示にするかどうか - デフォルト: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# ビューアアプリケーションのツールバーを非表示にするかどうか - デフォルト: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# スクロールバーのようなUI要素を非表示にするかどうか
# ページの内容のみを表示 - デフォルト: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# ドキュメントのページモード。フルスクリーンモードを終了するときにドキュメントをどのように表示するか。
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# ページレイアウト、つまり1ページ、1カラム
print "PageLayout :-" + str(doc.getPageLayout())

# ドキュメントを開いたときにどのように表示するか。
print "pageMode :-" + str(doc.getPageMode())
```


**コードをダウンロードする**

**Get Document Window and Page Display Properties (Aspose.PDF)** を以下のいずれかのソーシャルコーディングサイトからダウンロードします:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)