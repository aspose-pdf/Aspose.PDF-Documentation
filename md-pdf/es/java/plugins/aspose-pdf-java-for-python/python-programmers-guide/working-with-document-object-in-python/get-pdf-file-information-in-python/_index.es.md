---
title: Obtener Información del Archivo PDF en Python
type: docs
weight: 40
url: /java/get-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

Para obtener la información del archivo de un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoca la clase **GetPdfFileInfo**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obtener información del documento
doc_info = doc.getInfo();

# Mostrar información del documento
print "Autor:-" + str(doc_info.getAuthor())
print "Fecha de creación:-" + str(doc_info.getCreationDate())
print "Palabras clave:-" + str(doc_info.getKeywords())
print "Fecha de modificación:-" + str(doc_info.getModDate())
print "Asunto:-" + str(doc_info.getSubject())
print "Título:-" + str(doc_info.getTitle())
```

**Descargar Código en Ejecución**

Descarga **Obtener Información del Archivo PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)