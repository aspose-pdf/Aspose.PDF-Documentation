---
title: Supprimer les métadonnées d'un PDF en Ruby
type: docs
weight: 90
url: fr/java/remove-metadata-from-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Supprimer les métadonnées

Pour supprimer les métadonnées d'un document PDF en utilisant **Aspose.PDF Java for Ruby**, il suffit d'invoquer le module **RemoveMetadata**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Ouvrir un document pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

    doc.getMetadata().removeItem("pdfaid:part")

end    

if doc.getMetadata().contains("dc:format")

    doc.getMetadata().removeItem("dc:format")

end

# enregistrer le document mis à jour avec les nouvelles informations

doc.save(data_dir + "Remove_Metadata.pdf")

puts "Métadonnées supprimées avec succès, veuillez vérifier le fichier de sortie."
```

## Télécharger le code en cours d'exécution

Téléchargez **Remove Metadata (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)