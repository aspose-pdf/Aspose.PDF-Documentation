---
title: Проверка соответствия PDF-UA - Список ошибок
linktitle: Проверка соответствия PDF-UA - Список ошибок
type: docs
weight: 50
url: /ru/net/pdf-ua-compliance-test-errors-list/
description: Эта статья показывает список ошибок, которые могут возникнуть во время тестирования на соответствие PDF/UA с использованием API Aspose.PDF и C# или VB.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Проверка соответствия PDF-UA - Список ошибок",
    "alternativeHeadline": "Тестирование на соответствие PDF/UA с использованием API",
    "author": {
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF-документов",
    "keywords": "pdf, c#, генерация документов",
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
    "url": "/net/pdf-ua-compliance-test-errors-list/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-ua-compliance-test-errors-list/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья показывает список ошибок, которые могут возникнуть во время тестирования на соответствие PDF/UA с использованием API Aspose.PDF и C# или VB."
}
</script>

При проведении тестирования на соответствие PDF/UA с использованием API Aspose.PDF вас могут заинтересовать сообщения об ошибках, которые можно получить. Эти ошибки могут быть разных типов, таких как Общие, Текст, Шрифты, Заголовки и несколько других. Информация об этих ошибках может быть полезной для понимания точной причины ошибок и их обработки.

В этой статье мы перечисляем ошибки, которые могут возникнуть во время тестирования на соответствие PDF/UA с использованием API.

## **Общие**

|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|5:1|Ошибка|Отсутствует идентификатор PDF/UA|
|6.2:1.1|Ошибка|Структурное дерево родителей: обнаружена несоответствующая запись|
|7.1:1.1(14.8.1)|Ошибка|Документ не помечен как тегированный|
|7.1:1.1(14.8)|Ошибка|Объект [OBJECT_NAME] не помечен тегом|
|7.1:1.2(14.8.2.2)|Ошибка|Артефакт присутствует внутри тегированного содержимого|
|7.1:1.3(14.8.2.2)|Ошибка|Тегированное содержимое присутствует внутри артефакта|
|7.1:2.1|Предупреждение|Отсутствует структурное дерево|
|7.1:2.2|Предупреждение|Найден элемент структуры ‘Document’, который не является корневым элементом|
|7.1:2.3|Предупреждение|Элемент структуры ‘[ELEMENT_NAME]’ используется как корневой элемент|
|7.1:2.3|Предупреждение|Структурный элемент ‘[ELEMENT_NAME]’ использован в качестве корневого элемента|
|7.1:2.4.1|Предупреждение|Возможно неподходящее использование структурного элемента ‘[ELEMENT_NAME]’|
|7.1:2.4.2|Ошибка|Недопустимое использование структурного элемента ‘[ELEMENT_NAME]’|
|7.1:2.5|Предупреждение|Возможно неправильное вложение структурного элемента ‘[ELEMENT_NAME]’ в StructTreeRoot|
|7.1:3(14.8.4)|Ошибка|Нестандартный тип структуры ‘[TYPE_NAME]’ не сопоставлен со стандартным типом структуры или другим нестандартным типом структуры|
|7.1:4(14.8.4)|Предупреждение|Стандартный тип структуры ‘[TYPE_NAME]’ переназначен на ‘[TYPE_NAME]’|
|7.1:5|Требуется проверка в ручную|Контрастность цвета|
|7.1:6.1|Ошибка|Отсутствуют метаданные XMP в документе|
|7.1:6.2|Ошибка|Отсутствует заголовок в метаданных XMP документа|
|7.1:6.3|Предупреждение|Заголовок пуст в метаданных XMP документа|
|7.1:7.1(12.2)|Предупреждение|Отсутствует словарь ‘ViewerPreferences’|
|7.1:7.2(12.2)|Ошибка|Не установлена запись ‘DisplayDocTitle’|
|7.1:8(14.7.1)|Ошибка|Установлена запись ‘Suspects’|
|7.1:9.1(14.7)|Ошибка|Отсутствует ключ ‘StructParents’ на странице|
|7.1:9.2(14.7)|Ошибка|Отсутствует запись ‘StructParent’ в аннотации|
|7.1:9.2(14.7)|Ошибка|Отсутствует запись ‘StructParent’ в аннотации|
|7.1:9.3(14.7)|Ошибка|Запись для данного ‘StructParents’ не найдена|

