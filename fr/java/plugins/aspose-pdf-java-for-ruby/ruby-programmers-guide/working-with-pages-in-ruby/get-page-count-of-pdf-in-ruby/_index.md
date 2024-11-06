---
title: Obtenir le Nombre de Pages d'un PDF en Ruby
type: docs
weight: 40
url: fr/java/get-page-count-of-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtenir le Nombre de Pages

Pour obtenir le nombre de pages d'un document PDF en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **GetNumberOfPages**.

Code Ruby

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Créer un document PDF

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Nombre de Pages:" + page_count.to_s
```

## Télécharger le Code Exécutant

Téléchargez **Obtenir le Nombre de Pages (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)