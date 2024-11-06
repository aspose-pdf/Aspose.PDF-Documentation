---
title: 提取 PDF 页面
type: docs
weight: 20
url: zh/java/extract-pdf-pages/
description: 本节解释如何使用 PdfFileEditor 类从 com.aspose.pdf.facades 中提取 PDF 页面。
lastmod: "2021-06-05"
draft: false
---

## 使用文件路径提取两个数字之间的 PDF 页面

[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) 类的 [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) 方法允许您从 PDF 文件中提取指定范围的页面。此重载允许您在磁盘上操作 PDF 文件时提取页面。此重载需要以下参数：输入文件路径、开始页、结束页和输出文件路径。从开始页到结束页的页面将被提取，输出将保存在磁盘上。以下代码片段演示了如何使用文件路径提取两个数字之间的 PDF 页面。

```java
  public static void Extract_PDFPages_FilePaths() {
        // 创建 PdfFileEditor 对象
        PdfFileEditor pdfEditor = new PdfFileEditor();

        // 提取页面
        pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
    }
```


## 使用文件路径提取PDF页面数组

如果您不想提取一个范围的页面，而是特定的一组页面，[Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) 方法也允许您这样做。您首先需要创建一个包含所有需要提取的页码的整数数组。这个 [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) 方法的重载需要以下参数：输入PDF文件、要提取的页面的整数数组和输出PDF文件。以下代码片段向您展示了如何使用文件路径提取PDF页面。

```java
 public static void Extract_ArrayPDFPages_FilePaths() {
        // 创建 PdfFileEditor 对象
        PdfFileEditor pdfEditor = new PdfFileEditor();
        int[] pagesToExtract = new int[] { 1, 2 };
        // 提取页面
        pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
    }
```


## 使用流提取两个页码之间的PDF页面

[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) 类的 [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) 方法允许您使用流提取一系列页面。您需要将以下参数传递给此重载：输入流、起始页、结束页和输出流。在起始页和结束页之间指定范围的页面将从输入流中提取并保存到输出流。以下代码片段向您展示了如何使用流提取两个数字之间的PDF页面。

```java
public static void Extract_PDFPages_Streams()
    {
         // 创建 PdfFileEditor 对象
            PdfFileEditor pdfEditor = new PdfFileEditor();
         // 创建流
         using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
         using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
         // 提取页面
         pdfEditor.Extract(inputStream, 1, 3, outputStream);

    }
```


## 使用流提取PDF页面数组

可以从PDF流中提取一组页面，并使用[Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-)方法的适当重载将其保存在输出流中。如果您不想提取一系列页面，而是特定页面的集合，[Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-)方法也允许您这样做。您首先需要创建一个包含所有需要提取的页码的整数数组。[Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-)方法的这个重载需要以下参数：输入流、要提取的页面的整数数组和输出流。以下代码片段向您展示如何使用流提取PDF页面。

```java
public static void Extract_ArrayPDFPages_Streams()
        {
            // 创建PdfFileEditor对象
            PdfFileEditor pdfEditor = new PdfFileEditor();
            // 创建流
            using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
            using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
            {
                int[] pagesToExtract = new int[] { 1, 2 };
                // 提取页面
                pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
            }
        }
```