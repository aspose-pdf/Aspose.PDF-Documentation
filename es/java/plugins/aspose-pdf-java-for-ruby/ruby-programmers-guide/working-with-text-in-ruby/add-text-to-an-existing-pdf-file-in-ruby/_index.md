---
title: Agregar Texto a un archivo PDF existente en Ruby
type: docs
weight: 20
url: /es/java/add-text-to-an-existing-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Agregar Texto

Para agregar una cadena de texto en un documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **AddText**.

Código Ruby

```java

# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instanciar objeto Document

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# obtener página particular

pdf_page = doc.getPages().get_Item(1)

# crear fragmento de texto

text_fragment = Rjb::import('com.aspose.pdf.TextFragment').new("texto principal")

text_fragment.setPosition(Rjb::import('com.aspose.pdf.Position').new(100, 600))

font_repository = Rjb::import('com.aspose.pdf.FontRepository')

color = Rjb::import('com.aspose.pdf.Color')

# establecer propiedades de texto

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))

text_fragment.getTextState().setFontSize(14)

#text_fragment.getTextState().setForegroundColor(color.BLUE)

#text_fragment.getTextState().setBackgroundColor(color.GRAY)

# crear objeto TextBuilder

text_builder = Rjb::import('com.aspose.pdf.TextBuilder').new(pdf_page)

# agregar el fragmento de texto a la página PDF

text_builder.appendText(text_fragment)

# Guardar archivo PDF

doc.save(data_dir + "Text_Added.pdf")

puts "Texto agregado exitosamente"
```


## Descargar Código en Ejecución

Descargue **Agregar Texto (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addtext.rb)