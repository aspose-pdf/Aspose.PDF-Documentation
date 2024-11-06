---
title: 使用 .NET 5 合并 PDF 文件
linktitle: 如何合并 PDF
type: docs
weight: 75
url: zh/net/how-to-concatenate-pdf-files-in-different-ways/
description: 本文解释了将任意数量的现有 PDF 文件合并为单个 PDF 文件的可能方法。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

本文描述了如何使用 [Aspose.PDF for .NET](/pdf/net/) 组件将多个 PDF 文档[合并](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)为单个 PDF 文档。[Aspose.PDF for .NET](/pdf/net/) 使这个工作变得非常简单。

{{% /alert %}}

您所需要做的就是调用 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类的 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 方法，所有的输入 PDF 文件将被合并在一起，并生成一个单一的 PDF 文件。 让我们创建一个应用程序来练习 PDF 文件的连接。我们将使用 Visual Studio.NET 2019 创建一个应用程序。

{{% alert color="primary" %}}

Aspose.PDF for .NET 可以用于运行在 .NET Framework 上的任何类型的应用程序，无论是 ASP.NET Web 应用程序还是 Windows 应用程序

{{% /alert %}}

## 如何以不同方式连接 PDF 文件

在窗体中，有三个文本框 (textBox1, textBox2, textBox3)，各自具有用于浏览 PDF 文件的链接标签 (linkLabel1, linkLabel2, linkLabel3)。通过点击“浏览”链接标签，将会出现一个输入文件对话框 (inputFileDialog1)，它将使我们能够选择要连接的 PDF 文件。

```csharp

private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
  if(openFileDialog1.ShowDialog()==DialogResult.OK)
  {
     textBox1.Text=openFileDialog1.FileName;
  }
}
```

显示了一个 Windows 窗体应用程序的视图，用于演示用于 PDF 文件连接的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类。
![Concatenate PDF Files](how-to-concatenate-pdf-files-in-different-ways_1.png)

选择PDF文件并点击OK按钮后，完整的文件名和路径将分配给相关的文本框。

![Choose the PDF file](how-to-concatenate-pdf-files-in-different-ways_2.png)

同样，我们可以选择两个或三个输入PDF文件进行合并，如下所示：

![Choose two or three Input PDF Files](how-to-concatenate-pdf-files-in-different-ways_3.png)

最后一个文本框（textBox4）将获取输出PDF文件的目标路径及其名称，该输出文件将在此处创建。

![Destination Path of the Output PDF file](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Concatenate method](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Concatenate() 方法

Concatenate() 方法可以通过三种方式使用。让我们仔细看看每一种：

### 方法 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

这种方法仅适用于当您只需要合并两个PDF文件时。 第一和第二个参数（firstInputFile 和 secInputFile）提供了要合并的两个输入 PDF 文件的完整文件名及其存储路径。第三个参数（outputFile）提供了输出 PDF 文件的所需文件名及路径。

![使用文件名连接两个 PDF](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### 方法 2

- Concatenate(System.IO.Stream firstInputStream, System.IO.Stream secInputStream, System.IO.Stream outputStream)

类似于上述方法，这种方法也允许连接两个 PDF 文件。 前两个参数（firstInputStream 和 secInputStream）提供要连接的两个输入 PDF 文件作为流（流是位/字节的数组）。第三个参数（outputStream）提供所需输出 PDF 文件的流表示。

![使用文件流连接两个 PDF](how-to-concatenate-pdf-files-in-different-ways_7.png)

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

### 方法 3

- Concatenate(System.IO.Stream inputStreams[], System.IO.Stream outputStream)

如果你想连接两个以上的 PDF 文件，那么这种方法将是你的最终选择。 First argument (inputStreams[]) 提供要连接的输入 PDF 文件，这些文件以流数组的形式提供。第二个参数 (outputStream) 提供所需输出 PDF 文件的流表示。

![使用流数组连接多个 PDF](how-to-concatenate-pdf-files-in-different-ways_8.png)

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