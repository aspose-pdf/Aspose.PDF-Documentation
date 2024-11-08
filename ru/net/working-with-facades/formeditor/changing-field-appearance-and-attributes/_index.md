---
title: Внешний вид и атрибуты поля
type: docs
weight: 20
url: /ru/net/changing-field-appearance-and-attributes/
description: Этот раздел объясняет, как изменить внешний вид и атрибуты поля с помощью класса FormEditor.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Класс [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) из [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) позволяет не только изменять внешний вид и ощущения от поля формы, но и поведение поля. В этой статье мы посмотрим, как мы можем использовать класс FormEditor для изменения внешнего вида поля, атрибутов поля, а также ограничения поля.

{{% /alert %}}

## Детали реализации

Метод [SetFieldAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) используется для изменения внешнего вида поля формы. Он принимает AnnotationFlag в качестве параметра. AnnotationFlag — это перечисление, которое имеет различные члены, такие как Hidden или NoRotate и т.д.

Метод [SetFieldAttributes](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) используется для изменения атрибута поля формы. Параметр, переданный этому методу, является перечислением PropertyFlag, которое содержит такие члены, как ReadOnly или Required и т.д.

Класс [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) также предоставляет метод для установки ограничения поля. Он указывает полю, сколько символов оно может содержать. Приведенный ниже фрагмент кода показывает, как можно использовать все эти методы.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ChangingFieldAppearance-ChangingFieldAppearance.cs" >}}