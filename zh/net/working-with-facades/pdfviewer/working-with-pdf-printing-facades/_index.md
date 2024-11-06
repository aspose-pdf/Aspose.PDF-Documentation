---
title: 使用 PDF 打印 - 门面
type: docs
weight: 10
url: zh/net/working-with-pdf-printing-facades/
description: 本节介绍如何使用 Aspose.PDF Facades 的 PdfFileEditor 类打印 PDF 文件。
lastmod: "2021-06-05"
draft: false
---

## 使用打印机和页面设置将 PDF 文件打印到默认打印机

首先将文档转换为图像，然后在打印机上打印。
我们创建一个 [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) 类的实例，允许您使用 BindPdf 方法将 PDF 文件打印到默认打印机，并进行某些设置。在我们的示例中，我们使用 A4 格式，纵向。在 printerSettings 中，首先我们指明要打印到的打印机名称。否则它将打印到默认打印机。接下来，写下我们需要的副本数量。

```csharp
 public static void PrintingPDFFile()
        {
            // 创建 PdfViewer 对象
            PdfViewer viewer = new PdfViewer();

            // 打开输入 PDF 文件
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 设置打印属性
            viewer.AutoResize = true;         // 以调整后的大小打印文件
            viewer.AutoRotate = true;         // 以调整后的旋转角度打印文件
            viewer.PrintPageDialog = false;   // 打印时不显示页码对话框

            // 创建打印机和页面设置以及 PrintDocument 的对象
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
            System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

            // 设置打印机名称
            ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

            // 设置页面大小（如果需要）
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // 设置页面边距（如果需要）
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // 使用打印机和页面设置打印文档
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 打印后关闭 PDF 文件
            viewer.Close();
        }
```

为了显示打印对话框，请尝试使用以下代码片段：

```csharp
        public static void PrintingPDFDisplayPrintDialog()
        {
            // 创建 PdfViewer 对象
            PdfViewer viewer = new PdfViewer();

            // 打开输入 PDF 文件
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 设置打印属性
            viewer.AutoResize = true;         // 以调整后的大小打印文件
            viewer.AutoRotate = true;         // 以调整后的旋转打印文件

            // 创建打印机和页面设置以及 PrintDocument 的对象

            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings
            {

                // 设置 PageSize（如果需要）
                PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169),

                // 设置 PageMargins（如果需要）
                Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0)
            };

            System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
            if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                // 文档打印代码在这里
                // 使用打印机和页面设置打印文档
                System.Drawing.Printing.PrinterSettings ps = printDialog.PrinterSettings;
                viewer.PrintDocumentWithSettings(pgs, ps);
            }

            // 打印后关闭 PDF 文件
            viewer.Close();
        }
```

## 打印 PDF 到虚拟打印机

有些打印机可以打印到文件。我们设置虚拟打印机的名称，并通过与上一个例子的类比，进行设置。

```csharp
public static void PrintingPDFToSoftPrinter()
        {
            // 创建 PdfViewer 对象
            PdfViewer viewer = new PdfViewer();

            // 打开输入的 PDF 文件
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 设置打印属性
            viewer.AutoResize = true;         // 以调整后的大小打印文件
            viewer.AutoRotate = true;         // 以调整后的旋转角度打印文件
            viewer.PrintPageDialog = false;   // 打印时不显示页码对话框

            viewer.PrintAsImage = false;

            // 为打印机和页面设置以及 PrintDocument 创建对象
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // 设置打印机名称
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // 或者设置 PDF 打印机
            //ps.PrinterName = "Adobe PDF";

            // 设置页面大小（如果需要）
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // 设置页面边距（如果需要）
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // 使用打印机和页面设置打印文档
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 打印后关闭 PDF 文件
            viewer.Close();
        }
```

## 隐藏打印对话框

Aspose.PDF for .NET 允许您隐藏打印对话框。为此，请使用 [PrintPageDialog](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/properties/printpagedialog) 方法。

