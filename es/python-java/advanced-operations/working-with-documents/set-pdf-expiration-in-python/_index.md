---
title: Establecer Expiración de PDF en Python
type: docs
weight: 80
url: /es/python-java/set-pdf-expiration-in-python/
---

<ins>Para establecer la expiración de un documento Pdf utilizando **Aspose.PDF Java para Python**, simplemente invoque la clase **SetExpiration**.

**Código Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2014; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('El archivo ha expirado. Necesitas uno nuevo.');");

doc.setOpenAction(javascript);

# guardar documento actualizado con nueva información
doc.save(self.dataDir + "set_expiration.pdf");

print "Actualizar información del documento, por favor revisa el archivo de salida."
```

**Descargar Código en Ejecución**

Descargar **Establecer Expiración de PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)

```python
# Este script establece una fecha de expiración para el documento
import aspose.pdf as ap

# Crear un nuevo documento PDF
documento = ap.Document()

# Configurar propiedades de expiración del documento
documento.información.expiración = "2023-12-31"

# Guardar documento
documento.guardar("DocumentoConExpiracion.pdf")