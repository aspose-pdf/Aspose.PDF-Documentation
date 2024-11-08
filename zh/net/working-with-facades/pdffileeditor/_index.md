---
title: PdfFileEditor 类
type: docs
weight: 10
url: /zh/net/pdffileeditor-class/
description: 本节解释如何使用 PdfFileEditor 类处理 Aspose.PDF Facades。
lastmod: "2021-06-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

处理 PDF 文档包括各种功能。管理 PDF 文件的页面是这项工作的重要部分。Aspose.PDF.Facades 提供了 `PdfFileEditor` 类用于此目的。

PdfFileEditor 类包含帮助操作单个页面的方法；此类不编辑或操作页面的内容。您可以插入新页面、删除现有页面、拆分页面或使用 PdfFileEditor 指定页面的拼版。

此类提供的功能可以分为三个主要类别，即文件编辑、PDF 拼版和拆分。我们将在下面详细讨论这些部分：

## 文件编辑

我们可以在此部分中包含的功能有插入、附加、删除、连接和提取。 你可以使用 Insert 方法在指定位置插入新页面，或将页面追加到文件末尾。你还可以使用 Delete 方法通过指定一个包含要删除页面编号的整数数组来删除文件中的任意数量的页面。Concatenate 方法帮助你合并多个 PDF 文件中的页面。你可以使用 Extract 方法提取任意数量的页面，并将这些页面保存到另一个 PDF 文件或内存流中。

本节探讨了此类的功能并解释了其方法的用途。

- [合并 PDF 文档](/pdf/zh/net/concatenate-pdf-documents/)
- [提取 PDF 页面](/pdf/zh/net/extract-pdf-pages/)
- [插入 PDF 页面](/pdf/zh/net/insert-pdf-pages/)
- [删除 PDF 页面](/pdf/zh/net/delete-pdf-pages/)

## 使用分页符

分页符是一个特殊功能，允许重新调整文档的流动。

- [现有 PDF 中的分页符](/pdf/zh/net/page-break-in-existing-pdf/)

## PDF 拼版

拼版是在打印之前正确排列页面的过程。 `PdfFileEditor` 提供了两个方法用于此目的，即 `MakeBooklet` 和 `MakeNUp`。MakeBooklet 方法有助于排列页面，以便在打印后容易折叠或装订，而 MakeNUp 方法允许在 PDF 文件的一页上打印多个页面。

- [制作 PDF 小册子](/pdf/zh/net/make-booklet-of-pdf/)
- [制作 PDF 文件的 NUp](/pdf/zh/net/make-nup-of-pdf-files/)

## 拆分

拆分功能允许您将现有的 PDF 文件分成不同的部分。您可以拆分 PDF 文件的前部或后部。由于 PdfFileEditor 提供了多种拆分方法，您还可以将文件拆分为单独的页面或多个页面集。

- [拆分 PDF 页面](/pdf/zh/net/split-pdf-pages/)