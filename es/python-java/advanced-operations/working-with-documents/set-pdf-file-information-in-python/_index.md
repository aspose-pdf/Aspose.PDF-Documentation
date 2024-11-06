---
title: Establecer Información del Archivo PDF en Python
type: docs
weight: 90
url: es/python-java/set-pdf-file-information-in-python/
---

<ins>Para actualizar la información del documento PDF usando **Aspose.PDF Java for Python**, simplemente invoca la clase **SetPdfFileInfo**.

**Código Python**
```
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obtener información del documento
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF para java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("Información del PDF");
doc_info.setTitle("Estableciendo Información del Documento PDF");

# guardar documento actualizado con nueva información

doc.save(self.dataDir + "Updated_Information.pdf")
print "Actualizar la información del documento, por favor verifique el archivo de salida."
```

**Descargar Código en Ejecución**

Descargar **Establecer Información del Archivo PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)