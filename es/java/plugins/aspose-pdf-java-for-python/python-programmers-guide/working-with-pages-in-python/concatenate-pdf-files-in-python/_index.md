---
title: Concatenar archivos PDF en Python
type: docs
weight: 10
url: /es/java/concatenate-pdf-files-in-python/
lastmod: "2021-06-05"
---

Para concatenar archivos PDF usando **Aspose.PDF Java para Python**, simplemente invoca la clase **ConcatenatePdfFiles**.

```python
doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'input1.pdf'

# Abrir el documento fuente
pdf1 = self.Document()
pdf1 = self.dataDir + 'input2.pdf'

# Agregar las páginas del documento fuente al documento de destino
pdf1.getPages().add(pdf1.getPages())

# Guardar el archivo de salida concatenado (el documento de destino)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "El nuevo documento ha sido guardado, por favor revise el archivo de salida"
```

**Descargar código en ejecución**

Descarga **Concatenar archivos PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)