---
title: Obtenir le nombre de pages d'un PDF dans Ruby
linktitle: Obtenir le nombre de pages d'un PDF dans Ruby
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-ruby/
description: Récupérez le nombre total de pages d'un document PDF par programme à l'aide de Ruby avec Aspose.PDF.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Obtenir le nombre de pages



Pour obtenir le nombre de pages d'un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **GetNumberOfPages**.

Code Rubis


```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## 
Télécharger le code d'exécution



Téléchargez** Obtenir le nombre de pages (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)
