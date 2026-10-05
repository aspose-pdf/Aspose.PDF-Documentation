---
title: "Python での PDFファイルの結合"
linktitle: "Python での PDFファイルの結合"
type: docs
weight: 10
url: /ja/java/concatenate-pdf-files-in-python/
description: Aspose.PDF を使用して Python で複数の PDF ファイルを単一の PDF ドキュメントに結合し、ドキュメント管理を簡素化する方法を学びます。
lastmod: "2026-10-05"
---
**Aspose.PDF Java for Python** を使用して PDF ファイルを結合するには、単に **ConcatenatePdfFiles** クラスを呼び出すだけです。

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Open the source document
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Add the pages of the source document to the target document
pdf1.getPages().add(pdf1.getPages())

# Save the concatenated output file (the target document)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "New document has been saved, please check the output file"
```

**実行コードをダウンロード**

DownloadВ **Concatenate PDF Files (Aspose.PDF)**В fromВ 以下に記載されたソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)