## **Текст**

|**Код**|**Степень серьезности**|**Сообщение**|
| :- | :- | :- |
|7.2:1|Требуется ручная проверка|Логический порядок чтения|
|7.2:2(14.8.2.4.2)|Ошибка|Символы в текстовом объекте не могут быть сопоставлены с Unicode|
|7.2:3.1(14.9.2.2)|Ошибка|Невозможно определить естественный язык текстового объекта|
|7.2:3.2(14.9.2.2)|Ошибка|Невозможно определить естественный язык альтернативного текста|
|7.2:3.3(14.9.2.2)|Ошибка|Невозможно определить естественный язык фактического текста|
|7.2:3.4(14.9.2.2)|Ошибка|Невозможно определить естественный язык текста расширения|
|7.2:4(14.9.4)|Ошибка|Растягиваемый символ не помечен с использованием ActualText|

## **Шрифты**

|**Пункт**|**Степень серьезности**|**Сообщение**|
| :- | :- | :- |
|7.21.3.1|Ошибка|Коллекция символов в CIDFont несовместима с коллекцией символов внутренней CMap|
|7.21.3.2|Ошибка|CIDToGIDMap не встроен или неполный в шрифте ‘[FONT_NAME]’|
|7.21.3.2|Ошибка|CMap не встроен для шрифта ‘[FONT_NAME]’|
|7.21.3.2|Ошибка|CMap не встроен для шрифта ‘[FONT_NAME]’|
|7.21.4.2|Ошибка|CIDSet отсутствует или неполный для шрифта ‘[FONT_NAME]’|
|7.21.4.2|Ошибка|Отсутствуют глифы во встроенном шрифте ‘[FONT_NAME]’|
|7.21.6|Ошибка|Для несимвольного шрифта TrueType ‘[FONT_NAME]’ нет записей cmap|
|7.21.6|Ошибка|Запись кодировки запрещена для символьного шрифта TrueType ‘[FONT_NAME]’|
|7.21.6|Ошибка|Используется некорректная кодировка для шрифта TrueType ‘[FONT_NAME]’|
|7.21.6|Ошибка|Некорректный массив «Differences» для несимвольного шрифта TrueType ‘[FONT_NAME]’|

## **Графика**

|**Код**|**Степень серьезности**|**Сообщение**|
| :- | :- | :- |
|7.3:1(14.8.4.5)|Ошибка|Элемент ‘[ELEMENT_NAME]’ на одной странице без ограничивающего прямоугольника|
|7.3:2|Ошибка|Отсутствует альтернативный текст для структурного элемента ‘[ELEMENT_NAME]’|
|7.3:3|Ошибка|Отсутствует подпись, сопровождающая иллюстрацию|
|7.3:4(14.8.4.5)|Ошибка|Графический объект находится между операторами BT и ET|

## **Заголовки**

|**Код**|**Степень серьезности**|**Сообщение**|
| :- | :- | :- |
|7.4.2:1|Ошибка|Первый заголовок не на первом уровне|
|7.4.2:2|Ошибка|Нумерованный заголовок пропускает один или несколько уровней заголовков|
|7.4.2:2|Ошибка|Пронумерованный заголовок пропускает один или несколько уровней заголовков|
|7.4.4:1|Ошибка|Найдены структурные элементы ‘H’ и ‘Hn’|
|7.4.4:2|Ошибка|Более одного структурного элемента ‘H’ внутри родительского структурного элемента|

## **Таблицы**

|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|7.5:1|Предупреждение|Нерегулярная строка таблицы|
|7.5:2|Ошибка|У ячейки заголовка таблицы нет связанных подчиненных ячеек|
|7.5:3.1|Предупреждение|Отсутствуют заголовки таблицы|
|7.5:3.2|Предупреждение|Отсутствует сводка таблицы|

## **Списки**

|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|7.6:1|Ошибка|Структурный элемент ‘LI’ должен быть дочерним элементом ‘L’|
|7.6:2|Ошибка|Структурные элементы ‘Lbl’ и ‘LBody’ должны быть дочерними элементами ‘LI’|

## **Примечания и ссылки**

