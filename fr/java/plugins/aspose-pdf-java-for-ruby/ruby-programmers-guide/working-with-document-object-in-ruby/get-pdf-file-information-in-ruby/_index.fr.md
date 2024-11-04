---
title: Obtenez des informations sur le fichier PDF en Ruby
type: docs
weight: 50
url: /java/get-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtenez des informations sur le fichier PDF

Pour obtenir des informations sur le fichier du document Pdf en utilisant **Aspose.PDF Java for Ruby**, il suffit d'invoquer le module **GetPdfFileInfo**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir un document pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Obtenir des informations sur le document

doc_info = doc.getInfo()

# Afficher les informations sur le document

puts "Auteur:-" + doc_info.getAuthor().to_s

puts "Date de création:-" + doc_info.getCreationDate().to_string

puts "Mots-clés:-" + doc_info.getKeywords().to_s

puts "Date de modification:-" + doc_info.getModDate().to_string

puts "Sujet:-" + doc_info.getSubject().to_s

puts "Titre:-" + doc_info.getTitle().to_s
```

## Télécharger le code en cours d'exécution

Téléchargez **Obtenez des informations sur le fichier PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)

```ruby
# Ce script démontrera comment obtenir des informations de base sur un fichier PDF.
require 'rjb'

module Asposepdfjava
  module Document
    def self.get_pdf_file_info
      # Spécifiez le chemin d'accès au fichier PDF
      pdf_file_path = '/path/to/your/document.pdf'

      # Charger le document PDF
      pdf_document = Rjb::import('com.aspose.pdf.Document').new(pdf_file_path)

      # Afficher le nombre de pages du document
      puts "Nombre de pages : #{pdf_document.getPages().size()}"

      # Afficher le titre du document
      puts "Titre : #{pdf_document.getInfo().getTitle()}"

      # Afficher l'auteur du document
      puts "Auteur : #{pdf_document.getInfo().getAuthor()}"
    end
  end
end