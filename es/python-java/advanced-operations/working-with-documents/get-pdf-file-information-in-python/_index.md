---
title: Obtener Información de Archivos PDF en Python
type: docs
weight: 40
url: es/python-java/get-pdf-file-information-in-python/
---

<ins>Para obtener información de archivo de un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoca la clase **GetPdfFileInfo**.

**Código Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obtener información del documento
doc_info = doc.getInfo();

# Mostrar información del documento
print "Autor:-" + str(doc_info.getAuthor())
print "Fecha de Creación:-" + str(doc_info.getCreationDate())
print "Palabras clave:-" + str(doc_info.getKeywords())
print "Fecha de Modificación:-" + str(doc_info.getModDate())
print "Asunto:-" + str(doc_info.getSubject())
print "Título:-" + str(doc_info.getTitle())
```

**Descargar Código en Ejecución**

Descargar **Obtener Información de Archivo PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)