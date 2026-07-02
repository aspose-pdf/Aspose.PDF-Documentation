---
title: Извлечь табличные данные из PDF
linktitle: Извлечь табличные данные
type: docs
weight: 40
url: /ru/androidjava/extract-data-from-table-in-pdf/
description: Узнайте, как извлекать табличные данные из PDF с помощью Aspose.PDF for Android via Java.
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Извлекать таблицы из PDF программно

Извлечение таблиц из PDF не является тривиальной задачей, поскольку таблица может быть создана различными способами.

Aspose.PDF for Android via Java имеет инструмент, упрощающий извлечение таблиц. Чтобы извлечь данные таблицы, вам следует выполнить следующие шаги:

1. Откройте документ - создайте экземпляр [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object;
1. Создайте [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber) объект.
1. Определите, какие страницы следует проанализировать, и примените [посетить](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) к желаемым страницам. Табличные данные будут просканированы, и результат будет сохранён в список [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable). Мы можем получить этот список через [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) метод.
1. Чтобы получить данные, пройдите `TableList` и обработать список [поглощённые строки](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) и список поглощённых ячеек. Мы можем получить доступ к первому списку, вызвав [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) метод и ко второму, вызвав [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).
1. Каждый [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) содержит [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). Вы можете использовать его в своих целях.

Следующий пример показывает извлечение таблицы со всех страниц:

```java
public void extractTable () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.TableAbsorber absorber=new com.aspose.pdf.TableAbsorber();

        File file=new File(fileStorage, "extracted-text.txt");
        FileOutputStream fileOutputStream;

        try {
            fileOutputStream=new FileOutputStream(file);

        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(fileOutputStream));
        // Scan pages
        for (Page page : (Iterable<? extends Page>) document.getPages()) {
            absorber.visit(page);
            for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
                try {
                    bw.write("Table");
                    bw.newLine();
                    // Iterate through list of rows
                    for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                        // Iterate through list of cell
                        for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                            for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                                StringBuilder sb=new StringBuilder();
                                for (TextSegment seg :
                                        (Iterable<? extends TextSegment>) fragment.getSegments())
                                    sb.append(seg.getText());
                                bw.write(sb.toString() + "|");
                            }
                        }
                        bw.newLine();
                    }
                } catch (IOException e) {
                    resultMessage.setText(e.getMessage());
                    return;
                }
            }
        }
        try {
            bw.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Извлечь таблицу в определённой области страницы PDF

У каждой поглощённой таблицы есть [Rectangle](https://reference.aspose.com/pdf/java/aspose.pdf.text/absorbedtable/properties/rectangle) свойство, которое описывает положение таблицы на странице.

Итак, если вам нужно извлечь таблицы, расположенные в определённом регионе, вам придётся работать с конкретными координатами.

Следующий пример показывает, как извлечь таблицу, отмеченную квадратной аннотацией:

```java
public void extractMarkedTable () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.Page page=document.getPages().get_Item(1);

        com.aspose.pdf.AnnotationSelector annotationSelector=
                new com.aspose.pdf.AnnotationSelector(
                        new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

        List list=annotationSelector.getSelected();
        if (list.size() == 0) {
            resultMessage.setText("Marked tables not found..");
            return;
        }

        com.aspose.pdf.SquareAnnotation squareAnnotation = (com.aspose.pdf.SquareAnnotation) list.get(0);

        com.aspose.pdf.TableAbsorber absorber=new com.aspose.pdf.TableAbsorber();
        absorber.visit(page);

        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            {
                boolean isInRegion=(squareAnnotation.getRect().getLLX() < table.getRectangle().getLLX())
                        && (squareAnnotation.getRect().getLLY() < table.getRectangle().getLLY())
                        && (squareAnnotation.getRect().getURX() > table.getRectangle().getURX())
                        && (squareAnnotation.getRect().getURY() > table.getRectangle().getURY());

                if (isInRegion) {
                    File file=new File(fileStorage, "extracted-text.txt");
                    FileOutputStream fileOutputStream;

                    try {
                        fileOutputStream=new FileOutputStream(file);

                    } catch (FileNotFoundException e) {
                        resultMessage.setText(e.getMessage());
                        return;
                    }

                    BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(fileOutputStream));
                    try {
                        //Parse table
                        for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                            {
                                for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                                    for (com.aspose.pdf.TextFragment fragment :
                                            cell.getTextFragments()) {
                                        bw.write(fragment.getText());
                                    }
                                    bw.write("|");
                                }
                                bw.newLine();
                            }
                        }
                        bw.close();
                        // -------------
                    } catch (IOException e) {
                        resultMessage.setText(e.getMessage());
                        return;
                    }
                    resultMessage.setText(R.string.success_message);
                }
            }
        }
    }
```

## Извлечь данные таблицы из PDF и сохранить их в файл CSV

В следующем примере показано, как извлечь таблицу и сохранить её в файл CSV.
Чтобы увидеть, как преобразовать PDF в таблицу Excel, пожалуйста, обратитесь к [Преобразовать PDF в Excel](/pdf/ru/java/convert-pdf-to-excel/) статья.

```java
 public void extractTableSaveCSV () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "PDFToXLS_out.csv");
        // Instantiate ExcelSave Option object
        com.aspose.pdf.ExcelSaveOptions excelSave=new com.aspose.pdf.ExcelSaveOptions();
        excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);
        try {
            document.save(file.toString(), excelSave);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


