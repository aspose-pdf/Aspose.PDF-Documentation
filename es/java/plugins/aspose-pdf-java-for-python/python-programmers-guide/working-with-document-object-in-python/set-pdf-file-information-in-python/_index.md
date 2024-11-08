---
title: Establecer Información del Archivo PDF en Python
type: docs
weight: 90
url: /es/java/set-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

Para actualizar la información del documento Pdf utilizando **Aspose.PDF Java para Python**, simplemente invoque la clase **SetPdfFileInfo**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obtener información del documento
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("Información PDF");
doc_info.setTitle("Estableciendo Información del Documento PDF");

# guardar documento actualizado con nueva información

doc.save(self.dataDir + "Updated_Information.pdf")
print "Actualizar información del documento, por favor revise el archivo de salida."
```

**Descargar Código en Ejecución**

Descargar **Establecer Información del Archivo PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)