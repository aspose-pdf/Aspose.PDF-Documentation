---
title: Ajouter une chaîne HTML en utilisant DOM en Ruby
type: docs
weight: 10
url: fr/java/add-html-string-using-dom-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Ajouter du HTML

Pour ajouter une chaîne HTML dans un document PDF en utilisant **Aspose.PDF Java pour Ruby**, invoquez simplement le module **AddHtml**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instancier l'objet Document

doc = Rjb::import('com.aspose.pdf.Document').new

# Ajouter une page à la collection de pages du fichier PDF

page = doc.getPages().add()

# Instancier HtmlFragment avec le contenu HTML

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# définir MarginInfo pour les détails des marges

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# Définir les informations de marge

title.setMargin(margin)

# Ajouter le Fragment HTML à la collection de paragraphes de la page

page.getParagraphs().add(title)

# Enregistrer le fichier PDF

doc.save(data_dir + "html.output.pdf")

puts "HTML ajouté avec succès"
```


## Télécharger le Code en Exécution

Téléchargez **Ajouter HTML (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)