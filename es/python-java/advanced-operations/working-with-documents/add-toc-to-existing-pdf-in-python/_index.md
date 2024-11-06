---
title: Añadir TOC a un PDF Existente en Python
type: docs
weight: 20
url: es/python-java/add-toc-to-existing-pdf-in-python/
---

Para añadir TOC en un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoca la clase **AddToc**.

```python

# Abrir un documento pdf.
doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'input1.pdf'

# Obtener acceso a la primera página del archivo PDF
toc_page = doc.getPages().insert(1)

# Crear objeto para representar la información de TOC
toc_info = self.TocInfo()
title = self.TextFragment("Tabla de Contenidos")
title.getTextState().setFontSize(20)

# Establecer el título para TOC
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# Crear objetos de cadena que se utilizarán como elementos de TOC
titles = ["Primera página", "Segunda página"]

i = 0;
while (i < 2):

# Crear objeto de Encabezado
heading2 = self.Heading(1)

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# Especificar la página de destino para el objeto de encabezado
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# Página de destino
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# Coordenada de destino
segment2.setText(titles[i])

# Añadir encabezado a la página que contiene TOC
toc_page.getParagraphs().add(heading2)

i +=1

# Guardar Documento PDF
doc.save(self.dataDir + "TOC.pdf")

print "TOC añadido exitosamente, por favor revise el archivo de salida."
```


**Descargar Código en Ejecución**

Descargar **Agregar TOC (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)