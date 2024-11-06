---
title: Преобразование страниц PDF в изображения и распознавание штрих-кодов
type: docs
weight: 10
url: ru/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---

{{% alert color="primary" %}}

Документы PDF обычно содержат текст, изображения, таблицы, вложения, графики, аннотации и другие объекты. Некоторым нашим клиентам необходимо встраивать штрих-коды в документы, а затем идентифицировать штрих-коды в файле PDF. Следующая статья объясняет, как преобразовать страницы файла PDF в изображения и идентифицировать штрих-коды на изображениях с помощью Aspose.Barcode для .NET.

{{% /alert %}}
### **Преобразование страниц в изображения и распознавание штрих-кодов**

{{% alert color="primary" %}}

Aspose.PDF для .NET — это очень мощный продукт для управления документами PDF. Он упрощает преобразование страниц документов PDF в изображения. Aspose.BarCode для .NET не менее мощный продукт для генерации и распознавания штрих-кодов.

Класс PdfConverter в пространстве имен Aspose.PDF.Facades поддерживает преобразование страниц PDF в различные форматы изображений.
#### **Использование Aspose.PDF.Facades**

{{% alert color="primary" %}}

Класс PdfConverter содержит метод с названием GetNextImage, который создает изображение текущей страницы PDF. Для указания формата выходного изображения этот метод принимает аргумент из перечисления System.Drawing.Imaging.ImageFormat.

Aspose.Barcode содержит пространство имен BarCodeRecognition, в котором находится класс BarCodeReader. Класс BarCodeReader позволяет читать, определять и идентифицировать штрих-коды из файлов изображений.

Для целей этого примера сначала конвертируйте страницу в PDF файле в изображение с помощью Aspose.PDF.Facades.PdfConverter.
{{% /alert %}}

##### **Примеры программирования**
**C#**

{{< highlight csharp >}}

 //Создаем объект PdfConverter

PdfConverter converter = new PdfConverter();

//Привязываем входной PDF файл

converter.BindPdf("Source.pdf");

// Указываем начальную страницу для обработки

converter.StartPage = 1;

// Указываем конечную страницу для обработки

converter.EndPage = 1;

// Создаем объект Resolution для указания разрешения результирующего изображения

converter.Resolution = new Aspose.PDF.Devices.Resolution(300);

//Инициализируем процесс конвертации

converter.DoConvert();

// Создаем объект MemoryStream для хранения результирующего изображения

MemoryStream imageStream = new MemoryStream();

//Проверяем наличие страниц и затем конвертируем в изображение по одной

while (converter.HasNextImage())

{

    // Сохраняем изображение в заданном формате изображения

    converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

    // Устанавливаем позицию потока в начало потока

// Установите позицию потока в начало потока
imageStream.Position = 0;

// Создайте объект BarCodeReader
Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

// String txtResult.Text = "";

while (barcodeReader.Read())
{
    // Получите текст штрих-кода из изображения штрих-кода
    string code = barcodeReader.GetCodeText();

    // Выведите текст штрих-кода на консоль
    Console.WriteLine("BARCODE : " + code);
}

// Закройте объект BarCodeReader, чтобы освободить файл изображения
barcodeReader.Close();

// Закройте экземпляр PdfConverter и освободите ресурсы
converter.Close();

// Закройте поток, содержащий объект изображения
imageStream.Close();

{{< /highlight >}}

{{% alert color="primary" %}}
В приведенных выше фрагментах кода выходное изображение сохраняется в объекте MemoryStream.
{{% /alert %}}
```
В приведенных выше фрагментах кода выходное изображение сохраняется в объект MemoryStream.

{{% /alert %}}

{anchor:devices]
#### **Использование класса PngDevice**
В Aspose.PDF.Devices находится класс PngDevice. Этот класс позволяет конвертировать страницы PDF-документов в изображения PNG.

Для данного примера загрузите исходный PDF-файл в Document, а затем конвертируйте страницы документа в изображения PNG. После создания изображений используйте класс BarCodeReader из Aspose.BarCodeRecognition для определения и считывания штрих-кодов на изображениях.

{{% alert color="primary" %}}

Примеры кода, представленные здесь, проходят через страницы PDF-документа и пытаются идентифицировать штрих-коды на каждой странице.

{{% /alert %}}
##### **Примеры программирования**
**C#**

{{< highlight csharp >}}

 //Открыть PDF-документ

Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// Перебирать отдельные страницы PDF-файла

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)

{

    using (MemoryStream imageStream = new MemoryStream())

     using (MemoryStream imageStream = new MemoryStream())
    {
        // Создать объект Resolution
        Aspose.PDF.Devices.Resolution resolution = new Aspose.PDF.Devices.Resolution(300);

        // Создать объект PngDevice, передавая объект Resolution в качестве аргумента конструктору
        Aspose.PDF.Devices.PngDevice pngDevice = new Aspose.PDF.Devices.PngDevice(resolution);

        // Конвертировать определенную страницу и сохранить изображение в поток
        pngDevice.Process(pdfDocument.Pages[pageCount], imageStream);

        // Установить позицию потока в начало
        imageStream.Position = 0;

        // Создать объект BarCodeReader
        Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

        // Читать штрих-коды, пока они не закончатся
        while (barcodeReader.Read())
        {
            // Получить текст штрих-кода из изображения штрих-кода
            string code = barcodeReader.GetCodeText();
        }
    }
```
```csharp
string code = barcodeReader.GetCodeText();

// Записать текст штрих-кода в консольный вывод

Console.WriteLine("BARCODE : " + code);

}

// Закрыть объект BarCodeReader для освобождения файла изображения

barcodeReader.Close();

}

}

{{< /highlight >}}



{{% alert color="primary" %}}

Для получения дополнительной информации по темам, рассмотренным в этой статье, пожалуйста, перейдите по ссылке:

- Преобразование страниц PDF в различные форматы изображений (Facades)
- Преобразование всех страниц PDF в изображения PNG
- [Чтение штрих-кодов](https://docs.aspose.com/barcode/net/read-barcodes/)


{{% /alert %}}
```
