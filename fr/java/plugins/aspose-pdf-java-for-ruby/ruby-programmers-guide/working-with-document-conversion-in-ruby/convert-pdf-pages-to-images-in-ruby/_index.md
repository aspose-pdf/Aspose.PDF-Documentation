---
title: Convertir des pages PDF en images dans Ruby
linktitle: Convertir des pages PDF en images dans Ruby
type: docs
weight: 20
url: /java/convert-pdf-pages-to-images-in-ruby/
description: Découvrez comment convertir des pages PDF en images à l'aide de Ruby avec Aspose.PDF, facilitant ainsi l'extraction de contenu visuel à partir de PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir des pages PDF en images



Pour convertir toutes les pages en images d'un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **ConvertPagesToImages**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

В В В  converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

В В В  image_count +=1

end

puts "PDF pages are converted to individual images successfully!"
```

## 
Télécharger le code d'exécution



Téléchargez** Convertir des pages PDF en images (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)
