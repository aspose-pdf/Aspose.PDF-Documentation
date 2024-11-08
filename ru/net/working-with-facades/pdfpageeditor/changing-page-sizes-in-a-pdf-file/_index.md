---
title: Изменение размеров страниц в PDF файле
type: docs
weight: 30
url: /ru/net/changing-page-sizes-in-a-pdf-file/
description: Попробуйте узнать, как изменить размеры страниц в PDF файле, используя класс PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---

## Подробности

Класс [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) в [пространстве имен Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) содержит свойство с названием [PageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagesize), которое может использоваться для изменения размера страницы одного или нескольких страниц одновременно. Свойство Pages можно использовать для назначения номеров страниц, к которым необходимо применить новый размер страницы. Класс PageSize содержит список различных размеров страниц в качестве своих членов. Любой из членов этого класса может быть назначен свойству PageSize класса [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). Вы также можете получить размер страницы для любой страницы, используя метод GetPageSize и передавая номер страницы.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ChangePageSizes-ChangePageSizes.cs" >}}