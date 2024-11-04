---
title: Конвертировать PDF в Microsoft PowerPoint
linktitle: Конвертировать PDF в PowerPoint
type: docs
weight: 30
url: /php-java/convert-pdf-to-powerpoint/
lastmod: "2024-05-20"
description: Aspose.PDF позволяет конвертировать PDF в формат PowerPoint с использованием PHP. Один из способов - возможность конвертации PDF в PPTX слайдов как изображений.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for PHP** позволяет отслеживать прогресс конвертации PDF в PPTX.
У нас есть API под названием Aspose.Slides, который предлагает возможность создавать и изменять презентации PPT/PPTX. Этот API также предоставляет возможность конвертировать файлы PPT/PPTX в формат PDF. В Aspose.PDF for PHP мы внедрили функцию преобразования PDF-документов в формат PPTX. Во время этой конвертации отдельные страницы PDF-файла преобразуются в отдельные слайды в файле PPTX.

Во время конвертации PDF в PPTX текст отображается как текст, который можно выбрать/обновить, вместо того чтобы он отображался как изображение.
 Please note that in order to convert PDF files to PPTX format, Aspose.PDF provides a class named PptxSaveOptions. An object of the [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) class is passed as a second argument to the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) method.

Обратите внимание, что для преобразования PDF-файлов в формат PPTX Aspose.PDF предоставляет класс с именем PptxSaveOptions. Объект класса [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) передается в качестве второго аргумента методу [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Check next code snippet to resolve your tasks with conversion PDF to PowerPoint format:

Посмотрите следующий фрагмент кода для решения ваших задач по преобразованию PDF в формат PowerPoint:

```php
// Load the input PDF document
// Загрузите входной PDF-документ
$document = new Document($inputFile);

// Create an instance of PptxSaveOptions
// Создайте экземпляр PptxSaveOptions
$saveOption = new PptxSaveOptions();

// Save the PDF document as a PPTX file
// Сохраните PDF-документ как файл PPTX
$document->save($outputFile, $saveOption);
```

## Convert PDF to PPTX with Slides as Images

## Преобразование PDF в PPTX со слайдами в виде изображений

In case if you need to convert a searchable PDF to PPTX as images instead of selectable text, Aspose.PDF provides such a feature via [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) class.

В случае, если вам нужно преобразовать PDF с возможностью поиска в PPTX как изображения, а не выделяемый текст, Aspose.PDF предоставляет такую функцию через класс [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions). Для достижения этого установите свойство SlidesAsImages класса [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) в 'true', как показано в следующем примере кода.

Следующий фрагмент кода показывает процесс конвертации PDF файлов в формат PPTX слайды в виде изображений.

```php
// Загрузить входной PDF документ
$document = new Document($inputFile);

// Создать экземпляр PptxSaveOptions
$saveOption = new PptxSaveOptions();
$saveOption->setSlidesAsImages(true);

// Сохранить PDF документ как файл PPTX
$document->save($outputFile, $saveOption);

    public static void ConvertPDFtoPPTX_SlideAsImages() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX_out.pptx").toString();

        // Загрузить PDF документ
        Document doc = new Document(pdfDocumentFileName);
        // Создать экземпляр PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();
        // Сохранить вывод в формате PPTX
        pptx_save.setSlidesAsImages(true);

        doc.save(pptxDocumentFileName, pptx_save);
    }
```

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в PowerPoint онлайн**

Aspose.PDF для PHP предлагает вам бесплатное онлайн-приложение ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование PDF в PPTX с Бесплатным Приложением](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}