---
title: Обновление, удаление и получение закладок
type: docs
weight: 30
url: /ru/net/update-delete-and-get-bookmarks/
description: В этом разделе объясняется, как обновлять, удалять и получать закладки с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Обновление существующей закладки в PDF файле

Чтобы обновить существующую закладку в PDF файле, вам нужно использовать метод [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks). Этот метод принимает два аргумента: исходное название (название закладки, которую нужно изменить), конечное название (название, которое должно быть заменено). Вам нужно создать объект класса [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) и связать входной PDF файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого нужно вызвать метод [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks), а затем сохранить обновленный PDF, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Следующий фрагмент кода показывает, как изменить существующую закладку в PDF файле.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-UpdateBookmark-UpdateBookmark.cs" >}}

## Удаление всех закладок из PDF файла

Вы можете удалить все закладки из PDF файла, используя метод [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) без каких-либо параметров. В первую очередь, вам нужно создать объект класса [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) и привязать входной PDF файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого, вам нужно вызвать метод [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks), а затем сохранить обновленный PDF файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Приведенный ниже фрагмент кода показывает, как удалить все закладки из PDF файла.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteAllBookmarks-DeleteAllBookmarks.cs" >}}

## Удаление конкретной закладки из PDF файла

Чтобы удалить конкретную закладку, вам нужно вызвать метод [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) с параметром строки (название).  *title* здесь представляет закладку, которую нужно удалить из PDF. Создайте объект класса [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) и привяжите входной PDF-файл с использованием метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вызовите метод [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) и затем сохраните обновленный PDF-файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Следующий фрагмент кода показывает, как удалить конкретную закладку из PDF-файла.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteABookmark-DeleteABookmark.cs" >}}

## Получение закладок из документа PDF Facades

Класс [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) предоставляет возможность управлять закладками в существующем PDF-файле. Он предоставляет различные свойства для получения/установки информации о закладках. Следующий фрагмент кода показывает, как получить информацию, связанную с каждой закладкой в PDF файле.

## Извлечение Закладок из Существующего PDF Файла

Метод [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) позволяет извлекать закладки из PDF файла. В целях извлечения закладок необходимо создать объект [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) и связать PDF файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вам нужно вызвать метод [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3). Метод [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) возвращает объект [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks/methods/index). Затем вы можете пройтись по этим закладкам и получить отдельные объекты [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark). Наконец, сохраните обновленный PDF файл с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Следующий фрагмент кода показывает, как экспортировать закладки в XML файл.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExtractBookmarks-ExtractBookmarks.cs" >}}