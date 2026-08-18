---
title: 在 Python 中将 PDF 转换为 Excel 工作簿
linktitle: 在 Python 中将 PDF 转换为 Excel 工作簿
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-python/
description: 了解如何使用 Aspose.PDF 在 Python 中将 PDF 文档转换为 Excel 工作簿以进行结构化数据提取。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 将 PDF 文档转换为 Excel 工作簿，只需调用 **PdfToExcel** 模块即可。

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

**下载运行代码**

从以下任何社交编码网站下载**将 PDF 转换为 Excel 工作簿 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)
