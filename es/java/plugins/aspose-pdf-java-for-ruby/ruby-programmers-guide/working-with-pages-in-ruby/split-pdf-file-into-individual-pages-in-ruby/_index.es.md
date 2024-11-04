---
title: Dividir archivo PDF en páginas individuales en Ruby
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dividir Páginas

Para dividir un documento PDF en páginas individuales usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **SplitAllPages**.

Código Ruby

```java

# La ruta al directorio de documentos.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Abrir el documento objetivo

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# bucle a través de todas las páginas

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# crear un nuevo objeto Document

new_document = Rjb::import('com.aspose.pdf.Document').new

# obtener la página en un índice particular de la Colección de Páginas

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# guardar el archivo PDF recién generado

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "¡El proceso de división se completó con éxito!"
```


## Descargar Código en Ejecución

Descargue **Dividir Páginas (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)