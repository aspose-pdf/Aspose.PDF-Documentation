---
title: Establecer Expiración de PDF en Python
type: docs
weight: 80
url: /java/set-pdf-expiration-in-python/
lastmod: "2021-06-05"
---

Para establecer la expiración de un documento Pdf usando **Aspose.PDF Java para Python**, simplemente invoque la clase **SetExpiration**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('El archivo está expirado. Necesita uno nuevo.');");

doc.setOpenAction(javascript);

# guardar documento actualizado con nueva información
doc.save(self.dataDir + "set_expiration.pdf");

print "Actualizar la información del documento, por favor revise el archivo de salida."
```

**Descargar Código en Ejecución**

Descargue **Establecer Expiración de PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)