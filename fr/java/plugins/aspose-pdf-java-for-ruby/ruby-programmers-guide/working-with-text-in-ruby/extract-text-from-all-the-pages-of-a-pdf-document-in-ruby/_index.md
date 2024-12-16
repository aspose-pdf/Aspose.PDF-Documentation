---
title: Extraire le texte de toutes les pages d'un document PDF en Ruby
type: docs
weight: 30
url: /fr/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Extraire le texte de toutes les pages

Pour extraire le texte de toutes les pages d'un document PDF en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **ExtractTextFromAllPages**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir le document cible

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# créer un objet TextAbsorber pour extraire le texte

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# accepter l'absorbeur pour toutes les pages

pdf.getPages().accept(text_absorber)

# Afin d'extraire le texte d'une page spécifique du document, nous devons spécifier la page particulière en utilisant son index contre la méthode accept(..).

# accepter l'absorbeur pour une page PDF particulière

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# obtenir le texte extrait

extracted_text = text_absorber.getText()

# créer un écrivain et ouvrir le fichier

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# écrire une ligne de texte dans le fichier

# tw.WriteLine(extractedText);

# fermer le flux

writer.close()

puts "Texte extrait avec succès. Vérifiez le fichier de sortie."
```


## Télécharger le Code Exécutable

Téléchargez **Extraire le Texte de Toutes les Pages (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)