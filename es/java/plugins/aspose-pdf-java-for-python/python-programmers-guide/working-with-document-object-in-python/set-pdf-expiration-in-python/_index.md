---
title: Establecer expiración de PDF en Python
linktitle: Establecer expiración de PDF en Python
type: docs
weight: 80
url: /es/java/set-pdf-expiration-in-python/
description: Aprenda cómo establecer una fecha de vencimiento para un archivo PDF en Python usando Aspose.PDF para acceso a documentos sensibles al tiempo.
lastmod: "2026-09-03"
---
Para establecer la expiración deВ  documento PDF usando **Aspose.PDF Java for Python**, simplemente invoque la clase **SetExpiration**.

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

**Descargar Código en Ejecución**

DescargarВ **Establecer vencimiento de PDF (Aspose.PDF)**В de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
