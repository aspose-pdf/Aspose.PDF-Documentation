---
title: Извлечение шрифтов из PDF
linktitle: Извлечение шрифтов
type: docs
weight: 30
url: /php-java/extract-fonts-from-pdf/
description: Как извлечь шрифт из PDF с использованием Aspose.PDF для PHP
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Если вы хотите получить все шрифты из PDF-документа, вы можете использовать метод [Document.IDocumentFontUtilities.getAllFonts()](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getFontUtilities--), предоставляемый в классе Document.
Пожалуйста, ознакомьтесь с приведённым ниже фрагментом кода, чтобы получить все шрифты из существующего PDF-документа:

```php

    // Создайте новый экземпляр класса License и установите файл лицензии.
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // Установите путь к каталогу, содержащему PDF-документ, и выходному каталогу для извлечённых шрифтов.
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.pdf";

    // Инициализируйте переменную данных ответа.
    $responseData = "";

    try {
        // Загрузите PDF-документ.
        $document = new Document($inputFile);

        // Получите все шрифты, используемые в PDF-документе.
        $fonts = java_values($document->getFontUtilities()->getAllFonts());

        // Переберите каждый шрифт и сохраните его как файл шрифта TrueType.
        foreach ($fonts as $font) {
            // Установите путь к выходному файлу для файла шрифта.
            $outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . $font->getFontName() . ".ttf";

            // Создайте объект FileOutputStream для записи файла шрифта.
            $fontStream = new java("java.io.FileOutputStream", $outputFile);

            // Сохраните шрифт как файл шрифта TrueType.
            $font->save($fontStream);

            // Закройте поток шрифта.
            $fontStream->close();

            // Добавьте имя шрифта к данным ответа.
            $responseData = $responseData . $font->getFontName() . ", ";
        }

        // Закройте PDF-документ.
        $document->close();
    }
```