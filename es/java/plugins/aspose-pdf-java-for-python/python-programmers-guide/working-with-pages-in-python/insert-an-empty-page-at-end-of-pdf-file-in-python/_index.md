---
title: Insertar una Página Vacía al Final del Archivo PDF en Python
type: docs
weight: 60
url: es/java/insert-an-empty-page-at-end-of-pdf-file-in-python/
lastmod: "2021-06-05"
---

Para insertar una página vacía al final de un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoque la clase **InsertEmptyPageAtEndOfFile**.

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insertar una página vacía en un PDF
pdf_document.getPages().add();

# Guardar el archivo de salida concatenado (el documento objetivo)
pdf_document.save(self.dataDir + "output.pdf")

print "¡Página vacía añadida exitosamente!"

```

**Descargar Código en Ejecución**

Descargue **Insertar una Página Vacía al Final del Archivo PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)