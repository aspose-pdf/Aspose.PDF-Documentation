---
title: "Python での PDFのメタデータの削除"
linktitle: "Python での PDFのメタデータの削除"
type: docs
weight: 70
url: /ja/java/remove-metadata-from-pdf-in-python/
description: Aspose.PDFを使用してPythonでPDFドキュメントのメタデータを削除する方法を確認し、プライバシーとデータセキュリティを確保しましょう。
lastmod: "2026-10-05"
---
**Aspose.PDF Java for Python** を使用してPDF文書のメタデータを削除するには、単に **RemoveMetadata** クラスを呼び出すだけです。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# save update document with new information
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Removed metadata successfully, please check output file."

```

**実行コードをダウンロード**

以下のソーシャルコーディングサイトから **Remove Metadata (Aspose.PDF)** をダウンロード:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)
