---
title: Извлечение данных таблицы из PDF
linktitle: Извлечение данных таблицы
type: docs
weight: 40
url: /java/extract-data-from-table-in-pdf/
description: Узнайте, как извлечь табличные данные из PDF с помощью Aspose.PDF для Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Программное извлечение таблиц из PDF

Извлечение таблиц из PDF - это нетривиальная задача, поскольку таблица может быть создана по-разному.

Aspose.PDF для Java предлагает инструмент, упрощающий извлечение таблиц. Чтобы извлечь данные таблицы, выполните следующие шаги:

1. Откройте документ - создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document);
1. Создайте объект [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber).

1. Определите, какие страницы будут анализироваться, и примените [visit](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) к нужным страницам. Табличные данные будут сканироваться, и результат будет сохранен в списке [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable). Мы можем получить этот список с помощью метода [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--).
2. Чтобы получить данные, итерируйтесь через `TableList` и обрабатывайте список [absorbed rows](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) и список поглощенных ячеек. Мы можем получить доступ к первому списку, вызвав метод [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--), и ко второму, вызвав метод [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. Каждый [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) содержит [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). Вы можете обрабатывать его для своих целей.

Следующий пример показывает извлечение таблицы со всех страниц:

```java
public static void Extract_Table() {
    // Загрузить исходный PDF документ        
    String filePath = "/home/aspose/pdf-examples/Samples/sample_table.pdf";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();

    // Сканировать страницы
    for (com.aspose.pdf.Page page : pdfDocument.getPages()) {
        absorber.visit(page);
        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            System.out.println("Таблица");
            // Перебрать список строк
            for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                // Перебрать список ячеек
                for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                    for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                        StringBuilder sb = new StringBuilder();
                        for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                            sb.append(seg.getText());
                        System.out.print(sb.toString() + "|");
                    }
                }
                System.out.println();
            }
        }
    }
}
```


## Извлечение таблицы в определенной области страницы PDF

Каждая извлеченная таблица имеет свойство [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable#getRectangle--), которое описывает положение таблицы на странице.

Таким образом, если вам нужно извлечь таблицы, расположенные в определенной области, вам необходимо работать с конкретными координатами.

Следующий пример показывает, как извлечь таблицу, отмеченную квадратной аннотацией:

```java
public static void Extract_Marked_Table() {
    // Загрузить исходный PDF документ
    String filePath = "<... введите путь к pdf файлу здесь ...>";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);

    com.aspose.pdf.AnnotationSelector annotationSelector = new com.aspose.pdf.AnnotationSelector(
            new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

    java.util.List<com.aspose.pdf.Annotation> list = annotationSelector.getSelected();
    if (list.size() == 0) {
        System.out.println("Отмеченные таблицы не найдены..");
        return;
    }

    com.aspose.pdf.SquareAnnotation squareAnnotation = (com.aspose.pdf.SquareAnnotation) list.get(0);

    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();
    absorber.visit(page);

    for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
        {
            boolean isInRegion = (squareAnnotation.getRect().getLLX() < table.getRectangle().getLLX())
                    && (squareAnnotation.getRect().getLLY() < table.getRectangle().getLLY())
                    && (squareAnnotation.getRect().getURX() > table.getRectangle().getURX())
                    && (squareAnnotation.getRect().getURY() > table.getRectangle().getURY());

            if (isInRegion) {
                for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                    {
                        for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                            for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                                StringBuilder sb = new StringBuilder();
                                for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                                    sb.append(seg.getText());
                                System.out.print(sb.toString() + "|");
                            }
                        }
                        System.out.println();
                    }
                }
            }
        }
    }
}
```


## Извлечение данных таблицы из PDF и сохранение их в CSV файл

Следующий пример показывает, как извлечь таблицу и сохранить её как CSV файл.
Чтобы узнать, как конвертировать PDF в Excel Spreadsheet, пожалуйста, обратитесь к статье [Конвертация PDF в Excel](/pdf/java/convert-pdf-to-excel/).

```java
public static void Extract_Table_Save_CSV()
{
    String filePath = "/home/admin1/pdf-examples/Samples/sample_table.pdf";
    // Загрузить PDF документ
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // Создать объект ExcelSave Option
    com.aspose.pdf.ExcelSaveOptions excelSave = new com.aspose.pdf.ExcelSaveOptions();
    excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);

    // Сохранить результат в формате XLS
    pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
}
```