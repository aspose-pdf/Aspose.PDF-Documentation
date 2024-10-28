---
title: PythonでPDFをExcelワークブックに変換する
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python** を使用してPDF文書をExcelワークブックに変換するには、単に **PdfToExcel** モジュールを呼び出します。

```python

doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# ExcelSaveオプションオブジェクトをインスタンス化
excelsave=self.ExcelSaveOptions();

# 出力をXLS形式で保存
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
print "ドキュメントが正常に変換されました"
```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから **Convert PDF to Excel Workbook (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)