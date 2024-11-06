---
title: Définir l'Expiration du PDF en Ruby
type: docs
weight: 110
url: fr/java/set-pdf-expiration-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Définir l'Expiration du PDF

Pour définir l'expiration d'un document Pdf en utilisant **Aspose.PDF Java for Ruby**, il suffit d'invoquer le module **SetExpiration**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir un document pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

    "var year=2014;

    var month=4;

    today = new Date();

    today = new Date(today.getFullYear(), today.getMonth());

    expiry = new Date(year, month);

    if (today.getTime() > expiry.getTime())

    app.alert('Le fichier est expiré. Vous avez besoin d'un nouveau.');")

doc.setOpenAction(javascript)

# enregistrer le document mis à jour avec de nouvelles informations

doc.save(data_dir + "set_expiration.pdf")

puts "Mettre à jour les informations du document, veuillez vérifier le fichier de sortie."
```


## Télécharger le Code Exécutable

Téléchargez **Définir l'Expiration du PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)