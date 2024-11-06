---
title: Создание или добавление таблицы в PDF 
linktitle: Создание или добавление таблицы
type: docs
weight: 10
url: ru/java/add-table-in-existing-pdf-document/
description: Узнайте, как создать или добавить таблицу в PDF документ, применить стиль ячеек, разделить таблицу на страницы и настроить строки и столбцы и т.д.
lastmod: "2021-12-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Создание таблицы

 Пространство имен Aspose.PDF содержит классы под названием [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table), [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/cell) и [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row), которые предоставляют функциональность для создания таблиц при генерации PDF документов с нуля.

Таблица может быть создана путем создания объекта класса Table.

```java
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### Добавление таблицы в существующий PDF документ

Чтобы добавить таблицу в существующий PDF файл с помощью Aspose.PDF для Java, выполните следующие шаги:

1. Загрузите исходный файл.

1. Инициализируйте таблицу и задайте ее столбцы и строки.
1. Установите настройки таблицы (мы установили границы).
1. Заполните таблицу.
1. Добавьте таблицу на страницу.
1. Сохраните файл.

Следующие фрагменты кода показывают, как добавить текст в существующий PDF файл.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddTable {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void CreateTable() {
        Document doc = new Document(_dataDir + "input.pdf");
        // Инициализирует новый экземпляр таблицы
        Table table = new Table();
        // Установить цвет границы таблицы как LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // установить границу для ячеек таблицы
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // создать цикл для добавления 10 строк
        for (int row_count = 1; row_count < 10; row_count++) {
            // добавить строку в таблицу
            Row row = table.getRows().add();
            // добавить ячейки в таблицу
            row.getCells().add("Column (" + row_count + ", 1)");
            row.getCells().add("Column (" + row_count + ", 2)");
            row.getCells().add("Column (" + row_count + ", 3)");
        }
        // Добавить объект таблицы на первую страницу входного документа
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // Сохранить обновленный документ, содержащий объект таблицы
        doc.save(_dataDir + "document_with_table.pdf");
    }
```


### ColSpan и RowSpan в таблицах Aspose.PDF с использованием Java

Aspose.PDF для Java предоставляет метод [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) для объединения столбцов в таблице и метод [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) для объединения строк.

Мы используем методы [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) или [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) на объекте [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell), который создает ячейку таблицы. После применения необходимых свойств созданная ячейка может быть добавлена в таблицу.

```java
public static void AddTable_RowColSpan() {
        // Загрузить исходный PDF документ
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Инициализировать новый экземпляр таблицы
        Table table = new Table();
        // Установить цвет границы таблицы как LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // Установить границу для ячеек таблицы
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // Добавить первую строку в таблицу
        Row row1 = table.getRows().add();
        for (int cellCount = 1; cellCount < 5; cellCount++) {
            // Добавить ячейки в таблицу
            row1.getCells().add("Тест 1 " + cellCount);
        }

        // Добавить вторую строку в таблицу
        Row row2 = table.getRows().add();
        row2.getCells().add("Тест 2 1");
        Cell cell = row2.getCells().add("Тест 2 2");
        cell.setColSpan(2);
        row2.getCells().add("Тест 2 4");

        // Добавить третью строку в таблицу
        Row row3 = table.getRows().add();
        row3.getCells().add("Тест 3 1");
        row3.getCells().add("Тест 3 2");
        row3.getCells().add("Тест 3 3");
        row3.getCells().add("Тест 3 4");

        // Добавить четвертую строку в таблицу
        Row row4 = table.getRows().add();
        row3.getCells().add("Тест 4 1");
        cell = row3.getCells().add("Тест 4 2");
        cell.setRowSpan(2);
        row3.getCells().add("Тест 4 3");
        row3.getCells().add("Тест 4 4");

        // Добавить пятую строку в таблицу
        row4 = table.getRows().add();
        row4.getCells().add("Тест 5 1");
        row4.getCells().add("Тест 5 3");
        row4.getCells().add("Тест 5 4");

        // Добавить объект таблицы на первую страницу входного документа
        page.getParagraphs().add(table);

        // Сохранить обновленный документ, содержащий объект таблицы
        pdfDocument.save(_dataDir + "document_with_table_out.pdf");
    }
```


