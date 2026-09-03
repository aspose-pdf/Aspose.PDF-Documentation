---
title: Establecer la caducidad de PDF en Python
linktitle: Establecer la caducidad de PDF en Python
type: docs
weight: 80
url: /java/set-pdf-expiration-in-python/
description: Aprenda a establecer una fecha de vencimiento para un archivo PDF en Python usando Aspose.PDF para acceder a documentos urgentes.
lastmod: "2026-06-09"
---

Para establecer la caducidad de un documento PDF utilizando **Aspose.PDF Java para Python**, simplemente invoque la clase **SetExpiration**.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# save update document with new information
doc.save(self.dataDir + "set_expiration.pdf");

print "Update document information, please check output file."
```


**Descargar código de ejecución**

Descargue **Establecer caducidad de PDF (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
