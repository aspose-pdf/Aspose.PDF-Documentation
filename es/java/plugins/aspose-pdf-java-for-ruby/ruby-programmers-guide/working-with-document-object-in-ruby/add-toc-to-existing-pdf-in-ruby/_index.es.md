---
title: Agregar TOC a PDF Existente en Ruby
type: docs
weight: 30
url: /java/add-toc-to-existing-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Agregar TOC

<ins>Para agregar TOC en un documento PDF usando **Aspose.PDF Java for Ruby**, simplemente invoca el módulo **AddToc**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir un documento pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obtener acceso a la primera página del archivo PDF

toc_page = doc.getPages().insert(1)

# Crear objeto para representar la información del TOC

toc_info = Rjb::import('com.aspose.pdf.TocInfo').new

title = Rjb::import('com.aspose.pdf.TextFragment').new("Tabla de Contenidos")

title.getTextState().setFontSize(20)

#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Establecer el título para el TOC

toc_info.setTitle(title)

toc_page.setTocInfo(toc_info)

# Crear objetos de cadena que se usarán como elementos del TOC

titles = Array["Primera página", "Segunda página"]

i = 0

while i < 2

    # Crear objeto Heading

    heading2 = Rjb::import('com.aspose.pdf.Heading').new(1)

    segment2 = Rjb::import('com.aspose.pdf.TextSegment').new

    heading2.setTocPage(toc_page)

    heading2.getSegments().add(segment2)

    # Especificar la página de destino para el objeto heading

    heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

    # Página de destino

    heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

    # Coordenada de destino

    segment2.setText(titles[i])

    # Agregar heading a la página que contiene el TOC

    toc_page.getParagraphs().add(heading2)

    i +=1

end

# Guardar documento PDF

doc.save(data_dir + "TOC.pdf")

puts "TOC agregado exitosamente, por favor revisa el archivo de salida."
```


## <ins> **Descargar Código en Ejecución

Descargar **Agregar TOC (Aspose.PDF)** desde cualquiera de los siguientes sitios de codificación social:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addtoc.rb)