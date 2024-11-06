---
title: Converter Páginas de PDF em Imagens e Reconhecer Códigos de Barras
type: docs
weight: 10
url: pt/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---

{{% alert color="primary" %}}

Documentos PDF geralmente contêm texto, imagens, tabelas, anexos, gráficos, anotações e outros objetos. Alguns de nossos clientes precisam incorporar códigos de barras nos documentos e, em seguida, identificar códigos de barras no arquivo PDF. O artigo a seguir explica como transformar as páginas de um arquivo PDF em imagens e identificar códigos de barras nas imagens com Aspose.Barcode para .NET.

{{% /alert %}}
### **Convertendo Páginas em Imagens e Reconhecendo Códigos de Barras**

{{% alert color="primary" %}}


Aspose.PDF para .NET é um produto muito poderoso para gerenciar documentos PDF. Ele facilita a conversão de páginas de documentos PDF em imagens. Aspose.BarCode para .NET é um produto igualmente poderoso para gerar e reconhecer códigos de barras.

A classe PdfConverter sob o namespace Aspose.PDF.Facades suporta a conversão de páginas PDF para vários formatos de imagem.
A classe PdfConverter sob o namespace Aspose.PDF.Facades suporta a conversão de páginas PDF para vários formatos de imagem.

Quando as páginas são convertidas para um formato de imagem, podemos usar o Aspose.BarCode para .NET para identificar códigos de barras dentro delas. Os exemplos de código abaixo mostram como converter páginas usando PdfConverter ou PngDevice.

{{% /alert %}}

#### **Usando Aspose.PDF.Facades**

{{% alert color="primary" %}}

A classe PdfConverter contém um método chamado GetNextImage que gera uma imagem da página PDF atual. Para especificar o formato da imagem de saída, este método aceita um argumento da enumeração System.Drawing.Imaging.ImageFormat.

Aspose.Barcode contém um namespace, BarCodeRecognition, que contém a classe BarCodeReader. A classe BarCodeReader permite ler, determinar e identificar códigos de barras de arquivos de imagem.

Para os propósitos deste exemplo, primeiro converta uma página de um arquivo PDF em uma imagem com Aspose.PDF.Facades.PdfConverter.
##### **Exemplos de Programação**
**C#**

{{< highlight csharp >}}

 //Criar um objeto PdfConverter

PdfConverter converter = new PdfConverter();

//Vincular o arquivo PDF de entrada

converter.BindPdf("Source.pdf");

// Especificar a página inicial a ser processada

converter.StartPage = 1;

// Especificar a página final para processamento

converter.EndPage = 1;

// Criar um objeto Resolution para especificar a resolução da imagem resultante

converter.Resolution = new Aspose.PDF.Devices.Resolution(300);

//Iniciar o processo de conversão

converter.DoConvert();

// Criar um objeto MemoryStream para conter a imagem resultante

MemoryStream imageStream = new MemoryStream();

//Verificar se existem páginas e então converter para imagem uma a uma

while (converter.HasNextImage())

{

    // Salvar a imagem no formato de imagem especificado

    converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

    // Definir a posição do stream para o início do stream

    imageStream.Position = 0;

{{% /alert %}}

// Define a posição do fluxo para o início do fluxo

imageStream.Position = 0;

// Instancia um objeto BarCodeReader

Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

// String txtResult.Text = "";

while (barcodeReader.Read())

{

    // Obtém o texto do código de barras da imagem do código de barras

    string code = barcodeReader.GetCodeText();

    // Escreve o texto do código de barras na saída do Console

    Console.WriteLine("BARCODE : " + code);

}

// Fecha o objeto BarCodeReader para liberar o arquivo de imagem

barcodeReader.Close();

}

// Fecha a instância do PdfConverter e libera os recursos

converter.Close();

// Fecha o fluxo que contém o objeto de imagem

imageStream.Close();

{{< /highlight >}}

{{% alert color="primary" %}}

Nos trechos de código acima, a imagem de saída é salva em um objeto MemoryStream.
```
No código acima, a imagem de saída é salva em um objeto MemoryStream.

{{% /alert %}}

{anchor:devices]
#### **Usando a Classe PngDevice**
Na Aspose.PDF.Devices, está a PngDevice. Esta classe permite converter páginas de documentos PDF em imagens PNG.

Para o propósito deste exemplo, carregue o arquivo PDF fonte no Documento e converta as páginas do documento em imagens PNG. Após a criação das imagens, use a classe BarCodeReader sob Aspose.BarCodeRecognition para identificar e ler códigos de barras nas imagens.

{{% alert color="primary" %}}

Os exemplos de código fornecidos aqui percorrem as páginas do documento PDF e tentam identificar códigos de barras em cada página.

{{% /alert %}}
##### **Exemplos de Programação**
**C#**

{{< highlight csharp >}}

 //Abrir o documento PDF

Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// Percorrer as páginas individuais do arquivo PDF

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)

{

    using (MemoryStream imageStream = new MemoryStream())

using (MemoryStream imageStream = new MemoryStream())
{
    // Criar um objeto Resolution
    Aspose.PDF.Devices.Resolution resolution = new Aspose.PDF.Devices.Resolution(300);

    // Instanciar um objeto PngDevice passando um objeto Resolution como argumento para seu construtor
    Aspose.PDF.Devices.PngDevice pngDevice = new Aspose.PDF.Devices.PngDevice(resolution);

    // Converter uma página específica e salvar a imagem no stream
    pngDevice.Process(pdfDocument.Pages[pageCount], imageStream);

    // Definir a posição do stream para o início do Stream
    imageStream.Position = 0;

    // Instanciar um objeto BarCodeReader
    Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

    // String txtResult.Text = "";
    while (barcodeReader.Read())
    {
        // Obter o texto do código de barras da imagem do código de barras
        string code = barcodeReader.GetCodeText();
```

```csharp
string code = barcodeReader.GetCodeText();

// Escreva o texto do código de barras na saída do Console

Console.WriteLine("BARCODE : " + code);

}

// Feche o objeto BarCodeReader para liberar o arquivo de imagem

barcodeReader.Close();

}

}

{{< /highlight >}}



{{% alert color="primary" %}}

Para mais informações sobre os tópicos abordados neste artigo, por favor visite:

- Converter páginas de PDF para diferentes formatos de imagem (Facades)
- Converter todas as páginas do PDF para imagens PNG
- [Ler Códigos de Barras](https://docs.aspose.com/barcode/net/read-barcodes/)


{{% /alert %}}
```
