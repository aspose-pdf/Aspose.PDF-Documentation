---
title: 从 PDF 中提取表格数据使用 C#
linktitle: 提取表格数据
type: docs
weight: 40
url: /zh/net/extract-data-from-table-in-pdf/
description: 学习如何使用 Aspose.PDF for .NET 在 C# 中提取 PDF 中的表格数据
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 以编程方式从 PDF 提取表格

从 PDF 提取表格不是一项简单的任务，因为表格可以通过各种方式创建。

Aspose.PDF for .NET 提供了一个工具来简化表格数据的检索。要提取表格数据，您应该执行以下步骤：

1. 打开文档 - 实例化一个 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象；
1. 创建一个 [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) 对象。
1. `TableList` 是一个 [AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable) 的列表。要获取数据，遍历 `TableList` 并处理 [RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist) 和 [CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist)
2. 每个 [AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell) 包含一个 [TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments) 集合。您可以根据自己的需求处理它。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

以下示例显示了从所有页面提取表格的方法：

```csharp
public static void Extract_Table()
{
    // 加载源 PDF 文档
    var filePath="<... 在此处输入 pdf 文件的路径 ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);                       
    foreach (var page in pdfDocument.Pages)
    {
        Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);
        foreach (AbsorbedTable table in absorber.TableList)
        {
            Console.WriteLine("Table");
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {                                 
                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                            sb.Append(seg.Text);
                        Console.Write($"{sb.ToString()}|");
                    }                           
                }
                Console.WriteLine();
            }
        }
    }
}
```
## 在PDF页面特定区域提取表格

每个被吸收的表格都有一个[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle)属性，描述了表格在页面上的位置。

因此，如果您需要提取位于特定区域的表格，您必须处理特定的坐标。

以下代码片段也使用[Aspose.PDF.Drawing](/pdf/zh/net/drawing/)库。

以下示例展示如何提取标记为方形注释的表格：

```csharp
public static void Extract_Marked_Table()
{
    // 加载源PDF文档
    var filePath="<... 输入PDF文件路径 ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);  
    var page = pdfDocument.Pages[1];
    var squareAnnotation =
        page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
        as Annotations.SquareAnnotation;


    Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
    absorber.Visit(page);

    foreach (AbsorbedTable table in absorber.TableList)
    {
        var isInRegion = (squareAnnotation.Rect.LLX < table.Rectangle.LLX) &&
        (squareAnnotation.Rect.LLY < table.Rectangle.LLY) &&
        (squareAnnotation.Rect.URX > table.Rectangle.URX) &&
        (squareAnnotation.Rect.URY > table.Rectangle.URY);

        if (isInRegion)
        {
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {

                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                        {
                            sb.Append(seg.Text);
                        }
                        var text = sb.ToString();
                        Console.Write($"{text}|");
                    }
                }
                Console.WriteLine();
            }
        }
    }
}
```
## 从 PDF 提取表格数据并存储到 CSV 文件

以下示例展示了如何提取表格并将其存储为 CSV 文件。
要了解如何将 PDF 转换为 Excel 电子表格，请参考 [将 PDF 转换为 Excel](/pdf/zh/net/convert-pdf-to-excel/) 文章。

以下代码片段还可以与 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库一起使用。

```csharp
public static void Extract_Table_Save_CSV()
{
    // 要获取完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // 加载 PDF 文档
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // 实例化 ExcelSave 选项对象
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

    // 保存输出为 XLS 格式
    pdfDocument.Save("PDFToXLS_out.xlsx", excelSave);
}
```
