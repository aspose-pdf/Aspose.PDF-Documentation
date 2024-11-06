---
title: Ajouter un TOC à un PDF existant en Ruby
type: docs
weight: 30
url: fr/java/add-toc-to-existing-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Ajouter un TOC

<ins>Pour ajouter un TOC dans un document Pdf en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **AddToc**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir un document pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Accéder à la première page du fichier PDF

toc_page = doc.getPages().insert(1)

# Créer un objet pour représenter les informations du TOC

toc_info = Rjb::import('com.aspose.pdf.TocInfo').new

title = Rjb::import('com.aspose.pdf.TextFragment').new("Table des Matières")

title.getTextState().setFontSize(20)

#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Définir le titre pour le TOC

toc_info.setTitle(title)

toc_page.setTocInfo(toc_info)

# Créer des objets string qui seront utilisés comme éléments du TOC

titles = Array["Première page", "Deuxième page"]

i = 0

while i < 2

    # Créer un objet Heading

    heading2 = Rjb::import('com.aspose.pdf.Heading').new(1)

    segment2 = Rjb::import('com.aspose.pdf.TextSegment').new

    heading2.setTocPage(toc_page)

    heading2.getSegments().add(segment2)

    # Spécifier la page de destination pour l'objet heading

    heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

    # Page de destination

    heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

    # Coordonnée de destination

    segment2.setText(titles[i])

    # Ajouter le heading à la page contenant le TOC

    toc_page.getParagraphs().add(heading2)

    i +=1

end

# Enregistrer le document PDF

doc.save(data_dir + "TOC.pdf")

puts "TOC ajouté avec succès, veuillez vérifier le fichier de sortie."
```


## <ins> **Télécharger le Code en Exécution

Télécharger **Ajouter TOC (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addtoc.rb)