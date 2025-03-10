---
title: Aspose.PDF for .NET через COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/use-aspose-pdf-for-net-via-com-interop/
description: Узнайте, как использовать Aspose.PDF for .NET через COM Interop для бесшовной интеграции с приложениями, не использующими .NET.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose.PDF for .NET via COM Interop",
    "alternativeHeadline": "Aspose.PDF for .NET Enables COM Interop Usage",
    "abstract": "Aspose.PDF for .NET теперь поддерживает бесшовную интеграцию с различными языками программирования через COM Interop, позволяя разработчикам использовать его мощные возможности манипуляции PDF вне фреймворка .NET. Эта функция повышает гибкость, преобразуя объекты Aspose.PDF в объекты COM, упрощая взаимодействие с неуправляемым кодом, сохраняя при этом высокую производительность благодаря техникам раннего и позднего связывания.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1338",
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
    "url": "/net/use-aspose-pdf-for-net-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/use-aspose-pdf-for-net-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

Информация в этой теме относится к сценариям, когда вы хотите использовать [Aspose.PDF for .NET](/pdf/net/) через COM Interop на любом из следующих языков программирования:

- ASP
- Delphi
- JScript
- Perl
- PHP
- PowerBuilder
- Python
- VBScript
- Visual Basic
- C++

{{% /alert %}}

## Работа с COM Interop

Aspose.PDF for .NET выполняется под управлением .NET Framework, и это называется управляемым кодом. Код, написанный на всех вышеперечисленных языках, выполняется вне .NET Framework и называется неуправляемым кодом. Взаимодействие между неуправляемым кодом и Aspose.PDF происходит через механизм .NET, называемый COM Interop.

Объекты Aspose.PDF являются объектами .NET, но при использовании через COM Interop они появляются как объекты COM в вашем языке программирования. Поэтому лучше всего убедиться, что вы знаете, как создавать и использовать объекты COM в вашем языке программирования, прежде чем начать использовать [Aspose.PDF for .NET](/pdf/net/).

{{% alert color="primary" %}}

- В мире COM мы различаем COM-сервер и COM-клиент. COM-сервер хранит классы COM, в то время как COM-клиент запрашивает у COM-сервера экземпляры классов, т.е. объекты COM.
- COM-клиент или просто клиентское приложение может знать о содержимом класса COM что-то или быть совершенно неосведомленным о его методах и свойствах. Поэтому клиентское приложение может обнаружить структуру класса COM на этапе компиляции/сборки или только во время выполнения. Процесс "обнаружения" известен как связывание, и поэтому у нас есть **раннее связывание** и **позднее связывание**.
- вкратце, класс COM похож на черный ящик, и для работы с ним необходима библиотека типов, этот бинарный файл содержит описание методов, свойств класса COM, и любой язык высокого уровня, который поддерживает работу с объектами COM, часто имеет синтаксическое выражение для добавления библиотеки типов, например, это [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) в C++.
- библиотека типов используется для раннего связывания.
- объект COM может раскрывать свои методы и свойства двумя способами: с помощью **интерфейса диспетчера** (dispinterface) и в своей **vtable** (таблице виртуальных функций).
- в **dispinterface** каждый метод и свойство идентифицируется уникальным членом; этот член является идентификатором диспетчера функции (или **DispID**).
- **vtable** - это просто набор указателей на функции, которые поддерживает интерфейс класса COM.
- объект, который раскрывает свои методы через оба интерфейса, поддерживает **двойной интерфейс**.
- есть преимущества обоих типов связывания. Раннее связывание обеспечивает вам повышенную производительность и проверку синтаксиса на этапе компиляции. Позднее связывание наиболее выгодно, когда вы пишете клиентов, которые вы намерены сделать ***совместимыми с будущими версиями*** вашего класса COM. С поздним связыванием информация из библиотеки типов не "жестко запрограммирована" в вашем клиенте, поэтому вы можете быть более уверены, что ваш клиент сможет работать с будущими версиями класса COM без изменений в коде.
- механизм позднего связывания имеет большое преимущество: если создатель COM DLL решит выпустить новую версию с другим макетом интерфейса функций, любой код, вызывающий эти методы, не упадет, если методы больше не доступны; даже если **vtable** отличается, позднее связывание управляет обнаружением новых DISPIDs и вызовом соответствующих методов.
{{% /alert %}}

Вот темы, которые вам в конечном итоге нужно будет освоить:
{{% alert color="primary" %}}

