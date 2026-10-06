---
title: "Python で PDF を Excel ブックに変換"
linktitle: "Python で PDF を Excel ブックに変換"
type: docs
weight: 20
url: /ja/java/convert-pdf-to-excel-workbook-in-python/
description: "構造化データ抽出のために Aspose.PDF を使用して、Python で PDF ドキュメントを Excel ブックに変換する方法を学んでください。"
lastmod: "2026-10-06"
---
**Aspose.PDF Java for Python** を使用して PDF ドキュメントを Excel ブックに変換するには、単に **PdfToExcel** モジュールを呼び出してください。

```python

doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# Instantiate ExcelSave Option object
excelsave=self.ExcelSaveOptions();

# Save the output to XLS format
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
print "Document has been converted successfully"
```

**実行コードをダウンロード**

ダウンロード **Convert PDF to Excel Workbook (Aspose.PDF)** は、以下に記載されたソーシャルコーディングサイトのいずれかから行ってください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)
