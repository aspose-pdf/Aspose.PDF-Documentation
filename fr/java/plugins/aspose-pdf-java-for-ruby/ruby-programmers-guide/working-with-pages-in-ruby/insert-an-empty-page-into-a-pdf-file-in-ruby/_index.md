---
title: Insérer une page vide dans un fichier PDF en Ruby
linktitle: Insérer une page vide dans un fichier PDF en Ruby
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-ruby/
description: Découvrez comment insérer une page vide dans un emplacement spécifique d'un document PDF à l'aide de Ruby et Aspose.PDF pour une gestion précise des documents.
lastmod: "2026-09-21"
---
## Aspose.PDF - Insérer une page vide

Pour insérer une page vide dans un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, utilisez le module **InsertEmptyPage**.

Code Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().insert(1)

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## Télécharger l’exemple de code

Téléchargez **Insérer une page vide (Aspose.PDF)** à partir de l'un des plateformes d’hébergement de code mentionnées ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)
