---
title: Obtener Metadatos XMP de un Archivo PDF en Python
type: docs
weight: 50
url: es/java/get-xmp-metadata-from-pdf-file-in-python/
lastmod: "2021-06-05"
---

Para obtener Metadatos XMP de un documento Pdf usando **Aspose.PDF Java para Python**, simplemente invoque la clase **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obtener propiedades
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**Descargar Código en Ejecución**

Descargue **Obtener Metadatos XMP (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)