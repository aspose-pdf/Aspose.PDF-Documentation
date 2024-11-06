---
title: 使用PDF打印
type: docs
weight: 10
url: zh/java/print-pdf-file/
description: 本节说明如何使用Aspose.PDF Facades通过PdfViewer类打印PDF文件。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用打印机和页面设置打印PDF文件到默认打印机

[PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer)类允许您将PDF文件打印到默认打印机。因此，您需要创建一个[PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer)对象，并使用openPdfFile(..)方法打开PDF。

调用printDocument(..)方法将PDF打印到默认打印机。

以下代码片段显示了如何使用打印机和页面设置将PDF打印到默认打印机。

```java
 public static void PrintingPDFFile() {
        // 创建PdfViewer对象
        PdfViewer viewer = new PdfViewer();

        // 打开输入PDF文件
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 设置打印属性
        viewer.setAutoResize(true); // 以调整后的尺寸打印文件
        viewer.setAutoRotate(true); // 以调整后的旋转角度打印文件
        viewer.setPrintPageDialog(false); // 打印时不显示页码对话框

        // 为打印机和页面设置以及PrintDocument创建对象
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // 设置打印机名称
        printerSettings.setPrinterName("Microsoft Print to PDF");
        

        // 设置页面大小（如果需要）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // 设置页面边距（如果需要）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // 使用打印机和页面设置打印文档
        viewer.printDocumentWithSettings(pageSettings, printerSettings);
        
        // 打印后关闭PDF文件
        viewer.close();
    }
```


为了显示打印对话框，尝试使用以下代码片段：

```java
public static void PrintingPDFDisplayPrintDialog() {
        // 创建 PdfViewer 对象
        PdfViewer viewer = new PdfViewer();

        // 打开输入 PDF 文件
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 设置打印属性
        viewer.setAutoResize(true); // 打印文件时调整大小
        viewer.setAutoRotate(true); // 打印文件时调整旋转
        viewer.setPrintPageDialog(true);

        // 为打印机和页面设置以及 PrintDocument 创建对象
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // 设置页面大小（如果需要）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // 设置页面边距（如果需要）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        java.awt.print.PrinterJob pj = java.awt.print.PrinterJob.getPrinterJob();

        if (pj.printDialog()) {
            printerSettings.setPrinterName(pj.getPrintService().getName());
            printerSettings.setCopies((short) pj.getCopies());
            // 使用打印机和页面设置打印文档
            viewer.printDocumentWithSettings(pageSettings, printerSettings);
        }
        // 打印后关闭 PDF 文件
        viewer.close();
    }
```


## 打印 PDF 到虚拟打印机

有些打印机可以打印到文件。我们设置虚拟打印机的名称，并按照前面的例子进行设置。

```java
public static void PrintingPDFToSoftPrinter() {
        // 创建 PdfViewer 对象
        PdfViewer viewer = new PdfViewer();

        // 打开输入 PDF 文件
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 设置打印属性
        viewer.setAutoResize(true); // 打印时调整大小
        viewer.setAutoRotate(true); // 打印时调整旋转
        viewer.setPrintPageDialog(false); // 打印时不显示页码对话框

        // 创建打印机和页面设置以及 PrintDocument 对象
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // 设置打印机为 Microsoft 虚拟打印机
        printerSettings.setPrinterName("Microsoft Print to PDF");
        // 或者 Adobe
        // printerSettings.setPrinterName("Adobe PDF");

        // 设置页面大小（如果需要）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // 设置页面边距（如果需要）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // 使用打印机和页面设置打印文档
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 打印后关闭 PDF 文件
        viewer.close();
    }
```


## 隐藏打印对话框

