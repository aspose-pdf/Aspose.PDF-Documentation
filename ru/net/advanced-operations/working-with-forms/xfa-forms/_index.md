---
title: Работа с XFA формами
linktitle: XFA формы
type: docs
weight: 20
url: /ru/net/xfa-forms/
description: Aspose.PDF для .NET API позволяет работать с полями XFA и XFA Acroform в документе PDF. Aspose.PDF.Facades.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с XFA формами",
    "alternativeHeadline": "Заполнение, конвертация и получение XFA форм в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, заполнить xfa форму, получить xfa форму, конвертировать xfa форму",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
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
                "contactType": "продажи",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF для .NET API позволяет работать с полями XFA и XFA Acroform в документе PDF. Aspose.PDF.Facades."
}
</script>
{{% alert color="primary" %}}

Динамические формы основаны на спецификации XML, известной как XFA, "Архитектура XML-форм". Также возможно преобразование динамической формы XFA в стандартную Acroform. Информация о форме (насколько это касается PDF) очень скудная – она указывает, что поля существуют, с свойствами и событиями JavaScript, но не определяет их визуализацию. Объекты формы XFA отрисовываются в момент загрузки документа.

{{% /alert %}}

Класс Form предоставляет возможность работать со статической AcroForm, и вы можете получить экземпляр конкретного поля, используя метод GetFieldFacade(..) класса Form. Однако поля XFA недоступны через метод Form.GetFieldFacade(..). Вместо этого используйте [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa) для получения/установки значений полей и управления шаблоном поля XFA (установка свойств поля).

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Заполнение полей XFA

Следующий фрагмент кода показывает, как заполнить поля в форме XFA.
Следующий фрагмент кода показывает, как заполнять поля в форме XFA.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Загрузить XFA форму
Document doc = new Document(dataDir + "FillXFAFields.pdf");

// Получить имена полей XFA формы
string[] names = doc.Form.XFA.FieldNames;

// Установить значения полей
doc.Form.XFA[names[0]] = "Поле 0";
doc.Form.XFA[names[1]] = "Поле 1";
dataDir = dataDir + "Filled_XFA_out.pdf";
// Сохранить обновленный документ
doc.Save(dataDir);
```

## Конвертация XFA в Acroform

{{% alert color="primary" %}}

Попробуйте онлайн
Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке: [products.aspose.app/pdf/xfa/](https://products.aspose.app/pdf/xfa/)

{{% /alert %}}

Динамические формы основаны на XML спецификации, известной как XFA, "XML Forms Architecture".
Динамические формы основаны на спецификации XML, известной как XFA, "Архитектура форм XML".

В настоящее время PDF поддерживает два различных метода интеграции данных и форм PDF:

- AcroForms (также известные как формы Acrobat), введенные и включенные в спецификацию формата PDF 1.2.
- Формы Adobe XML Forms Architecture (XFA), введенные в спецификацию формата PDF 1.5 как необязательная функция (спецификация XFA не включена в спецификацию PDF, она только упоминается.)

Мы не можем извлекать или манипулировать страницами форм XFA, потому что содержимое формы генерируется во время выполнения (при просмотре формы XFA) в приложении, пытающемся отобразить или визуализировать форму XFA. Aspose.PDF имеет функцию, которая позволяет разработчикам конвертировать формы XFA в стандартные AcroForms.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Загрузка динамической XFA формы
Document document = new Document(dataDir + "DynamicXFAToAcroForm.pdf");

// Установка типа полей формы как стандартный AcroForm
document.Form.Type = FormType.Standard;

dataDir = dataDir + "Standard_AcroForm_out.pdf";
// Сохранение результирующего PDF
document.Save(dataDir);
```
## Получение свойств полей XFA

Для доступа к свойствам полей сначала используйте Document.Form.XFA.Teamplate для доступа к шаблону поля. Следующий фрагмент кода показывает шаги получения координат X и Y поля формы XFA.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Загрузить форму XFA
Document doc = new Document(dataDir + "GetXFAProperties.pdf");

string[] names = doc.Form.XFA.FieldNames;

// Установить значения полей
doc.Form.XFA[names[0]] = "Поле 0";
doc.Form.XFA[names[1]] = "Поле 1";

// Получить позицию поля
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);

// Получить позицию поля
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);

dataDir = dataDir + "Filled_XFA_out.pdf";
// Сохранить обновленный документ
doc.Save(dataDir);
```

