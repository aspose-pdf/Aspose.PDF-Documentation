---
title: Obtener información del archivo PDF en Python
linktitle: Obtener información del archivo PDF en Python
type: docs
weight: 40
url: /es/java/get-pdf-file-information-in-python/
description: Explore cómo obtener información detallada del archivo PDF, como metadatos y propiedades, en Python usando Aspose.PDF para la gestión de documentos.
lastmod: "2026-09-03"
---
Para obtener información del archivo de documento Pdf usando **Aspose.PDF Java for Python**, simplemente invoque la clase **GetPdfFileInfo**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

# Show document information
print "Author:-" + str(doc_info.getAuthor())
print "Creation Date:-" + str(doc_info.getCreationDate())
print "Keywords:-" + str(doc_info.getKeywords())
print "Modify Date:-" + str(doc_info.getModDate())
print "Subject:-" + str(doc_info.getSubject())
print "Title:-" + str(doc_info.getTitle())
```

**Descargar código en ejecución**

DescargarВ **Obtener información del archivo PDF (Aspose.PDF)**В deВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
