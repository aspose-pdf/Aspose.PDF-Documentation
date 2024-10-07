---
title: Merge PDF files using .NET 5 
linktitle: How to merge PDF
type: docs
weight: 75
url: /net/how-to-concatenate-pdf-files-in-different-ways/
description: Este artigo explica as possíveis maneiras de concatenar qualquer número de arquivos PDF existentes em um único arquivo PDF.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Este artigo descreve como você pode [Concatenar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) vários documentos PDF em um único documento PDF com a ajuda do componente [Aspose.PDF for .NET](/pdf/net/). [Aspose.PDF for .NET](/pdf/net/) torna este trabalho como um pedaço de bolo.

{{% /alert %}}

Tudo o que você precisa fazer é chamar o método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) e todos os seus arquivos PDF de entrada serão concatenados juntos e um único arquivo PDF será gerado. Vamos criar um aplicativo para praticar a concatenação de arquivos PDF. Vamos criar um aplicativo usando o Visual Studio.NET 2019.

{{% alert color="primary" %}}

Aspose.PDF para .NET pode ser usado em qualquer tipo de aplicação que esteja rodando no .NET Framework, seja ela uma aplicação web ASP.NET ou uma aplicação Windows.

{{% /alert %}}

## Como Concatenar Arquivos PDF de Diferentes Formas

No formulário, há três Caixas de Texto (textBox1, textBox2, textBox3) com seus respectivos Rótulos de Link (linkLabel1, linkLabel2, linkLabel3) para navegar nos arquivos PDF. Ao clicar no Rótulo de Link "Browse", um Diálogo de Arquivo de Entrada (inputFileDialog1) aparecerá, permitindo-nos escolher os arquivos PDF (a serem concatenados).

```csharp

private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
  if(openFileDialog1.ShowDialog()==DialogResult.OK)
  {
     textBox1.Text=openFileDialog1.FileName;
  }
}
```

Uma visualização da aplicação de formulário do Windows é mostrada para a demonstração da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) para a concatenação de arquivos PDF.
![Concatenate PDF Files](how-to-concatenate-pdf-files-in-different-ways_1.png)

Depois que escolhemos o arquivo PDF e clicamos no botão OK. O nome completo do arquivo com o caminho é atribuído à Caixa de Texto relacionada.

![Choose the PDF file](how-to-concatenate-pdf-files-in-different-ways_2.png)

Da mesma forma, podemos escolher dois ou três Arquivos PDF de Entrada para concatenar, como mostrado abaixo:

![Choose two or three Input PDF Files](how-to-concatenate-pdf-files-in-different-ways_3.png)

A última Caixa de Texto (textBox4) receberá o Caminho de Destino do arquivo PDF de Saída com seu nome onde este arquivo de saída será criado.

![Destination Path of the Output PDF file](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Concatenate method](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Método Concatenate()

O método Concatenate() pode ser usado de três maneiras. Vamos dar uma olhada mais de perto em cada uma delas:

### Abordagem 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

Esta abordagem é boa apenas se você precisar juntar apenas dois arquivos PDF. Primeiros dois argumentos (firstInputFile e secInputFile) fornecem os nomes completos dos arquivos com seu caminho de armazenamento dos dois arquivos PDF de entrada que devem ser concatenados. O terceiro argumento (outputFile) fornece o nome desejado do arquivo com o caminho do arquivo PDF de saída.

![Concatenar dois PDFs usando Nomes de Arquivos](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### Abordagem 2

- Concatenate(System.IO.Stream firstInputStream, System.IO.Stream secInputStream, System.IO.Stream outputStream)

Semelhante à abordagem acima, esta abordagem também permite unir dois arquivos PDF. First two arguments (firstInputStream and secInputStream) provide the two input PDF files as Streams (a stream is an array of bits/bytes) that are to be concatenated. Third argument (outputStream) provides the stream representation of desired output PDF file.

![Concatenate two PDFs using File Streams](how-to-concatenate-pdf-files-in-different-ways_7.png)

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

### Abordagem 3

- Concatenate(System.IO.Stream inputStreams[], System.IO.Stream outputStream)

Se você quiser juntar mais de dois arquivos PDF, então essa abordagem seria sua escolha definitiva. Argumento primeiro (inputStreams[]) fornece os arquivos PDF de entrada na forma de um Array de Streams que devem ser concatenados. Segundo argumento (outputStream) fornece a representação do stream do arquivo PDF de saída desejado.

![Concatenar múltiplos PDFs usando Array de Streams](how-to-concatenate-pdf-files-in-different-ways_8.png)

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