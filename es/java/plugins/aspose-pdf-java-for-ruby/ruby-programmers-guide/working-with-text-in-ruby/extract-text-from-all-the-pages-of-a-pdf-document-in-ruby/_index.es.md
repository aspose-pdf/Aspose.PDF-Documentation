---
title: Extraer Texto de Todas las Páginas de un Documento PDF en Ruby
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Extraer Texto de Todas las Páginas

Para extraer texto de todas las páginas de un documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **ExtractTextFromAllPages**.

Código Ruby

```java
# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir el documento objetivo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# crear un objeto TextAbsorber para extraer texto

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# aceptar el absorber para todas las páginas

pdf.getPages().accept(text_absorber)

# Para extraer texto de una página específica del documento, necesitamos especificar la página particular utilizando su índice contra el método accept(..).

# aceptar el absorber para una página particular del PDF

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# obtener el texto extraído

extracted_text = text_absorber.getText()

# crear un escritor y abrir el archivo

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# escribir una línea de texto en el archivo

# tw.WriteLine(extractedText);

# cerrar el flujo

writer.close()

puts "Texto extraído exitosamente. Verifique el archivo de salida."
```


## Descargar Código en Ejecución

Descargar **Extraer Texto de Todas las Páginas (Aspose.PDF)** desde cualquiera de los sitios sociales de codificación mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)