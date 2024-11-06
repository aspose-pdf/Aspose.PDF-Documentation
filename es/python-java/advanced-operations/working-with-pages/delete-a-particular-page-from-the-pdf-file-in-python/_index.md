---
title: Eliminar una Página Particular del Archivo PDF en Python
type: docs
weight: 20
url: es/python-java/delete-a-particular-page-from-the-pdf-file-in-python/
---

Para eliminar una página particular del documento PDF usando **Aspose.PDF Java para Python**, simplemente invoca la clase **DeletePage**.

```python
doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'input1.pdf'

# eliminar una página particular
pdf.getPages().delete(2)

# guardar el archivo PDF recién generado
doc.save(self.dataDir + "output.pdf")

print "¡Página eliminada exitosamente!"

```

**Descargar Código en Ejecución**

Descargar **Eliminar Página (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)