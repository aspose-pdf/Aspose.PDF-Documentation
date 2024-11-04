---
title: Eliminar Metadatos de PDF en Python
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-python/
lastmod: "2021-06-05"
---

Para eliminar metadatos de un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoque la clase **RemoveMetadata**.

```python

doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/', doc.getMetadata())):
    doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/', doc.getMetadata())):
    doc.getMetadata().removeItem("dc:format")


# guardar el documento actualizado con la nueva información
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Metadatos eliminados con éxito, por favor verifique el archivo de salida."

```

**Descargar Código en Ejecución**

Descargue **Eliminar Metadatos (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)