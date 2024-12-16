---
title: В чем разница между форматами FDF, XML и XFDF
type: docs
weight: 30
url: /ru/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: Этот раздел различает формы XML, FDF и XFDF с использованием класса Form из Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Мы смешали множество различных терминов, таких как FDF, XML и XFDF. Все эти термины связаны друг с другом каким-то образом. Эта статья исследует эти концепции и их взаимосвязь.

{{% /alert %}}

## Распутывание форм

Aspose.PDF для .NET используется для работы с PDF-документами, стандартизированными Adobe. PDF-документы содержат интерактивные формы, называемые AcroForms. Эти интерактивные формы имеют ряд полей формы, таких как комбинированные списки, текстовые поля и переключатели. Интерактивные формы Adobe и поля формы работают так же, как HTML-форма и ее поля формы.

Возможно хранить значения полей формы в отдельном файле: файле FDF (Формат Данных Форм). Этот документ содержит значения полей формы в формате ключ/значение. FDF файлы до сих пор используются для этой цели. Но Adobe также предоставляет тип FDF, закодированный в XML, называемый XFDF. XFDF файл сохраняет значения полей формы иерархическим способом с использованием XML тегов.

С Aspose.PDF разработчики могут не только экспортировать значения полей формы PDF в файл FDF или XFDF, но также в файл XML. Все эти файлы используют разный синтаксис для сохранения значений полей формы PDF. Пример ниже объясняет различия.

Предположим, что есть некоторые поля формы PDF, значения которых нужно представить в формах FDF, XML и XFDF. Эти предполагаемые поля формы с их именами полей и значениями показаны ниже:

|**Field Name**|**Field Value**|
| :- | :- |
|Company|Aspose.com|
|Address.1|Sydney, Австралия|
|Address.2|Дополнительная строка адреса|
Давайте посмотрим, как представить эти значения в форматах FDF, XML и XFDF.

### Что такое формат FDF?

Как мы знаем, файл FDF хранит данные в формате Ключ/Значение, где /T представляет Ключ, /V представляет Значение, а данные в скобках () представляют содержимое либо Ключа, либо Значения. For example, /T(Company) означает, что Company является ключом поля, а /V(Aspose.com) предназначен для значения поля.

/T(Company) /V(Aspose.com) /T(Address.1) /V( Sydney , Australia ) /T(Address.2) /V(Additional Address Line)

### Что такое формат XML?

Разработчики могут представлять каждое поле формы PDF в виде тега поля, `<field>`. Каждый тег поля имеет атрибут, имя, показывающее имя поля, и под тегом, `<value>`, представляющим значение поля, как показано ниже:

```xml
 <?xml version="1.0" ?>
 <fields>
  <field name="Company">
    <value>Aspose.com</value>
  </field>
  <field name="Address.1">
    <value>Sydney, Australia</value>
  </field>
  <field name="Address.2">
    <value>Additional Address Line</value>
  </field>
 </fields>
```

### ### Что такое формат XFDF?

Представление вышеуказанных данных в формате XFDF похоже на XML, за исключением нескольких различий. В XFDF файлах мы добавляем их XML Namespace, который является <http://ns.adpbe.com/xfdf/>, и есть дополнительный тег `<f>`, который используется для указания на PDF документ, содержащий эти поля формы PDF. Как и XML, XFDF также содержит поля в виде тегов полей, `<field>`, как показано ниже:

```xml

<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">   
   <f href="CompanyForm.pdf"/> 
   <fields>
      <field name="Company">
         <value>Aspose.com</value>
      </field>
      <field name="Address">
         <field name="1">
            <value>Sydney, Australia</value>
         </field>
         <field name="2">
            <value>Additional Address Line</value>
         </field>
      </field>
   </fields>
 </xfdf>
```

### Идентификация имен полей формы

Aspose.PDF для .NET предоставляет возможность создавать, редактировать и заполнять уже созданные PDF формы. Он содержит класс [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), который имеет функцию с именем [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index), и она принимает два параметра, т.е. имя поля, которое нужно заполнить, и значение поля. Поэтому, чтобы заполнить поля формы, вы должны знать точное имя поля формы. Мы часто сталкиваемся со сценарием, в котором нам нужно заполнить форму, созданную в каком-либо инструменте, т.е. Adobe Designer, и мы не уверены в названиях полей формы. Чтобы выполнить наше требование, нам нужно прочитать названия всех полей формы PDF. Класс [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) предоставляет свойство с названием [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames), которое возвращает все названия полей и возвращает null, если в PDF нет полей. Но это свойство вернет все названия полей формы PDF, и мы не будем уверены, какое название соответствует какому полю на форме.

В качестве решения этой проблемы нам потребуется атрибуты внешнего вида каждого поля. [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) класс имеет функцию с именем GetFieldFacade, которая возвращает атрибуты, включая расположение, цвет, стиль границы, шрифт, элемент списка и так далее. Чтобы сохранить эти значения, мы будем использовать класс [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), который используется для записи визуальных атрибутов полей. Получив эти атрибуты, мы можем добавить текстовое поле под каждым полем, которое будет отображать имя поля. Здесь возникает вопрос, как определить место, где добавить текстовое поле? Решение этой проблемы — свойство Box в классе [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), которое содержит расположение поля. Мы сохраним эти значения в массив типа прямоугольник и будем использовать эти значения для определения позиции, где добавлять новые текстовые поля. В пространстве имен Aspose.Pdf.Facades у нас есть класс с именем [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor), который предоставляет возможность манипулировать формой PDF. Откройте PDF-форму, добавьте текстовое поле под каждым существующим полем формы и сохраните PDF-форму под новым именем.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-DifferenceBetweenFile-DifferenceBetweenFile.cs" >}}