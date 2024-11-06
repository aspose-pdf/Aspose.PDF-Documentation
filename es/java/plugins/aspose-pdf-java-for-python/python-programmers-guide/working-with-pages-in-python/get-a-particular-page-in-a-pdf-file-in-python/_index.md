---
title: Obtener una Página Particular en un Archivo PDF en Python
type: docs
weight: 30
url: es/java/get-a-particular-page-in-a-pdf-file-in-python/
lastmod: "2021-06-05"
---

Para obtener una página particular en un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoca la clase **GetPage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# obtener la página en un índice particular de la Colección de Páginas
pdf_page = pdf.getPages().get_Item(1)

# crear un nuevo objeto Document
new_document = self.Document()

# añadir página a la colección de páginas del nuevo objeto documento
new_document.getPages().add(pdf_page)

# guardar el archivo PDF recién generado
new_document.save(self.dataDir + "output.pdf")

print "¡Proceso completado con éxito!

```

 **Descargar Código en Ejecución**

Descargar **Obtener Página (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)