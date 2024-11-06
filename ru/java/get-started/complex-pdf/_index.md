---
title: Создание сложного PDF
linktitle: Создание сложного PDF
type: docs
weight: 60
url: ru/java/complex-pdf-example/
description: Aspose.PDF for Java позволяет создавать более сложные документы, содержащие изображения, текстовые фрагменты и таблицы в одном документе.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Пример [Hello, World](/pdf/java/hello-world-example/) показал простые шаги по созданию PDF-документа с использованием Java и Aspose.PDF. В этой статье мы рассмотрим создание более сложного документа с использованием Java и Aspose.PDF for Java. В качестве примера возьмем документ от вымышленной компании, занимающейся пассажирскими паромными перевозками.
Наш документ будет содержать изображение, два текстовых фрагмента (заголовок и абзац) и таблицу. Для создания такого документа мы будем использовать подход на основе DOM. Подробнее можно прочитать в разделе [Основы DOM API](/pdf/java/basics-of-dom-api/).

Если мы создаем документ с нуля, нам необходимо следовать определенным шагам:

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). На этом этапе мы создадим пустой PDF-документ с некоторыми метаданными, но без страниц.
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) в объект документа. Теперь наш документ будет иметь одну страницу.
1. Добавьте [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). Это сложная операция, основанная на низкоуровневых действиях с операторами PDF.
    - Загрузите изображение из потока
    - Добавьте изображение в коллекцию Images ресурсов страницы
    - Используйте оператор GSave: этот оператор сохраняет текущее состояние графики.
    - Создайте объект [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/).
    - Используйте оператор ConcatenateMatrix: определяет, как должно быть размещено изображение.
    - Используйте оператор Do: этот оператор рисует изображение.
    - Используйте оператор GRestore: этот оператор восстанавливает состояние графики.

1. Создайте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) для заголовка. Для заголовка мы будем использовать шрифт Arial с размером шрифта 24pt и выравниванием по центру.
1. Добавьте заголовок в [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) страницы.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) для описания. Для описания мы будем использовать шрифт Arial с размером шрифта 24pt и выравниванием по центру.
1. Добавьте (описание) в Paragraphs страницы.
1. Создайте таблицу, добавьте свойства таблицы.
1. Добавьте (таблицу) в [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) страницы.
1. Сохраните документ "Complex.pdf".

```java
package com.aspose.pdf.examples;

/**
 * Сложный пример
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.LocalTime;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.ConcatenateMatrix;
import com.aspose.pdf.operators.Do;
import com.aspose.pdf.operators.GRestore;
import com.aspose.pdf.operators.GSave;

public final class ComplexExample {

    private ComplexExample() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/");

    public static void main(String[] args) throws FileNotFoundException {
        // Инициализировать объект документа
        Document document = new Document();
        // Добавить страницу
        Page page = document.getPages().add();

        // -------------------------------------------------------------
        // Добавить изображение
        Path imageFileName = Paths.get(_dataDir.toString(),"logo.png");
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(imageFileName.toString()));
        // Добавить изображение в коллекцию изображений ресурсов страницы
        page.getResources().getImages().add(imageStream);

        // Использование оператора GSave: этот оператор сохраняет текущее состояние графики
        page.getContents().add(new GSave());
        Rectangle _logoPlaceHolder = new Rectangle(20, 730, 120, 830);

        // Создать объект Matrix
        Matrix matrix = new Matrix(new double[] {
            _logoPlaceHolder.getURX() - _logoPlaceHolder.getLLX(), 0, 0,
            _logoPlaceHolder.getURY() - _logoPlaceHolder.getLLY(),
            _logoPlaceHolder.getLLX(), _logoPlaceHolder.getLLY() });

        // Использование оператора ConcatenateMatrix (конкатенация матрицы): определяет, как должно быть размещено изображение
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Использование оператора Do: этот оператор рисует изображение
        page.getContents().add(new Do(ximage.getName()));
        // Использование оператора GRestore: этот оператор восстанавливает состояние графики
        page.getContents().add(new GRestore());

        // -------------------------------------------------------------
        // Добавить заголовок
        TextFragment header = new TextFragment("Новые маршруты паромов осенью 2020 года");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // Добавить описание
        String descriptionText = "Посетители должны покупать билеты онлайн, и билеты ограничены до 5000 в день. Паромное обслуживание работает с половинной мощностью и по сокращенному расписанию. Ожидайте очередей.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);

        // Добавить таблицу
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("Отправляется из города");
        headerRow.getCells().add("Отправляется с острова");

        for (Cell headerRowCell : headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState().setForegroundColor(Color.getWhiteSmoke());
        }

        LocalTime time = LocalTime.of(6,0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time=time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save(Paths.get(_dataDir.toString(), "Complex.pdf").toString());
    }

}
```