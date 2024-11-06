---
title: Pythonでのドキュメントウィンドウおよびページ表示プロパティの取得
type: docs
weight: 30
url: ja/java/get-document-window-and-page-display-properties-in-python/
lastmod: "2021-06-05"
---

Pdfドキュメントのドキュメントウィンドウおよびページ表示プロパティを**Aspose.PDF Java for Python**を使用して取得するには、単に**GetDocumentWindow**クラスを呼び出します。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# ドキュメントの異なるプロパティを取得する
# ドキュメントウィンドウの位置 - デフォルト: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# 主な読書順序; 並べて表示されるときのページの位置を決定する - デフォルト: L2R
print "Direction :- " + str(doc.getDirection())

# ウィンドウのタイトルバーがドキュメントタイトルを表示するかどうか。
# falseの場合、タイトルバーはPDFファイル名を表示します - デフォルト: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

# ドキュメントのウィンドウを最初に表示されたページのサイズに合わせて
# リサイズするかどうか - デフォルト: false
print "FitWindow :- " + str(doc.getFitWindow())

# ビューアアプリケーションのメニューバーを隠すかどうか - デフォルト: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# ビューアアプリケーションのツールバーを隠すかどうか - デフォルト: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# スクロールバーのようなUI要素を隠し、ページ内容のみを表示するかどうか - デフォルト: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# ドキュメントのページモード。フルスクリーンモードを終了したときのドキュメントの表示方法。
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# ページレイアウト、すなわちシングルページ、1カラム
print "PageLayout :-" + str(doc.getPageLayout())

# 開いたときにドキュメントがどのように表示されるか。
print "pageMode :-" + str(doc.getPageMode())
```


**実行コードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから、**ドキュメントウィンドウとページ表示プロパティを取得 (Aspose.PDF)** をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)