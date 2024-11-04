---
title: Identifying form fields names
type: docs
weight: 10
url: /net/identifying-form-fields-names/
description: Aspose.PDF.Facades позволяет определять имена полей формы с использованием класса Form.
lastmod: "2021-06-05"
draft: false
---

[Aspose.PDF for .NET](/pdf/net/) предоставляет возможность создавать, редактировать и заполнять уже созданные PDF-формы. Пространство имен [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) содержит класс [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), который содержит функцию с именем [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index), и она принимает два аргумента, т.е. имя поля и значение поля. Таким образом, для заполнения полей формы необходимо знать точное имя поля формы.

## Implementation details

Часто мы сталкиваемся с ситуацией, когда необходимо заполнить форму, созданную в каком-либо инструменте, т.е. Adobe Designer, и мы не уверены в названиях полей формы. Чтобы заполнить поля формы, сначала нам нужно прочитать названия всех полей формы Pdf. Класс [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) предоставляет свойство с именем [FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames), которое возвращает все имена полей и возвращает null, если PDF не содержит никаких полей. Однако при использовании этого свойства мы получаем имена всех полей в форме PDF, и мы не можем быть уверены, какое имя соответствует какому полю в форме.

В качестве решения этой проблемы мы будем использовать атрибуты внешнего вида каждого поля. Form class имеет функцию с именем [GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade), которая возвращает атрибуты, включая местоположение, цвет, стиль границы, шрифт, элемент списка и так далее. Чтобы сохранить эти значения, нам нужно использовать класс [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), который используется для записи визуальных атрибутов полей. Как только у нас есть эти атрибуты, мы можем добавить текстовое поле под каждым полем, которое будет отображать имя поля.

{{% alert color="primary" %}}
На этом этапе возникает вопрос: "как мы определим местоположение, где добавить текстовое поле?"
{{% /alert %}}

{{% alert color="primary" %}}
Решением этой проблемы является свойство Box в классе [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), которое содержит местоположение поля. Мы должны сохранить эти значения в массив типа прямоугольников и использовать эти значения для определения позиции, где добавить новые текстовые поля.

{{% /alert %}}

В пространстве имен [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) у нас есть класс под названием [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor), который предоставляет возможность манипулировать PDF-формами. Откройте PDF-форму; добавьте текстовое поле под каждым существующим полем формы и сохраните PDF-форму с новым именем.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-IdentifyFormFields-IdentifyFormFields.cs" >}}