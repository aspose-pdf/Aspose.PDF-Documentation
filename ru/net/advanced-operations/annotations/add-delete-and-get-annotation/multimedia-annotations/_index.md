---
title: Аннотация мультимедиа в PDF с использованием C#
linktitle: Аннотация мультимедиа
type: docs
weight: 40
url: /ru/net/multimedia-annotation/
description: Aspose.PDF для .NET позволяет добавлять, получать и удалять мультимедийные аннотации из вашего PDF-документа.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Аннотация мультимедиа в PDF с использованием C#",
    "alternativeHeadline": "Как добавить мультимедийную аннотацию в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, мультимедийная аннотация, аннотация экрана, звуковая аннотация, виджет-аннотация, 3D аннотация",
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
    "url": "/net/multimedia-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/multimedia-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF для .NET позволяет добавлять, получать и удалять мультимедийные аннотации из вашего PDF-документа."
}
</script>
Аннотации в документе PDF содержатся в коллекции Annotations объекта [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Эта коллекция содержит все аннотации только для этой конкретной страницы: каждая страница имеет свою собственную коллекцию Annotations. Чтобы добавить аннотацию на определенную страницу, добавьте ее в коллекцию Annotations этой страницы с помощью метода Add.

Используйте класс [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) в пространстве имен Aspose.PDF.InteractiveFeatures.Annotations для включения файлов SWF в качестве аннотаций в документ PDF. Аннотация на экране указывает область страницы, на которой могут воспроизводиться медиаклипы.

Когда вам нужно добавить внешнюю видеоссылку в документ PDF, вы можете использовать [MovieAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation).
Аннотация Movie содержит анимированную графику и звук, которые должны представляться на компьютерном экране и через динамики.

[Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) аналогична текстовой аннотации, за исключением того, что вместо текстовой заметки она содержит звук, записанный с микрофона компьютера или импортированный из файла.
Аннотация [Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) аналогична текстовой аннотации, за исключением того, что вместо текстовой заметки она содержит звук, записанный с микрофона компьютера или импортированный из файла.

Однако, когда возникает необходимость вставить медиа в документ PDF, вам нужно использовать [RichMediaAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

Можно использовать следующие методы/свойства класса RichMediaAnnotation.

- Stream CustomPlayer { set; }: Позволяет установить плеер для воспроизведения видео.
- string CustomFlashVariables { set; }: Позволяет установить переменные, которые передаются флеш-приложению. Эта строка состоит из пар "ключ=значение", которые разделены символом '&'.
- void AddCustomData(strig name, Stream data): Добавляет дополнительные данные для плеера. Например, source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: Событие, активирующее плеер; возможные значения: Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Устанавливает видео/аудио данные для воспроизведения.
- void SetContent(Stream stream, string name): Установить видео/аудио данные для воспроизведения.
- void Update(): Создать структуру данных аннотации. Этот метод должен вызываться последним.
- void SetPoster(Stream): Установить постер видео, то есть изображение, показываемое, когда плеер не активен.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Добавление аннотации на экран

Следующий фрагмент кода показывает, как добавить аннотацию на экран к файлу PDF:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.IO;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleMultimediaAnnotation
    {
        // Путь к директории с документами.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddScreenAnnotation()
        {
            // Загрузить файл PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "input.swf");
            // Создать аннотацию на экран
            var screenAnnotation = new ScreenAnnotation(
                document.Pages[1],
                new Rectangle(170, 190, 470, 380),
                mediaFile);
            document.Pages[1].Annotations.Add(screenAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_swf.pdf"));
        }
    }
}
```
## Добавление аннотации со звуком

Следующий фрагмент кода показывает, как добавить аннотацию со звуком в файл PDF:

```csharp
        public static void AddSoundAnnotation()
        {
            // Загрузить файл PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "file_example_WAV_1MG.wav");
            // Создать аннотацию со звуком
            var soundAnnotation = new SoundAnnotation(
                document.Pages[1],
                new Rectangle(20, 700, 60, 740),
                mediaFile)
            {
                Color = Color.Blue,
                Title = "Джон Смит",
                Subject = "Демонстрация аннотации со звуком",
                Popup = new PopupAnnotation(document)
            };

            document.Pages[1].Annotations.Add(soundAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_wav.pdf"));
        }
```

## Добавление RichMediaAnnotation

Следующий фрагмент кода показывает, как добавить RichMediaAnnotation в файл PDF:
Следующий фрагмент кода показывает, как добавить RichMediaAnnotation в файл PDF:

```csharp
        public static void AddRichMediaAnnotation()
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
            var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
            Page page = doc.Pages.Add();
            //даем имя видео данным. Эти данные будут встроены в документ с этим именем и на них будут ссылаться из переменных flash по этому имени.
            //videoName не должно содержать путь к файлу; это скорее "ключ" для доступа к данным внутри документа PDF
            const string videoName = "file_example_MP4_480_1_5MG.mp4";
            const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
            //также мы используем обложку для видео плеера
            string skinName = "SkinOverAllNoFullNoCaption.swf";
            RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600))
            {
                //здесь мы должны указать поток, содержащий код видеоплеера
                CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp,"Players","Videoplayer.swf"), FileMode.Open, FileAccess.Read),
                //составляем строку переменных flash для плеера. обратите внимание, что разные плееры могут иметь разные форматы строки переменных flash. Ссылайтесь на документацию для вашего плеера.
                CustomFlashVariables = $"source={videoName}&skin={skinName}"
            };
            //добавляем код обложки.
            rma.AddCustomData(skinName,
                new FileStream(Path.Combine(pathToAdobeApp,"SkinOverAllNoFullNoCaption.swf"), FileMode.Open, FileAccess.Read));
            //устанавливаем постер для видео
            rma.SetPoster(new FileStream(Path.Combine(_dataDir, posterName), FileMode.Open, FileAccess.Read));

            Stream fs = new FileStream(Path.Combine(_dataDir,videoName), FileMode.Open, FileAccess.Read);

            //устанавливаем видео контент
            rma.SetContent(videoName, fs);

            //устанавливаем тип содержимого (видео)
            rma.Type = RichMediaAnnotation.ContentType.Video;

            //активация плеера по клику
            rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

            //обновление данных аннотации. Этот метод следует вызывать после всех назначений/настроек. Этот метод инициализирует структуру данных аннотации и встраивает необходимые данные.
            rma.Update();

            //добавляем аннотацию на страницу.
            page.Annotations.Add(rma);

            doc.Save(Path.Combine(_dataDir,"RichMediaAnnotation.pdf"));
        }
