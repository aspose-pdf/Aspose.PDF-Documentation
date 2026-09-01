---
title: Optimiser un document PDF pour le Web dans Ruby
linktitle: Optimiser un document PDF pour le Web dans Ruby
type: docs
weight: 70
url: /java/optimize-pdf-document-for-the-web-in-ruby/
description: Rationalisez les PDF pour une livraison Web plus rapide et une taille de fichier réduite à l'aide d'Aspose.PDF dans Ruby.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Optimiser le PDF pour le Web



Pour optimiser un document PDF pour le Web à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement la méthode **optimize_web** du module **Optimize**.

Code Rubis


```java

 def optimize_web()

В В В  # The path to the documents directory.

В В В  data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

В В В  # Open a pdf document.

В В В  doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

В В В  # Optimize for web

В В В  doc.optimize()

В В В  #Save output document

В В В  doc.save(data_dir + "Optimized_Web.pdf")

В В В  puts "Optimized PDF for the Web, please check output file."

end
```В 

## 
Télécharger le code d'exécution



Téléchargez** Optimiser le PDF pour le Web (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
