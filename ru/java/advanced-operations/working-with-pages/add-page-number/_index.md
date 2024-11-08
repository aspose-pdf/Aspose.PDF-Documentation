---
title: Add Page Number to PDF 
linktitle: Add Page Number
type: docs
weight: 100
url: /ru/java/add-page-number/
description: Aspose.PDF for Java позволяет добавлять штамп номера страницы в ваш PDF-файл с использованием класса PageNumber Stamp.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Все документы должны содержать номера страниц. Номер страницы облегчает читателю поиск различных частей документа. **Aspose.PDF for Java** позволяет добавлять номера страниц с помощью PageNumberStamp.

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество конверсии Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

Вы можете использовать класс [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) для добавления штампа номера страницы в документ PDF.
 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) класс предоставляет методы для создания штампа с номером страницы, такие как формат, поля, выравнивание, начальный номер и т.д. Чтобы добавить штамп с номером страницы, вам нужно создать объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и объект [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) с необходимыми свойствами. После этого вы можете вызвать метод [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) класса [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) для добавления штампа в PDF файл. Вы также можете установить атрибуты шрифта для штампа с номером страницы.

Следующий фрагмент кода показывает, как добавить номера страниц в PDF файл.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleAddPageNumberToPDF {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // Создать штамп номера страницы
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // Является ли штамп фоном
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // Установить свойства текста
        pageNumberStamp.getTextState().setFont (FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize (14.0F);
        pageNumberStamp.getTextState().setFontStyle (FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor (Color.getAqua());

        // Добавить штамп на определенную страницу
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // Сохранить выходной документ
        pdfDocument.save(_dataDir);

    }
}
```