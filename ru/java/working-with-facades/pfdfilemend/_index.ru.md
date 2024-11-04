---

title: PdfFileMend Class
type: docs
weight: 20
url: /java/pdffilemend-class/
description: Этот раздел объясняет, как работать с Aspose.PDF Facades, используя класс PdfFileMend.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Задача вставки [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) в PDF документ не кажется сложной, при условии, что у вас есть оригинальная редактируемая версия этого документа. Предположим, вы создали документ, а потом вспомнили, что нужно добавить еще одну строку, или мы говорим о большом объеме документов, в обоих случаях вам поможет Aspose.PDF Facades. Рассмотрим возможность добавления текста в существующий PDF файл с помощью класса [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend).

## Добавление текста в существующий PDF файл (facades)

Мы можем добавить текст несколькими способами.
 Рассмотрим первый. Мы берем [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) и добавляем его на страницу. Затем указываем координаты нижнего левого угла, и после этого добавляем наш текст на страницу.

```java
    public static void AddText01()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("Добро пожаловать в Aspose!");

        mender.AddText(message, 1, 10, 750);

        // сохранить выходной файл
        mender.Save(_dataDir + "PdfFileMend01_output.pdf");
    }
```

Посмотрите, как это выглядит:

![Добавить текст](/pdf/net/images/add_text.png)

Второй способ добавить [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formattedtext). Дополнительно указываем прямоугольник, в который должен вписаться наш текст.

```java
public static void AddText02()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("Добро пожаловать в Aspose! Добро пожаловать в Aspose!");

        mender.AddText(message, 1, 10, 700, 55, 810);
        mender.WrapMode = WordWrapMode.ByWords;

        // сохранить выходной файл
        mender.Save(_dataDir + "PdfFileMend02_output.pdf");
    }
```

The third example provides the ability to Add Text to specified pages. In our example, let's add a caption on pages 1 and 3 of the document.

```java
public static void AddText03()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(document);
        FormattedText message = new FormattedText("Welcome to Aspose!");
        int[] pageNums = new int[] { 1, 3 };
        mender.AddText(message, pageNums, 10, 750, 310, 760);

        // save the output file
        mender.Save(_dataDir + "PdfFileMend03_output.pdf");
    }
```

## Добавление изображения в существующий PDF файл (фасады)

Вы когда-нибудь пробовали добавить изображение в существующий PDF файл?
 Мы уверены, что вы знаете, что это непростая задача. Возможно, вы заполняете форму онлайн, и вам нужно прикрепить фотографию для идентификации или прикрепить своё фото к уже существующему резюме. Ранее такая задача решалась созданием фотографии, её прикреплением к документу, дальнейшим сканированием и отправкой. Этот процесс был весьма хлопотным и отнимал много времени.

Добавление изображений и текста в существующий PDF-файл является распространённой задачей, и пространство имён com.aspose.pdf.facades отлично справляется с этой задачей. Оно предоставляет класс [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend), который позволяет добавлять изображения в PDF-файл.

Эта статья покажет вам, как вставить изображение в PDF, используя com.aspose.pdf.facades. Также существует несколько вариантов добавления изображений в PDF.

Вставьте изображение в PDF-документ, установив параметры прямоугольника.

```java
public static void AddImage01()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        PdfFileMend mender = new PdfFileMend();

        // Загрузить изображение в поток
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        mender.AddImage(imageStream, 1, 10, 650, 110, 750);

        // сохранить выходной файл
        mender.Save(_dataDir + "PdfFileMend04_output.pdf");
    }
```

![Add Image](/pdf/net/images/add_image1.png)

Рассмотрим второй фрагмент кода. Используя вариации параметров класса [CompositingParameters](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters), мы можем получить различные дизайнерские эффекты. Мы попробовали один из них.

```java
 public static void AddImage02()
    {
        Document document = new Document(_dataDir + "sample_color.pdf");
        PdfFileMend mender = new PdfFileMend();
        // Загрузить изображение в поток
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        int pageNum = 1;
        int lowerLeftX = 10;
        int lowerLeftY = 650;
        int upperRightX = 110;
        int upperRightY = 750;
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // сохранить выходной файл
        mender.Save(_dataDir + "PdfFileMend05_output.pdf");
    }
```


![Add Image](/pdf/net/images/add_image2.png)

В следующем фрагменте кода мы используем [ImageFilterType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageFilterType). ImageFilterType указывает тип кодека потока, который будет использоваться для кодирования, по умолчанию Jpeg. если вы загружаете изображение в формате PNG, то оно будет сохранено в документе как JPEG (или в другом формате, который я указал).

```java
    public static void AddImage03()
    {
        Document document = new Document(_dataDir + "sample_color.pdf");
        PdfFileMend mender = new PdfFileMend();
        // Загрузить изображение в поток
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        int pageNum = 1;
        int lowerLeftX = 10;
        int lowerLeftY = 650;
        int upperRightX = 110;
        int upperRightY = 750;
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // сохранить выходной файл
        mender.Save(_dataDir + "PdfFileMend06_output.pdf");
    }
```


В следующем фрагменте кода вы можете отметить использование метода [IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--).

[IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--) — это флаг, который указывает, следует ли применять маску к изображению, чтобы достичь прозрачности оригинального изображения.

```java
public static void AddImage04()
{
    Document document = new Document(_dataDir + "sample_color.pdf");
    PdfFileMend mender = new PdfFileMend();
    // Загрузить изображение в поток
    var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
    mender.BindPdf(document);
    int pageNum = 1;
    int lowerLeftX = 10;
    int lowerLeftY = 650;
    int upperRightX = 110;
    int upperRightY = 750;
    CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
    mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

    // сохранить выходной файл
    mender.Save(_dataDir + "PdfFileMend07_output.pdf");
}
```