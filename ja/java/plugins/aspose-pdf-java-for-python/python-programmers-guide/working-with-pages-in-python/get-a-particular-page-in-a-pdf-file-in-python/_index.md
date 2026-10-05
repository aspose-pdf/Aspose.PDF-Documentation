---
title: "Python での PDFファイルの特定のページの取得"
linktitle: "Python での PDFファイルの特定のページの取得"
type: docs
weight: 30
url: /ja/java/get-a-particular-page-in-a-pdf-file-in-python/
description: Aspose.PDF を使用して、PythonでPDFファイルから特定のページを抽出する方法を詳しく探ります。
lastmod: "2026-10-05"
---
**Aspose.PDF Java for Python** を使用して PDF ドキュメントの特定のページを取得するには、単に **GetPage** クラスを呼び出します。

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get the page at particular index of Page Collection
pdf_page = pdf.getPages().get_Item(1)

# create a new Document object
new_document = self.Document()

# add page to pages collection of new document object
new_document.getPages().add(pdf_page)

# save the newly generated PDF file
new_document.save(self.dataDir + "output.pdf")

print "Process completed successfully!

```

 **実行コードをダウンロード**

Download **Get Page (Aspose.PDF)** から以下に記載されたソーシャルコーディングサイトのいずれかで:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)
