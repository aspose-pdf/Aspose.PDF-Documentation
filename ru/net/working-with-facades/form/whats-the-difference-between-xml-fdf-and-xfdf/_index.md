---
title: Какова разница между форматами FDF, XML и XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ru/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: В этом разделе рассматривается разница между формами XML, FDF и XFDF с использованием Facades Aspose.PDF и класса Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats is the difference between FDF, XML, and XFDF formats",
    "alternativeHeadline": "Understanding FDF, XML, and XFDF Formats in Aspose.PDF for .NET",
    "abstract": "Узнайте о различиях между форматами FDF, XML и XFDF в манипуляции данными форм PDF через Aspose.PDF for .NET. Эта функция позволяет разработчикам без проблем экспортировать значения интерактивных полей форм в различных форматах, каждый из которых имеет свою собственную синтаксис, одновременно улучшая понимание и использование этих основных типов файлов в обработке PDF. Оптимизируйте обработку форм PDF с подробными сведениями о том, как представлять поля форм в различных форматах данных.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1045",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/whats-the-difference-between-xml-fdf-and-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whats-the-difference-between-xml-fdf-and-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

Мы смешали много различных терминов, таких как FDF, XML и XFDF. Все эти термины каким-то образом связаны друг с другом. Эта статья исследует эти концепции и их взаимосвязь.

{{% /alert %}}

## Раскрытие форм

Aspose.PDF for .NET используется для манипуляции PDF-документами, стандартизированными Adobe. PDF-документы содержат интерактивные формы, называемые AcroForms. Эти интерактивные формы имеют ряд полей формы, таких как комбинированный, текстовое поле и радиокнопка. Интерактивные формы Adobe и поля формы работают так же, как HTML-форма и ее поля формы.

Возможно хранить значения полей формы в отдельном файле: файле FDF (Forms Data Format). Он содержит значения полей формы в формате ключ/значение. FDF-файлы все еще используются для этой цели. Но Adobe также предоставляет XML-кодированный тип FDF, называемый XFDF. Файл XFDF хранит значения полей формы иерархически, используя XML-теги.

С помощью Aspose.PDF разработчики могут не только экспортировать значения полей формы PDF в файл FDF или XFDF, но и в файл XML. Все эти файлы используют различный синтаксис для сохранения значений полей формы PDF. Пример ниже объясняет различия.

Предположим, что есть некоторые поля формы PDF, значения которых необходимо представить в формах FDF, XML и XFDF. Эти предполагаемые поля формы с их именами и значениями показаны ниже:

|**Имя поля**|**Значение поля**|
| :- | :- |
|Компания|Aspose.com|
|Адрес.1|Сидней, Австралия|
|Адрес.2|Дополнительная строка адреса|
Давайте посмотрим, как представить эти значения в форматах FDF, XML и XFDF.

### Что такое формат FDF?

Как мы знаем, файл FDF хранит данные в формате ключ/значение, где /T представляет ключ, /V представляет значение, а данные в скобках () представляют содержимое либо ключа, либо значения. Например, /T(Компания) означает, что Компания является ключом поля, а /V(Aspose.com) предназначено для значения поля.

/T(Компания) /V(Aspose.com)
/T(Адрес.1) /V(Сидней, Австралия)
/T(Адрес.2) /V(Дополнительная строка адреса)

### Что такое формат XML? 

Разработчики могут представлять каждое поле формы PDF в виде тега поля, `<field>`. Каждый тег поля имеет атрибут, name, показывающий имя поля, и подтаг, `<value>`, представляющий значение поля, как показано ниже:

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

### Что такое формат XFDF?  

Представление вышеуказанных данных в форме XFDF похоже на форму XML, за исключением нескольких различий. В XFDF-файлах мы добавляем их XML-пространство имен, которое является <http://ns.adpbe.com/xfdf/>, и есть дополнительный тег, `<f>`, который используется для указания на PDF-документ, содержащий эти поля формы PDF. Как и XML, XFDF также содержит поля в виде тегов поля, `<field>`, как показано ниже:

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

### Определение имен полей формы

Aspose.PDF for .NET предоставляет возможность создавать, редактировать и заполнять уже созданные PDF-формы. Он содержит [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form) класс, который имеет функцию под названием [FillField](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/fillfield/index), и она принимает два параметра: имя поля, которое необходимо заполнить, и значение поля. Таким образом, чтобы заполнить поля формы, вы должны знать точное имя поля формы.
Мы часто сталкиваемся со сценарием, в котором нам нужно заполнить форму, созданную в каком-то инструменте, например, Adobe Designer, и мы не уверены в именах полей формы. Чтобы выполнить нашу задачу, нам нужно прочитать имена всех полей формы PDF. Класс [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form) предоставляет свойство под названием [FieldsNames](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/properties/fieldnames), которое возвращает все имена полей и возвращает null, если в PDF нет полей. Но это свойство вернет все имена полей формы PDF, и мы не будем уверены, какое имя соответствует какому полю на форме.

В качестве решения этой проблемы нам потребуются атрибуты внешнего вида каждого поля. Класс [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) имеет функцию под названием GetFieldFacade, которая возвращает атрибуты, включая местоположение, цвет, стиль границы, шрифт, элементы списка и так далее. Чтобы сохранить эти значения, мы будем использовать класс [FormFieldFacade](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formfieldfacade), который используется для записи визуальных атрибутов полей. Как только у нас будут эти атрибуты, мы можем добавить текстовое поле под каждым полем, которое будет отображать имя поля. Здесь возникает вопрос, как мы определим местоположение, где добавить текстовое поле? Решение этой проблемы - свойство Box в классе [FormFieldFacade](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formfieldfacade), которое хранит местоположение поля. Мы сохраним эти значения в массиве типа прямоугольник и используем эти значения для определения позиции, где добавить новые текстовые поля.
В пространстве имен Aspose.Pdf.Facades у нас есть класс [FormEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor), который предоставляет возможность манипулировать PDF-формой. Откройте PDF-форму, добавьте текстовое поле под каждым существующим полем формы и сохраните PDF-форму с новым именем.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DifferenceBetweenFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // First a input pdf file should be assigned
    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf"))
    {
        // Get all field names
        String[] allfields = form.FieldNames;
        // Create an array which will hold the location coordinates of Form fields
        var box = new System.Drawing.Rectangle[allfields.Length];
        for (int i = 0; i < allfields.Length; i++)
        {
            // Get the appearance attributes of each field, consecutively
            var facade = form.GetFieldFacade(allfields[i]);
            // Box in FormFieldFacade class holds field's location.
            box[i] = facade.Box;
        }
        // Save PDF document
        form.Save(dataDir + "DifferenceBetweenFile_out.pdf");
            
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
        {
            // Now we need to add a textfield just upon the original one
            FormEditor editor = new Aspose.Pdf.Facades.FormEditor(document);
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "TextField" + i, allfields[i], 1, box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "DifferenceBetweenFile_out.pdf");
        }
    }
}
```