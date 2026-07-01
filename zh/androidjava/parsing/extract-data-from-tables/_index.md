---
title: 从 PDF 中提取表格数据
linktitle: 提取表格数据
type: docs
weight: 40
url: /zh/androidjava/extract-data-from-table-in-pdf/
description: 了解如何使用 Aspose.PDF for Android via Java 从 PDF 中提取表格。
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 以编程方式从 PDF 中提取表格

从 PDF 中提取表格并非一件轻松的任务，因为表格的创建方式多种多样。

Aspose.PDF for Android via Java 提供了一个工具，使检索表格变得简便。要提取表格数据，您应执行以下步骤：

1. 打开文档 - 实例化一个 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象;
1. 创建一个 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber) 对象。
1. 确定要分析并应用的页面 [访问](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) 到所需页面。表格数据将被扫描，结果将以列表形式保存 [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable). 我们可以通过以下方式获取此列表 [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) 方法。
1. 要获取数据，请遍历 `TableList` 并处理列表 [已吸收的行](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) 以及已吸收的单元格列表。我们可以通过调用来访问第一个列表 [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) 方法，第二个则通过调用 [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).
1. 每个 [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) 包含 [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). 您可以将其用于自己的目的。

以下示例展示了从所有页面中提取表格：

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

## 在 PDF 页面特定区域提取表格

每个被吸收的表格都有 [矩形](https://reference.aspose.com/pdf/java/aspose.pdf.text/absorbedtable/properties/rectangle) 描述表格在页面上位置的属性。

因此，如果您需要提取位于特定区域的表格，必须使用特定的坐标。

以下示例展示了如何提取使用方形注释标记的表格：

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

## 从 PDF 中提取表格数据并存储为 CSV 文件

以下示例展示了如何提取表格并将其存储为 CSV 文件。
要了解如何将 PDF 转换为 Excel 电子表格，请参阅 [将 PDF 转换为 Excel](/pdf/zh/java/convert-pdf-to-excel/) 文章。

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

