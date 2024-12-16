---
title: Extensible Metadata Platform - XMP
type: docs
weight: 10
url: /ru/net/working-with-extensible-metadata-platform-xmp/
description: Этот раздел объясняет, как работать с Extensible Metadata Platform - XMP, используя класс PdfXmpMetadata.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Extensible Metadata Platform (XMP) — это стандарт, созданный компанией Adobe Systems Inc. Этот стандарт был разработан для обработки и хранения стандартизированных и проприетарных метаданных. Эти метаданные могут быть встроены в различные форматы файлов, но в этой статье мы сосредоточимся только на формате файла PDF. Мы увидим, как можно встроить метаданные в PDF-файл, используя пространство имен Aspose.Pdf.Facades в Aspose.PDF для .NET. Мы будем использовать класс [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) для обработки XMP в PDF-документе.

{{% /alert %}}

## Background

PDF-файл проходит через множество стадий в течение своего жизненного цикла.
``` Мы создаем PDF-документ и затем передаем его другим людям или отделам для дальнейшей обработки. Однако в процессе этого нам нужно отслеживать различные аспекты внесенных изменений. XMP служит для этой цели, чтобы отслеживать изменения или другую информацию о данных в файле.

## Объяснение

Для того чтобы управлять XMP с использованием Aspose.Pdf.Facades, мы будем использовать класс [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class). Мы будем использовать этот класс для управления предопределенными свойствами метаданных. Класс [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) добавляет эти свойства в PDF-файл. Он также помогает открывать и сохранять PDF-файлы, в которые мы добавляем метаданные. Таким образом, используя класс [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class), мы можем легко управлять XMP в PDF-файле.

Следующий фрагмент кода поможет вам понять, как использовать класс [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) для работы с XMP:
{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ExtensibleMetadataPlatform-ExtensibleMetadataPlatform.cs" >}}

## Заключение

{{% alert color="primary" %}}
В этой статье мы рассмотрели, как можно работать с XMP, используя Aspose.Pdf.Facades. [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class), использованный в этой статье, делает работу с метаданными в PDF-документе очень простой для пользователя. Если класс [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) используется правильно, будет очень легко внедрять интеллект в PDF-файлы и приблизить реализацию семантической сети.
{{% /alert %}}