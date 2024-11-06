---
title: Получение разрешения и размеров изображений
linktitle: Получение разрешения и размеров
type: docs
weight: 40
url: ru/net/get-resolution-and-dimensions-of-embedded-images/
description: Этот раздел показывает детали получения разрешения и размеров встроенных изображений
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Получение разрешения и размеров изображений",
    "alternativeHeadline": "Как получить разрешение и размеры встроенных изображений",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "создание документов PDF",
    "keywords": "pdf, c#, получение разрешения, получение размеров",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2022-02-04",
    "description": "Этот раздел показывает детали получения разрешения и размеров встроенных изображений"
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Эта тема объясняет, как использовать классы операторов в пространстве имен Aspose.PDF, которые предоставляют возможность получать информацию о разрешении и размерах изображений, не извлекая их.

Существуют различные способы достижения этого. В этой статье объясняется, как использовать `arraylist` и [классы размещения изображений](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement).

1. Сначала загрузите исходный PDF-файл (с изображениями).
1. Затем создайте объект ArrayList для хранения имен всех изображений в документе.
1. Получите изображения, используя свойство Page.Resources.Images.
1. Создайте объект стека для хранения графического состояния изображения и используйте его для отслеживания различных состояний изображений.
1.
1. Поскольку мы можем модифицировать матрицу с помощью ConcatenateMatrix, нам также может потребоваться вернуться к исходному состоянию изображения. Используйте операторы GSave и GRestore. Эти операторы используются парами и должны вызываться вместе. Например, если вы выполняете работу с графикой с использованием сложных трансформаций и в конечном итоге возвращаете трансформации в исходное состояние, подход будет следующим:

```csharp
// Рисуем некоторый текст
GSave

ConcatenateMatrix  // поворачиваем содержимое после оператора

// Некоторая графическая работа

ConcatenateMatrix // масштабируем (с предыдущим поворотом) содержимое после оператора

// Другая графическая работа

GRestore

// Рисуем некоторый текст
```

В результате текст рисуется в обычной форме, но между операторами текста выполняются некоторые трансформации. Для отображения изображения или для рисования форм объектов и изображений нам нужно использовать оператор Do.

У нас также есть класс с именем XImage, который предоставляет два свойства, Width и Height, которые можно использовать для получения размеров изображения.

1.
1.
1. Отображение информации в командной строке вместе с именем изображения.

Следующий фрагмент кода показывает, как получить размеры и разрешение изображения, не извлекая его из документа PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Загрузка исходного PDF файла
Document doc = new Document(dataDir+ "ImageInformation.pdf");

// Определение стандартного разрешения для изображения
int defaultResolution = 72;
System.Collections.Stack graphicsState = new System.Collections.Stack();
// Определение объекта списка, который будет содержать имена изображений
System.Collections.ArrayList imageNames = new System.Collections.ArrayList(doc.Pages[1].Resources.Images.Names);
// Вставка объекта в стек
graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

// Получение всех операторов на первой странице документа
foreach (Operator op in doc.Pages[1].Contents)
{
    // Использование операторов GSave/GRestore для возврата преобразований к ранее установленным
    Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
    Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
    // Создание объекта ConcatenateMatrix, поскольку он определяет текущую матрицу преобразования.
    Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
    // Создание оператора Do, который рисует объекты из ресурсов. Он рисует объекты Form и объекты Image
    Aspose.Pdf.Operators.Do opDo = op as Aspose.Pdf.Operators.Do;

    if (opSaveState != null)
    {
        // Сохранение предыдущего состояния и помещение текущего состояния в верхнюю часть стека
        graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
    }
    else if (opRestoreState != null)
    {
        // Отбрасывание текущего состояния и восстановление предыдущего
        graphicsState.Pop();
    }
    else if (opCtm != null)
    {
        System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
           (float)opCtm.Matrix.A,
           (float)opCtm.Matrix.B,
           (float)opCtm.Matrix.C,
           (float)opCtm.Matrix.D,
           (float)opCtm.Matrix.E,
           (float)opCtm.Matrix.F);

        // Умножение текущей матрицы на матрицу состояния
        ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

        continue;
    }
    else if (opDo != null)
    {
        // В случае, если это оператор рисования изображения
        if (imageNames.Contains(opDo.Name))
        {
            System.Drawing.Drawing2D.Matrix lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
            // Создание объекта XImage для хранения изображений первой страницы PDF
            XImage image = doc.Pages[1].Resources.Images[opDo.Name];

            // Получение размеров изображения
            double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
            double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
            // Получение информации о высоте и ширине изображения
            double originalWidth = image.Width;
            double originalHeight = image.Height;

            // Расчёт разрешения на основе полученной информации
            double resHorizontal = originalWidth * defaultResolution / scaledWidth;
            double resVertical = originalHeight * defaultResolution / scaledHeight;

            // Отображение информации о размерах и разрешении каждого изображения
            Console.Out.WriteLine(
                    string.Format(dataDir + "image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                 opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                 resVertical));
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Библиотека Aspose.PDF для .NET",
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
```