Результатом выполнения кода ниже является таблица, изображенная на следующем изображении:

![Демо ColSpan и RowSpan](colspan_rowspan.png)

## Работа с границами, отступами и полями

Aspose.PDF для Java позволяет разработчикам создавать таблицы в PDF-документах. Согласно модели объектов документа Aspose.PDF, таблица является элементом уровня абзаца.

Пожалуйста, обратите внимание, что также поддерживается возможность установки стиля границ, отступов и полей ячеек для таблиц. Прежде чем углубляться в технические детали, важно понять концепции границы, отступов и полей, которые представлены ниже на диаграмме:

![Границы, отступы и поля](set-border-style-margins-and-padding-of-table_1.png)

На рисунке выше видно, что границы таблицы, строки и ячейки перекрываются. Используя Aspose.PDF, таблица может иметь отступы, а ячейки могут иметь поля. Чтобы установить отступы ячеек, мы должны установить поля ячеек.

## Границы

Чтобы установить границы объектов [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setBorder-com.aspose.pdf.BorderInfo-), [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setBorder-com.aspose.pdf.BorderInfo-) и [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setBorder-com.aspose.pdf.BorderInfo-), используйте методы [Table.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setBorder-com.aspose.pdf.BorderInfo-), [Row.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setBorder-com.aspose.pdf.BorderInfo-) и [Cell.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setBorder-com.aspose.pdf.BorderInfo-).
 Границы ячеек можно также установить с использованием метода [DefaultCellBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setDefaultCellBorder-com.aspose.pdf.BorderInfo-) класса [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table) или [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row). Все вышеупомянутые свойства, связанные с границами, назначаются экземпляру класса Row, который создается вызовом его конструктора. Класс Row имеет множество перегрузок, которые принимают почти все параметры, необходимые для настройки границ.

## Поля или Отступы

Отступы ячеек можно управлять с использованием метода [DefaultCellPadding](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setDefaultCellPadding-com.aspose.pdf.MarginInfo-) класса Table. Все свойства, связанные с отступами, назначаются экземпляру класса [MarginInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/MarginInfo), который принимает информацию о параметрах `Left`, `Right`, `Top` и `Bottom` для создания пользовательских отступов.

В следующем примере ширина границы ячейки установлена на 0.1 пункта, ширина границы таблицы установлена на 1 пункт, а отступ ячейки установлен на 5 пунктов.

![Отступ и граница в таблице PDF](margin-border.png)

```java
public static void MargingPadding() {
        // Создайте объект Document, вызвав его пустой конструктор
        Document doc = new Document();
        Page page = doc.getPages().add();
        // Создайте объект таблицы
        Table tab1 = new Table();
        // Добавьте таблицу в коллекцию параграфов нужного раздела
        page.getParagraphs().add(tab1);
        // Установите ширину колонок таблицы
        tab1.setColumnWidths ("50 50 50");
        // Установите границу ячейки по умолчанию с использованием объекта BorderInfo
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));
        // Установите границу таблицы, используя другой настраиваемый объект BorderInfo
        tab1.setBorder (new BorderInfo(BorderSide.All, 1F));

        // Создайте объект MarginInfo и установите его левый, нижний, правый и верхний отступы
        MarginInfo margin = new MarginInfo();
        margin.setTop (5f);
        margin.setLeft (5f);
        margin.setRight (5f);
        margin.setBottom (5f);

        // Установите отступ ячейки по умолчанию в объект MarginInfo
        tab1.setDefaultCellPadding(margin);

        // Создайте строки в таблице, а затем ячейки в строках
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 with large text string");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Сохраните PDF
        doc.save(_dataDir + "MarginsOrPadding_out.pdf");
    }
}
```

