---
title: Объединение PDF файлов с использованием .NET 5
linktitle: Как объединить PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 75
url: /ru/net/how-to-concatenate-pdf-files-in-different-ways/
description: Эта статья объясняет возможные способы объединения любого количества существующих PDF файлов в один PDF файл.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge PDF files",
    "alternativeHeadline": "Effortlessly Combine Multiple PDFs",
    "abstract": "Объедините несколько PDF файлов в один документ без усилий с новой функциональностью в Aspose.PDF for .NET. Эта функция позволяет разработчикам объединять любое количество PDF через простые вызовы методов, повышая производительность в управлении и манипуляции PDF. Легко интегрируйте эту возможность в различные приложения .NET, включая ASP.NET и Windows приложения, с универсальными подходами, которые соответствуют различным потребностям.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "840",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/how-to-concatenate-pdf-files-in-different-ways/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/how-to-concatenate-pdf-files-in-different-ways/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

Эта статья описывает, как вы можете [Объединить](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) несколько PDF документов в один PDF документ с помощью компонента [Aspose.PDF for .NET](/pdf/ru/net/). [Aspose.PDF for .NET](/pdf/ru/net/) делает эту работу легкой.

{{% /alert %}}

Все, что вам нужно сделать, это вызвать метод [Concatenate](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor), и все ваши входные PDF файлы будут объединены, и будет сгенерирован один PDF файл. Давайте создадим приложение, чтобы попрактиковаться в объединении PDF файлов. Мы создадим приложение с использованием Visual Studio.NET 2019.

{{% alert color="primary" %}}

Aspose.PDF for .NET может использоваться в любом приложении, работающем на .NET Framework, будь то веб-приложение ASP.NET или Windows приложение.

{{% /alert %}}

## Как объединить PDF файлы различными способами

В форме есть три текстовых поля (textBox1, textBox2, textBox3) с соответствующими метками ссылок (linkLabel1, linkLabel2, linkLabel3) для выбора PDF файлов. Нажав на метку "Обзор", появится диалоговое окно выбора файла (inputFileDialog1), которое позволит нам выбрать PDF файлы (для объединения).

```csharp
private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
    if (openFileDialog1.ShowDialog()==DialogResult.OK)
    {
        textBox1.Text=openFileDialog1.FileName;
    }
}
```

Представлен вид приложения Windows Forms для демонстрации класса [PdfFileEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor) для объединения PDF файлов.

![Объединить PDF файлы](how-to-concatenate-pdf-files-in-different-ways_1.png)

После того как мы выберем PDF файл и нажмем кнопку OK, полное имя файла с путем будет присвоено соответствующему текстовому полю.

![Выбор PDF файла](how-to-concatenate-pdf-files-in-different-ways_2.png)

Аналогично, мы можем выбрать два или три входных PDF файла для объединения, как показано ниже:

![Выбор двух или трех входных PDF файлов](how-to-concatenate-pdf-files-in-different-ways_3.png)

Последнее текстовое поле (textBox4) будет принимать путь назначения выходного PDF файла с его именем, где будет создан этот выходной файл.

![Путь назначения выходного PDF файла](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Метод Concatenate](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Метод Concatenate()

Метод Concatenate() может использоваться тремя способами. Давайте подробнее рассмотрим каждый из них:

### Подход 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

Этот подход хорош только в том случае, если вам нужно объединить только два PDF файла. Первые два аргумента (firstInputFile и secInputFile) предоставляют полные имена файлов с их путями хранения для двух входных PDF файлов, которые нужно объединить. Третий аргумент (outputFile) предоставляет желаемое имя файла с путем для выходного PDF файла.

![Объединить два PDF файла по именам файлов](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### Подход 2

- Concatenate(Stream firstInputStream, Stream secInputStream, Stream outputStream)

Аналогично предыдущему подходу, этот подход также позволяет объединять два PDF файла. Первые два аргумента (firstInputStream и secInputStream) предоставляют два входных PDF файла в виде потоков (поток - это массив битов/байтов), которые нужно объединить. Третий аргумент (outputStream) предоставляет потоковое представление желаемого выходного PDF файла.

![Объединить два PDF файла по потокам файлов](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
            {
                var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                pdfEditor.Concatenate(pdf1, pdf2, outputStream);
            }
        }
    }
}
```

### Подход 3

- Concatenate(Stream inputStreams[], Stream outputStream)

Если вы хотите объединить более двух PDF файлов, то этот подход будет вашим окончательным выбором. Первый аргумент (inputStreams[]) предоставляет входные PDF файлы в виде массива потоков, которые нужно объединить. Второй аргумент (outputStream) предоставляет потоковое представление желаемого выходного PDF файла.

![Объединить несколько PDF файлов с использованием массива потоков](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var pdf3 = new FileStream(textBox3.Text, FileMode.Open))
            {
                var pdfStreams = new Stream[] { pdf1, pdf2, pdf3 };
                using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
                {
                    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                    pdfEditor.Concatenate(pdfStreams, outputStream);
                }
            }
        }
    }
}
```