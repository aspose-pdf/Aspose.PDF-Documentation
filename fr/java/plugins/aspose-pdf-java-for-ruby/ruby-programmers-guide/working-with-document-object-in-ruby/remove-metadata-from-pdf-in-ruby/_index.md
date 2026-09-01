---
title: Supprimer les métadonnées du PDF dans Ruby
linktitle: Supprimer les métadonnées du PDF dans Ruby
type: docs
weight: 90
url: /java/remove-metadata-from-pdf-in-ruby/
description: Effacez les métadonnées sensibles ou indésirables des fichiers PDF par programme avec Aspose.PDF pour Ruby.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Supprimer les métadonnées



Pour supprimer les métadonnées d'un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **RemoveMetadata**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

В В В  doc.getMetadata().removeItem("pdfaid:part")

endВ В  В

if doc.getMetadata().contains("dc:format")

В В В  doc.getMetadata().removeItem("dc:format")

end

# save update document with new information

doc.save(data_dir + "Remove_Metadata.pdf")

puts "Removed metadata successfully, please check output file."
```

## 
Télécharger le code d'exécution



Téléchargez** Supprimer les métadonnées (Aspose.PDF)** de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)