Чтобы создать таблицу с закругленными углами, используйте значение `RoundedBorderRadius` класса [BorderInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/BorderInfo) и установите стиль углов таблицы в закругленный.

```java
    public static void RoundedBorderRadius() {
        Document doc = new Document();
        Page page = doc.getPages().add();

        // Создать экземпляр объекта таблицы
        Table tab1 = new Table();

        // Добавить таблицу в коллекцию параграфов нужного раздела
        page.getParagraphs().add(tab1);

        GraphInfo graph = new GraphInfo();
        graph.setColor(Color.getRed());
        // Создать пустой объект BorderInfo
        BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
        // Установить закругленную границу, где радиус закругления равен 15
        bInfo.setRoundedBorderRadius(15);
        // Установить стиль углов таблицы как закругленный.
        tab1.setCornerStyle(BorderCornerStyle.Round);
        // Установить информацию о границах таблицы
        tab1.setBorder(bInfo);
        // Создать строки в таблице и затем ячейки в строках
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 with large text string");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Сохранить PDF
        doc.save(_dataDir + "BorderRadius_out.pdf");
    }
```


### Свойство AutoFitToWindow в перечислении ColumnAdjustmentType

```java
 public static void AutoFitToWindowProperty() {
        // Создайте объект Pdf, вызвав его пустой конструктор
        Document doc = new Document();
        // Создайте раздел в объекте Pdf
        Page sec1 = doc.getPages().add();

        // Создайте объект таблицы
        Table tab1 = new Table();
        // Добавьте таблицу в коллекцию абзацев нужного раздела
        sec1.getParagraphs().add(tab1);

        // Установите ширину столбцов таблицы
        tab1.setColumnWidths("50 50 50");
        tab1.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);

        // Установите границу ячеек по умолчанию, используя объект BorderInfo
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));

        // Установите границу таблицы, используя другой настраиваемый объект BorderInfo
        tab1.setBorder(new BorderInfo(BorderSide.All, 1F));

        // Создайте объект MarginInfo и задайте его отступы слева, снизу, справа и сверху
        MarginInfo margin = new MarginInfo();
        margin.setTop(5f);
        margin.setLeft(5f);
        margin.setRight(5f);
        margin.setBottom(5f);

        // Установите отступ ячеек по умолчанию в объект MarginInfo
        tab1.setDefaultCellPadding(margin);

        // Создайте строки в таблице, а затем ячейки в строках
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add("col3");
        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Сохраните обновленный документ, содержащий объект таблицы
        doc.save(_dataDir + "AutoFitToWindow_out.pdf");
    }
```


### Получение ширины таблицы

