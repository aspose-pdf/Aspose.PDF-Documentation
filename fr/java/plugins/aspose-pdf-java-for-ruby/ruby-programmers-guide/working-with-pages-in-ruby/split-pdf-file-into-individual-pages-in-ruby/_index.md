---
title: Diviser un fichier PDF en pages individuelles en Ruby
type: docs
weight: 80
url: fr/java/split-pdf-file-into-individual-pages-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Diviser les pages

Pour diviser un document PDF en pages individuelles en utilisant **Aspose.PDF Java pour Ruby**, invoquez simplement le module **SplitAllPages**.

Code Ruby

```java

# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir le document cible

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# parcourir toutes les pages

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# créer un nouvel objet Document

new_document = Rjb::import('com.aspose.pdf.Document').new

# obtenir la page à un index particulier de la collection de pages

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# enregistrer le fichier PDF nouvellement généré

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "Le processus de division s'est terminé avec succès !"
```


## Télécharger le Code Exécutable

Téléchargez **Split Pages (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)