---
title: Извлечение данных из таблицы в PDF с помощью Java
linktitle: Извлечь данные из таблицы
type: docs
weight: 40
url: /java/extract-data-from-table-in-pdf/
description: Узнайте, как извлекать данные таблиц из файлов PDF с помощью Aspose.PDF для Java и экспортировать обнаруженные таблицы для дальнейшей обработки.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Data from Table in PDF via Java
Abstract: В этой статье объясняется, как извлекать и обрабатывать табличные данные из PDF-документов с помощью Aspose.PDF для Java. Он показывает, как сканировать страницы с помощью `TableAbsorber`, читать строки и ячейки из обнаруженных таблиц, ограничивать извлечение определенной аннотированной областью и экспортировать результат в Excel.
---
## Extract tables from PDF

Используйте `TableAbsorber`, чтобы находить таблицы на каждой странице и перебирать строки, ячейки, текстовые фрагменты и сегменты текста.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Выполните итерацию по объектам документа [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), поскольку таблицы обнаруживаются страница за страницей.
1. Создайте [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) для каждой страницы и вызовите `visit(page)`, чтобы заполнить список обнаруженных таблиц.
1. Выполните итерацию по обнаруженным объектам [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) и `TextSegment`.
1. Создайте извлеченный текст строки из содержимого фрагмента и распечатайте данные таблицы.

```java
public static void extractTablesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);

            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table");
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## Извлеките таблицу из определенной отмеченной области

В этом примере находит квадратную аннотацию, сравнивает ее прямоугольник с каждой обнаруженной таблицей и выводит только таблицы внутри отмеченной области.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите целевую [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и найдите квадрат [Аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/), который отмечает область извлечения.
1. Создайте [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) и вызовите `visit(page)`, чтобы обнаружить таблицы на этой странице.
1. Сравните каждую обнаруженную [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) с границами прямоугольника аннотации.
1. Переберите соответствующие объекты [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) и [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) и восстановите текст строки.
1. Распечатайте данные таблицы только для отмеченного региона.

```java
public static void extractTableFromSpecificArea(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Annotation squareAnnotation = null;
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                squareAnnotation = annotation;
                break;
            }
        }

        if (squareAnnotation == null) {
            System.out.println("No square annotation found.");
            return;
        }

        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(page);

        for (AbsorbedTable table : absorber.getTableList()) {
            Rectangle tableRect = table.getRectangle();
            Rectangle annotationRect = squareAnnotation.getRect();

            boolean isInRegion = annotationRect.getLLX() < tableRect.getLLX()
                    && annotationRect.getLLY() < tableRect.getLLY()
                    && annotationRect.getURX() > tableRect.getURX()
                    && annotationRect.getURY() > tableRect.getURY();

            if (isInRegion) {
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## Экспорт таблиц в Excel

1. Open the source PDF in a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instance.
1. Create [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) for the export.
1. Установите формат вывода Excel на `XLSX`, чтобы обнаруженный макет таблицы был записан в виде книги Excel.
1. Позвоните `document.save(outputFile.toString(), excelSave)`, чтобы экспортировать документ в формат Excel.

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
