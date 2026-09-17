---
title: Convertir un PDF au format DOC ou DOCX dans Ruby
linktitle: Convertir un PDF au format DOC ou DOCX dans Ruby
type: docs
weight: 30
url: /java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: Apprenez à convertir des documents PDF aux formats DOC ou DOCX dans Ruby avec Aspose.PDF, permettant une édition et un traitement plus faciles.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir un PDF en DOC ou DOCX



Pour convertir un document PDF au format DOC ou DOCX à l'aide de **Aspose.PDF Java for Ruby**, invoquez simplement le module **PdfToDoc**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Save the concatenated output file (the target document)

pdf.save(data_dir + "output.doc")

puts "Document has been converted successfully"
```

## 
Télécharger le code d'exécution



Téléchargez** Convertir un PDF en DOC ou DOCX (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)
