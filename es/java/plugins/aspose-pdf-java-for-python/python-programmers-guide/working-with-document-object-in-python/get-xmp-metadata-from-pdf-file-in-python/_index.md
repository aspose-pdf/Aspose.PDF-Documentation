---
title: Obtener metadatos XMP de un archivo PDF en Python
linktitle: Obtener metadatos XMP de un archivo PDF en Python
type: docs
weight: 50
url: /es/java/get-xmp-metadata-from-pdf-file-in-python/
description: Descubra cómo recuperar los metadatos XMP de un archivo PDF en Python usando Aspose.PDF, lo que permite un análisis detallado del contenido.
lastmod: "2026-09-03"
---
Para obtener metadatos XMP de un documento Pdf usando **Aspose.PDF Java for Python**, simplemente invoque la clase **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get properties
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**Descargar código en ejecución**

DescargarВ **Get XMP Metadata (Aspose.PDF)**В desdeВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)