- Использование объектов COM в вашем языке программирования. См. документацию по вашему языку программирования и темы, специфичные для языка, далее в этой документации.

- Работа с объектами COM, раскрытыми через .NET COM Interop. См. [Взаимодействие с неуправляемым кодом](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) и [Раскрытие компонентов .NET Framework для COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) в MSDN.

- Модель объектов документа Aspose.PDF. См. [Руководство программиста Aspose.PDF](http://www.aspose.com/docs/display/pdfnet/Programmers+Guide) и [Справочник API](http://www.aspose.com/docs/display/pdfnet/Aspose.PDF+for+.NET+API+Reference).

{{% /alert %}}

## Регистрация Aspose.PDF for .NET с COM Interop

Вам необходимо установить Aspose.PDF for .NET и убедиться, что он зарегистрирован с COM Interop (обеспечивая возможность вызова из неуправляемого кода).

{{% alert color="primary" %}}

Чтобы вручную зарегистрировать Aspose.PDF for .NET для COM Interop:

1. В меню **Пуск** выберите **Все программы**, затем **Microsoft Visual Studio**, **Инструменты Visual Studio** и, наконец, **Командная строка Visual Studio**.
1. Введите команду для регистрации сборки:
   1. .NET Framework 4.8.1
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /codebase
   1. .NET 6.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /codebase
   1. .NET 7.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /codebase
   1. .NET 8.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /codebase
   1. .NET Standard 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

Обратите внимание, что /codebase необходим только в том случае, если Aspose.PDF.dll не находится в GAC, использование этой опции заставляет regasm поместить путь к сборке в реестр.

{{% alert color="primary" %}}

regasm.exe - это инструмент, включенный в SDK .NET Framework. Все инструменты SDK .NET Framework находятся в директории *\Microsoft .NET\Framevork\<FrameworkVersion>*, например *C:\Windows\Microsoft .NET\Framework\v4.0.30319*. Если вы используете Visual Studio .NET:
Из меню **Пуск** выберите **Программы**, затем **Visual Studio 2022**, наконец, **Командная строка разработчика для VS 2022**.
Это запускает командную строку со всеми необходимыми переменными окружения.

{{% /alert %}}

### ProgIDs

ProgID означает "программный идентификатор". Это имя класса COM, которое используется для создания объекта. ProgIDs состоят из имени библиотеки "Aspose.PDF" и имени класса.

### Библиотека типов

{{% alert color="primary" %}}

Если ваш язык программирования (например, Visual Basic или Delphi) позволяет вам ссылаться на библиотеку типов COM, то добавьте ссылку на Aspose.PDF.tlb, чтобы увидеть все классы, методы, свойства и перечисления Aspose.PDF for .NET в вашем Обозревателе объектов.

Чтобы сгенерировать файл TLB:

- .NET Framework 4.8.1
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.tlb" /codebase
- .NET 6.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.tlb" /codebase
- .NET 7.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.tlb" /codebase
- .NET 8.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.tlb" /codebase
- .NET Standard 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## Создание объектов COM

Создание объекта COM похоже на создание обычного объекта .NET:

```vb
'Instantiate Pdf instance by calling its empty constructor
Dim document
Set document = CreateObject("Aspose.Pdf.Document")

```

После создания вы сможете получить доступ к методам и свойствам объекта, как если бы это был объект COM:

```vb
'Add page to the document
document.Pages.Add()
```

Некоторые методы имеют перегрузки, и они будут раскрыты через COM Interop с добавленным числовым суффиксом, за исключением самого первого метода, который остается неизменным. Например, перегрузки метода Document.Save становятся Document.Save, Document.Save_2 и так далее.

Для получения дополнительной информации смотрите статьи, специфичные для языка, далее в этой документации.

## Создание обертки для сборки

Если вам нужно использовать много классов, методов и свойств Aspose.PDF for .NET, рассмотрите возможность создания обертки для сборки (используя C# или любой другой язык программирования .NET). Обертки для сборок помогают избежать использования Aspose.PDF for .NET напрямую из неуправляемого кода.

Хороший подход - разработать сборку .NET, которая ссылается на Aspose.PDF for .NET и выполняет всю работу с ним, и только раскрывает минимальный набор классов и методов для неуправляемого кода. Ваше приложение тогда должно работать только с вашей библиотекой-оберткой.

Сокращение количества классов и методов, которые вам нужно вызывать через COM Interop, упрощает проект. Использование классов .NET через COM Interop часто требует продвинутых навыков.