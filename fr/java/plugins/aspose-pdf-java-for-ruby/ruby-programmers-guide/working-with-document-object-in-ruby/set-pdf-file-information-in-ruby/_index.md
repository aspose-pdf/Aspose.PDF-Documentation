---
title: Définir les Informations du Fichier PDF en Ruby
type: docs
weight: 120
url: /fr/java/set-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Définir les Informations du Fichier PDF

Pour mettre à jour les informations d'un document Pdf en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **SetPdfFileInfo**.

Code Ruby

```java

# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrez un document pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obtenez les informations du document

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF pour java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("Informations PDF")

doc_info.setTitle("Définition des Informations du Document PDF")

# Enregistrez le document mis à jour avec les nouvelles informations

doc.save(data_dir + "Updated_Information.pdf")

puts "Mise à jour des informations du document, veuillez vérifier le fichier de sortie."
```


## Télécharger le Code en Exécution

Téléchargez **Définir les Informations du Fichier PDF (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)