---
title: Convertir PDF a libro de Excel en Python
linktitle: Convertir PDF a libro de Excel en Python
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-python/
description: Aprenda a convertir documentos PDF en libros de Excel en Python usando Aspose.PDF para la extracción de datos estructurados.
lastmod: "2026-06-09"
---

Para convertir un documento PDF a un libro de Excel usando **Aspose.PDF Java para Python**, simplemente invoque el módulo **PdfToExcel**.


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


**Descargar código de ejecución**

Descargue **Convierta PDF a libro de Excel (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)
