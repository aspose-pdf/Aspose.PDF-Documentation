---
title: Извлечь данные из таблицы в PDF с помощью Java
linktitle: Извлечь данные из таблицы
type: docs
weight: 40
url: /ru/java/extract-data-from-table-in-pdf/
description: Узнайте, как извлекать данные таблиц из PDF‑файлов с помощью Aspose.PDF for Java и экспортировать обнаруженные таблицы для дальнейшей обработки.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь данные из таблицы в PDF с помощью Java
Abstract: В этой статье объясняется, как извлекать и обрабатывать табличные данные из PDF‑документов с помощью Aspose.PDF for Java. Показано, как сканировать страницы с `TableAbsorber`, считывать строки и ячейки из обнаруженных таблиц, ограничивать извлечение конкретным аннотированным регионом и экспортировать результат в Excel.
---
## Извлеките таблицы из PDF

Использовать `TableAbsorber` найти таблицы на каждой странице и итеративно проходить строки, ячейки, текстовые фрагменты и текстовые сегменты.

1. Откройте исходный PDF в [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Перебрать документ [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) объекты, потому что таблицы обнаруживаются постранично.
1. Создайте [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) для каждой страницы и вызвать `visit(page)` для заполнения обнаруженного списка таблиц.
1. Итерировать обнаруженные [ПоглощённаяТаблица](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [ПоглощённаяСтрока](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [ПоглощённаяЯчейка](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), и `TextSegment` объекты.
1. Постройте извлечённый текст строки из содержимого фрагмента и выведите данные таблицы.

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

## Извлеките таблицу из конкретной отмеченной области

В этом примере находят квадратную аннотацию, сравнивают её прямоугольник с каждой обнаруженной таблицей и выводят только таблицы, находящиеся внутри отмеченной области.

1. Откройте исходный PDF в [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Получите цель [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и найдите квадрат [Аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) которая отмечает область извлечения.
1. Создайте [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) и вызвать `visit(page)` для обнаружения таблиц на этой странице.
1. Сравните каждый обнаруженный [ПоглощённаяТаблица](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Прямоугольник](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) с границами прямоугольника аннотации.
1. Перебрать совпадающие [ПоглощённаяСтрока](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) и [ПоглощённаяЯчейка](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) объекты и восстановить текст строки.
1. Вывести данные таблицы только для отмеченной области.

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

## Экспортировать таблицы в Excel

1. Откройте исходный PDF в [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) для экспорта.
1. Установите формат вывода Excel в `XLSX` поэтому обнаруженный макет таблицы записывается как рабочая книга Excel.
1. Вызов `document.save(outputFile.toString(), excelSave)` для экспорта документа в формат Excel.

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```

