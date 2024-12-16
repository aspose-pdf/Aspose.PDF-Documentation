---
title: Eliminar Metadatos de PDF en Python
type: docs
weight: 70
url: /es/python-java/remove-metadata-from-pdf-in-python/
---

<ins>Para eliminar metadatos de un documento PDF utilizando **Aspose.PDF Java para Python**, simplemente invoque la clase **RemoveMetadata**.

**Código Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# guardar el documento actualizado con nueva información
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Metadatos eliminados exitosamente, por favor revise el archivo de salida."
```


**Descargar Código en Ejecución**

Descargue **Eliminar Metadatos (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)