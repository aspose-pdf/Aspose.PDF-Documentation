---
title: Извлечение текста со всех страниц PDF‑документа на PHP
linktitle: Извлечение текста со всех страниц PDF‑документа на PHP
type: docs
weight: 30
url: /ru/java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
description: Узнайте, как извлекать текст со всех страниц PDF‑документа на PHP с помощью Aspose.PDF для анализа текста.
lastmod: "2026-08-19"
---
## Aspose.PDF — извлечение текста со всех страниц

Чтобы извлечь TexrFrom All the Pages Pdf документ с помощью **Aspose.PDF Java for PHP**, просто вызовите модуль **ExtractTextFromAllPages**.
Код PHP

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

**Скачать исполняемый код**

СкачатьВ **Извлечь текст со всех страниц (Aspose.PDF)**В изВ любого из ниже перечисленных сайтов совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)


