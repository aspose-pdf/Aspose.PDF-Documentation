---
title: Генерация миниатюрных изображений из PDF
linktitle: Генерация миниатюрных изображений
type: docs
weight: 110
url: /net/generate-thumbnail-images-from-pdf-documents/
description: Этот раздел описывает, как создавать миниатюрные изображения из документов PDF
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Генерация миниатюрных изображений из PDF",
    "alternativeHeadline": "Как создать миниатюрные изображения из файла PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, генерация миниатюрных изображений",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "Этот раздел описывает, как создавать миниатюрные изображения из документов PDF"
}
</script>
{{% alert color="primary" %}}

Набор инструментов Adobe Acrobat SDK - это набор инструментов, который помогает вам разрабатывать программное обеспечение, взаимодействующее с технологией Acrobat. SDK содержит файлы заголовков, библиотеки типов, простые утилиты, примеры кода и документацию.

Используя Acrobat SDK, вы можете разрабатывать программное обеспечение, которое интегрируется с Acrobat и Adobe Reader несколькими способами:

- **JavaScript** — Пишите сценарии, либо в отдельном документе PDF, либо внешне, чтобы расширить функциональность Acrobat или Adobe Reader.
- **Плагины** — Создавайте плагины, которые динамично связаны и расширяют функциональность Acrobat или Adobe Reader.
- **Межприложенческая коммуникация** — Пишите отдельный процесс приложения, который использует межприложенческую коммуникацию (IAC) для управления функциональностью Acrobat. DDE и OLE поддерживаются в Microsoft® Windows®, а события Apple/AppleScript – в Mac OS®. IAC недоступна в UNIX®.

Aspose.PDF для .NET предоставляет много той же функциональности, освобождая вас от зависимости от автоматизации Adobe Acrobat.
Aspose.PDF для .NET предоставляет множество тех же функций, освобождая вас от зависимости от автоматизации Adobe Acrobat.

{{% /alert %}}

## Разработка приложений с использованием API межприложенческой коммуникации Acrobat

Считайте, что API Acrobat имеет два отдельных уровня, которые используют объекты межприложенческой коммуникации (IAC):

- Уровень приложения Acrobat (AV). Уровень AV позволяет вам контролировать, как просматривается документ. Например, вид объекта документа находится на уровне, связанном с Acrobat.
- Уровень портативного документа (PD). Уровень PD предоставляет доступ к информации внутри документа, например, к странице. С уровня PD вы можете выполнять базовые манипуляции с PDF-документами, такие как удаление, перемещение или замена страниц, а также изменение атрибутов аннотаций. Вы также можете печатать страницы PDF, выбирать текст, доступ к измененному тексту и создавать или удалять миниатюры.

Поскольку наша цель заключается в преобразовании страниц PDF в миниатюрные изображения, мы сосредотачиваемся более на IAC.
Поскольку наша цель заключается в преобразовании страниц PDF в изображения миниатюр, мы больше сосредоточены на IAC.

### Подход Acrobat

Для генерации миниатюрных изображений каждого документа мы использовали Adobe Acrobat 7.0 SDK и Microsoft .NET 2.0 Framework.

[Acrobat SDK](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/), используемый с полной версией Adobe Acrobat, предоставляет библиотеку объектов COM (к сожалению, бесплатная версия Adobe Reader не предоставляет интерфейсы COM), которые можно использовать для манипуляции и доступа к информации PDF. Используя эти объекты COM через COM Interop, загрузите документ PDF, получите первую страницу и отобразите эту страницу в буфер обмена. Затем, с помощью .NET Framework, скопируйте это в битмап, масштабируйте и объедините изображение и сохраните результат в виде файла GIF или PNG.

После установки Adobe Acrobat используйте regedit.exe и посмотрите в HKEY_CLASSES_ROOT на запись под названием AcroExch.PDDoc.

**Реестр, показывающий запись AcroExch.PDDDoc**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)
![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImagesUsingAdobe-CreateThumbnailImagesUsingAdobe.cs" >}}

## Подход Aspose.PDF для .NET

Aspose.PDF для .NET предоставляет обширную поддержку для работы с документами PDF. Также поддерживается возможность конвертации страниц документов PDF в различные форматы изображений. Описанная выше функциональность может быть легко достигнута с использованием Aspose.PDF для .NET.

Aspose.PDF имеет отличные преимущества:

- Вам не нужно устанавливать Adobe Acrobat на вашу систему для работы с файлами PDF.
- Использование Aspose.PDF для .NET простое и понятное по сравнению с автоматизацией Acrobat.

Если нам нужно конвертировать страницы PDF в JPEG, пространство имен [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) предоставляет класс под названием [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) для рендеринга страниц PDF в изображения JPEG.
Если нам нужно конвертировать страницы PDF в JPEG, пространство имён [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) предоставляет класс под названием [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) для рендеринга страниц PDF в изображения JPEG.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImages-CreateThumbnailImages.cs" >}}

{{% alert color="primary" %}}

- Спасибо CodeProject за [Генерация миниатюрных изображений из документа PDF](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- Спасибо Acrobat за [Справочник по SDK Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

{{% /alert %}}

