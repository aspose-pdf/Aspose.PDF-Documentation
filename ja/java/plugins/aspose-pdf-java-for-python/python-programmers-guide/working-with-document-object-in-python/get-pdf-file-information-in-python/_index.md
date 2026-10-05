---
title: "Python での PDFファイル情報の取得"
linktitle: "Python での PDFファイル情報の取得"
type: docs
weight: 40
url: /ja/java/get-pdf-file-information-in-python/
description: Aspose.PDF を使用したドキュメント管理において、メタデータやプロパティなどの詳細な PDF ファイル情報を Python で取得する方法を探ります。
lastmod: "2026-10-05"
---
**Aspose.PDF Java for Python** を使用して PDF ドキュメントのファイル情報を取得するには、単に **GetPdfFileInfo** クラスを呼び出すだけです。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

# Show document information
print "Author:-" + str(doc_info.getAuthor())
print "Creation Date:-" + str(doc_info.getCreationDate())
print "Keywords:-" + str(doc_info.getKeywords())
print "Modify Date:-" + str(doc_info.getModDate())
print "Subject:-" + str(doc_info.getSubject())
print "Title:-" + str(doc_info.getTitle())
```

**実行コードのダウンロード**

ダウンロードВ **PDF ファイル情報の取得 (Aspose.PDF)**В fromВ 以下に示すソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
