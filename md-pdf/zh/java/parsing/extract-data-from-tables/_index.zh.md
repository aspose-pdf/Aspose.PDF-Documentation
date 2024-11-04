---
title: 从PDF中提取表格数据
linktitle: 提取表格数据
type: docs
weight: 40
url: /java/extract-data-from-table-in-pdf/
description: 学习如何使用Aspose.PDF for Java从PDF中提取表格数据
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 以编程方式从PDF中提取表格

从PDF中提取表格并不是一项简单的任务，因为表格的创建方式多种多样。

Aspose.PDF for Java 提供了一个工具，可以轻松检索表格。要提取表格数据，您应该执行以下步骤：

1. 打开文档 - 实例化一个[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象；
1. 创建一个[TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber)对象。

1. 决定要分析哪些页面，并对所需页面应用[访问](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-)。表格数据将被扫描，结果将保存在[AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable)的列表中。我们可以通过[getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--)方法获取此列表。

1. 要获取数据，遍历`TableList`并处理[吸收行](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow)列表和吸收单元格列表。我们可以通过调用[getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--)方法访问第一个列表，通过调用[getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--)访问第二个列表。

1. 每个 [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) 包含 [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection)。您可以根据自己的需要处理它。

以下示例显示了从所有页面中提取表格：

```java
public static void Extract_Table() {
    // 加载源 PDF 文档
    String filePath = "/home/aspose/pdf-examples/Samples/sample_table.pdf";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();

    // 扫描页面
    for (com.aspose.pdf.Page page : pdfDocument.getPages()) {
        absorber.visit(page);
        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            System.out.println("表格");
            // 迭代行列表
            for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                // 迭代单元格列表
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


## 在PDF页面的特定区域提取表格

每个吸收的表格都有一个[矩形](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable#getRectangle--)属性，该属性描述了表格在页面上的位置。

因此，如果您需要提取位于特定区域的表格，您必须处理特定的坐标。

以下示例显示如何提取用方形注释标记的表格：

```java
public static void Extract_Marked_Table() {
    // 加载源PDF文档
    String filePath = "<... 这里输入PDF文件路径 ...>";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);

    com.aspose.pdf.AnnotationSelector annotationSelector = new com.aspose.pdf.AnnotationSelector(
            new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

    java.util.List<com.aspose.pdf.Annotation> list = annotationSelector.getSelected();
    if (list.size() == 0) {
        System.out.println("未找到标记的表格..");
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


## 从 PDF 提取表格数据并存储到 CSV 文件

以下示例展示了如何提取表格并将其存储为 CSV 文件。要了解如何将 PDF 转换为 Excel 电子表格，请参阅 [Convert PDF to Excel](/pdf/java/convert-pdf-to-excel/) 文章。

```java
public static void Extract_Table_Save_CSV()
{
    String filePath = "/home/admin1/pdf-examples/Samples/sample_table.pdf";
    // 加载 PDF 文档
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // 实例化 ExcelSaveOption 对象
    com.aspose.pdf.ExcelSaveOptions excelSave = new com.aspose.pdf.ExcelSaveOptions();
    excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);

    // 以 XLS 格式保存输出
    pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
}
```