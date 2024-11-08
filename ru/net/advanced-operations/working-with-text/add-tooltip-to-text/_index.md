---
title: PDF Tooltip с использованием C#
linktitle: PDF Tooltip
type: docs
weight: 20
url: /ru/net/pdf-tooltip/
description: Узнайте, как добавить всплывающую подсказку к фрагменту текста в PDF с использованием C# и Aspose.PDF
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip с использованием C#",
    "alternativeHeadline": "Добавление всплывающей подсказки в PDF к тексту",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, c#, добавление всплывающей подсказки в pdf",
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
    "url": "/net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-tooltip/"
    },
    "dateModified": "2022-02-04",
    "description": "Узнайте, как добавить всплывающую подсказку к фрагменту текста в PDF с использованием C# и Aspose.PDF"
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Добавление всплывающей подсказки к искомому тексту путем добавления невидимой кнопки

Часто требуется добавить некоторые детали для фразы или конкретного слова в виде всплывающей подсказки в документ PDF, чтобы она появлялась, когда пользователь наводит курсор мыши на текст. Aspose.PDF для .NET предоставляет эту функцию для создания всплывающих подсказок, добавляя невидимую кнопку над искомым текстом. Следующий фрагмент кода покажет вам способ достижения этой функциональности:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string outputFile = dataDir + "Tooltip_out.pdf";

// Создание образца документа с текстом
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("Наведите курсор мыши сюда, чтобы отобразить всплывающую подсказку"));
doc.Pages[1].Paragraphs.Add(new TextFragment("Наведите курсор мыши сюда, чтобы отобразить очень длинную всплывающую подсказку"));
doc.Save(outputFile);

// Открытие документа с текстом
Document document = new Document(outputFile);
// Создание объекта TextAbsorber для поиска всех фраз, соответствующих регулярному выражению
TextFragmentAbsorber absorber = new TextFragmentAbsorber("Наведите курсор мыши сюда, чтобы отобразить всплывающую подсказку");
// Применение absorber к страницам документа
document.Pages.Accept(absorber);
// Получение извлеченных текстовых фрагментов
TextFragmentCollection textFragments = absorber.TextFragments;

// Перебор фрагментов
foreach (TextFragment fragment in textFragments)
{
    // Создание невидимой кнопки на позиции текстового фрагмента
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // Значение AlternateName будет отображаться как всплывающая подсказка в приложении просмотра
    field.AlternateName = "Всплывающая подсказка для текста.";
    // Добавление поля кнопки в документ
    document.Form.Add(field);
}

// Далее будет пример очень длинной всплывающей подсказки
absorber = new TextFragmentAbsorber("Наведите курсор мыши сюда, чтобы отобразить очень длинную всплывающую подсказку");
document.Pages.Accept(absorber);
textFragments = absorber.TextFragments;

foreach (TextFragment fragment in textFragments)
{
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // Установка очень длинного текста
    field.AlternateName = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                            " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                            " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                            " Duis aute irure dolor in reprehenderit in voluptate velit" +
                            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                            " occaecat cupidatat non proident, sunt in culpa qui officia" +
                            " deserunt mollit anim id est laborum.";
    document.Form.Add(field);
}

// Сохранение документа
document.Save(outputFile);
```
{{% alert color="primary" %}}

Что касается длины всплывающей подсказки, текст всплывающей подсказки содержится в документе PDF как строка типа PDF, вне потока содержимого. В файлах PDF нет эффективных ограничений на такие строки (см. Приложение C к справочнику по PDF). Однако соответствующее устройство чтения (например, Adobe Acrobat), работающее на конкретном процессоре и в конкретной операционной среде, имеет такое ограничение. Пожалуйста, обратитесь к документации вашего приложения для чтения PDF.

{{% /alert %}}

## Создание скрытого текстового блока и его отображение при наведении мыши

В Aspose.PDF реализована функция скрытия действий, с помощью которой можно показывать/скрывать текстовое поле (или любой другой тип аннотации) при наведении/выходе мыши на невидимую кнопку. Для этой цели используется класс Aspose.Pdf.Annotations.HideAction для назначения действия скрытия/показа текстового блока. Пожалуйста, используйте следующий фрагмент кода для показа/скрытия текстового блока при наведении/выходе мыши.

Также учтите, что действия PDF в документах работают нормально в соответствующих устройствах чтения (например,
Пожалуйста, учитывайте, что действия с PDF в документах работают корректно в соответствующих ридерах (например,

- Все реализации действия скрытия в документах PDF работают корректно в Internet Explorer версии 11.0.
- Все реализации действия скрытия также работают в Opera версии 12.14, но мы заметили некоторую задержку ответа при первом открытии документа.
- Только реализация, использующая конструктор HideAction, принимающий имя поля, работает, если документ просматривается в Google Chrome версии 61.0. Пожалуйста, используйте соответствующие конструкторы, если просмотр в Google Chrome имеет значение:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string outputFile = dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

// Создание образца документа с текстом
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("Наведите курсор мыши сюда, чтобы отобразить всплывающий текст"));
doc.Save(outputFile);

// Открытие документа с текстом
Document document = new Document(outputFile);
// Создание объекта TextAbsorber для поиска всех фраз, соответствующих регулярному выражению
TextFragmentAbsorber absorber = new TextFragmentAbsorber("Наведите курсор мыши сюда, чтобы отобразить всплывающий текст");
// Принять поглотитель для страниц документа
document.Pages.Accept(absorber);
// Получить первый извлеченный текстовый фрагмент
TextFragmentCollection textFragments = absorber.TextFragments;
TextFragment fragment = textFragments[1];

// Создание скрытого текстового поля для всплывающего текста в указанном прямоугольнике страницы
TextBoxField floatingField = new TextBoxField(fragment.Page, new Rectangle(100, 700, 220, 740));
// Установка текста для отображения в качестве значения поля
floatingField.Value = "Это \"всплывающее текстовое поле\".";
// Рекомендуется сделать поле 'только для чтения' для данного сценария
floatingField.ReadOnly = true;
// Установка флага 'hidden' для скрытия поля при открытии документа
floatingField.Flags |= AnnotationFlags.Hidden;

// Установка уникального имени поля не обязательна, но разрешена
floatingField.PartialName = "FloatingField_1";

// Установка характеристик внешнего вида поля не обязательна, но делает его лучше
floatingField.DefaultAppearance = new DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
floatingField.Border = new Border(floatingField);
floatingField.Border.Width = 1;
floatingField.Multiline = true;

// Добавление текстового поля в документ
document.Form.Add(floatingField);

// Создание невидимой кнопки на позиции текстового фрагмента
ButtonField buttonField = new ButtonField(fragment.Page, fragment.Rectangle);
// Создание нового действия скрытия для указанного поля (аннотации) и флага невидимости.
// (Вы также можете ссылаться на всплывающее поле по имени, если вы указали его выше.)
// Добавление действий при входе/выходе мыши на невидимое кнопочное поле
buttonField.Actions.OnEnter = new HideAction(floatingField, false);
buttonField.Actions.OnExit = new HideAction(floatingField);

// Добавление кнопочного поля в документ
document.Form.Add(buttonField);

// Сохранение документа
document.Save(outputFile);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для библиотеки .NET",
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
    "applicationCategory": "Библиотека для манипуляций с PDF для .NET",
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
```

