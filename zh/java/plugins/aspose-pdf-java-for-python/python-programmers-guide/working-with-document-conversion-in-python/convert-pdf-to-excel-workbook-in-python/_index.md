---
title: 将 PDF 转换为 Excel 工作簿在 Python 中
type: docs
weight: 20
url: /zh/java/convert-pdf-to-excel-workbook-in-python/
lastmod: "2021-06-05"
---

要使用 **Aspose.PDF Java for Python** 将 PDF 文档转换为 Excel 工作簿，只需调用 **PdfToExcel** 模块。

```python

doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# 实例化 ExcelSave Option 对象
excelsave=self.ExcelSaveOptions();

# 将输出保存为 XLS 格式
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
print "Document has been converted successfully"
```

**下载运行代码**

从以下任一社交编码网站下载 **Convert PDF to Excel Workbook (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)