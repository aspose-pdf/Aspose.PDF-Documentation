---
title: Eliminar metadatos de PDF en Python
linktitle: Eliminar metadatos de PDF en Python
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-python/
description: Descubra cómo eliminar metadatos de documentos PDF en Python usando Aspose.PDF, garantizando la privacidad y la seguridad de los datos.
lastmod: "2026-06-09"
---

Para eliminar metadatos de un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoque la clase **RemoveMetadata**.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# save update document with new information
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Removed metadata successfully, please check output file."

```


**Descargar código de ejecución**

DescargarВ **Eliminar metadatos (Aspose.PDF)**В de cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)
