---
title: PythonでPDFをExcelブックに変換
linktitle: PythonでPDFをExcelブックに変換
type: docs
weight: 20
url: /ja/java/convert-pdf-to-excel-workbook-in-python/
description: 構造化データ抽出のために Aspose.PDF を使用して、PythonでPDFドキュメントをExcelブックに変換する方法を学びましょう。
lastmod: "2026-10-05"
---
**Aspose.PDF Java for Python** を使用してPDFドキュメントをExcelブックに変換するには、単に **PdfToExcel** モジュールを呼び出します。

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

ダウンロード\u0412\u00A0**Convert PDF to Excel Workbook (Aspose.PDF)**\u0412\u00A0から\u0412\u00A0以下に記載されたソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)
