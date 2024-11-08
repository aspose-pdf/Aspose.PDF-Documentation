---
title: Преобразование FDF в формат XML
type: docs
weight: 10
url: /ru/net/converting-an-fdf-to-xml-format/
description: Этот раздел объясняет, как можно преобразовать FDF в формат XML с помощью класса FormDataConverter.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Пространство имен [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) в [Aspose.PDF for .NET](/pdf/ru/net/) хорошо поддерживает AcroForms. Оно также поддерживает импорт и экспорт данных форм в различные форматы файлов, такие как FDF, XFDF и XML. Однако иногда разработчикам может потребоваться преобразовать один формат в другой. В этой статье рассматривается функция, которая преобразует FDF в XML.

{{% /alert %}}

## Подробности

FDF обозначает Формат Данных Форм, и файл FDF содержит значения формы в виде пар ключ/значение. Мы также знаем, что XML файл содержит значения в виде тегов. Где, в основном, ключ представлен в виде имени тега, а значение представлено в виде значения внутри этого тега. Теперь, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) предоставляет нам возможность преобразовать формат файла FDF в формат XML.

Мы можем использовать класс [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter) для этой цели. Этот класс предоставляет нам различные методы для преобразования одного формата данных в другой. В этой статье мы будем использовать только один метод под названием [ConvertFdfToXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml). Этот метод принимает FDF файл в качестве входного или исходного потока и сохраняет его в формате XML.

Следующий фрагмент кода показывает, как преобразовать файл FDF в файл XML: