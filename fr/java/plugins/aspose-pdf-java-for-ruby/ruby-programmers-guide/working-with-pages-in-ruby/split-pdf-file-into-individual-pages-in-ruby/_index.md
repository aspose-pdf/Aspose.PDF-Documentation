---
title: Diviser un fichier PDF en pages individuelles dans Ruby
linktitle: Diviser un fichier PDF en pages individuelles dans Ruby
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-ruby/
description: Comprenez comment diviser un fichier PDF en pages individuelles avec Ruby et Aspose.PDF, facilitant ainsi la gestion et l'extraction du contenu.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Pages divisées



Pour diviser un document PDF en pages individuelles à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **SplitAllPages**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# loop through all the pages

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# get the page at particular index of Page Collection

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "Split process completed successfully!"
```

## 
Télécharger le code d'exécution



Téléchargez **Split Pages (Aspose.PDF)**В à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)
