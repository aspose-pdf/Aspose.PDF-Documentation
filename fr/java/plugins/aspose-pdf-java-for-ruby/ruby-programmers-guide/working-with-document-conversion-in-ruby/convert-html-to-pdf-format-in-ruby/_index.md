---
title: Convertir HTML au format PDF en Ruby
linktitle: Convertir HTML au format PDF en Ruby
type: docs
weight: 10
url: /java/convert-html-to-pdf-format-in-ruby/
description: Découvrez comment convertir du contenu HTML au format PDF en Ruby à l'aide d'Aspose.PDF pour une génération de documents fiable et précise.
lastmod: "2026-09-21"
---
## Aspose.PDF - Convertir le HTML au format PDF

Pour convertir du HTML au format PDF à l'aide de **Aspose.PDF Java pour Ruby**, utilisez le module **HtmlToPdf**.

Code Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Load HTML file

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Save the concatenated output file (the target document)

pdf.save(data_dir + "html.pdf")

puts "Document has been converted successfully"
```

## Télécharger l’exemple de code

Téléchargez **Convertir le HTML au format PDF (Aspose.PDF)** à partir de l'un des plateformes d’hébergement de code mentionnées ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)
