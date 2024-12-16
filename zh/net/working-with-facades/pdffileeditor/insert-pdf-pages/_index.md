---
title: 插入 PDF 页面
type: docs
weight: 50
url: /zh/net/insert-pdf-pages/
description: 本节说明如何使用 PdfFileEditor 类通过 Aspose.PDF Facades 插入 PDF 页面。
lastmod: "2021-06-05"
draft: false
---

## 使用文件路径在两个数字之间插入 PDF 页面

可以使用 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类的 [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) 方法从一个 PDF 插入特定范围的页面到另一个 PDF 中。 为了做到这一点，您需要一个要插入页面的输入PDF文件，一个要从中提取页面以进行插入的端口文件，一个要插入页面的位置，以及要插入输入PDF文件的端口文件的页面范围。这个范围由开始页面和结束页面参数指定。最后，输出PDF文件会保存指定范围的页面插入到输入文件中。以下代码片段向您展示如何使用文件流在两个数字之间插入PDF页面。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesBetweenNumbers-InsertPagesBetweenNumbers.cs" >}}

## 使用文件路径插入PDF页面数组

如果您想将一些指定页面插入到另一个PDF文件中，那么您可以使用[Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index)方法的一个重载，它需要一个页面的整数数组。 在这个数组中，你可以指定要插入到输入 PDF 文件中的特定页面。为此，你需要一个输入 PDF 文件（你希望在其中插入页面）、一个端口文件（从中提取页面以进行插入）、页面要插入的位置以及从端口文件中需要插入到输入 PDF 文件中的页面的整数数组。该数组包含你希望插入到输入 PDF 文件中的特定页面列表。最后，输出 PDF 文件会保存插入到输入文件中指定页面数组。

以下代码片段向你展示如何使用文件路径插入 PDF 页面的数组。

## 使用流在两个数字之间插入 PDF 页面

如果你想使用流插入页面范围，你只需使用 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类的 [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) 方法的适当重载。 为了做到这一点，您需要一个输入 PDF 流，其中您想要插入页面，一个需要提取页面以进行插入的端口流，一个要插入页面的位置，以及一个需要插入输入 PDF 流的端口流的页面范围。这个范围是通过起始页和结束页参数指定的。最后，输出 PDF 流会保存插入指定页面范围的输入流。以下代码片段向您展示如何使用流在两个数字之间插入 PDF 页面。

## 使用流插入 PDF 页面的数组

您还可以使用流将一组页面插入到另一个 PDF 文件中，使用需要一个整型数组页面的 Insert 方法的适当重载。 在此数组中，您可以指定要插入输入 PDF 流中的特定页面。为此，您需要一个输入 PDF 流，其中您希望插入页面，一个端口流，从中需要获取页面进行插入，页面要插入的位置，以及一个要插入输入 PDF 文件的端口流页面的整数数组。此数组包含您希望插入到输入 PDF 流中的特定页面列表。最后，输出 PDF 流将保存插入了指定页面数组的输入文件。以下代码片段向您展示如何使用流插入 PDF 页面数组。