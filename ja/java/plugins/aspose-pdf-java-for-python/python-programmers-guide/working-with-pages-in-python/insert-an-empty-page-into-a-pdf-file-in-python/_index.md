---
title: "Python での PDFファイルへの空白ページの挿入"
linktitle: "Python での PDFファイルへの空白ページの挿入"
type: docs
weight: 70
url: /ja/java/insert-an-empty-page-into-a-pdf-file-in-python/
description: PythonとAspose.PDFを使用して、PDFファイル内の任意の位置に空白ページを挿入し、柔軟なドキュメント構造を実現する方法を学びます。
lastmod: "2026-10-05"
---
**Aspose.PDF Java for Python** を使用して PDF ドキュメントに空白ページを挿入するには、単に **InsertEmptyPage** クラスを呼び出します。

```Python

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().insert(1)

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

**実行コードをダウンロード**

ダウンロードВ **空ページの挿入 (Aspose.PDF)**В からВ 以下に示すソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)
