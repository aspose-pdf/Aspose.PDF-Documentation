---
title: Convert PDF to Microsoft PowerPoint 
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: ru/java/convert-pdf-to-powerpoint/
lastmod: "2021-11-19"
description: Aspose.PDF позволяет конвертировать PDF в формат PowerPoint с использованием Java. Один из способов - это возможность конвертировать PDF в PPTX слайдов в виде изображений.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Java** позволяет отслеживать прогресс конвертации PDF в PPTX.
У нас есть API под названием Aspose.Slides, который предлагает возможность создавать и изменять презентации PPT/PPTX. Этот API также предоставляет функцию конвертации файлов PPT/PPTX в формат PDF. В Aspose.PDF for Java мы внедрили функцию преобразования документов PDF в формат PPTX. Во время этой конвертации отдельные страницы PDF файла преобразуются в отдельные слайды в файле PPTX.

Во время конвертации PDF в PPTX текст отображается как текст, который можно выбрать/обновить, вместо того чтобы быть отображенным как изображение.
 Пожалуйста, обратите внимание, что для преобразования файлов PDF в формат PPTX, Aspose.PDF предоставляет класс с именем PptxSaveOptions. Объект класса [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) передается в качестве второго аргумента методу [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Проверьте следующий фрагмент кода, чтобы решить ваши задачи по конверсии PDF в формат PowerPoint:

```java
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_Simple();
        convertPDFtoPPTX_SlideAsImages();
        convertPDFtoPPTX_ProgresDetails();
    }

    public static void convertPDFtoPPTX_Simple() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // Загрузить PDF документ
        Document document = new Document(documentFileName);

        // Создать экземпляр PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // Сохранить вывод в формате PPTX
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```

## Преобразование PDF в PPTX с слайдами в виде изображений

В случае, если вам нужно преобразовать PDF с возможностью поиска в PPTX в виде изображений вместо выделяемого текста, Aspose.PDF предоставляет такую возможность через класс [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions). Чтобы достичь этого, установите свойство SlidesAsImages класса [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) в 'true', как показано в следующем примере кода.

Следующий фрагмент кода показывает процесс преобразования PDF файлов в формат PPTX слайды в виде изображений.

```java
public static void convertPDFtoPPTX_SlideAsImages() {
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
    String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

    // Загрузить PDF документ
    Document document = new Document(documentFileName);
    // Создать экземпляр PptxSaveOptions
    PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();
    // Сохранить вывод в формате PPTX
    pptxSaveOptions.setSlidesAsImages(true);

    document.save(pptxDocumentFileName, pptxSaveOptions);
    document.close();
}
```


## Показать прогресс в консоли с помощью Aspose.PDF для Java выглядит следующим образом:

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.PptxSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Конвертация PDF в PPTX.
 */
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_ProgressDetails();
    }

    public static void convertPDFtoPPTX_ProgressDetails() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // Загрузить PDF документ
        Document document = new Document(documentFileName);

        // Создать экземпляр PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // Указать пользовательский обработчик прогресса
        pptx_save.setCustomProgressHandler(new ShowProgressOnConsole());

        // Сохранить вывод в формате PPTX
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```


## Детали прогресса конверсии PPTX

Aspose.PDF для Java позволяет отслеживать прогресс конверсии PDF в PPTX. Класс [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) предоставляет свойство [CustomProgressHandler](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlSaveOptions), которое может быть указано на пользовательский метод для отслеживания прогресса конверсии, как показано в следующем примере кода.

```java
package com.aspose.pdf.examples;

import java.time.LocalDateTime;

import com.aspose.pdf.ProgressEventType;
import com.aspose.pdf.UnifiedSaveOptions.ConversionProgressEventHandler;
import com.aspose.pdf.UnifiedSaveOptions.ProgressEventHandlerInfo;

class ShowProgressOnConsole extends ConversionProgressEventHandler{

    @Override
    public void invoke(ProgressEventHandlerInfo eventInfo) {        
        switch (eventInfo.EventType) {
            case ProgressEventType.TotalProgress:
                System.out.println(
                        String.format("%s  - Прогресс конверсии : %d %%.", LocalDateTime.now().toString(), eventInfo.Value));
                break;
            case ProgressEventType.ResultPageCreated:
                System.out.println(String.format("%s  - Страница результата %s из %d создана.", LocalDateTime.now().toString(),
                        eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.ResultPageSaved:
                System.out.println(String.format("%s  - Страница результата %d из %d экспортирована.", LocalDateTime.now(), eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.SourcePageAnalysed:
                System.out.println(String.format("%s  - Исходная страница %d из %d проанализирована.", LocalDateTime.now(),  eventInfo.Value, eventInfo.MaxValue));
                break;
            default:
                break;
        }
    }
```


{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PowerPoint онлайн**

Aspose.PDF for Java предлагает вам бесплатное онлайн-приложение ["PDF в PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в PPTX с бесплатным приложением](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}