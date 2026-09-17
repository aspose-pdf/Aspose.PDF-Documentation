---
title: Ajouter une chaîne HTML en utilisant DOM dans Ruby
linktitle: Ajouter une chaîne HTML en utilisant DOM dans Ruby
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-ruby/
description: Découvrez comment ajouter une chaîne HTML à un document PDF à l'aide de l'API DOM dans Ruby avec Aspose.PDF pour la génération de contenu dynamique.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Ajouter du HTML



Pour ajouter une chaîne HTML dans un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **AddHtml**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate Document object

doc = Rjb::import('com.aspose.pdf.Document').new

# Add a page to pages collection of PDF file

page = doc.getPages().add()

# Instantiate HtmlFragment with HTML contents

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# set MarginInfo for margin details

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# Set margin information

title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page

page.getParagraphs().add(title)

# Save PDF file

doc.save(data_dir + "html.output.pdf")

puts "HTML added successfully"
```

## 
Télécharger le code d'exécution



Téléchargez** Ajouter du HTML (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)
