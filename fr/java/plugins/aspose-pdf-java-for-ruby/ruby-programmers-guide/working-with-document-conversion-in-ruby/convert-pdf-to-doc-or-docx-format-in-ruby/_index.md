---
title: Convertir un PDF au format DOC ou DOCX en Ruby
linktitle: Convertir un PDF au format DOC ou DOCX en Ruby
type: docs
weight: 30
url: /java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: Apprenez à convertir des documents PDF aux formats DOC ou DOCX en Ruby avec Aspose.PDF, permettant une édition et un traitement plus faciles.
lastmod: "2026-09-21"
---
## Aspose.PDF - Convertir un PDF en DOC ou DOCX

Pour convertir un document PDF au format DOC ou DOCX à l'aide de **Aspose.PDF Java for Ruby**, utilisez le module **PdfToDoc**.

Code Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Save the concatenated output file (the target document)

pdf.save(data_dir + "output.doc")

puts "Document has been converted successfully"
```

## Télécharger l’exemple de code

Téléchargez **Convertir un PDF en DOC ou DOCX (Aspose.PDF)** à partir de l'un des plateformes d’hébergement de code mentionnées ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)
