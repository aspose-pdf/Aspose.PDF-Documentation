---
title: Работа с операторами
linktitle: Работа с операторами
type: docs
weight: 170
url: /ru/net/operators/
description: Эта тема объясняет, как использовать операторы с Aspose.PDF. Классы операторов предоставляют отличные возможности для манипуляций с PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-operators/
    - /net/operator/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с операторами",
    "alternativeHeadline": "Как использовать операторы PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, операторы в pdf, использование операторов pdf",
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
    "url": "/net/operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/operators/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта тема объясняет, как использовать операторы с Aspose.PDF. Классы операторов предоставляют отличные возможности для манипуляций с PDF."
}
</script>

## Введение в операторы PDF и их использование

Оператор — это ключевое слово PDF, указывающее на выполнение определённого действия, такого как рисование графической формы на странице. Ключевое слово оператора отличается от именованного объекта отсутствием начального символа косой черты (2Fh). Операторы имеют значение только внутри потока содержимого.

Поток содержимого — это объект потока PDF, данные которого состоят из инструкций, описывающих графические элементы, которые должны быть нарисованы на странице. Более подробную информацию об операторах PDF можно найти в [спецификации PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Детали реализации

В этой теме объясняется, как использовать операторы с Aspose.PDF.
Эта тема объясняет, как использовать операторы с Aspose.PDF.

- Оператор **GSave** сохраняет текущее графическое состояние PDF.
- Оператор **ConcatenateMatrix** (конкатенация матрицы) используется для определения размещения изображения на странице PDF.
- Оператор **Do** отображает изображение на странице.
- Оператор **GRestore** восстанавливает графическое состояние.

Для добавления изображения в файл PDF:

1. Создайте объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) и откройте входной документ PDF.
1. Получите конкретную страницу, на которую будет добавлено изображение.
1. Добавьте изображение в коллекцию Resources страницы.
1. Используйте операторы для размещения изображения на странице:
   - Сначала используйте оператор GSave для сохранения текущего графического состояния.
   - Затем используйте оператор ConcatenateMatrix для указания места размещения изображения.
   - Используйте оператор Do для отображения изображения на странице.
1. Наконец, используйте оператор GRestore для сохранения обновленного графического состояния.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Следующий фрагмент кода показывает, как использовать операторы PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

// Открыть документ
Document pdfDocument = new Document(dataDir+ "PDFOperators.pdf");

// Задать координаты
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Получить страницу, где нужно добавить изображение
Page page = pdfDocument.Pages[1];
// Загрузить изображение в поток
FileStream imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open);
// Добавить изображение в коллекцию изображений ресурсов страницы
page.Resources.Images.Add(imageStream);
// Использование оператора GSave: этот оператор сохраняет текущее состояние графики
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// Создать объекты Rectangle и Matrix
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// Использование оператора ConcatenateMatrix (конкатенация матрицы): определяет, как должно быть размещено изображение
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Использование оператора Do: этот оператор рисует изображение
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// Использование оператора GRestore: этот оператор восстанавливает состояние графики
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "PDFOperators_out.pdf";
// Сохранить обновленный документ
pdfDocument.Save(dataDir);
```
## Отрисовка XForm на странице с помощью операторов

Эта тема демонстрирует, как использовать операторы GSave/GRestore, оператор ContatenateMatrix для позиционирования xForm и оператор Do для отрисовки xForm на странице.

Приведенный ниже код оборачивает существующее содержимое файла PDF с помощью пары операторов GSave/GRestore. Этот подход помогает получить начальное графическое состояние в конце существующего содержимого. Без этого подхода в конце существующей цепочки операторов могут остаться нежелательные преобразования.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();


string imageFile = dataDir+ "aspose-logo.jpg";
string inFile = dataDir + "DrawXFormOnPage.pdf";
string outFile = dataDir + "blank-sample2_out.pdf";

using (Document doc = new Document(inFile))
{
    OperatorCollection pageContents = doc.Pages[1].Contents;

    // Пример демонстрирует
    // использование операторов GSave/GRestore
    // использование оператора ContatenateMatrix для позиционирования xForm
    // использование оператора Do для отрисовки xForm на странице

    // Оборачиваем существующее содержимое парой операторов GSave/GRestore
    //        это делается для получения начального графического состояния в конце существующего содержимого
    //        в противном случае могут остаться некоторые нежелательные преобразования в конце цепочки существующих операторов
    pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // Добавляем оператор сохранения графического состояния для правильной очистки графического состояния после новых команд
    pageContents.Add(new Aspose.Pdf.Operators.GSave());

    #region создание xForm

    // Создаем xForm
    XForm form = XForm.CreateNewForm(doc.Pages[1], doc);
    doc.Pages[1].Resources.Forms.Add(form);
    form.Contents.Add(new Aspose.Pdf.Operators.GSave());
    // Определяем ширину и высоту изображения
    form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));
    // Загружаем изображение в поток
    Stream imageStream = new FileStream(imageFile, FileMode.Open);
    // Добавляем изображение в коллекцию изображений ресурсов XForm
    form.Resources.Images.Add(imageStream);
    XImage ximage = form.Resources.Images[form.Resources.Images.Count];
    // Используем оператор Do: этот оператор рисует изображение
    form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
    form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

    #endregion

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // Размещаем форму в координатах x=100 y=500
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
    // Рисуем форму с помощью оператора Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // Размещаем форму в координатах x=100 y=300
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
    // Рисуем форму с помощью оператора Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore();

    // Восстанавливаем графическое состояние с помощью GRestore после GSave
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());
    doc.Save(outFile);
}
```
## Удаление графических объектов с использованием классов операторов

Классы операторов предоставляют отличные возможности для манипуляций с PDF. Когда файл PDF содержит графику, которую нельзя удалить с использованием метода [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), вместо этого можно использовать классы операторов.

Следующий фрагмент кода показывает, как удалить графику. Обратите внимание, что если файл PDF содержит текстовые метки для графики, они могут остаться в файле PDF при использовании этого подхода. Поэтому ищите графические операторы альтернативным методом для удаления таких изображений.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

Document doc = new Document(dataDir+ "RemoveGraphicsObjects.pdf");
Page page = doc.Pages[2];
OperatorCollection oc = page.Contents;

// Используемые операторы рисования путей
Operator[] operators = new Operator[] {
        new Aspose.Pdf.Operators.Stroke(),
        new Aspose.Pdf.Operators.ClosePathStroke(),
        new Aspose.Pdf.Operators.Fill()
};

oc.Delete(operators);
doc.Save(dataDir+ "No_Graphics_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Библиотека Aspose.PDF для .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Организация",
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
                "@type": "Контактное лицо",
                "telephone": "+1 903 306 1676",
                "contactType": "продажи",
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "Контактное лицо",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "Контактное лицо",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Предложение",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF в .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "Совокупный рейтинг",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

