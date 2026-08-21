---
title: Extraire le texte de toutes les pages d'un document PDF dans Ruby
linktitle: Extraire le texte de toutes les pages d'un document PDF dans Ruby
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
description: Comprenez comment extraire le texte de toutes les pages d'un document PDF à l'aide de Ruby et Aspose.PDF, idéal pour l'analyse de contenu.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Extraire le texte de toutes les pages



Pour extraire TextrFrom All the Pages Pdf à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **ExtractTextFromAllPages**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# create TextAbsorber object to extract text

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# accept the absorber for all the pages

pdf.getPages().accept(text_absorber)

# In order to extract text from specific page of document, we need to specify the particular page using its index against accept(..) method.

# accept the absorber for particular PDF page

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

#get the extracted text

extracted_text = text_absorber.getText()

# create a writer and open the file

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# write a line of text to the file

# tw.WriteLine(extractedText);

# close the stream

writer.close()

puts "Text extracted successfully. Check output file."
```

## 
Télécharger le code d'exécution



Téléchargez** Extraire le texte de toutes les pages (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)
