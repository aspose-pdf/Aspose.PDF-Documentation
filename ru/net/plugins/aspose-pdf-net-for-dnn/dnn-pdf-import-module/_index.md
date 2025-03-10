---
title: Модуль импорта PDF для DNN
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/dnn-pdf-import-module/
description: Узнайте, как установить и использовать модуль импорта PDF для DotNetNuke
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "DNN PDF Import Module",
    "alternativeHeadline": "Effortless PDF Content Import for DotNetNuke",
    "abstract": "Модуль импорта PDF DNN использует технологию Aspose.PDF for .NET для бесшовного извлечения и отображения содержимого из PDF-документов непосредственно в DotNetNuke, устраняя необходимость в дополнительном программном обеспечении, таком как Adobe Acrobat. Этот инновационный модуль упрощает процесс импорта документов с интуитивно понятным интерфейсом, позволяя пользователям легко просматривать файлы и импортировать содержимое PDF на свои веб-страницы.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "878",
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
    "url": "/net/dnn-pdf-import-module/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/dnn-pdf-import-module/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для опытных пользователей и разработчиков."
}
</script>

## Введение

Aspose .NET PDF Import для DNN Module позволяет разработчикам получать/читать содержимое PDF-документов без необходимости в каком-либо другом программном обеспечении, таком как Adobe Acrobat или PDF-ридер.

### Особенности модуля

Этот модуль демонстрирует мощную функцию импорта, предоставляемую [Aspose.PDF](https://products.aspose.com/pdf/net/). Он добавляет простой элемент управления для выбора файлов, выбор панели содержимого и кнопку **Импорт из PDF** на странице, где добавлен модуль. При нажатии на кнопку содержимое документа немедленно отображается на экране.

## Системные требования и поддерживаемые платформы

### Системные требования

Для настройки Aspose .NET Pdf Import для DNN Module необходимо выполнить следующие требования:

- DNN 7.0+.

Пожалуйста, не стесняйтесь обращаться к нам, если вы хотите установить этот модуль на других версиях DNN.

### Поддерживаемые платформы

Aspose .NET Pdf Import для DNN Module в настоящее время поддерживает

- DNN 7.0+.

Пожалуйста, не стесняйтесь обращаться к нам, если вы хотите установить этот модуль на других версиях DNN.

## Загрузка

Вы можете скачать Aspose .NET Pdf Import для DNN из одного из следующих мест

- [Github](https://github.com/asposemarketplace/Aspose_for_DNN/releases).
- [Sourceforge](https://sourceforge.net/projects/asposednn/files/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-dnn/downloads).

## Установка

После загрузки выполните следующие шаги для установки модуля на ваш сайт DNN:

1. Войдите на свой сайт как **Хост** или другой аккаунт уровня суперпользователя.
1. Перейдите в меню Хост и выберите **Расширения**.
1. Нажмите на **Мастер установки расширений**.
1. Как указано, перейдите к расположению загруженного zip-файла, выберите его и нажмите **Открыть**.
1. Нажмите **Далее**, примите лицензию, продолжайте установку. Когда закончите, нажмите кнопку **Вернуться**.

Пожалуйста, посмотрите [это видео по установке модуля](http://www.dnnsoftware.com/community/learn/video-library/view-video/video/542/view/details/how-to-install-a-module-in-dotnetnuke-7) от DNN для получения дополнительных деталей.

**Примечание:** Если вы получили ошибку при загрузке модуля, это связано с ограничением maxRequestLength в web.config вашей установки DNN. Откройте web.config и обновите maxRequestLength до 20MB, установив **maxRequestLength=”20480″**, и попробуйте загрузить модуль снова.

## Использование

После установки Aspose .NET PDF Import для модуля DNN действительно просто начать его использовать на вашем сайте. Пожалуйста, выполните следующие простые шаги, чтобы начать

1. Убедитесь, что вы вошли в DNN как аккаунт уровня Хост или Администратор.
1. Перейдите на страницу, где вы хотите добавить модуль импорта.
1. Выберите **Модули** -> **Добавить новый модуль** из верхней ленты.

1. Из списка выберите **Aspose .NET PDF Import для DNN** и перетащите его в место по вашему выбору на странице.

Вы успешно добавили модуль Aspose .NET PDF Import для DNN на свою страницу. Элемент выбора файла и кнопка с названием **Импорт из PDF** теперь появятся на странице вместе с выпадающим списком выбора панели содержимого. Любой может просто выбрать PDF-файл и нажать кнопку **Импорт из PDF**, чтобы отобразить содержимое выбранного документа на странице.

## Видео демонстрация

Пожалуйста, посмотрите [видео](https://www.youtube.com/watch?v=Q3z22RQgOe8) ниже, чтобы увидеть модуль в действии.

## Поддержка, расширение и вклад

### **Поддержка**

С первых дней существования Aspose мы знали, что просто предоставление нашим клиентам хороших продуктов будет недостаточно. Нам также нужно было предоставить хорошее обслуживание. Мы сами разработчики и понимаем, как это раздражает, когда техническая проблема или особенность программного обеспечения мешает вам делать то, что вам нужно. Мы здесь, чтобы решать проблемы, а не создавать их.

Вот почему мы предлагаем бесплатную поддержку. Каждый, кто использует наш продукт, независимо от того, купил он его или использует оценочную версию, заслуживает нашего полного внимания и уважения.

Вы можете сообщить о любых проблемах или предложениях, связанных с модулем Aspose .NET Pdf Import для DNN, используя любую из следующих платформ

- [Github](https://github.com/asposemarketplace/Aspose_for_DNN/issues).
- [Sourceforge](https://sourceforge.net/p/asposednn/tickets/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-dnn/issues?status=new&status=open).

### Расширение и вклад

Aspose .NET PDF Import для DNN является открытым исходным кодом, и его исходный код доступен на основных социальных сайтах кодирования, перечисленных ниже. Разработчики поощряются к загрузке исходного кода и расширению функциональности в соответствии с их собственными требованиями.

#### Исходный код

Вы можете получить последний исходный код из одного из следующих мест

- [Github](https://github.com/asposemarketplace/Aspose_for_DNN).
- [Sourceforge](https://sourceforge.net/p/asposednn/code/ci/master/tree/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-dnn/src).

#### Как настроить исходный код

Вам необходимо установить следующее, чтобы открыть и расширить исходный код

- Visual Studio 2010 или выше.
- [Шаблон разработки DNN](https://docs.aspose.com/total/net/aspose-dnn-module-development-template/#downloading).

Пожалуйста, выполните следующие простые шаги, чтобы начать

1. Загрузите/клонируйте исходный код.
1. Откройте Visual Studio 2010 и выберите **Файл** > **Открыть проект**.
1. Перейдите к последнему загруженному исходному коду и откройте **AsposeDNNPdfImport.csproj**.