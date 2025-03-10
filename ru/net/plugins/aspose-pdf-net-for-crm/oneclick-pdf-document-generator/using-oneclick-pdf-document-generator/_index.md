---
title: Использование генератора PDF-документов OneClick
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/using-oneclick-pdf-document-generator/
description: Узнайте, как использовать Aspose.PDF OneClick PDF Document Generator в Microsoft Dynamics
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using OneClick PDF Document Generator",
    "alternativeHeadline": "Streamlined PDF Generation in Microsoft Dynamics",
    "abstract": "Откройте для себя бесшовную генерацию документов в Microsoft Dynamics с помощью Aspose.PDF OneClick PDF Document Generator. Эта инновационная функция позволяет пользователям создавать настраиваемые PDF-шаблоны непосредственно в CRM, эффективно генерировать документы одним щелчком мыши и легко интегрировать кнопки OneClick в формы для упрощенного доступа. Улучшите свои возможности управления данными и повысите производительность с помощью этого мощного инструмента",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
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
    "url": "/net/using-oneclick-pdf-document-generator/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-oneclick-pdf-document-generator/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Создание шаблона и добавление в CRM

- Откройте Word и создайте шаблон.
- Вставьте поля MailMerge для данных, поступающих из CRM.

![Insert MailMerg fields](using-oneclick-pdf-document-generator_1.png)

- Убедитесь, что имя поля точно совпадает с полем CRM.
- Шаблоны специфичны для использования с отдельной сущностью.

![Demo Template](using-oneclick-pdf-document-generator_2.png)

- После создания шаблона откройте сущность конфигурации OneClick PDF в CRM и создайте новую запись.
- Укажите имя шаблона, выберите сущность, для которой определен шаблон, и прикрепите созданный документ в приложении.

![Select Template](using-oneclick-pdf-document-generator_3.png)

## Генерация документа с помощью кнопки на ленте

- Откройте запись, в которой хотите сгенерировать документ. (Убедитесь, что шаблон уже прикреплен в конфигурации для этой сущности)
- Нажмите кнопку OneClick PDF на ленте.

![Click OneClick PDF](using-oneclick-pdf-document-generator_4.png)

- В всплывающем окне: выберите шаблон, имя файла и действие, затем нажмите "Генерировать".
- Проверьте загруженный файл или заметки на основе выбора.

## Настройка кнопок OneClick и их использование

- Чтобы использовать кнопку OneClick непосредственно из формы, откройте настройку формы.
- Вставьте WebResource, где хотите добавить кнопки OneClick.
- Выберите OpenButtonPage в WebResource и дайте ему имя.
- Настройте кнопки в поле данных в следующем примере.

![WebResource Properties](using-oneclick-pdf-document-generator_5.png)

- Используйте отдельную строку для каждой кнопки и используйте следующий синтаксис:
  - Синтаксис: Имя шаблона |<Действие: Загрузка/Заметка>|Имя выходного файла
  - Пример:Demo|Download|My Downloaded File
- Сохраните и опубликуйте настройку.
- Кнопка доступна на форме.

![The button is available on the form](using-oneclick-pdf-document-generator_6.png)