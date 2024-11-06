---
title: Actualizar Dimensiones de Página en Python
type: docs
weight: 90
url: es/python-java/update-page-dimensions-in-python/
---

<ins>Para actualizar las dimensiones de página usando **Aspose.PDF Java para Python**, simplemente invoque la clase **UpdatePageDimensions**.

**Código Python**
```s
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# obtener la colección de páginas
page_collection = pdf.getPages()

# obtener una página en particular
pdf_page = page_collection.get_Item(1)

# establecer el tamaño de la página como A4 (11.7 x 8.3 in) y en Aspose.PDF, 1 pulgada = 72 puntos
# así que las dimensiones A4 en puntos serán (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# guardar el archivo PDF recién generado
pdf.save(self.dataDir + "output.pdf")

print "¡Dimensiones actualizadas con éxito!"

```

**Descargar Código en Ejecución**

Descargar **Actualizar Dimensiones de Página (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)