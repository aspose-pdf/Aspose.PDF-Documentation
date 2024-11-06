---
title: Ajout de JavaScript dans Ruby
type: docs
weight: 10
url: fr/java/adding-javascript-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Ajout de JavaScript

Pour ajouter JavaScript dans un document Pdf en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **AddJavaScript**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir un document pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Ajout de JavaScript au niveau du document

# Instancier JavascriptAction avec l'instruction JavaScript désirée

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Assigner l'objet JavascriptAction à l'action désirée du document

doc.setOpenAction(javaScript)

# Ajout de JavaScript au niveau de la page

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is opened')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is closed')"))

# Enregistrer le document PDF

doc.save(data_dir + "JavaScript-Added.pdf")

puts "Ajout de JavaScript réussi, veuillez vérifier le fichier de sortie."
```


## Télécharger le Code Exécutable

Téléchargez **Ajouter JavaScript (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)