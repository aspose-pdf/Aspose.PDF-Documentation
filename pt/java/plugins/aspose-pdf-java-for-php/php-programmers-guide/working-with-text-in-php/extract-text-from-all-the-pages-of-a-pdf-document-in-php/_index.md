---
title: Extraia texto de todas as páginas de um documento PDF em PHP
linktitle: Extraia texto de todas as páginas de um documento PDF em PHP
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
description: Descubra como extrair texto de todas as páginas de um documento PDF em PHP usando Aspose.PDF para análise de texto.
lastmod: "2026-06-09"
---
## Aspose.PDF - Extraia texto de todas as páginas

Para extrair o documento PDF TextrFrom All the Pages usando **Aspose.PDF Java para PHP**, basta invocar o módulo **ExtractTextFromAllPages**.
Código PHP

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

**Baixar código em execução**

Baixe ** Extrair texto de todas as páginas (Aspose.PDF) ** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)
