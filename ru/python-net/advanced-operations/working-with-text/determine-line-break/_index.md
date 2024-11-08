---
title: Определить Перенос Строки
linktitle: Определить Перенос Строки
type: docs
weight: 70
url: /ru/python-net/determine-line-break/
description: Узнайте больше о том, как определить перенос строки в многострочном TextFragment с использованием Python
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Определить Перенос Строки",
    "alternativeHeadline": "Как определить перенос строки в TextFragment",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, определить перенос строки",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда Aspose.PDF Doc",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/determine-line-break/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/determine-line-break/"
    },
    "dateModified": "2024-02-04",
    "description": "Узнайте больше о том, как определить перенос строки в многострочном TextFragment с использованием Python"
}
</script>


## Отслеживание разрыва строк в многострочном TextFragment

Следующий фрагмент кода показывает, как отслеживать поведение разрыва строк в многострочном TextFragment в PDF-документе.

Функция track_line_breaking() определена для демонстрации этой функциональности. Она начинается с задания путей для выходных файлов как для созданного PDF-документа, так и для соответствующего текстового файла, который будет содержать информацию о разрывах строк.

Внутри функции создается новый объект PDF-документа, и к нему добавляется новая страница. Затем используется цикл для создания четырех экземпляров TextFragment, содержащих текст с разрывами строк ("\r\n"), вставленными в строку для имитации многострочного текста.

Каждый TextFragment настроен с размером шрифта в 20 пунктов перед добавлением в абзацы страницы.

После добавления всех TextFragment документ сохраняется.

Затем функция извлекает уведомления о разрывах строк со второй страницы созданного PDF-документа, используя метод get_notifications().
 Эти уведомления записываются в текстовый файл, указанный ранее.

Этот фрагмент кода иллюстрирует, как создать PDF-документ, содержащий многострочный текст, а затем извлечь информацию о поведении переноса строк, предоставляя представление о том, как текст размещен в документе.

```python

    import aspose.pdf as ap

    def track_line_breaking():
        """Отслеживание переноса строк в многострочном TextFragment"""
        output_pdf = DIR_OUTPUT_TEXTS + "track_line_breaking.pdf"
        output_txt = DIR_OUTPUT_TEXTS + "track_line_breaking.txt"

        # Создать новый объект документа
        document = ap.Document()
        page = document.pages.add()

        for i in range(4):
            text = ap.text.TextFragment(
                "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            )
            text.text_state.font_size = 20
            page.paragraphs.add(text)
        document.save(output_pdf)

        notifications = document.pages[1].get_notifications()
        with open(output_txt, "w") as f:
            f.write(notifications)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для .NET Библиотека",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека манипуляции PDF для .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>