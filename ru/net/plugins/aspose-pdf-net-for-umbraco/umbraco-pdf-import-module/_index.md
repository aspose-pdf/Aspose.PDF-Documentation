---
title: Модуль импорта PDF-файлов для Umbraco
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/umbraco-pdf-import-module/
description: Узнайте, как установить и использовать модуль импорта PDF-файлов для Umbraco
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Umbraco PDF Import Module",
    "alternativeHeadline": "Umbraco Module Simplifies PDF Content Import Process",
    "abstract": "Модуль импорта PDF-файлов Umbraco позволяет разработчикам легко импортировать PDF-контент на свои веб-сайты Umbraco без необходимости в дополнительном программном обеспечении. Это мощное дополнение с открытым исходным кодом упрощает работу с документами, предоставляя удобный интерфейс для мгновенного извлечения и отображения содержимого PDF-файлов, повышая эффективность управления контентом в приложениях .NET.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "950",
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
    "url": "/net/umbraco-pdf-import-module/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/umbraco-pdf-import-module/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

## Введение

**Aspose.PDF for .NET** — это компонент создания и обработки PDF-документов, который позволяет вашим приложениям .NET читать, записывать и обрабатывать существующие PDF-документы без использования Adobe Acrobat. Он также позволяет создавать формы и управлять полями форм, встроенными в PDF-документ.

**Aspose.PDF for .NET** доступен по цене и предлагает невероятное количество функций, включая параметры сжатия PDF; создание и обработку таблиц; поддержку графических объектов; расширенные возможности гиперссылок; расширенные средства контроля безопасности; работу с пользовательскими шрифтами; интеграцию с источниками данных; добавление или удаление закладок; создание оглавления; добавление, обновление, удаление вложений и аннотаций; импорт или экспорт данных форм PDF; добавление, замену или удаление текста и изображений; разделение, объединение, извлечение или вставку страниц; преобразование страниц в изображения; печать PDF-документов и многое другое.

### **Функции модуля**

Импорт PDF-файлов в Umbraco — это дополнение с открытым исходным кодом от Aspose, которое позволяет разработчикам получать содержимое любого PDF-документа без какого-либо другого программного обеспечения. Это дополнение демонстрирует мощную функцию импорта, предоставляемую Aspose.PDF. Оно добавляет простой элемент управления файловым браузером и кнопку «Импортировать из PDF» на страницу, где добавлено дополнение. При нажатии на кнопку содержимое документа извлекается из файла и немедленно отображается на экране.

## Системные требования и поддерживаемые платформы

### Системные требования

Чтобы настроить Aspose .NET Pdf Import для модуля Umbraco, необходимо выполнить следующие требования:

- Umbraco 6.0+.

Пожалуйста, свяжитесь с нами, если вы хотите установить этот модуль на другие версии Umbraco.

### Поддерживаемые платформы

Модуль поддерживается во всех версиях

- Umbraco, работающих на ASP.NET 4.0.

## Загрузка

Вы можете загрузить Aspose .NET Pdf Import для Umbraco в одном из следующих мест:

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/releases).
- [Sourceforge](https://sourceforge.net/projects/asposeumbraco/files/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/downloads).
- [Umbraco](https://our.umbraco.com/packages/developer-tools/import-from-pdf-using-asposepdf/).

## Установка

После загрузки выполните следующие действия, чтобы установить этот пакет на свой веб-сайт Umbraco:

1. Войдите в раздел Umbraco **Developer**, например, http://www.myblog.com/umbraco/.
1. В дереве разверните папку **Packages**.
   Отсюда есть два способа установить пакет: выбрать **Установить локальный пакет** или просмотреть **Репозиторий пакетов Umbraco**.
1. Если вы устанавливаете **локальный пакет**, не разархивируйте его, а загрузите zip-файл в Umbraco.
1. Следуйте инструкциям на экране.

**Примечание:** при установке вы можете получить сообщение об ошибке «Превышена максимальная длина запроса». Вы можете легко решить эту проблему, обновив значение maxRequestLength в файле web.config вашего Umbraco.

```xml
  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
```

## Использование

После установки макроса его очень просто использовать на своём веб-сайте:

1. Убедитесь, что вы вошли в раздел Umbraco **Developer**, например http://www.myblog.com/umbraco/.
1. Нажмите **Settings** в списке разделов в левом нижнем углу экрана.
1. Разверните узел **Templates** и выберите шаблон, к которому вы хотите добавить макрос, например, запись в блоге.
1. Выберите позицию в выбранном шаблоне, где вы хотите разместить кнопку.
1. Нажмите **Insert Macro** на верхней ленте.
1. В разделе **Выбрать макрос** выберите установленный макрос и нажмите **OK**.

Вы успешно добавили шаблон. Теперь на всех страницах, созданных с использованием этого шаблона, появляется кнопка с названием **Импорт из PDF**. Любой может просто нажать кнопку и импортировать содержимое PDF-документа.

## Видеодемонстрация

Посмотрите [видео](https://www.youtube.com/watch?v=zmZTJ86B25E) ниже, чтобы увидеть работу модуля в действии.

## Поддержка, расширение и участие

### Поддержка

С первых дней существования Aspose мы знали, что недостаточно просто предоставить нашим клиентам хорошие продукты. Нам также нужно было обеспечить хорошее обслуживание. Мы сами разработчики и понимаем, насколько неприятно, когда техническая проблема или ошибка в программном обеспечении мешает вам делать то, что вам нужно. Мы здесь, чтобы решать проблемы, а не создавать их.

Вот почему мы предлагаем бесплатную поддержку. Все, кто пользуется нашим продуктом, независимо от того, купили они его или используют пробную версию, заслуживают нашего полного внимания и уважения.

Вы можете сообщать о любых проблемах или предложениях, связанных с Aspose