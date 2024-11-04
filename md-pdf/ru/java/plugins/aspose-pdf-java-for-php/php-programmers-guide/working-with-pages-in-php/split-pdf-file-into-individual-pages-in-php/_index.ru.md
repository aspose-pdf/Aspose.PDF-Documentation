---
title: Разделение PDF файла на отдельные страницы в PHP
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Разделение страниц

Чтобы разделить PDF-документ на отдельные страницы с использованием **Aspose.PDF Java для PHP**, просто вызовите класс **SplitAllPages**.

PHP код

```php

# Открыть целевой документ
$pdf = new Document($dataDir . 'input1.pdf');

# пройти по всем страницам
$pdf_page = 1;
$total_size = $pdf->getPages()->size();
#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)
while ($pdf_page <= $total_size)

{

    # создать новый объект Document
    $new_document = new Document();

    # получить страницу по определенному индексу коллекции страниц
    $new_document->getPages()->add($pdf->getPages()->get_Item($pdf_page));

    # сохранить вновь сгенерированный PDF файл
    $new_document->save($dataDir . "page_#{$pdf_page}.pdf");

    $pdf_page++;

}

print "Процесс разделения завершен успешно!";

```

**Скачать выполняемый код**

Скачайте **Split Pages (Aspose.PDF)** с любого из нижеупомянутых социальных кодинг-сайтов:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)