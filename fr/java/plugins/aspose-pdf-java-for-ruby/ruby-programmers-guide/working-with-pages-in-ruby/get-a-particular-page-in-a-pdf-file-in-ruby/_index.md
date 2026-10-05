---
title: Obtenir une page particulière dans un fichier PDF en Ruby
linktitle: Obtenir une page particulière dans un fichier PDF en Ruby
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-ruby/
description: Accédez et manipulez des pages individuelles dans des documents PDF à l'aide de Ruby et Aspose.PDF.
lastmod: "2026-09-21"
---
## Aspose.PDF - Obtenir la page

Pour obtenir une page particulière dans un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, utilisez le module **GetPage**.

Code Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get the page at particular index of Page Collection

pdf_page = pdf.getPages().get_Item(1)

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# add page to pages collection of new document object

new_document.getPages().add(pdf_page)

# save the newly generated PDF file

new_document.save(data_dir + "output.pdf")

puts "Process completed successfully!"
```

## Télécharger l’exemple de code

Téléchargez **Obtenir la page (Aspose.PDF)** à partir de l'un des plateformes d’hébergement de code mentionnées ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)
