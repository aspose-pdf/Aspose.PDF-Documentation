---
title: Конвертация XML в формат FDF
type: docs
weight: 20
url: /net/converting-an-xml-to-fdf-format/
description: Этот раздел объясняет, как вы можете конвертировать XML в формат FDF с помощью FormDataConverter.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Пространство имен [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) в [Aspose.PDF for .NET](/pdf/net/) отлично поддерживает AcroForms. Оно также поддерживает импорт и экспорт данных формы в различные форматы файлов, такие как FDF, XFDF и XML. Однако иногда разработчику необходимо конвертировать один формат в другой. В этой статье мы рассмотрим функцию, которая позволяет нам конвертировать формат FDF в XML.

{{% /alert %}}

## Детали

FDF означает Формат Данных Форм, и файл FDF содержит значения формы в виде пары ключ/значение. Мы также знаем, что XML файл содержит значения в виде тегов. Где, в основном, ключ представлен как имя тега, а значение представлено как значение внутри этого тега. Теперь, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) предоставляет гибкость для преобразования формата XML файла в формат FDF.

Используйте класс [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter) для этой цели. Этот класс предоставляет различные методы для преобразования одного формата данных в другой. Эта статья показывает, как использовать один метод, ConvertXmlToFdf(..), который принимает файл FDF в качестве входного или исходного потока и сохраняет его в формате XML. Следующий фрагмент кода показывает, как преобразовать файл FDF в файл XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-XMLToPdf-XMLToPdf.cs" >}}