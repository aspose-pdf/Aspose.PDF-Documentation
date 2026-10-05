---
title: Supprimer une page particulière du fichier PDF en Ruby
linktitle: Supprimer une page particulière du fichier PDF en Ruby
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-ruby/
description: Supprimez des pages spécifiques des fichiers PDF par programme à l'aide d'Aspose.PDF pour Ruby.
lastmod: "2026-09-21"
---
## Aspose.PDF - Supprimer la page

Pour supprimer une page particulière du document PDF à l'aide de **Aspose.PDF Java pour Ruby**, utilisez le module **DeletePage**.

Code Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# delete a particular page

pdf.getPages().delete(2)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Page deleted successfully!"
```

## Télécharger l’exemple de code

Téléchargez **Supprimer la page (Aspose.PDF)** à partir de l'un des plateformes d’hébergement de code mentionnées ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)
