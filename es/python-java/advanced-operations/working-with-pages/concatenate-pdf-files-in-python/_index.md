---
title: Concatenar Archivos PDF en Python
type: docs
weight: 10
url: es/python-java/concatenate-pdf-files-in-python/
---

Para concatenar archivos PDF usando **Aspose.PDF Java para Python**, simplemente invoca la clase **ConcatenatePdfFiles**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Abre el documento fuente
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Agrega las páginas del documento fuente al documento de destino
pdf1.getPages().add(pdf1.getPages())

# Guarda el archivo de salida concatenado (el documento de destino)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "El nuevo documento ha sido guardado, por favor revisa el archivo de salida"
```


**Descargar Código en Ejecución**

Descargar **Concatenar Archivos PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)