Иногда требуется динамически получить ширину таблицы. Класс Aspose.PDF.Table имеет метод [GetWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#getWidth--) для этой цели. Например, вы не задали ширину столбцов таблицы явно и установили [ColumnAdjustment](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColumnAdjustment) в AutoFitToContent. В этом случае вы можете получить ширину таблицы следующим образом.

```java
public static void GetTableWidth() {
        // Создать новый документ
        Document doc = new Document();
        // Добавить страницу в документ
        Page page = doc.getPages().add();

        // Инициализировать новую таблицу
        Table table = new Table();

        // Добавить таблицу в коллекцию параграфов нужного раздела
        page.getParagraphs().add(table);
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);

        // Добавить строку в таблицу
        Row row = table.getRows().add();
        // Добавить ячейку в таблицу
        row.getCells().add("Текст ячейки 1");
        row.getCells().add("Текст ячейки 2");
        // Получить ширину таблицы
        System.out.println(table.getWidth());
    }
```


## Добавить SVG объект в ячейку таблицы

Aspose.PDF для Java поддерживает возможность добавления ячейки таблицы в PDF файл. При создании таблицы возможно добавлять текст или изображения в ячейки. Кроме того, API также предлагает возможность конвертировать SVG файлы в формат PDF. Используя комбинацию этих функций, можно загрузить SVG изображение и добавить его в ячейку таблицы.

Следующий фрагмент кода показывает шаги для создания экземпляра таблицы и добавления SVG изображения в ячейку таблицы.

```java
 public static void AddSVGObjectToTableCell() {
        // Создать экземпляр объекта Document
        Document doc = new Document();
        // Создать экземпляр изображения
        com.aspose.pdf.Image img = new com.aspose.pdf.Image();
        // Установить тип изображения как SVG
        img.setFileType (com.aspose.pdf.ImageFileType.Svg);
        // Путь к исходному файлу
        img.setFile (_dataDir + "SVGToPDF.svg");
        // Установить ширину для экземпляра изображения
        img.setFixWidth (50);
        // Установить высоту для экземпляра изображения
        img.setFixHeight (50);
        // Создать экземпляр таблицы
        com.aspose.pdf.Table table = new com.aspose.pdf.Table();
        // Установить ширину для ячеек таблицы
        table.setColumnWidths ("100 100");
        // Создать объект строки и добавить его в экземпляр таблицы
        com.aspose.pdf.Row row = table.getRows().add();
        // Создать объект ячейки и добавить его в экземпляр строки
        com.aspose.pdf.Cell cell = row.getCells().add();
        // Добавить текстовый фрагмент в коллекцию параграфов объекта ячейки
        cell.getParagraphs().add(new TextFragment("First cell"));
        // Добавить ещё одну ячейку в объект строки
        cell = row.getCells().add();
        // Добавить SVG изображение в коллекцию параграфов недавно добавленного экземпляра ячейки
        cell.getParagraphs().add(img);
        // Создать объект страницы и добавить его в коллекцию страниц экземпляра документа
        Page page = doc.getPages().add();
        // Добавить таблицу в коллекцию параграфов объекта страницы
        page.getParagraphs().add(table);
        // Сохранить PDF файл
        doc.save(_dataDir + "AddSVGObject_out.pdf");
    }
```


## Добавление HTML тегов в таблицу

Aspose.PDF для Java позволяет добавлять новый HTML фрагмент в абзац вашего PDF файла.

{{% alert color="primary" %}}

Пожалуйста, примите во внимание, что использование HTML тегов внутри элемента таблицы увеличивает время генерации документа, так как API необходимо обработать HTML теги соответствующим образом и отобразить их в выходном PDF документе.

{{% /alert %}}

```java
  public static void AddHTMLFragmentToTableCell() {
        Document doc = new Document(_dataDir + "input.pdf");
        // Инициализирует новый экземпляр таблицы
        Table table = new Table();
        // Установите цвет границы таблицы как LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // установите границу для ячеек таблицы
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // создайте цикл для добавления 10 строк
        for (int row_count = 1; row_count < 10; row_count++) {
            Cell cell;
            // добавьте строку в таблицу
            Row row = table.getRows().add();
            // добавьте ячейки таблицы
            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Колонка <strong>(" + row_count + ", 1)</strong>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Колонка <span style='color:red'>(" + row_count + ", 2)</span>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Колонка <span style='text-decoration: underline'>(" + row_count + ", 3)</span>"));
        }
        // Добавьте объект таблицы на первую страницу входного документа
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // Сохраните обновленный документ, содержащий объект таблицы
        doc.save(_dataDir + "AddHTMLObject_out.pdf");
    }

}
```


## Вставка разрыва страницы между строками таблицы

По умолчанию, при создании таблицы внутри PDF файла, таблица переходит на последующие страницы, когда достигает нижнего поля таблицы. Однако, у нас может быть требование вставить разрыв страницы, когда добавлено определенное количество строк для таблицы. Следующий фрагмент кода показывает шаги по вставке разрыва страницы, когда добавлено 10 строк для таблицы.

```java
    public static void InsertPageBreak() {
        // Создать экземпляр класса Document
        Document doc = new Document();
        // Добавить страницу в коллекцию страниц PDF файла
        Page page = doc.getPages().add();
        // Создать экземпляр таблицы
        Table tab = new Table();
        // Установить стиль границы для таблицы
        tab.setBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // Установить стиль границы по умолчанию для таблицы с цветом границы Красный
        tab.setDefaultCellBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // Указать ширину столбцов таблицы
        tab.setColumnWidths ("100 100");
        // Создать цикл для добавления 200 строк в таблицу
        for (int counter = 0; counter <= 200; counter++) {
            Row row = new Row();
            tab.getRows().add(row);
            Cell cell1 = new Cell();
            cell1.getParagraphs().add(new TextFragment("Ячейка " + counter + ", 0"));
            row.getCells().add(cell1);
            Cell cell2 = new Cell();
            cell2.getParagraphs().add(new TextFragment("Ячейка " + counter + ", 1"));
            row.getCells().add(cell2);
            // Когда добавлено 10 строк, отобразить новую строку на новой странице
            if (counter % 10 == 0 && counter != 0)
                row.setInNewPage(true);
        }
        // Добавить таблицу в коллекцию абзацев PDF файла
        page.getParagraphs().add(tab);

        // Сохранить PDF документ
        doc.save(_dataDir + "InsertPageBreak_out.pdf");
    }
```


## Скрытие границ объединённых ячеек

При добавлении ячеек в таблицу, границы объединённых ячеек могут отображаться, когда они переносятся на другую строку. Такие объединённые границы могут быть скрыты, как показано в следующем примере кода.

```java
Document doc = new Document();
com.aspose.pdf.Page page = doc.getPages().add();

//Создать объект таблицы, который будет вложен внутрь outerTable и будет переноситься
//в пределах одной страницы
com.aspose.pdf.Table mytable = new com.aspose.pdf.Table();
mytable.setBroken(TableBroken.Vertical);
mytable.setDefaultCellBorder(new BorderInfo(BorderSide.All));
mytable.setRepeatingColumnsCount(2);
page.getParagraphs().add(mytable);

//Добавить строку заголовка
com.aspose.pdf.Row row = mytable.getRows().add();
Cell cell = row.getCells().add("header 1");
cell.setColSpan(2);
cell.setBackgroundColor(Color.getLightGray());
Cell header3 = row.getCells().add("header 3");
Cell cell2 = row.getCells().add("header 4");
cell2.setColSpan(2);
cell2.setBackgroundColor(Color.getLightBlue());
row.getCells().add("header 6");
Cell cell3 = row.getCells().add("header 7");
cell3.setColSpan(2);
cell3.setBackgroundColor(Color.getLightGreen());
Cell cell4 = row.getCells().add("header 9");
cell4.setColSpan(3);
cell4.setBackgroundColor(Color.getLightCoral());
row.getCells().add("header 12");
row.getCells().add("header 13");
row.getCells().add("header 14");
row.getCells().add("header 15");
row.getCells().add("header 16");
row.getCells().add("header 17");

for (int rowCounter = 0; rowCounter < 1; rowCounter++)
{
  //Создать строки в таблице, а затем ячейки в строках
  com.aspose.pdf.Row row1 = mytable.getRows().add();
  row1.getCells().add("col "+rowCounter+", 1");
  row1.getCells().add("col "+rowCounter+", 2");
  row1.getCells().add("col "+rowCounter+", 3");
  row1.getCells().add("col "+rowCounter+", 4");
  row1.getCells().add("col "+rowCounter+", 5");
  row1.getCells().add("col "+rowCounter+", 6");
  row1.getCells().add("col "+rowCounter+", 7");
  row1.getCells().add("col "+rowCounter+", 8");
  row1.getCells().add("col "+rowCounter+", 9");
  row1.getCells().add("col "+rowCounter+", 10");
  row1.getCells().add("col "+rowCounter+", 11");
  row1.getCells().add("col "+rowCounter+", 12");
  row1.getCells().add("col "+rowCounter+", 13");
  row1.getCells().add("col "+rowCounter+", 14");
  row1.getCells().add("col "+rowCounter+", 15");
  row1.getCells().add("col "+rowCounter+", 16");
  row1.getCells().add("col "+rowCounter+", 17");
}
doc.save(dataDir + "3_out.pdf");
```