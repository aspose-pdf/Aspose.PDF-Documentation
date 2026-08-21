---
title: Extraire le texte de toutes les pages d'un document PDF en PHP
linktitle: Extraire le texte de toutes les pages d'un document PDF en PHP
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
description: Découvrez comment extraire le texte de toutes les pages d'un document PDF en PHP en utilisant Aspose.PDF pour l'analyse de texte.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Extraire le texte de toutes les pages



Pour extraire TextrFrom All the Pages Pdf à l'aide de **Aspose.PDF Java pour PHP**, invoquez simplement le module **ExtractTextFromAllPages**.
Code PHP


```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# create TextAbsorber object to extract text
$text_absorber = new TextAbsorber();

# accept the absorber for all the pages
$pdf->getPages()->accept($text_absorber);

# In order to extract text from specific page of document, we need to specify the particular page using its index against accept(..) method.
# accept the absorber for particular PDF page
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

#get the extracted text
$extracted_text = $text_absorber->getText();

# create a writer and open the file
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# write a line of text to the file
# tw.WriteLine(extractedText);
# close the stream
$writer->close();

print "Text extracted successfully. Check output file." . PHP_EOL;

```


**Télécharger le code d'exécution**



Téléchargez** Extraire le texte de toutes les pages (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)
