---
title: Извлечение сырого текста из PDF файла
linktitle: Извлечь текст из PDF
type: docs
weight: 10
url: /ru/php-java/extract-text-from-all-pdf/
description: В этой статье описаны различные способы извлечения текста из PDF-документов с использованием Aspose.PDF для PHP. Извлечение с целых страниц, из конкретной части, на основе колонок и т.д.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Извлечение текста со всех страниц PDF документа

Извлечение текста из PDF документа является обычной задачей. В этом примере вы увидите, как Aspose.PDF для PHP позволяет извлекать текст со всех страниц PDF документа.
Чтобы извлечь текст со всех страниц PDF:

1. Создайте объект класса [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Откройте PDF, используя класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и вызовите метод [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) коллекции [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. Класс [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) извлекает текст из документа и возвращает его в методе [getText()](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/#getText--).

Следующий фрагмент кода показывает, как извлечь текст со всех страниц PDF-документа.

```php

    // Создайте новый объект Document из входного PDF-файла.
    $document = new Document($inputFile);

    // Создайте новый объект TextAbsorber для извлечения текста из документа.
    $textAbsorber = new TextAbsorber();

    // Извлеките текст из документа.
    $textAbsorber->visit($document);

    // Получите извлеченное текстовое содержимое.
    $content = $textAbsorber->getText();

    // Сохраните извлеченный текст в выходной файл.
    file_put_contents($outputFile, $content);
```