---
title: Obtenga metadatos XMP de un archivo PDF en Python
linktitle: Obtenga metadatos XMP de un archivo PDF en Python
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-python/
description: Descubra cómo recuperar metadatos XMP de un archivo PDF en Python usando Aspose.PDF, lo que permite un análisis de contenido detallado.
lastmod: "2026-06-09"
---

Para obtener metadatos XMP de un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoque la clase **GetXMPMetadata**.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get properties
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```


**Descargar código de ejecución**

DescargarВ **Obtener metadatos XMP (Aspose.PDF)**В de cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)
