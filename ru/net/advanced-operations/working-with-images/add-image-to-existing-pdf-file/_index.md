---
title: Добавление изображения в PDF с использованием C#
linktitle: Добавить изображение
type: docs
weight: 10
url: /ru/net/add-image-to-existing-pdf-file/
description: В этом разделе описывается, как добавить изображение в существующий PDF-файл с использованием библиотеки C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление изображения в PDF с использованием C#",
    "alternativeHeadline": "Как добавить изображение в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, добавление изображения в pdf",
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
    "url": "/net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "В этом разделе описывается, как добавить изображение в существующий PDF-файл с использованием библиотеки C#."
}
</script>
## Добавление изображения в существующий PDF-файл

Каждая страница PDF содержит свойства Ресурсы и Содержимое. Ресурсы могут быть изображениями и формами, например, в то время как содержимое представлено набором операторов PDF. Каждый оператор имеет свое имя и аргумент. В этом примере используются операторы для добавления изображения в файл PDF.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Чтобы добавить изображение в существующий файл PDF:

- Создайте объект Document и откройте входной PDF-документ.
- Получите страницу, на которую вы хотите добавить изображение.
- Добавьте изображение в коллекцию Ресурсов страницы.
- Используйте операторы для размещения изображения на странице:
- Используйте оператор GSave для сохранения текущего графического состояния.
- Используйте оператор ConcatenateMatrix для указания местоположения изображения.
- Используйте оператор Do для отрисовки изображения на странице.
- Наконец, используйте оператор GRestore для сохранения обновленного графического состояния.
- Сохраните файл.
Следующий фрагмент кода показывает, как добавить изображение в документ PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Открыть документ
Document pdfDocument = new Document(dataDir+ "AddImage.pdf");

// Установить координаты
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Получить страницу, куда нужно добавить изображение
Page page = pdfDocument.Pages[1];
// Загрузить изображение в поток
FileStream imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open);
// Добавить изображение в коллекцию изображений ресурсов страницы
page.Resources.Images.Add(imageStream);
// Использование оператора GSave: этот оператор сохраняет текущее графическое состояние
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// Создать объекты Rectangle и Matrix
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// Использование оператора ConcatenateMatrix (конкатенация матрицы): определяет, как должно быть размещено изображение
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Использование оператора Do: этот оператор рисует изображение
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// Использование оператора GRestore: этот оператор восстанавливает графическое состояние
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "AddImage_out.pdf";
// Сохранить обновленный документ
pdfDocument.Save(dataDir);
```
{{% alert color="primary" %}}
По умолчанию качество JPEG установлено на 100%. Для лучшего сжатия и качества используйте следующие перегрузки:
{{% /alert %}}

- добавлена перегрузка метода Replace в класс XImageCollection: public void Replace(int index, Stream stream, int quality)
- добавлена перегрузка метода Add в класс XImageCollection: public void Add(Stream stream, int quality)

## Добавление изображения в существующий PDF файл (Facades)

Существует также альтернативный, более простой способ добавить изображение в PDF файл.
Существует также альтернативный, более простой способ добавить изображение в файл PDF.

```csharp
string imageFileName = Path.Combine(_dataDir, "Images", "Sample-01.jpg");
string outputPdfFileName = Path.Combine(_dataDir, "Example-add-image-mender.pdf");
Document document = new Document();
Page page = document.Pages.Add();
page.SetPageSize(PageSize.A3.Height, PageSize.A3.Width);
page = document.Pages.Add();
Aspose.Pdf.Facades.PdfFileMend mender = new Aspose.Pdf.Facades.PdfFileMend(document);
mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);
document.Save(outputPdfFileName);
```

## Размещение изображения на странице с сохранением (контролем) пропорций

Если мы не знаем размеры изображения, существует большая вероятность получения искаженного изображения на странице. Следующий пример показывает один из способов избежать этого.

```csharp
public static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    var bitmap = System.Drawing.Image.FromFile(_dataDir + "3410492.jpg");

    int width;
    int height;

    width = bitmap.Width;
    height = bitmap.Height;

    var document = new Aspose.Pdf.Document();

    var page = document.Pages.Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page.AddImage(_dataDir + "3410492.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));
    document.Save(_dataDir + "sample_image.pdf");
}
```
## Определите, является ли изображение в PDF цветным или черно-белым

Различные типы сжатия могут быть применены к изображениям для уменьшения их размера. Тип применяемого сжатия зависит от цветового пространства исходного изображения, то есть если изображение цветное (RGB), то следует применить сжатие JPEG2000, а если оно черно-белое, то следует использовать сжатие JBIG2/JBIG2000. Поэтому определение типа каждого изображения и использование соответствующего типа сжатия позволит создать оптимальный результат.

Файл PDF может содержать элементы Текста, Изображения, Графики, Вложения, Аннотации и т.д., и если исходный файл PDF содержит изображения, мы можем определить цветовое пространство изображения и применить соответствующее сжатие для уменьшения размера файла PDF. Следующий фрагмент кода показывает шаги для определения, является ли изображение в PDF цветным или черно-белым.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Счетчик для изображений в оттенках серого
int grayscaled = 0;
// Счетчик для RGB изображений
int rgd = 0;

using (Document document = new Document(dataDir + "ExtractImages.pdf"))
{
    foreach (Page page in document.Pages)
    {
        Console.WriteLine("--------------------------------");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
        page.Accept(abs);
        // Получаем количество изображений на конкретной странице
        Console.WriteLine("Всего изображений = {0} на странице номер {1}", abs.ImagePlacements.Count, page.Number);
        // Document.Pages[29].Accept(abs);
        int image_counter = 1;
        foreach (ImagePlacement ia in abs.ImagePlacements)
        {
            ColorType colorType = ia.Image.GetColorType();
            switch (colorType)
            {
                case ColorType.Grayscale:
                    ++grayscaled;
                    Console.WriteLine("Изображение {0} в оттенках серого...", image_counter);
                    break;
                case ColorType.Rgb:
                    ++rgd;
                    Console.WriteLine("Изображение {0} в RGB...", image_counter);
                    break;
            }
            image_counter += 1;
        }
    }
}
```
## Контроль качества изображения

Возможно контролировать качество изображения, которое добавляется в файл PDF. Используйте перегруженный метод [Replace](https://reference.aspose.com/pdf/net/aspose.pdf.ximagecollection/replace/methods/1) в классе [XImageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/ximagecollection).

Следующий фрагмент кода демонстрирует, как конвертировать все изображения документа в JPEG, используя 80% качества для сжатия.

```csharp
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document(inFile);
foreach (Aspose.PDF.Page page in pdfDocument.Pages)
{
    int idx = 1;
    foreach (Aspose.PDF.XImage image in page.Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
            page.Resources.Images.Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }
}

// pdfDocument.OptimizeResources();

pdfDocument.Save(outFile);
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
    "applicationCategory": "Библиотека для манипулирования PDF для .NET",
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

