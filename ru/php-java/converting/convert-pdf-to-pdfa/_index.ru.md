---
title: Преобразование PDF в форматы PDF/A
linktitle: Преобразование PDF в форматы PDF/A
type: docs
weight: 100
url: /php-java/convert-pdf-to-pdfa/
lastmod: "2024-05-20"
description: В этой теме показано, как Aspose.PDF позволяет преобразовать PDF файл в PDF файл, соответствующий стандарту PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for PHP** позволяет преобразовать PDF файл в PDF файл, соответствующий стандарту PDF/A. Перед этим файл должен быть валидирован. В этой статье объясняется, как это сделать.

Обратите внимание, что мы используем Adobe Preflight для проверки соответствия PDF/A. Все инструменты на рынке имеют свою собственную "репрезентацию" соответствия PDF/A. Пожалуйста, ознакомьтесь с этой статьей о [инструментах проверки PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) для справки. Мы выбрали продукты Adobe для проверки того, как Aspose.PDF создает PDF файлы, потому что Adobe находится в центре всего, что связано с PDF.

Перед преобразованием PDF в файл, соответствующий стандарту PDF/A, проверьте PDF, используя метод validate.
 Результат проверки сохраняется в XML-файл, а затем этот результат также передается в метод преобразования. Вы также можете указать действие для элементов, которые не могут быть преобразованы, используя перечисление [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

## Конвертация PDF в PDF/A

Следующий фрагмент кода показывает, как конвертировать PDF-файлы в PDF, соответствующий PDF/A-1b.

```php
// Создайте новый объект Document и загрузите входной PDF-файл.
$document = new Document($inputFile);

// Преобразуйте документ в формат PDF/A-1a и укажите файл журнала и действие при ошибке.
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// Сохраните преобразованный документ в выходной файл.
$document->save($outputFile);
```

Чтобы выполнить только проверку, используйте следующую строку кода:

```php
// Создайте новый объект Document и загрузите входной PDF-файл.
$document = new Document($inputFile);

// Преобразуйте документ в формат PDF/A-1a и укажите файл журнала и действие при ошибке.
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// Проверка PDF для PDF/A-1a
if ($document->validate("validation-result-A1A.xml", PdfFormat.PDF_A_1A))
{
    echo "Действителен";
}
else
{
    echo "Недействителен";
}
```

{{% alert color="primary" %}}
**Попробуйте преобразовать PDF в PDF/A онлайн**

Aspose.PDF для PHP предлагает вашему вниманию бесплатное онлайн-приложение ["PDF в PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Преобразование PDF в PDF/A с бесплатным приложением](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}