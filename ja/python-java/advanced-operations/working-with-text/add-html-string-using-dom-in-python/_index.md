---
title: PythonでDOMを使用してHTML文字列を追加
type: docs
weight: 10
url: ja/python-java/add-html-string-using-dom-in-python/
---

**Aspose.PDF Java for Python**を使用してPdfドキュメントにHTML文字列を追加するには、単に**AddHtml**モジュールを呼び出します。

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

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Add HTML (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)