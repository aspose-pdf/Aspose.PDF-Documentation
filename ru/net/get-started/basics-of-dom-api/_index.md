---
title: Основы API DOM Aspose.PDF
linktitle: Основы API DOM
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /ru/net/basics-of-dom-api/
description: Aspose.PDF for .NET также использует идею DOM для представления структуры PDF-документа в терминах объектов.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Basics of Aspose.PDF DOM API",
    "alternativeHeadline": "Enhanced PDF Manipulation with Aspose.PDF DOM API in C#",
    "abstract": "Новый API DOM Aspose.PDF for .NET предоставляет надежный объектно-ориентированный подход к манипулированию PDF-документами, представляя их структуру в виде иерархического дерева. Эта функция позволяет разработчикам легко получать доступ, обновлять и экспортировать элементы PDF, одновременно повышая гибкость и контроль над манипуляцией документами через интуитивно понятный программный интерфейс.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "891",
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
    "url": "/net/basics-of-dom-api/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/basics-of-dom-api/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Введение в API DOM

Модель объектов документа (DOM) — это форма представления структурированных документов в виде объектно-ориентированной модели. DOM является официальным стандартом Всемирного консорциума веба (W3C) для представления структурированных документов в платформонезависимом и нейтральном к языку формате.

Проще говоря, DOM — это дерево объектов, представляющее структуру некоторого документа. Aspose.PDF for .NET также использует идею DOM для представления структуры PDF-документа в терминах объектов. Однако аспекты DOM (такие как его элементы) манипулируются в рамках синтаксиса используемого языка программирования. Публичный интерфейс DOM определяется в его интерфейсе программирования приложений (API).

### Введение в PDF-документ

Формат переносимого документа (PDF) является открытым стандартом для обмена документами. PDF-документ представляет собой комбинацию текстовых и бинарных данных. Если вы откроете его в текстовом редакторе, вы увидите сырые объекты, которые определяют структуру и содержимое документа.

Логическая структура PDF-файла иерархическая и определяет последовательность, по которой приложение для просмотра отображает страницы документа и их содержимое. PDF состоит из четырех компонентов: объектов, структуры файла, структуры документа и потоков содержимого.

### Структура PDF-документа

Поскольку структура PDF-файла иерархическая, Aspose.PDF for .NET также получает доступ к элементам тем же образом. Следующая иерархия показывает, как логически структурирован PDF-документ и как API DOM Aspose.PDF for .NET его строит.

![Структура PDF-документа](../images/structure.png)

### Доступ к элементам PDF-документа

Объект Document находится на корневом уровне модели объектов. API DOM Aspose.PDF for .NET позволяет вам создать объект Document и затем получить доступ ко всем другим объектам в иерархии. Вы можете получить доступ как к любым коллекциям, таким как Pages, так и к отдельным элементам, таким как Page и т.д. API DOM предоставляет единственные точки входа и выхода для манипуляции PDF-документом, как показано ниже:

- Открыть PDF-документ.
- Получить доступ к структуре PDF-документа в стиле DOM.
- Обновить данные в PDF-документе.
- Проверить PDF-документ.
- Экспортировать PDF-документ в различные форматы.
- Наконец, сохранить обновленный PDF-документ.

## Как использовать новый API Aspose.PDF for .NET

Эта тема объяснит новый API Aspose.PDF for .NET и поможет вам быстро и легко начать. Обратите внимание, что детали использования конкретных функций не являются частью этой статьи.

Aspose.PDF for .NET состоит из двух частей:

- API DOM Aspose.PDF for .NET.
- Aspose.Pdf.Facades (старый Aspose.PDF.Kit для .NET).

Вы найдете детали каждой из этих областей ниже.

### API DOM Aspose.PDF for .NET

API DOM Aspose.PDF for .NET соответствует структуре PDF-документа, что помогает вам работать с PDF-документами не только на уровне файла и документа, но и на уровне объектов. Мы предоставили разработчикам больше гибкости для доступа ко всем элементам и объектам PDF-документа. Используя классы API DOM Aspose.PDF, вы можете получить программный доступ к элементам документа и форматированию. Этот новый API DOM состоит из различных пространств имен, как указано ниже:

### Aspose.PDF

Это пространство имен предоставляет класс Document, который позволяет вам открывать и сохранять PDF-документ. Класс License также является частью этого пространства имен. Оно также предоставляет классы, связанные со страницами PDF, вложениями и закладками, такие как Page, PageCollection, FileSpecification, EmbeddedFileCollection, OutlineItemCollection и OutlineCollection и т.д.

#### Aspose.Text

Это пространство имен предоставляет классы, которые помогают вам работать с текстом и его различными аспектами, например Font, FontCollection, FontRepository, FontStyles, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment и TextSegmentCollection и т.д.

#### Aspose.Text.TextOptions

Это пространство имен предоставляет классы, которые позволяют вам устанавливать различные параметры для поиска, редактирования или замены текста, например TextEditOptions, TextReplaceOptions и TextSearchOptions.

#### Aspose.InteractiveFeatures

Это пространство имен содержит классы, которые помогают вам работать с интерактивными функциями PDF-документа, например, работая с документом и другими действиями. Это пространство имен содержит классы, такие как GoToAction, GoToRemoteAction и GoToURIAction и т.д.

#### Aspose.InteractiveFeatures.Annotations

Аннотации являются частью интерактивных функций PDF-документа. Мы выделили пространство имен для аннотаций. Это пространство имен содержит классы, которые помогают вам работать с аннотациями, например, Annotation, AnnotationCollection, CircleAnnotation и LinkAnnotation и т.д.

#### Aspose.InteractiveFeatures.Forms

Это пространство имен содержит классы, которые помогают вам работать с PDF-формами и полями форм, например, Form, Field, TextBoxField и OptionCollection и т.д.

#### Aspose.Pdf.Devices

Мы можем выполнять различные операции с PDF-документами, такие как преобразование PDF-документа в различные форматы изображений. Однако такие операции не относятся к объекту Document, и мы не можем расширить класс Document для таких операций. Вот почему мы ввели концепцию Устройства в новом API DOM.

#### Aspose.Pdf.Facades

До Aspose.PDF for .NET вам нужен был Aspose.PDF.Kit для .NET для манипуляции существующими PDF-файлами. Чтобы выполнить старый код Aspose.PDF.Kit, вы можете использовать пространство имен Aspose.PDF.Facades.