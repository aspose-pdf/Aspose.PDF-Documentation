---
title: Создание закладок
type: docs
weight: 10
url: ru/net/create-bookmarks/
description: Этот раздел объясняет, как создать закладки в вашем PDF файле с использованием Aspose.PDF Facades и класса PdfBookmarkEditor.
lastmod: "2021-06-05"
draft: false
---

## Создание закладок для всех страниц

Чтобы создать закладки для всех страниц, вам нужно использовать метод [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) без параметров. Класс [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) позволяет создавать закладки для всех страниц PDF файла. Сначала вам нужно создать объект класса [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) и связать входной PDF, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Затем вам нужно вызвать метод [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) и сохранить выходной PDF файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Следующий фрагмент кода показывает, как создать закладки.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksAll-CreateBookmarksAll.cs" >}}

## Создание закладок для всех страниц с характеристиками

Класс [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) позволяет создавать закладки для всех страниц PDF файла и задавать свойства (Цвет, Жирный, Курсив). Вы можете сделать это с помощью метода [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Сначала вам нужно создать объект класса [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) и связать входной PDF с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Затем, вы должны вызвать метод [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) и сохранить выходной PDF файл с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Следующий фрагмент кода показывает, как создать закладки для всех страниц с их свойствами.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksPagesProperties-CreateBookmarksPagesProperties.cs" >}}

## Создание закладки для конкретной страницы

Вы можете создать закладку для конкретной страницы в существующем PDF файле, используя метод [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1). Этот метод принимает два аргумента: название закладки и номер страницы. Сначала вам нужно создать объект класса [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) и связать входной PDF-файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Затем вы должны вызвать метод [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) и сохранить выходной PDF-файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Следующий фрагмент кода показывает, как создать закладку для конкретной страницы.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPage-CreateBookmarkPage.cs" >}}

## Создание закладок для диапазона страниц

Класс [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) позволяет создавать закладки для диапазона страниц. Вы можете использовать метод [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) с двумя параметрами: список закладок (список названий закладок) и список страниц (список страниц для создания закладок). Сначала вам нужно создать объект класса [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) и связать входной PDF файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Затем вы должны вызвать метод [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) и сохранить выходной PDF, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Следующий фрагмент кода показывает, как создать закладки для диапазона страниц.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPageRange-CreateBookmarkPageRange.cs" >}}
## Добавление закладки в существующий PDF файл

Вы можете добавить закладку в существующий PDF файл, используя класс [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). Чтобы создать закладку, необходимо создать объект [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) и установить необходимые атрибуты закладки. После этого, нужно передать объект [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) в метод [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) класса [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). Наконец, нужно сохранить обновленный PDF файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Следующий фрагмент кода показывает, как добавить закладку в существующий PDF файл.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddBookmark-AddBookmark.cs" >}}

## Добавление дочерней закладки в существующий PDF файл

Вы можете добавить дочерние закладки в существующий PDF файл, используя класс [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). In order to add child bookmarks, you need to create [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) объекты. You can add individual [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) объекты в [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) объект. Вы также должны создать объект [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) и установить его свойство [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) в объект [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks). Затем вам нужно передать этот объект [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) с [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) в метод [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Наконец, вам нужно сохранить обновленный PDF, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) класса [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). Следующий фрагмент кода показывает, как добавить дочерние закладки в существующий PDF файл.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddChildBookmark-AddChildBookmark.cs" >}}
## See also

Попробуйте сравнить и найти способ работы с закладками, который подходит вам. Давайте изучим раздел [Работа с закладками в PDF](/pdf/net/bookmarks/).