---
title: Объединение PDF файлов с использованием .NET 5 
linktitle: Как объединить PDF
type: docs
weight: 75
url: /net/how-to-concatenate-pdf-files-in-different-ways/
description: Эта статья объясняет возможные способы объединения любого количества существующих PDF файлов в один PDF файл.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Эта статья описывает, как вы можете [Объединить](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) несколько PDF документов в один PDF документ с помощью компонента [Aspose.PDF for .NET](/pdf/net/). [Aspose.PDF for .NET](/pdf/net/) делает эту задачу простой как пирог.

{{% /alert %}}

Вам просто нужно вызвать метод [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor), и все ваши входные PDF файлы будут объединены, и будет сгенерирован один PDF файл. Давайте создадим приложение для практики объединения PDF файлов. Мы создадим приложение, используя Visual Studio.NET 2019.

{{% alert color="primary" %}}

Aspose.PDF for .NET может использоваться в любом приложении, работающем на .NET Framework, будь то веб-приложение ASP.NET или Windows приложение.

{{% /alert %}}

## Как объединять PDF файлы разными способами

В форме расположены три текстовых поля (textBox1, textBox2, textBox3), имеющие соответствующие ссылки (linkLabel1, linkLabel2, linkLabel3) для поиска PDF файлов. При нажатии на ссылку "Обзор" появится диалоговое окно выбора файла (inputFileDialog1), которое позволит выбрать PDF файлы (для объединения).

```csharp

private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
  if(openFileDialog1.ShowDialog()==DialogResult.OK)
  {
     textBox1.Text=openFileDialog1.FileName;
  }
}
```

Показан вид приложения Windows Forms для демонстрации класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) для объединения PDF файлов.
![Concatenate PDF Files](how-to-concatenate-pdf-files-in-different-ways_1.png)

После того как мы выбираем PDF файл и нажимаем кнопку OK. Полное имя файла с путем назначается соответствующему текстовому полю.

![Choose the PDF file](how-to-concatenate-pdf-files-in-different-ways_2.png)

Аналогично, мы можем выбрать два или три входных PDF файла для конкатенации, как показано ниже:

![Choose two or three Input PDF Files](how-to-concatenate-pdf-files-in-different-ways_3.png)

Последнее текстовое поле (textBox4) примет путь назначения выходного PDF файла с его именем, где этот выходной файл будет создан.

![Destination Path of the Output PDF file](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Concatenate method](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Метод Concatenate()

Метод Concatenate() может быть использован тремя способами. давайте подробнее рассмотрим каждый из них:

### Подход 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

Этот подход хорош только если необходимо соединить только два PDF файла. Два первых аргумента (firstInputFile и secInputFile) предоставляют полные имена файлов с их путями хранения для двух входных PDF файлов, которые необходимо объединить. Третий аргумент (outputFile) предоставляет желаемое имя файла с путем для выходного PDF файла.

![Объединить два PDF с использованием имен файлов](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### Подход 2

- Concatenate(System.IO.Stream firstInputStream, System.IO.Stream secInputStream, System.IO.Stream outputStream)

Похожий на вышеописанный подход, этот метод также позволяет объединить два PDF файла. Первые два аргумента (firstInputStream и secInputStream) предоставляют два входных PDF файла в виде потоков (поток — это массив битов/байтов), которые должны быть объединены. Третий аргумент (outputStream) предоставляет потоковое представление желаемого выходного PDF файла.

![Объединение двух PDF файлов с использованием потоков файлов](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
  FileStream pdf1 = new FileStream(textBox1.Text,FileMode.Open);
  FileStream pdf2 = new FileStream(textBox2.Text,FileMode.Open);
  FileStream outputPDF = new FileStream(textBox4.Text,FileMode.Create);
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(pdf1,pdf2,outputPDF);
  outputPDF.Close();
}
```

### Подход 3

- Concatenate(System.IO.Stream inputStreams[], System.IO.Stream outputStream)

Если вы хотите объединить более двух PDF файлов, то этот подход будет вашим окончательным выбором. Аргумент первый (inputStreams[]) предоставляет входные PDF-файлы в виде массива потоков, которые следует объединить. Второй аргумент (outputStream) предоставляет потоковое представление желаемого выходного PDF-файла.

![Объединение нескольких PDF с использованием массива потоков](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
  FileStream pdf1 = new FileStream(textBox1.Text,FileMode.Open);
  FileStream pdf2 = new FileStream(textBox2.Text,FileMode.Open);
  FileStream pdf3 = new FileStream(textBox3.Text,FileMode.Open);
  Stream[] pdfStreams = new Stream[]{pdf1,pdf2,pdf3};
  FileStream outputPDF = new FileStream(textBox4.Text,FileMode.Create);
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(pdfStreams,outputPDF);
  outputPDF.Close();
}
```