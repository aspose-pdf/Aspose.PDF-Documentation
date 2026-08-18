---
title: Извлечение таблиц из PDF в Java
linktitle: Извлечь таблицу
type: docs
weight: 20
url: /java/extracting-table/
description: Узнайте, как извлечь данные таблицы из существующих PDF-документов на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение данных таблицы из файлов PDF с помощью Java
Abstract: В этой статье объясняется, как извлекать таблицы из PDF-документов с помощью Aspose.PDF для Java. В нем показано, как использовать TableAbsorber для обнаружения таблиц по страницам, перебора строк и ячеек и сбора текста ячеек для последующей обработки.
---
Используйте `TableAbsorber`, когда вам нужно обнаружить структуры таблиц в существующем PDF-файле и прочитать их содержимое.

## Извлеките текст из обнаруженных таблиц

Используйте этот пример, когда вам нужно найти таблицы на каждой странице и собрать текст их ячеек.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Посетите каждую страницу с помощью [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Выполните итерацию по поглощенным таблицам, строкам и ячейкам, а затем выведите извлеченный текст.

```java
public static void extract(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);
            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table ----");
                for (AbsorbedRow row : table.getRowList()) {
                    System.out.println("Row:");
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            for (TextSegment segment : fragment.getSegments()) {
                                cellText.append(segment.getText());
                            }
                        }
                        rowText.append(" | ").append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```
