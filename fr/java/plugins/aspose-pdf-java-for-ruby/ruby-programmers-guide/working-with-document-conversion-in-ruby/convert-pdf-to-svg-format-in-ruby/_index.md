---
title: Convertir un PDF au format SVG dans Ruby
linktitle: Convertir un PDF au format SVG dans Ruby
type: docs
weight: 50
url: /java/convert-pdf-to-svg-format-in-ruby/
description: Découvrez comment convertir des fichiers PDF au format SVG à l'aide de Ruby et Aspose.PDF, permettant des graphiques vectoriels évolutifs et modifiables.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir un PDF en SVG



Pour convertir un PDF au format SVG à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **PdfToSvg**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# instantiate an object of SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# do not compress SVG image to Zip archive

save_options.CompressOutputToZipArchive = false

# Save the output to XLS format

pdf.save(data_dir + "Output.svg", save_options)

puts "Document has been converted successfully"
```

## 
Télécharger le code d'exécution



Téléchargez** Convertir un PDF au format SVG (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)
