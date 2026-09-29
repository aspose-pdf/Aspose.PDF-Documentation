---
title: Establecer información del archivo PDF en Python
linktitle: Establecer información del archivo PDF en Python
type: docs
weight: 90
url: /es/java/set-pdf-file-information-in-python/
description: Aprenda cómo establecer la información del archivo PDF, como autor, título y más, en Python usando Aspose.PDF para organizar documentos.
lastmod: "2026-09-29"
---
Para actualizar la información del documento PDF usando **Aspose.PDF Java for Python**, simplemente invoque la clase **SetPdfFileInfo**.

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

**Descargar código en ejecución**

Descargar **Establecer la información del archivo PDF (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