下面的代码片段演示了如何隐藏打印对话框。

```csharp
public static void PrintingPDFHidePrintDialog()
        {
            // 创建 PdfViewer 对象
            PdfViewer viewer = new PdfViewer();

            // 打开输入 PDF 文件
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 设置打印属性
            viewer.AutoResize = true;         // 以调整后的大小打印文件
            viewer.AutoRotate = true;         // 以调整后的旋转打印文件

            viewer.PrintPageDialog = false;   // 打印时不生成页码对话框

            // 为打印机和页面设置以及 PrintDocument 创建对象
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // 设置 XPS/PDF 打印机名称
            ps.PrinterName = "OneNote for Windows 10";

            // 设置 PageSize（如果需要）
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // 设置 PageMargins（如果需要）
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // 使用打印机和页面设置打印文档
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 打印后关闭 PDF 文件
            viewer.Close();
        }
```

## 打印彩色 PDF 为灰度的 XPS 文件

彩色 PDF 文档可以使用 [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) 打印为灰度的 XPS 文件。为了实现这一点，您需要使用属性 PdfViewer.PrintAsGrayscale 并将其设置为 *true*。以下代码片段演示了 PdfViewer.PrintAsGrayscale 属性的实现。

```csharp
public static void PrintingPDFasGrayscale()
        {
            // 创建 PdfViewer 对象
            PdfViewer viewer = new PdfViewer();

            // 打开输入 PDF 文件
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 设置打印属性
            viewer.AutoResize = true;         // 按调整后的尺寸打印文件
            viewer.AutoRotate = true;         // 按调整后的旋转打印文件

            viewer.PrintPageDialog = false;   // 打印时不弹出页码对话框
            viewer.PrintAsGrayscale = false;

            // 创建打印机和页面设置以及 PrintDocument 的对象
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // 设置 XPS/PDF 打印机名称
            ps.PrinterName = "OneNote for Windows 10";

            // 设置 PageSize（如果需要）
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // 设置 PageMargins（如果需要）
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // 使用打印机和页面设置打印文档
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 打印后关闭 PDF 文件
            viewer.Close();
        }
```

## PDF to PostScript 转换

[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) 类提供了打印 PDF 文档的功能，并且借助该类，我们还可以将 PDF 文件转换为 PostScript 格式。要将 PDF 文件转换为 PostScript，首先安装任何 PS 打印机，然后在 PdfViewer 的帮助下打印到文件。

以下代码片段向您展示如何打印和转换 PDF 为 PostScript 格式。

```csharp
public static void PrintingPDFToPostScript()
        {
            // 创建 PdfViewer 对象
            PdfViewer viewer = new PdfViewer();

            // 打开输入 PDF 文件
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 设置打印属性
            viewer.AutoResize = true;         // 以调整的大小打印文件
            viewer.AutoRotate = true;         // 以调整的旋转打印文件
            viewer.PrintPageDialog = false;   // 打印时不显示页码对话框

            viewer.PrintAsImage = false;

            // 为打印机和页面设置以及 PrintDocument 创建对象
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // 设置 XPS/PDF 打印机名称
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // 设置输出文件名和 PrintToFile 属性
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // 设置 PageSize（如果需要）
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // 设置 PageMargins（如果需要）
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // 使用打印机和页面设置打印文档
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 打印后关闭 PDF 文件
            viewer.Close();
        }
```

## 检查打印任务状态

PDF 文件可以打印到物理打印机以及 Microsoft XPS Document Writer，而无需显示打印对话框，使用 [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) 类。在打印大型 PDF 文件时，过程可能需要很长时间，因此用户可能无法确定打印过程是否完成或遇到问题。要确定打印任务的状态，请使用 PrintStatus 属性。以下代码片段展示了如何将 PDF 文件打印到 XPS 文件并获取打印状态。

