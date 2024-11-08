---
title: Удалить страницы PDF
type: docs
weight: 70
url: /ru/net/delete-pdf-pages/
description: В этом разделе объясняется, как удалить страницы PDF с использованием Aspose.PDF Facades и класса PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

Если вы хотите удалить несколько страниц из PDF файла, который находится на диске, вы можете использовать перегрузку метода [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index), который принимает следующие три параметра: путь к входному файлу, массив номеров страниц для удаления и путь к выходному PDF файлу. Второй параметр — это массив целых чисел, представляющий все страницы, которые нужно удалить. Указанные страницы удаляются из входного файла, и результат сохраняется в выходной файл. Следующий фрагмент кода показывает, как удалить страницы PDF, используя пути к файлам.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingFilePath-DeletePagesUsingFilePath.cs" >}}


## Удаление страниц PDF с использованием потоков

The [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) метод класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) также предоставляет перегрузку, которая позволяет удалять страницы из входного PDF-файла, при этом как входной, так и выходной файлы находятся в потоках. Эта перегрузка принимает следующие три параметра: входной поток, целочисленный массив страниц PDF для удаления и выходной поток. Следующий фрагмент кода показывает, как удалить страницы PDF, используя потоки.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingStream-DeletePagesUsingStream.cs" >}}