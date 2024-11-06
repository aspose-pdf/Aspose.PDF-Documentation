---
title: Ajouter du texte à un fichier PDF existant en Ruby
type: docs
weight: 20
url: fr/java/add-text-to-an-existing-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Ajouter du texte

Pour ajouter une chaîne de texte dans un document Pdf en utilisant **Aspose.PDF Java pour Ruby**, invoquez simplement le module **AddText**.

Code Ruby

```java

# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instancier l'objet Document

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# obtenir une page particulière

pdf_page = doc.getPages().get_Item(1)

# créer un fragment de texte

text_fragment = Rjb::import('com.aspose.pdf.TextFragment').new("texte principal")

text_fragment.setPosition(Rjb::import('com.aspose.pdf.Position').new(100, 600))

font_repository = Rjb::import('com.aspose.pdf.FontRepository')

color = Rjb::import('com.aspose.pdf.Color')

# définir les propriétés du texte

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))

text_fragment.getTextState().setFontSize(14)

#text_fragment.getTextState().setForegroundColor(color.BLUE)

#text_fragment.getTextState().setBackgroundColor(color.GRAY)

# créer l'objet TextBuilder

text_builder = Rjb::import('com.aspose.pdf.TextBuilder').new(pdf_page)

# ajouter le fragment de texte à la page PDF

text_builder.appendText(text_fragment)

# Enregistrer le fichier PDF

doc.save(data_dir + "Text_Added.pdf")

puts "Texte ajouté avec succès"
```


## Télécharger le Code Exécutable

Téléchargez **Ajouter du Texte (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addtext.rb)