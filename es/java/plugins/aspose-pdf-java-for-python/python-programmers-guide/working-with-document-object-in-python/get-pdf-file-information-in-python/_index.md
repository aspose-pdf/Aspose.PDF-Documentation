---
title: Obtener información de archivos PDF en Python
linktitle: Obtener información de archivos PDF en Python
type: docs
weight: 40
url: /java/get-pdf-file-information-in-python/
description: Explore cómo recuperar información detallada de un archivo PDF, como metadatos y propiedades, en Python utilizando Aspose.PDF para la gestión de documentos.
lastmod: "2026-06-09"
---

Para obtener información del archivo de un documento PDF utilizando **Aspose.PDF Java para Python**, simplemente invoque la clase **GetPdfFileInfo**.


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


**Descargar código de ejecución**

DescargarВ **Obtener información del archivo PDF (Aspose.PDF)**В de cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
