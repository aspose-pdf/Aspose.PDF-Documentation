---
title: Convertir PDF a Libro de Excel en Python
type: docs
weight: 20
url: /es/java/convert-pdf-to-excel-workbook-in-python/
lastmod: "2021-06-05"
---

Para convertir un documento PDF a un Libro de Excel usando **Aspose.PDF Java para Python**, simplemente invoca el módulo **PdfToExcel**.

```python

doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# Instanciar objeto de opción de guardado en Excel
excelsave=self.ExcelSaveOptions();

# Guardar el resultado en formato XLS
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
print "El documento ha sido convertido con éxito"
```

**Descargar Código en Ejecución**

Descargar **Convertir PDF a Libro de Excel (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)