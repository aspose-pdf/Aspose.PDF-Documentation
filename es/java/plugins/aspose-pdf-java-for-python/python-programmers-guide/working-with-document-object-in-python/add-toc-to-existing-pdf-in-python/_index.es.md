---
title: Añadir TOC a un PDF existente en Python
type: docs
weight: 20
url: /java/add-toc-to-existing-pdf-in-python/
lastmod: "2021-06-05"
---

Para añadir TOC en un documento PDF usando **Aspose.PDF Java para Python**, simplemente invoque la clase **AddToc**.

```python

# Abrir un documento pdf.
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Obtener acceso a la primera página del archivo PDF
toc_page = doc.getPages().insert(1)

# Crear objeto para representar la información del TOC
toc_info = self.TocInfo()
title = self.TextFragment("Tabla de Contenidos")
title.getTextState().setFontSize(20)

# Establecer el título para el TOC
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# Crear objetos de cadena que se utilizarán como elementos del TOC
titles = ["Primera página", "Segunda página"]

i = 0;
while (i < 2):

# Crear objeto de Encabezado
heading2 = self.Heading(1);

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# Especificar la página de destino para el objeto de encabezado
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# Página de destino
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# Coordenada de destino
segment2.setText(titles[i])

# Añadir encabezado a la página que contiene el TOC
toc_page.getParagraphs().add(heading2)

i +=1;

# Guardar Documento PDF
doc.save(self.dataDir + "TOC.pdf")

print "TOC añadido con éxito, por favor revise el archivo de salida."
```


**Descargar Código en Ejecución**

Descargue **Agregar TOC (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)