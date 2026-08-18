---
title: Converter PDF em pasta de trabalho do Excel em Python
linktitle: Converter PDF em pasta de trabalho do Excel em Python
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-python/
description: Aprenda como converter documentos PDF em pastas de trabalho do Excel em Python usando Aspose.PDF para extração estruturada de dados.
lastmod: "2026-06-09"
---
Para converter um documento PDF em uma pasta de trabalho do Excel usando **Aspose.PDF Java para Python**, basta invocar o módulo **PdfToExcel**.

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

**Baixar código em execução**

Baixe **Converter PDF para Excel Workbook (Aspose.PDF)**Â de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)
