---
title: Convertir un fichier SVG au format PDF dans Ruby
linktitle: Convertir un fichier SVG au format PDF dans Ruby
type: docs
weight: 60
url: /java/convert-svg-file-to-pdf-format-in-ruby/
description: Apprenez à convertir des fichiers SVG au format PDF dans Ruby à l'aide d'Aspose.PDF pour une transformation de document précise et évolutive.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir SVG en PDF



Pour convertir un fichier SVG au format PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **SvgToPdf**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate LoadOption object using SVG load option

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Create document object

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Save the output to XLS format

pdf.save(data_dir + "SVG.pdf")

puts "Document has been converted successfully"
```

## 
Télécharger le code d'exécution



Téléchargez** Convertir SVG en PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)
