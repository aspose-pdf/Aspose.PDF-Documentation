---
title: Извлечение текста со всех страниц PDF-документа на PHP
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Извлечение текста со всех страниц

Чтобы извлечь текст со всех страниц PDF-документа с использованием **Aspose.PDF Java for PHP**, просто вызовите модуль **ExtractTextFromAllPages**.
Код PHP

```php

# Открыть целевой документ
$pdf = new Document($dataDir . 'input1.pdf');

# создать объект TextAbsorber для извлечения текста
$text_absorber = new TextAbsorber();

# применить абсорбер для всех страниц
$pdf->getPages()->accept($text_absorber);

# Чтобы извлечь текст с конкретной страницы документа, нам нужно указать конкретную страницу, используя ее индекс в методе accept(..).
# применить абсорбер для конкретной страницы PDF
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# получить извлеченный текст
$extracted_text = $text_absorber->getText();

# создать писатель и открыть файл
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# записать строку текста в файл
# tw.WriteLine(extractedText);
# закрыть поток
$writer->close();

print "Текст успешно извлечен. Проверьте выходной файл." . PHP_EOL;

```


**Загрузка выполняемого кода**

Скачайте **Извлечение текста со всех страниц (Aspose.PDF)** с любого из указанных ниже сайтов социального программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)