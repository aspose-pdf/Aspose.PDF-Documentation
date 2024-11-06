---
title: Optimiser le document PDF pour le Web en Ruby
type: docs
weight: 70
url: fr/java/optimize-pdf-document-for-the-web-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Optimiser le PDF pour le Web

Pour optimiser un document PDF pour le web en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer la méthode **optimize_web** du module **Optimize**.

Code Ruby

```java

 def optimize_web()

    # Le chemin vers le répertoire des documents.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # Ouvrir un document pdf.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # Optimiser pour le web

    doc.optimize()

    #Sauvegarder le document de sortie

    doc.save(data_dir + "Optimized_Web.pdf")

    puts "PDF optimisé pour le Web, veuillez vérifier le fichier de sortie."

end
```

## Télécharger le code en cours d'exécution

Téléchargez **Optimize PDF for Web (Aspose.PDF)** à partir de n'importe lequel des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)