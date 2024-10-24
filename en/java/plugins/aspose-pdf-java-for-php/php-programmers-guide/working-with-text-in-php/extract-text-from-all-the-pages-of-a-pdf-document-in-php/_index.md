---
title: Extract Text From All the Pages of a PDF Document in PHP
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Extract Text From All the Pages

To extract TextrFrom All the Pages Pdf document using **Aspose.PDF Java for PHP**, simply invoke **ExtractTextFromAllPages** module.
PHP Code

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

**Download Running Code**

Download **Extract Text From All the Pages (Aspose.PDF)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)
