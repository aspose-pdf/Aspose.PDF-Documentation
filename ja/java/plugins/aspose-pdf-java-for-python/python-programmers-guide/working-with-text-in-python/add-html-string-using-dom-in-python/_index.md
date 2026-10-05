---
title: "Python での DOMを使用したHTML文字列の追加"
linktitle: "Python での DOMを使用したHTML文字列の追加"
type: docs
weight: 10
url: /ja/java/add-html-string-using-dom-in-python/
lastmod: "2026-10-05"
description: PythonとPDFファイル形式ライブラリを使用して、DOMにHTML文字列を追加する方法を説明します
---
## Pythonを使用したPDF DOMにHTML文字列の追加

**Aspose.PDF Java for Python** を使用してPDFドキュメントにHTML文字列を追加するには、単に **AddHtml** モジュールを呼び出します。

```python

# Instantiate Document object
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Set margin information
title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page
page.getParagraphs().add(title)

# Save PDF file
doc.save(self.dataDir + 'html.output.pdf')

print "HTML added successfully"
```

**実行コードをダウンロード**

ダウンロードВ **HTML を追加 (Aspose.PDF)**В からV 以下に記載されたソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)
