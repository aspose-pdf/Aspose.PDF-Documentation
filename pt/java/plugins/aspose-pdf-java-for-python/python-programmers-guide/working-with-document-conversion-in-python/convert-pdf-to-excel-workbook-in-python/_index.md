---
title: Converter PDF para pasta de trabalho Excel em Python
linktitle: Converter PDF para pasta de trabalho Excel em Python
type: docs
weight: 20
url: /pt/java/convert-pdf-to-excel-workbook-in-python/
description: Aprenda como converter documentos PDF para pastas de trabalho Excel em Python usando Aspose.PDF para extração de dados estruturados.
lastmod: "2026-10-06"
---
Para converter um documento PDF para Excel Workbook usando **Aspose.PDF Java for Python**, basta invocar o módulo **PdfToExcel**.

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

**Download do Código em Execução**

Baixar **Convert PDF to Excel Workbook (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)
