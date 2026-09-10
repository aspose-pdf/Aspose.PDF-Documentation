---
title: Obtenir des informations sur un fichier PDF dans Ruby
linktitle: Obtenir des informations sur un fichier PDF dans Ruby
type: docs
weight: 50
url: /java/get-pdf-file-information-in-ruby/
description: Extrayez les métadonnées et les détails des fichiers PDF par programme à l'aide d'Aspose.PDF dans Ruby.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtenir des informations sur le fichier PDF



Pour obtenir les informations sur le fichier d'un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **GetPdfFileInfo**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

# Show document information

puts "Author:-" + doc_info.getAuthor().to_s

puts "Creation Date:-" + doc_info.getCreationDate().to_string

puts "Keywords:-" + doc_info.getKeywords().to_s

puts "Modify Date:-" + doc_info.getModDate().to_string

puts "Subject:-" + doc_info.getSubject().to_s

puts "Title:-" + doc_info.getTitle().to_s
```

## 
Télécharger le code d'exécution



Téléchargez** Obtenez des informations sur le fichier PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)