```
### Получение MultimediaAnnotation

Пожалуйста, используйте следующий фрагмент кода для получения MultimediaAnnotation из PDF документа.

```csharp
        public static void GetMultimediaAnnotation()
        {
            // Загрузка PDF файла
            Document document = new Document(
                Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var mediaAnnotations = document.Pages[1].Annotations
                .Where(a => (a.AnnotationType == AnnotationType.Screen)
                || (a.AnnotationType == AnnotationType.Sound)
                || (a.AnnotationType == AnnotationType.RichMedia))
                .Cast<Annotation>();
            foreach (var ma in mediaAnnotations)
            {
                Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
            }
        }
```

### Удаление MultimediaAnnotation

Следующий фрагмент кода показывает, как удалить MultimediaAnnotation из PDF файла.

```csharp
        public static void DeletePolyAnnotation()
        {
            // Загрузка PDF файла
            Document document = new Document(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var richMediaAnnotations = document.Pages[1].Annotations
                            .Where(a => a.AnnotationType == AnnotationType.RichMedia)
                            .Cast<RichMediaAnnotation>();

            foreach (var rma in richMediaAnnotations)
            {
                document.Pages[1].Annotations.Delete(rma);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation_del.pdf"));
        }
```
## Добавление виджетов аннотаций

Интерактивные формы используют [Виджеты Аннотаций](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) для представления внешнего вида полей и управления взаимодействиями пользователя.
Мы используем эти элементы форм, которые добавляем в PDF, чтобы упростить ввод, отправку информации или выполнение других взаимодействий пользователя.

Виджеты Аннотаций являются графическим представлением поля формы на определенных страницах, поэтому мы не можем создать их напрямую как аннотацию.

Каждый Виджет Аннотации будет иметь соответствующую графику (внешний вид) в зависимости от его типа. После создания можно изменить определенные визуальные аспекты, такие как стиль границы и цвет фона.
Другие свойства, такие как цвет текста и шрифт, могут быть изменены через поле, после его прикрепления.

В некоторых случаях вы можете захотеть, чтобы поле отображалось более чем на одной странице, повторяя ту же самую значение.
В некоторых случаях вы можете захотеть, чтобы поле отображалось более чем на одной странице, повторяя то же значение.
Тот, кто заполняет форму, может использовать любой из этих виджетов для обновления значения поля, и это будет отражено во всех других виджетах.

Каждое поле формы для каждого места в документе представляет одну Виджет-Аннотацию. Данные, специфичные для местоположения Виджет-Аннотации, добавляются на конкретную страницу. Каждое поле формы имеет несколько вариантов. Кнопка может быть радио-кнопкой, флажком или кнопкой нажатия. Виджет выбора может быть списочным полем или комбинированным полем.

В этом примере мы научимся добавлять кнопки навигации в документ.

### Добавить кнопку в документ

```csharp
document = new Document();
var page = document.Pages.Add();
var rect = new Rectangle(72, 748, 164, 768);
var printButton = new ButtonField(page, rect)
{
    AlternateName = "Распечатать текущий документ",
    Color = Color.Black,
    PartialName = "printBtn1",
    NormalCaption = "Распечатать документ"
};
var border = new Border(printButton)
{
    Style = BorderStyle.Solid,
    Width = 2
};
printButton.Border = border;
printButton.Characteristics.Border =
    System.Drawing.Color.FromArgb(255, 0, 0, 255);
printButton.Characteristics.Background =
    System.Drawing.Color.FromArgb(255, 0, 191, 255);
document.Form.Add(printButton);
```
Эта кнопка имеет рамку и установлен фон. Также мы установили имя кнопки (Name), всплывающую подсказку (AlternateName), метку (NormalCaption) и цвет текста метки (Color).

### Использование действий навигации по документам

Существует более сложный пример использования Виджет-Аннотаций - навигация по документу в PDF. Это может потребоваться для подготовки презентации PDF-документа.

Этот пример показывает, как создать 4 кнопки:

```csharp
var document = new Document(@"C:\\tmp\\JSON Fundamenals.pdf");
var buttons = new ButtonField[4];
var alternateNames = new[] { "Перейти на первую страницу", "Перейти на предыдущую страницу", "Перейти на следующую страницу", "Перейти на последнюю страницу" };
var normalCaptions = new[] { "Первая", "Пред.", "След.", "Последняя" };
PredefinedAction[] actions = {
PredefinedAction.FirstPage,
PredefinedAction.PrevPage,
PredefinedAction.NextPage,
PredefinedAction.LastPage };
var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);
```

Мы должны создать кнопки, не прикрепляя их к странице.
Мы должны создать кнопки без их прикрепления к странице.

```csharp
for (var i = 0; i < 4; i++)
{
    buttons[i] = new ButtonField(document,
           new Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
    {
       AlternateName = alternateNames[i],
       Color = Color.White,
       NormalCaption = normalCaptions[i],
       OnActivated = new NamedAction(actions[i])
    };
    buttons[i].Border = new Border(buttons[i])
    {
       Style = BorderStyle.Solid,
       Width = 2
    };
    buttons[i].Characteristics.Border = clrBorder;
    buttons[i].Characteristics.Background = clrBackGround;
}
```

Мы должны продублировать этот массив кнопок на каждой странице документа. 

```csharp
for (var pageIndex = 1; pageIndex <= document.Pages.Count;
                                                        pageIndex++)
    for (var i = 0; i < 4; i++)
        document.Form.Add(buttons[i],
          $"btn{pageIndex}_{i + 1}", pageIndex);

```

Мы вызываем [метод Form.Add](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) с следующими параметрами: field, name, и индекс страниц, на которые будет добавлено это поле.
Мы вызываем [метод Form.Add](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) с такими параметрами: поле, имя и индекс страниц, на которые будет добавлено это поле.

И для получения полного результата нам нужно отключить кнопки "Первая" и "Предыдущая" на первой странице и кнопки "Следующая" и "Последняя" на последней странице.

```csharp
document.Form["btn1_1"].ReadOnly = true;
document.Form["btn1_2"].ReadOnly = true;

document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
```

Для более подробной информации и возможностей этой функции смотрите также раздел [Работа с формами](/pdf/ru/net/acroforms/).

В документах PDF можно просматривать и управлять высококачественным 3D-контентом, созданным с помощью 3D CAD или программного обеспечения для 3D-моделирования и встроенным в документ PDF. Можно вращать 3D-элементы во всех направлениях, как если бы вы держали их в руках.

Зачем вообще нужно 3D-отображение изображений?

За последние несколько лет технологии сделали огромные прорывы во всех областях благодаря 3D-печати.
За последние несколько лет технологии сделали огромные прорывы во всех областях благодаря 3D-печати.

Основная задача 3D-моделирования заключается в представлении будущего объекта или предмета, потому что для его создания необходимо понимание всех деталей его конструкции для последующего воспроизводства в промышленном дизайне или архитектуре.

## Добавление 3D аннотации

3D аннотация добавляется с использованием модели, созданной в формате U3D.

1. Создайте новый [Документ](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Загрузите данные желаемой 3D модели (в нашем случае "Ring.u3d"), чтобы создать [PDF3DContent](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent)
1. Создайте объект [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) и свяжите его с документом и 3DContent
1. Настройте объект pdf3dArtWork:

    - 3DLightingScheme - (мы установим `CAD` в примере)
    - 3DRenderMode - (мы установим `Solid` в примере)
    - Заполните `ViewArray`, создайте по крайней мере один [3D View](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) и добавьте его в массив.

- Заполните `ViewArray`, создайте хотя бы один [3D View](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) и добавьте его в массив.

1. Установите 3 основных параметра в аннотации:
    - `страницу`, на которой будет размещена аннотация,
    - `прямоугольник`, внутри которого будет аннотация,
    - и объект `3dArtWork`.
1. Для лучшей презентации 3D объекта установите рамку границы
1. Установите вид по умолчанию (например - TOP)
1. Добавьте некоторые дополнительные параметры: имя, предварительный просмотр постера и т.д.
1. Добавьте аннотацию на [страницу](https://reference.aspose.com/pdf/net/aspose.pdf/page)
1. Сохраните результат

### Пример

Пожалуйста, ознакомьтесь со следующим фрагментом кода для добавления 3D аннотации.

```csharp
    public static void Add3dAnnotation()
    {
    // Загрузите PDF файл
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(System.IO.Path.Combine(_dataDir,"Ring.u3d"));
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent)
    {
        LightingScheme = new PDF3DLightingScheme(LightingSchemeType.CAD),
        RenderMode = new PDF3DRenderMode(RenderModeType.Solid),
    };
    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.Pages.Add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.Border = new Border(pdf3dAnnotation);
    pdf3dAnnotation.SetDefaultViewIndex(1);
    pdf3dAnnotation.Flags = AnnotationFlags.NoZoom;
    pdf3dAnnotation.Name = "Ring.u3d";
    //установите предварительный просмотр изображения, если это необходимо
    //pdf3dAnnotation.SetImagePreview(System.IO.Path.Combine(_dataDir, "sample_3d.png"));
    document.Pages[1].Annotations.Add(pdf3dAnnotation);

    document.Save(System.IO.Path.Combine(_dataDir, "sample_3d.pdf"));
    }
```
Этот пример кода показал нам такую модель:

![3D Annotation demo](3d_demo.png)

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
                "areaServed": "US",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
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