|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|7.9:2.1|Ошибка|Отсутствует ID в структурном элементе ‘Note’|
|7.9:2.2|Ошибка|Запись ID в структурном элементе ‘Note’ не уникальна|

## **Дополнительное содержимое**

|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|7.10:1|Ошибка|Отсутствует ‘Name’ в конфигурационном словаре дополнительного содержимого|
|7.10:1|Error|Отсутствует ‘Name’ в словаре конфигурации необязательного содержимого|
|7.10:2|Error|Словарь конфигурации необязательного содержимого содержит ключ ‘AS’|

## **Встроенные файлы**

|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|7.11:1|Error|Отсутствуют ключи ‘F’ или ‘UF’ в спецификации файла|
|7.11:2|Warning|Отсутствует ключ ‘Desc’ в спецификации файла|

## **Цифровые подписи**

|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|7.13:1|Error|Поле подписи формы ‘[FIELD_NAME]’ не соответствует спецификации|
|7.13:2.1|Error|Не удается определить естественный язык альтернативного названия поля формы ‘[FIELD_NAME]’|
|7.13:2.2|Error|Отсутствует запись альтернативного названия поля в поле формы ‘[FIELD_NAME]’|

## **Неинтерактивные формы**

|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|7.14:1|Error|Отсутствует атрибут ‘PrintField’ в элементе неинтерактивной формы|

## **XFA**

|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|7.15:1|Error|PDF содержит динамическую форму XFA|

## **Безопасность**

|**Код**|**Серьезность**|**Сообщение**|
|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|7.16:1(7.6.3.2)|Ошибка|Настройки безопасности блокируют доступ вспомогательных технологий к содержимому документа|
|7.16:2(7.6.3.2)|Ошибка|Преобразование не разрешено из-за ограничений прав доступа|

## **Навигация**

|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|7.17:1|Ошибка|Ошибка структуры документа|
|7.17:2|Ошибка|Невозможно определить естественный язык структуры|
|7.17:3|Требуется ручная проверка|Семантически корректные метки страниц|

## **Аннотации**

|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|7.18.1:1|Ошибка|Невозможно определить естественный язык записи содержимого|
|7.18.1:2|Ошибка|Отсутствует альтернативное описание для аннотации|
|7.18.1:3|Ошибка|Аннотация не вложена в структурный элемент ‘Annot’|
|7.18.2:1|Ошибка|Аннотация с неопределенным в ISO 32000 подтипом не соответствует 7.18.1|
|7.18.2:2|Ошибка|Существует аннотация подтипа TrapNet|
|7.18.3:1|Ошибка|Порядок вкладок на странице с аннотациями не установлен в 'S' (Структура)|
|7.18.4:1|Ошибка|Аннотация ‘Widget’ не вложена в структурный элемент ‘Form’|
|7.18.4:1|Ошибка|Аннотация 'Widget' не вложена в структурный элемент 'Form'|
|7.18.5:1|Ошибка|Аннотация 'Link' не вложена в структурный элемент 'Link'|
|7.18.6.2:1|Ошибка|Отсутствует ключ CT в словаре данных медиа-клипа|
|7.18.6.2:2|Ошибка|Отсутствует ключ Alt в словаре данных медиа-клипа|
|7.18.7:1|Ошибка|Аннотация прикрепления файла. Отсутствует ключ 'F' или 'UF' в спецификации файла|
|7.18.7:2|Предупреждение|Аннотация прикрепления файла. Отсутствует ключ 'Desc' в спецификации файла|
|7.18.8:1|Ошибка|Аннотация PrinterMark включена в логическую структуру|
|7.18.8:2|Ошибка|Поток внешнего вида аннотации PrinterMark не помечен как артефакт|

## **Действия**

|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|7.19:1|Требуется проверка вручную|Обнаружены действия. Необходимо проверить действия в соответствии с спецификацией PDF/UA вручную|

## **XObjects**

|**Код**|**Серьезность**|**Сообщение**|
| :- | :- | :- |
|7.20:1|Ошибка|Ссылочный XObject не должен использоваться в соответствующем файле PDF/UA|
|7.20:2|Ошибка|Содержимое Form XObject не включено в структурные элементы|
|7.20:2|Ошибка|Содержимое Form XObject не включено в структурные элементы|

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