Aspose.PDF for Java 允许您隐藏打印对话框。为此，请使用[getPrintPageDialog](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer#getPrintPageDialog--)方法。

以下代码片段向您展示了如何隐藏打印对话框。

```java
public static void PrintingPDFHidePrintDialog() {
        // 创建 PdfViewer 对象
        PdfViewer viewer = new PdfViewer();

        // 打开输入 PDF 文件
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 设置打印属性
        viewer.setAutoResize(true); // 打印调整大小的文件
        viewer.setAutoRotate(true); // 打印调整旋转的文件

        viewer.setPrintPageDialog(false); // 打印时不显示页码对话框

        // 为打印机和页面设置以及 PrintDocument 创建对象
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // 设置打印机为 Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // 设置页面大小（如果需要）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // 设置页面边距（如果需要）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // 使用打印机和页面设置打印文档
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 打印后关闭 PDF 文件
        viewer.close();
    }
```


## 打印彩色 PDF 为灰度 XPS 文件

可以使用 [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) 将彩色 PDF 文档打印为灰度 XPS 文档。为此，您需要使用属性 PdfViewer.PrintAsGrayscale 并将其设置为 *true*。

以下代码片段演示了 PdfViewer.PrintAsGrayscale 属性的实现。

```java
 public static void PrintingPDFasGrayscale() {
        // 创建 PdfViewer 对象
        PdfViewer viewer = new PdfViewer();

        // 打开输入 PDF 文件
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 设置打印属性
        viewer.setAutoResize(true); // 以调整后的大小打印文件
        viewer.setAutoRotate(true); // 以调整后的旋转打印文件

        viewer.setPrintAsGrayscale(true);

        // 创建打印机和页面设置对象以及 PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // 设置打印机 Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // 设置页面大小（如果需要）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // 设置页面边距（如果需要）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // 使用打印机和页面设置打印文档
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 打印后关闭 PDF 文件
        viewer.close();
    }
```


## PDF 转换为 PostScript

[PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) 类提供了打印 PDF 文档的功能，并且借助这个类，我们也可以将 PDF 文件转换为 PostScript 格式。要将 PDF 文件转换为 PostScript，首先安装任何 PS 打印机，然后借助 PdfViewer 打印到文件。

以下代码片段展示了如何打印并将 PDF 转换为 PostScript 格式。

```java
public static void PrintingPDFToPostScript() {
        // 创建 PdfViewer 对象
        PdfViewer viewer = new PdfViewer();

        // 打开输入 PDF 文件
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 设置打印属性
        viewer.setAutoResize(true); // 打印调整大小的文件
        viewer.setAutoRotate(true); // 打印调整旋转的文件

        viewer.setPrintAsGrayscale(true);
        

        // 创建打印机和页面设置以及 PrintDocument 的对象
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // 设置 PostScript 打印机
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");
        printerSettings.setPrintToFile(true);
        printerSettings.setPrintFileName(_dataDir+"result.ps");

        // 设置页面大小（如果需要）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // 设置页面边距（如果需要）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // 使用打印机和页面设置打印文档
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 打印后关闭 PDF 文件
        viewer.close();
    }
```


## 检查打印作业状态

可以将 PDF 文件打印到物理打印机以及 Microsoft XPS Document Writer，而无需显示打印对话框，使用 [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) 类。在打印大型 PDF 文件时，可能需要很长时间，因此用户可能不确定打印过程是否完成或遇到问题。要确定打印作业的状态，请使用 PrintStatus 属性。以下代码片段向您展示如何将 PDF 文件打印到 XPS 文件并获取打印状态。

```java
public static void CheckingPrintJobStatus() {
        // 创建 PdfViewer 对象
        PdfViewer viewer = new PdfViewer();

        // 打开输入 PDF 文件
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 设置打印属性
        viewer.setAutoResize(true); // 打印调整大小的文件
        viewer.setAutoRotate(true); // 打印调整旋转的文件

        viewer.setPrintAsGrayscale(true);

        // 为打印机和页面设置以及 PrintDocument 创建对象
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // 设置打印机 Microsoft Soft Printer
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");

        // 设置页面大小（如果需要）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // 设置页面边距（如果需要）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // 使用打印机和页面设置打印文档
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 检查打印状态
        if (viewer.getPrintStatus() != null) {
            Exception ex = (Exception) viewer.getPrintStatus();
            System.out.println(ex.getMessage());
        } else {
            // 未发现错误。打印作业已成功完成
            System.out.println("一切正常！");
        }
        // 打印后关闭 PDF 文件
        viewer.close();
    }
```