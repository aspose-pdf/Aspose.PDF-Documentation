---
title: Optimiser la taille du fichier PDF dans Ruby
linktitle: Optimiser la taille du fichier PDF dans Ruby
type: docs
weight: 80
url: /java/optimize-pdf-file-size-in-ruby/
description: Apprenez à réduire la taille des fichiers PDF sans compromettre la qualité à l'aide d'Aspose.PDF pour Ruby.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Optimiser la taille du fichier PDF



Pour optimiser la taille du fichier d'un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, appelez la méthode **optimize_filesize** du module **Optimize**.

Code Rubis


```java
 def optimize_filesize()

В В В  # The path to the documents directory.

В В В  data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

В В В  # Open a pdf document.

В В В  doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

В В В  # Optimize the file size by removing unused objects

В В В  opt = Rjb::import('aspose.document.OptimizationOptions').new

В В В  opt.setRemoveUnusedObjects(true)

В В В  opt.setRemoveUnusedStreams(true)

В В В  opt.setLinkDuplcateStreams(true)

В В В  doc.optimizeResources(opt)

В В В  # Save output document

В В В  doc.save(data_dir + "Optimized_Filesize.pdf")

В В В  puts "Optimized PDF Filesize, please check output file."

endВ
```

## 
Télécharger le code d'exécution



Téléchargez** Optimiser la taille du fichier PDF (Aspose.PDF)**В à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
