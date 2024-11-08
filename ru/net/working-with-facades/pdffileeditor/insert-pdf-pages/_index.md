---
title: Вставка страниц PDF
type: docs
weight: 50
url: /ru/net/insert-pdf-pages/
description: Этот раздел объясняет, как вставлять страницы PDF с использованием Aspose.PDF Facades с помощью класса PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Вставка страниц PDF между двумя номерами с использованием путей к файлам

Определенный диапазон страниц может быть вставлен из одного PDF в другой с использованием метода [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Чтобы сделать это, вам нужен входной PDF-файл, в который вы хотите вставить страницы, файл порта, из которого страницы должны быть взяты для вставки, место, куда страницы должны быть вставлены, и диапазон страниц файла порта, которые должны быть вставлены во входной PDF-файл. Этот диапазон указывается с параметрами начальной и конечной страницы. Наконец, выходной PDF-файл сохраняется с заданным диапазоном страниц, вставленных во входной файл. Следующий фрагмент кода показывает, как вставить страницы PDF между двумя числами, используя файловые потоки.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesBetweenNumbers-InsertPagesBetweenNumbers.cs" >}}

## Вставка массива страниц PDF с использованием путей к файлам

Если вы хотите вставить некоторые указанные страницы в другой PDF-файл, то вы можете использовать перегрузку метода [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index), который требует целочисленного массива страниц. In this array, you can specify which particular pages you want to insert in the input PDF file. In order to do that, you need an input PDF file in which you want to insert the pages, a port file from which the pages need to be taken for insertion, a location where the pages are to be inserted, and integer array of the pages from port file which have to be inserted in the input PDF file. This array contains a list of particular pages which you’re interested to insert in the input PDF file. Finally, the output PDF file is saved with the specified array of pages inserted in the input file.
The following code snippet shows you how to insert array of PDF pages using file paths.

В этом массиве вы можете указать, какие именно страницы вы хотите вставить в входной PDF файл. Для этого вам нужен входной PDF файл, в который вы хотите вставить страницы, файл-источник, из которого страницы должны быть взяты для вставки, место, где страницы должны быть вставлены, и целочисленный массив страниц из файла-источника, которые должны быть вставлены во входной PDF файл. Этот массив содержит список конкретных страниц, которые вы хотите вставить во входной PDF файл. Наконец, выходной PDF файл сохраняется с указанным массивом страниц, вставленных во входной файл.
Следующий фрагмент кода показывает, как вставить массив страниц PDF, используя пути к файлам.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertArrayOfPages-InsertArrayOfPages.cs" >}}

## Insert PDF Pages between Two Numbers Using Streams

## Вставка PDF страниц между двумя номерами с использованием потоков

If you want to insert the range of pages using streams, you only need to use the appropriate overload of the [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class.

Если вы хотите вставить диапазон страниц, используя потоки, вам нужно использовать соответствующую перегрузку метода [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Для этого вам нужен входной поток PDF, в который вы хотите вставить страницы, поток порта, из которого страницы будут взяты для вставки, место, куда страницы должны быть вставлены, и диапазон страниц потока порта, которые должны быть вставлены во входной поток PDF. Этот диапазон указывается с параметрами начальной и конечной страницы. Наконец, выходной поток PDF сохраняется с указанным диапазоном страниц, вставленных во входной поток. Следующий фрагмент кода показывает, как вставить страницы PDF между двумя числами, используя потоки.

## Вставка массива страниц PDF с использованием потоков

Вы также можете вставить массив страниц в другой PDF файл, используя потоки с помощью соответствующей перегрузки метода Insert, которая требует целочисленного массива страниц. В этом массиве вы можете указать, какие конкретные страницы вы хотите вставить в входной поток PDF. Для этого вам нужен входной поток PDF, в который вы хотите вставить страницы, поток порта, из которого страницы должны быть взяты для вставки, место, куда страницы должны быть вставлены, и целочисленный массив страниц из потока порта, которые должны быть вставлены в входной файл PDF. Этот массив содержит список конкретных страниц, которые вы хотите вставить в входной поток PDF. Наконец, выходной поток PDF сохраняется с указанным массивом страниц, вставленных в входной файл. Следующий фрагмент кода показывает, как вставить массив страниц PDF с использованием потоков.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesUsingStreams-InsertPagesUsingStreams.cs" >}}