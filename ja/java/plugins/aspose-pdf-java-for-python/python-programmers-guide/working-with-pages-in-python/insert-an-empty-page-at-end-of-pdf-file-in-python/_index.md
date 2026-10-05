---
title: "Python での PDFファイルの末尾に空のページの挿入"
linktitle: "Python での PDFファイルの末尾に空のページの挿入"
type: docs
weight: 60
url: /ja/java/insert-an-empty-page-at-end-of-pdf-file-in-python/
description: Aspose.PDF を使用して、PythonでPDFドキュメントの末尾に空のページを挿入し、ドキュメントを簡単に拡張する方法を紹介します。
lastmod: "2026-10-05"
---
**Aspose.PDF Java for Python** を使用して PDF ドキュメントの末尾に空のページを挿入するには、単に **InsertEmptyPageAtEndOfFile** クラスを呼び出すだけです。

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().add();

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

**実行コードをダウンロード**

ダウンロード **Insert an Empty Page at End of PDF File (Aspose.PDF)**В fromВ 以下に記載されたソーシャルコーディングサイトから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)
