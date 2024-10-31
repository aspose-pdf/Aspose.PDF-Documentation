---
title: 从PDF中提取表格数据
linktitle: 提取表格数据
type: docs
weight: 40
url: /androidjava/extract-data-from-table-in-pdf/
description: 了解如何使用Aspose.PDF for Android via Java从PDF中提取表格数据。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 以编程方式从PDF中提取表格

从PDF中提取表格并不是一项简单的任务，因为表格可以以多种方式创建。

Aspose.PDF for Android via Java提供了一种工具，使得检索表格变得容易。要提取表格数据，您应执行以下步骤：

1. 打开文档 - 实例化一个[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象；
1. 创建一个[TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber)对象。

1. 决定要分析的页面并应用 [visit](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) 到所需的页面。表格数据将被扫描，结果将保存在 [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable) 的列表中。我们可以通过 [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) 方法获取此列表。

1. 要获取数据，遍历 `TableList` 并处理 [absorbed rows](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) 和吸收的单元格列表。我们可以通过调用 [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) 方法访问第一个列表，通过调用 [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--) 方法访问第二个列表。

1. 每个 [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) 包含 [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection)。你可以根据自己的需要进行处理。

以下示例显示了从所有页面提取表格：

```java
public void extractTable () {
        // 打开文档
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
        // 扫描页面
        for (Page page : (Iterable<? extends Page>) document.getPages()) {
            absorber.visit(page);
            for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
                try {
                    bw.write("Table");
                    bw.newLine();
                    // 遍历行列表
                    for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                        // 遍历单元格列表
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


## 提取 PDF 页面特定区域的表格

每个吸收的表格都有 [Rectangle](https://reference.aspose.com/pdf/java/aspose.pdf.text/absorbedtable/properties/rectangle) 属性，描述了表格在页面上的位置。

因此，如果需要提取位于特定区域的表格，则必须使用特定的坐标。

以下示例展示了如何提取用方形注释标记的表格：

```java
public void extractMarkedTable () {
        // 打开文档
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
            resultMessage.setText("未找到标记的表格..");
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
                        //解析表格
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


## 从 PDF 中提取表格数据并存储到 CSV 文件

以下示例展示了如何提取表格并将其存储为 CSV 文件。要查看如何将 PDF 转换为 Excel 电子表格，请参考[将 PDF 转换为 Excel](/pdf/java/convert-pdf-to-excel/)文章。

```java
 public void extractTableSaveCSV () {
        // 打开文档
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "PDFToXLS_out.csv");
        // 实例化 ExcelSave Option 对象
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