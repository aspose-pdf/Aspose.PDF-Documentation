---
title: Convertir les pages PDF en images en Ruby
type: docs
weight: 20
url: fr/java/convert-pdf-pages-to-images-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir les pages PDF en images

Pour convertir toutes les pages d'un document PDF en images en utilisant **Aspose.PDF Java for Ruby**, il suffit d'invoquer le module **ConvertPagesToImages**.

Code Ruby

```java

# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

    converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

    image_count +=1

end

puts "Les pages PDF sont converties en images individuelles avec succès!"
```

## Télécharger le code en cours d'exécution

Téléchargez **Convertir les pages PDF en images (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)