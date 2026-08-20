---
title: Dividir un archivo PDF en páginas individuales en Ruby
linktitle: Dividir un archivo PDF en páginas individuales en Ruby
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-ruby/
description: Comprenda cómo dividir un archivo PDF en páginas individuales con Ruby y Aspose.PDF, lo que facilita la administración y extracción de contenido.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Dividir páginas



Para dividir un documento PDF en páginas individuales usando **Aspose.PDF Java para Ruby**, simplemente invoque el módulo **SplitAllPages**.

Código Rubí


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# loop through all the pages

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# get the page at particular index of Page Collection

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "Split process completed successfully!"
```

## 
Descargar código de ejecución



Descargue **Split Pages (Aspose.PDF)** de cualquiera de los sitios de codificación social mencionados a continuación:


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)
