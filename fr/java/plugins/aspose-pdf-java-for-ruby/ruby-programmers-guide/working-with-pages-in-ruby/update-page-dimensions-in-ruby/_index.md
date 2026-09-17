---
title: Mettre à jour les dimensions de la page dans Ruby
linktitle: Mettre à jour les dimensions de la page dans Ruby
type: docs
weight: 90
url: /java/update-page-dimensions-in-ruby/
description: Découvrez comment mettre à jour les dimensions de la page d'un document PDF à l'aide de Ruby avec Aspose.PDF pour un formatage de page précis.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Mettre à jour les dimensions de la page



Pour mettre à jour les dimensions de la page à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **UpdatePageDimensions**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get page collection

page_collection = pdf.getPages()

# get particular page

pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points

# so A4 dimensions in points will be (842.4, 597.6)

pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Dimensions updated successfully!"
```

## 
Télécharger le code d'exécution



Téléchargez** Mettre à jour les dimensions de la page (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)
