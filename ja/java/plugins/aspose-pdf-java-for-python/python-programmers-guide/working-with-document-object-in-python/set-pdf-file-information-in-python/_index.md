---
title: "Python での PDF ファイル情報の設定"
linktitle: "Python での PDF ファイル情報の設定"
type: docs
weight: 90
url: /ja/java/set-pdf-file-information-in-python/
description: "Aspose.PDF を使用して、著者やタイトルなどの PDF ファイル情報を Python で設定し、ドキュメントを整理する方法を学びます。"
lastmod: "2026-10-06"
---
**Aspose.PDF Java for Python** を使用して PDF ドキュメント情報を更新するには、**SetPdfFileInfo** クラスを呼び出してください。

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("PDF Information");
doc_info.setTitle("Setting PDF Document Information");

# save update document with new information

doc.save(self.dataDir + "Updated_Information.pdf")
print "Update document information, please check output file."
```

**実行コードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから、**PDF ファイル情報の設定 (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
