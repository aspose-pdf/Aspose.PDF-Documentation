---
title: Optimiser la Taille du Fichier PDF en Ruby
type: docs
weight: 80
url: /java/optimize-pdf-file-size-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Optimiser la Taille du Fichier PDF

Pour optimiser la taille du fichier d'un document PDF en utilisant **Aspose.PDF Java pour Ruby**, appelez la méthode **optimize_filesize** du module **Optimize**.

Code Ruby

```java

 def optimize_filesize()

    # Le chemin vers le répertoire des documents.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # Ouvrir un document pdf.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # Optimiser la taille du fichier en supprimant les objets inutilisés

    opt = Rjb::import('aspose.document.OptimizationOptions').new

    opt.setRemoveUnusedObjects(true)

    opt.setRemoveUnusedStreams(true)

    opt.setLinkDuplcateStreams(true)

    doc.optimizeResources(opt)

    # Enregistrer le document de sortie

    doc.save(data_dir + "Optimized_Filesize.pdf")

    puts "Taille du fichier PDF optimisée, veuillez vérifier le fichier de sortie."

end 
```


## Télécharger le Code Fonctionnel

Download **Optimize PDF File Size (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)