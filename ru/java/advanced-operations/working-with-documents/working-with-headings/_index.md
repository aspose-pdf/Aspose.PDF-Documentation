---
title: Работа с заголовками в PDF
type: docs
weight: 70
url: ru/java/working-with-headings/
lastmod: "2021-06-05"
description: Создавайте нумерацию в заголовках вашего PDF-документа с помощью Java. Aspose.PDF для Java предлагает различные стили нумерации.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Применение стиля нумерации в заголовке

Заголовки являются важными частями любого документа. Авторы всегда стараются сделать заголовки более заметными и значимыми для своих читателей. Если в документе есть более одного заголовка, у автора есть несколько вариантов для организации этих заголовков. Один из самых распространенных подходов к организации заголовков — это написание заголовков в стиле нумерации.

Aspose.PDF для Java предлагает множество предопределенных стилей нумерации. Эти предопределенные стили нумерации хранятся в перечислении NumberingStyle. Предопределенные значения перечисления NumberingStyle и их описания приведены ниже:

|**Типы заголовков**|**Описание**|
| :- | :- |
|NumeralsArabic|Арабский тип, например, 1,1.1,...|

|NumeralsRomanUppercase|Римский верхний тип, например, I,I.II, ...|
|NumeralsRomanLowercase|Римский нижний регистр, например, i,i.ii, ...|
|LettersUppercase|Английский верхний регистр, например, A,A.B, ...|
|LettersLowercase|Английский нижний регистр, например, a,a.b, ...|
Свойство [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) класса [com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) используется для установки стилей нумерации заголовков.

Исходный код, для получения результата, показанного на рисунке выше, приведен ниже в примере.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleHeading {
    // Путь к каталогу документов.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ApplyNumberingStyleinHeading() {

        Document pdfDoc = new Document();
        pdfDoc.getPageInfo().setWidth(612.0);
        pdfDoc.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        Page pdfPage = pdfDoc.getPages().add();
        pdfPage.getPageInfo().setWidth(612.0);
        pdfPage.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        FloatingBox floatBox = new FloatingBox();
        floatBox.setMargin(pdfPage.getPageInfo().getMargin());

        pdfPage.getParagraphs().add(floatBox);

        Heading heading = new Heading(1);
        heading.setInList(true);
        heading.setStartNumber(1);
        heading.setText("Список 1");
        heading.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading.setAutoSequence(true);

        floatBox.getParagraphs().add(heading);
        Heading heading2 = new Heading(1);
        heading2.setInList(true);
        heading2.setStartNumber(13);
        heading2.setText("Список 2");
        heading2.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading2.setAutoSequence(true);

        floatBox.getParagraphs().add(heading2);

        Heading heading3 = new Heading(2);
        heading3.setInList(true);
        heading3.setStartNumber(1);
        heading3.setText("стоимость, по состоянию на дату вступления в силу плана, имущества, подлежащего распределению по плану в счет каждого допустимого");
        heading3.setStyle (NumberingStyle.LettersLowercase);
        heading3.setAutoSequence(true);

        floatBox.getParagraphs().add(heading3);
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDoc.save(_dataDir);

    }

}
```