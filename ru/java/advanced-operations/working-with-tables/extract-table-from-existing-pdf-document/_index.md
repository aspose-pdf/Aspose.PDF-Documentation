---
title: Извлечение таблиц из PDF на Java
linktitle: Извлечение таблицы
type: docs
weight: 20
url: /ru/java/extracting-table/
description: Узнайте, как извлекать данные таблиц из существующих PDF‑документов на Java.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлекать данные таблиц из PDF‑файлов с помощью Java
Abstract: В этой статье объясняется, как извлекать таблицы из PDF‑документов с использованием Aspose.PDF for Java. Показано, как использовать TableAbsorber для обнаружения таблиц по страницам, перебора строк и ячеек и сбора текста ячеек для последующей обработки.
---
Используйте `TableAbsorber`, когда вам нужно обнаружить структуры таблиц в существующем PDF и прочитать их содержимое.

## Извлечение текста из обнаруженных таблиц

Используйте этот пример, когда вам нужно находить таблицы на каждой странице и собирать текст их ячеек.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Обработайте каждую страницу с помощью [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Переберите обнаруженные таблицы, строки и ячейки, затем выведите извлечённый текст.

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


