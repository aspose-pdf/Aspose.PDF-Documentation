---
title: Исследование возможностей класса FormEditor
type: docs
weight: 10
url: /net/exploring-features-of-formeditor-class/
description: Вы можете узнать детали исследования возможностей класса FormEditor с библиотекой Aspose.PDF для .NET
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

PDF документы иногда содержат интерактивные формы, которые известны как AcroForm. Это похоже на форму, используемую на веб-страницах. Эти формы содержат различные типы элементов управления, такие как текстовые поля, флажки и кнопки и т. д. Разработчику, работающему с PDF файлами, иногда может потребоваться редактировать эти формы. В этой статье мы рассмотрим, как [пространство имен Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) позволяет нам это делать.

{{% /alert %}}

## Детали реализации

Разработчики могут использовать [пространство имен Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) не только для добавления новых форм и полей форм в PDF документ, но и для редактирования существующих полей. Область применения этой статьи ограничена функциями [Aspose.PDF for .NET](/pdf/net/), которые связаны с редактированием форм.

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) — это класс, содержащий большинство методов и свойств, которые позволяют разработчикам редактировать поля форм. Вы можете не только добавлять новые поля, но и удалять существующие, перемещать одно поле на другую позицию, изменять имя поля или его атрибуты и т.д. Список функций, предоставляемых этим классом, довольно обширен, и работать с полями форм с помощью этого класса очень легко.

Эти методы можно разделить на две основные категории, одна из которых используется для манипуляции полями, а другая — для установки новых атрибутов этих полей. Методы, которые мы можем сгруппировать под первую категорию, включают AddField, AddListItem, RemoveListItem, CopyInnerField, CopyOuterField, DelListItem, MoveField, RemoveField и RenameField и т. д. Во вторую категорию методов можно включить SetFieldAlignment, SetFieldAppearance, SetFieldAttribute, SetFieldLimit, SetFieldScript. Следующий фрагмент кода демонстрирует некоторые из методов класса FormEditor в работе:

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-FormEditorFeatures-FormEditorFeatures.cs" >}}