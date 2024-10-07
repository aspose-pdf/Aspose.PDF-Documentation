---
title: Разделить страницы PDF
type: docs
weight: 60
url: /net/split-pdf-pages/
description: Этот раздел объясняет, как разделить страницы PDF с помощью Aspose.PDF Facades, используя класс PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Разделение страниц PDF с первой страницы с использованием путей к файлам

Метод [SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) позволяет разделить PDF файл, начиная с первой страницы и заканчивая указанным номером страницы. Если вы хотите обрабатывать PDF файлы с диска, вы можете передать пути к входному и выходному PDF файлам этому методу. Следующий фрагмент кода показывает, как разделить страницы PDF с первой, используя пути к файлам.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingPaths-SplitPagesUsingPaths.cs" >}}

## Разделение страниц PDF с первой страницы с использованием потоков файлов


[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) метод класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) позволяет разделить PDF файл, начиная с первой страницы и заканчивая указанным номером страницы. Если вы хотите обрабатывать PDF файлы из потоков, вы можете передать входные и выходные потоки PDF в этот метод. Следующий фрагмент кода показывает, как разделить страницы PDF, начиная с первой, используя файловые потоки.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingStreams-SplitPagesUsingStreams.cs" >}}

## Разделение страниц PDF на наборы с использованием путей к файлам

Метод [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) позволяет разделить PDF файл на несколько наборов страниц. In this example, we require two sets of pages (1, 2) and (5, 6). If you want to access the PDF file from the disk, you need to pass the input PDF as file path. This method returns an array of MemoryStream. You can loop through this array and save the individual sets of pages as separate files. The following code snippet shows you how to split PDF pages to bulk using file paths.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingPaths-SplitPagesToBulkUsingPaths.cs" >}}

## Разделение страниц PDF на группы с использованием потоков

Метод [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет вам разделить файл PDF на несколько наборов страниц. В этом примере нам нужны два набора страниц (1, 2) и (5, 6). Вы можете передать поток в этот метод вместо доступа к файлу с диска. Этот метод возвращает массив MemoryStream. Вы можете перебрать этот массив и сохранить отдельные наборы страниц как отдельные файлы. Следующий пример кода показывает, как разделить страницы PDF на группы, используя потоки.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingStreams-SplitPagesToBulkUsingStreams.cs" >}}

## Разделение страниц PDF до конца, используя пути к файлам

Метод [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет разделить PDF с указанного номера страницы до конца PDF-файла и сохранить его как новый PDF. Для этого, используя пути к файлам, вам нужно передать пути к входному и выходному файлам и номер страницы, с которой нужно начать разделение. Выходной PDF будет сохранен на диск. Следующий фрагмент кода показывает, как разделить страницы PDF до конца, используя пути к файлам.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingPaths-SplitPagesToEndUsingPaths.cs" >}}

## Разделение страниц PDF до конца, используя потоки

Метод [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет разделить PDF, начиная с указанного номера страницы и до конца файла PDF, и сохранить его как новый PDF. Для того чтобы сделать это, используя потоки, вам нужно передать входные и выходные потоки и номер страницы, с которой нужно начать разделение. Выходной PDF будет сохранён в выходной поток. Следующий фрагмент кода показывает, как разделить страницы PDF до конца, используя потоки.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingStreams-SplitPagesToEndUsingStreams.cs" >}}

## Разделить PDF на отдельные страницы, используя пути к файлам

{{% alert color="primary" %}}

Вы можете попробовать разделить PDF-документ и просмотреть результаты онлайн по этой ссылке:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

Чтобы разделить PDF-файл на отдельные страницы, вам нужно передать PDF как путь к файлу в метод [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Этот метод вернет массив MemoryStream, содержащий отдельные страницы PDF-файла. Вы можете пройтись по этому массиву MemoryStream и сохранить отдельные страницы как отдельные PDF-файлы на диск. Следующий фрагмент кода показывает, как разделить PDF на отдельные страницы, используя пути к файлам.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingPaths-SplitToIndividualPagesUsingPaths.cs" >}}

## Разделение PDF на отдельные страницы с использованием потоков

Чтобы разделить PDF-файл на отдельные страницы, вам нужно передать PDF в виде потока методу [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Этот метод вернет массив MemoryStream, содержащий отдельные страницы PDF файла. Вы можете перебрать этот массив MemoryStream и сохранить отдельные страницы как отдельные PDF файлы на диске, или вы можете оставить эти отдельные страницы в потоке памяти для последующего использования в вашем приложении. Следующий фрагмент кода показывает, как разделить PDF на отдельные страницы с использованием потоков.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingStreams-SplitToIndividualPagesUsingStreams.cs" >}}