```csharp
public static void CheckingPrintJobStatus()
        {
            // 创建 PdfViewer 对象
            PdfViewer viewer = new PdfViewer();

            // 打开输入 PDF 文件
            viewer.BindPdf(_dataDir + "sample1.pdf");

            // 设置打印属性
            viewer.AutoResize = true;         // 以调整后的大小打印文件
            viewer.AutoRotate = true;         // 以调整后的旋转角度打印文件
            viewer.PrintPageDialog = false;   // 打印时不生成页码对话框

            viewer.PrintAsImage = false;

            // 为打印机和页面设置以及 PrintDocument 创建对象
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // 设置 XPS/PDF 打印机名称
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // 设置输出文件名和 PrintToFile 属性
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // 设置 PageSize（如果需要）
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // 设置 PageMargins（如果需要）
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // 使用打印机和页面设置打印文档
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 检查打印状态
            if (viewer.PrintStatus != null && viewer.PrintStatus is Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            else
            {
                // 没有发现错误。打印任务成功完成
                Console.WriteLine("打印已成功完成，没有任何问题..");
            }

            // 打印后关闭 PDF 文件
            viewer.Close();
        }

        struct PrintingJobSettings
        {
            public int ToPage { get; set; }
            public int FromPage { get; set; }
            public string OutputFile { get; set; }
            public System.Drawing.Printing.Duplex Mode { get; set; }
        }
```

## 打印页面为单面和双面模式

在特定的打印作业中，PDF文档的页面可以以双面或单面模式进行打印，但在一个打印作业中不能将某些页面打印为单面而另一些页面打印为双面。然而，为了满足此需求，可以使用不同的页面范围和PrintingJobSettings对象。以下代码片段演示了如何在PDF文件中打印某些页面为单面模式和某些页面为双面模式。

```csharp
 public static void PrintingPagesInSimplexAndDuplexMode()
        {
            int printingJobIndex = 0;
            string inPdf = _dataDir + "sample-8page.pdf";
            string output = _dataDir;
            IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

            PrintingJobSettings printingJob1 = new PrintingJobSettings
            {
                FromPage = 1,
                ToPage = 3,
                OutputFile = output + "sample_1_3.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob1);

            PrintingJobSettings printingJob2 = new PrintingJobSettings
            {
                FromPage = 4,
                ToPage = 6,
                OutputFile = output + "sample_4_6.xps",
                Mode = Duplex.Simplex
            };

            printingJobs.Add(printingJob2);

            PrintingJobSettings printingJob3 = new PrintingJobSettings
            {
                FromPage = 7,
                ToPage = 7,
                OutputFile = output + "sample_7.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob3);

            PdfViewer viewer = new PdfViewer();

            viewer.BindPdf(inPdf);
            viewer.AutoResize = true;
            viewer.AutoRotate = true;
            viewer.PrintPageDialog = false;

            PrinterSettings ps = new PrinterSettings();
            PageSettings pgs = new PageSettings();

            ps.PrinterName = "Microsoft XPS Document Writer";
            ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
            ps.PrintToFile = true;
            ps.FromPage = printingJobs[printingJobIndex].FromPage;
            ps.ToPage = printingJobs[printingJobIndex].ToPage;
            ps.Duplex = printingJobs[printingJobIndex].Mode;
            ps.PrintRange = PrintRange.SomePages;

            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
            ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            viewer.EndPrint += (sender, args) =>
            {
                if (++printingJobIndex < printingJobs.Count)
                {
                    ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
                    ps.FromPage = printingJobs[printingJobIndex].FromPage;
                    ps.ToPage = printingJobs[printingJobIndex].ToPage;
                    ps.Duplex = printingJobs[printingJobIndex].Mode;
                    viewer.PrintDocumentWithSettings(pgs, ps);
                }
            };

            viewer.PrintDocumentWithSettings(pgs, ps);
        }
```