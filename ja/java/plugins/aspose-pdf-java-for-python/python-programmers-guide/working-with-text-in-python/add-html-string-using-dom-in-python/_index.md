---
title: PythonでDOMを使用してHTML文字列を追加
type: docs
weight: 10
url: /ja/java/add-html-string-using-dom-in-python/
lastmod: "2021-06-05"
keywords: html dom python, python html dom library
description: PythonでDOMを使用してHTML文字列を追加する方法をPDFファイル形式ライブラリで説明します
---

## PythonでPDF DOMにHTML文字列を追加
**Aspose.PDF Java for Python**を使用してPdf文書にHTML文字列を追加するには、**AddHtml**モジュールを呼び出します。

```python

# Documentオブジェクトをインスタンス化
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# マージン情報を設定
title.setMargin(margin)

# ページの段落コレクションにHTMLフラグメントを追加
page.getParagraphs().add(title)

# PDFファイルを保存
doc.save(self.dataDir + 'html.output.pdf')

print "HTMLが正常に追加されました"
```

**実行コードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Add HTML (Aspose.PDF)**をダウンロードしてください:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)