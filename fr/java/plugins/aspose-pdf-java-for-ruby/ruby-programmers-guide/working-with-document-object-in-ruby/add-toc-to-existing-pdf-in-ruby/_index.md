---
title: Ajouter une table des matières au PDF existant dans Ruby
linktitle: Ajouter une table des matières au PDF existant dans Ruby
type: docs
weight: 30
url: /java/add-toc-to-existing-pdf-in-ruby/
description: Découvrez comment ajouter une table des matières à un PDF existant dans Ruby à l'aide d'Aspose.PDF pour une navigation améliorée dans les documents.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Ajouter une table des matières



<ins>Pour ajouter une table des matières dans un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **AddToc**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get access to first page of PDF file

toc_page = doc.getPages().insert(1)

# Create object to represent TOC information

toc_info = Rjb::import('com.aspose.pdf.TocInfo').new

title = Rjb::import('com.aspose.pdf.TextFragment').new("Table Of Contents")

title.getTextState().setFontSize(20)

#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Set the title for TOC

toc_info.setTitle(title)

toc_page.setTocInfo(toc_info)

# Create string objects which will be used as TOC elements

titles = Array["First page", "Second page"]

i = 0

while i < 2

В В В  # Create Heading object

В В В  heading2 = Rjb::import('com.aspose.pdf.Heading').new(1)

В В В  segment2 = Rjb::import('com.aspose.pdf.TextSegment').new

В В В  heading2.setTocPage(toc_page)

В В В  heading2.getSegments().add(segment2)

В В В  # Specify the destination page for heading object

В В В  heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

В В В  # Destination page

В В В  heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

В В В  # Destination coordinate

В В В  segment2.setText(titles[i])

В В В  # Add heading to page containing TOC

В В В  toc_page.getParagraphs().add(heading2)

В В В  i +=1

end

# Save PDF Document

doc.save(data_dir + "TOC.pdf")

puts "Added TOC Successfully, please check the output file."
```

## 
<ins> **Télécharger le code d'exécution



Téléchargez** Ajouter une table des matières (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addtoc.rb)
