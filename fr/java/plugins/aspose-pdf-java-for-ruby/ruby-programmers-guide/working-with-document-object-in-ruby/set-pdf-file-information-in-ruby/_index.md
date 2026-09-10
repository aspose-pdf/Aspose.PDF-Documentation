---
title: Définir les informations du fichier PDF dans Ruby
linktitle: Définir les informations du fichier PDF dans Ruby
type: docs
weight: 120
url: /java/set-pdf-file-information-in-ruby/
description: Définissez et mettez à jour par programmation les métadonnées PDF telles que le titre, l'auteur et les mots-clés à l'aide de Ruby.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Définir les informations du fichier PDF



Pour mettre à jour les informations du document PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **SetPdfFileInfo**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF for java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("PDF Information")

doc_info.setTitle("Setting PDF Document Information")

# save update document with new information

doc.save(data_dir + "Updated_Information.pdf")

puts "Update document information, please check output file."
```

## 
Télécharger le code d'exécution



Téléchargez** Définir les informations du fichier PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)
