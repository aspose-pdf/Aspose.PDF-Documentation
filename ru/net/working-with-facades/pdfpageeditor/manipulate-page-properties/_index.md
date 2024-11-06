---
title: Манипуляция с Свойствами Страницы
type: docs
weight: 80
url: ru/net/manipulate-page-properties/
description: В этом разделе объясняется, как манипулировать свойствами страницы с помощью Aspose.PDF Facades, используя класс PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---

## Получение Свойств Страницы PDF из Существующего PDF Файла

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) позволяет работать с отдельными страницами PDF файла. It helps you get the individual page's properties like different page box sizes, page rotation, page zoom etc. In order to get those properties, you need to create [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) object and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, you can use different methods to get the page properties like [GetPageRotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation), [GetPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpages), [GetPageBoxSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize) etc.

Следующий фрагмент кода показывает, как получить свойства страницы PDF из существующего PDF файла.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-GetPageProperties-GetPageProperties.cs" >}}
## Установка свойств страницы PDF в существующем PDF файле

Чтобы установить свойства страницы, такие как поворот страницы, масштабирование или начальная точка, необходимо использовать класс [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). Этот класс предоставляет различные методы и свойства для настройки этих свойств страницы. Прежде всего, вам нужно создать объект класса [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) и привязать входной PDF файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вы можете использовать эти методы и свойства для установки свойств страницы. Наконец, сохраните обновленный PDF файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

Следующий фрагмент кода показывает, как установить свойства страницы PDF в существующем PDF файле.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-SetPageProperties-SetPageProperties.cs" >}}

## Изменение размера содержимого страниц на определённых страницах в PDF-файле

Метод ResizeContents класса [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) позволяет изменить размер содержимого страниц в PDF-файле. Класс [ContentsResizeParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) используется для указания параметров, которые будут использованы для изменения размера страницы(страниц), например, отступы в процентах или единицах и т.д. Вы можете изменить размер всех страниц или указать массив страниц, размер которых нужно изменить, с помощью метода ResizeContents.

Следующий фрагмент кода показывает, как изменить размер содержимого некоторых конкретных страниц PDF-файла.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-ResizePageContents-ResizePageContents.cs" >}}