---
title: Concaténer des fichiers PDF dans Ruby
linktitle: Concaténer des fichiers PDF dans Ruby
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-ruby/
description: Combinez efficacement plusieurs PDF en un seul document à l’aide de Ruby et Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Concaténer des fichiers PDF



Pour concaténer des fichiers PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **ConcatenatePdfFiles**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Open the source document

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Add the pages of the source document to the target document

pdf1.getPages().add(pdf2.getPages())

# Save the concatenated output file (the target document)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "New document has been saved, please check the output file"
```

## 
Télécharger le code d'exécution



Téléchargez** Concaténer des fichiers PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)
