---
title: Импорт и экспорт закладок
type: docs
weight: 20
url: /net/import-and-export-bookmarks/
description: В этом разделе объясняется, как импортировать и экспортировать закладки с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Импорт закладок из XML в существующий PDF файл

Метод [ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) позволяет импортировать закладки в PDF файл из XML файла. Чтобы импортировать закладки, необходимо создать объект [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) и связать PDF файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). После этого нужно вызвать метод [ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/importbookmarkswithxml/methods/1). Наконец, сохраните обновленный PDF файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). В следующем фрагменте кода показано, как импортировать закладки из XML файла.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ImportFromXML-ImportFromXML.cs" >}}

## Экспорт закладок в XML из существующего PDF файла

Метод ExportBookmarksToXml позволяет экспортировать закладки из PDF файла в XML файл.

Для экспорта закладок:

1. Создайте объект PdfBookmarkEditor и свяжите PDF файл, используя метод BindPdf.  
1. Вызовите метод ExportBookmarksToXml.  
1. Сохраните обновленный PDF файл, используя метод Save.  

Следующий фрагмент кода показывает, как экспортировать закладки в XML файл.  

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExportToXML-ExportToXML.cs" >}}