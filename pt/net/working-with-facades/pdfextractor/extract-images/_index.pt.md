```
---
title: Extrair Imagens usando PdfExtractor
type: docs
weight: 20
url: /net/extract-images/
description: Esta seção explica como extrair Imagens com Aspose.PDF Facades usando a Classe PdfExtractor.
lastmod: "2021-07-15"
---

## Extrair Imagens do PDF Inteiro para Arquivos (Facades)

A classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) permite que você extraia imagens de um arquivo PDF.
``` First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Primeiro, você precisa criar um objeto da classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Após isso, chame o método [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extrair todas as imagens para a memória. Uma vez que as imagens são extraídas, você pode obtê-las com a ajuda dos métodos [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) e [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Você precisa percorrer todas as imagens extraídas usando um loop while. Para salvar as imagens no disco, você pode chamar a sobrecarga do método [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) que leva o caminho do arquivo como argumento. O seguinte trecho de código mostra como extrair imagens do PDF inteiro para arquivos.

```csharp
   public static void ExtractImagesWholePDF()
        {
            // Open input PDF
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Extract all the images
            pdfExtractor.ExtractImage();

            // Get all the extracted images
            while (pdfExtractor.HasNextImage())
                pdfExtractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
```
## Extrair Imagens do PDF Completo para Fluxos (Facades)

A classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) permite que você extraia imagens de um arquivo PDF para fluxos. 
Primeiro, você precisa criar um objeto da classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index).
``` Após isso, chame o método [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extrair todas as imagens para a memória. Uma vez que as imagens são extraídas, você pode obter essas imagens com a ajuda dos métodos [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) e [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Você precisa percorrer todas as imagens extraídas usando um loop while. Para salvar as imagens no fluxo, você pode chamar a sobrecarga do método [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) que leva Stream como argumento. O trecho de código a seguir mostra como extrair imagens de todo o PDF para fluxos.

```csharp
    public static void ExtractImagesWholePDFStreams()
        {
            // Abrir PDF de entrada
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Extrair imagens
            pdfExtractor.ExtractImage();
            // Obter todas as imagens extraídas
            while (pdfExtractor.HasNextImage())
            {
                // Ler imagem na memória
                MemoryStream memoryStream = new MemoryStream();
                pdfExtractor.GetNextImage(memoryStream);

                // Escrever no disco, se desejar, ou usar de outra forma.
                FileStream fileStream = new
                FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
                memoryStream.WriteTo(fileStream);
                fileStream.Close();
            }
        }
```
## Extrair Imagens de uma Página Específica de um PDF (Facades)

Você pode extrair imagens de uma página específica de um arquivo PDF. In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) e [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) propriedades para a página específica da qual você deseja extrair imagens. First of all, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Antes de tudo, você precisa criar um objeto da classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Secondly, you have to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) * e [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) propriedades. Depois disso, chame o método [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extrair todas as imagens para a memória. Uma vez que as imagens são extraídas, você pode obtê-las com a ajuda dos métodos [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) e [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Você precisa percorrer todas as imagens extraídas usando um loop while. Você pode salvar as imagens no disco ou em um stream. Você só precisa chamar a sobrecarga apropriada do método [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). O trecho de código a seguir mostra como extrair imagens de uma página específica do PDF para streams.

```csharp
public static void ExtractImagesParticularPage()
{
    // Abra o PDF de entrada
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Defina as propriedades StartPage e EndPage para o número da página da qual
    // você deseja extrair imagens
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // Extraia as imagens
    pdfExtractor.ExtractImage();
    // Obtenha as imagens extraídas
    while (pdfExtractor.HasNextImage())
    {
        // Leia a imagem no stream de memória
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // Escreva no disco, se desejar, ou utilize de outra forma.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## Extract Images from a Range of Pages of a PDF (Facades)

Você pode extrair imagens de um intervalo de páginas de um arquivo PDF. Para fazer isso, você precisa definir as propriedades [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) e [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) para o intervalo de páginas do qual deseja extrair imagens. First of all, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Antes de tudo, você precisa criar um objeto da classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Secondly, you have to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) e [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) propriedades. Depois disso, chame o método [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extrair todas as imagens na memória. Uma vez que as imagens são extraídas, você pode obtê-las com a ajuda dos métodos [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) e [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Você precisa percorrer todas as imagens extraídas usando um loop while. Você pode salvar as imagens no disco ou em stream. Você só precisa chamar a sobrecarga apropriada do método [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). O trecho de código a seguir mostra como extrair imagens de um intervalo de páginas de um PDF para streams.

```csharp
public static void ExtractImagesRangePages()
{
    // Abrir PDF de entrada
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Definir propriedades StartPage e EndPage para o número da página
    // De onde você deseja extrair imagens
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // Extrair imagens
    pdfExtractor.ExtractImage();
    // Obter imagens extraídas
    while (pdfExtractor.HasNextImage())
    {
        // Ler imagem na memória
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // Escrever no disco, se desejar, ou usar de outra forma.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## Extrair Imagens usando o Modo de Extração de Imagens (Fachadas)

A classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) permite que você extraia imagens de um arquivo PDF. Aspose.PDF suporta dois modos de extração; o primeiro é ActuallyUsedImage, que extrai as imagens realmente usadas no documento PDF. Second mode is [DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode) que extrai as imagens definidas nos recursos do documento PDF (modo de extração padrão). First, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Primeiro, você precisa criar um objeto da classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Após isso, especifique o modo de extração de imagem usando a propriedade [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode). Em seguida, chame o método [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extrair todas as imagens na memória, dependendo do modo que você especificou. Uma vez que as imagens são extraídas, você pode obtê-las com a ajuda dos métodos [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) e [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Você precisa percorrer todas as imagens extraídas usando um loop while. Para salvar as imagens no disco, você pode chamar a sobrecarga do método [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) que leva o caminho do arquivo como argumento.

O seguinte trecho de código mostra como extrair imagens de um arquivo PDF usando a opção ExtractImageMode.
```csharp
public static void ExtractImagesImageExtractionMode()
{
    // Abrir PDF de entrada
    PdfExtractor extractor = new PdfExtractor();
    extractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Especificar o Modo de Extração de Imagem
    //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
    extractor.ExtractImageMode = ExtractImageMode.DefinedInResources;

    // Extrair Imagens com base no Modo de Extração de Imagem
    extractor.ExtractImage();

    // Obter todas as imagens extraídas
    while (extractor.HasNextImage())
    {
        extractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
    }
}
```

Para verificar se o PDF contém Texto ou Imagens use o próximo trecho de código:

```csharp
public static void CheckIfPdfContainsTextOrImages()
        {
            // Instanciar um objeto memoryStream para armazenar o texto extraído do Documento
            MemoryStream ms = new MemoryStream();
            // Instanciar objeto PdfExtractor
            PdfExtractor extractor = new PdfExtractor();

            // Vincular o documento PDF de entrada ao extrator
            extractor.BindPdf(_dataDir + "FilledForm.pdf");
            // Extrair texto do documento PDF de entrada
            extractor.ExtractText();
            // Salvar o texto extraído em um arquivo de texto
            extractor.GetText(ms);
            // Verificar se o comprimento do MemoryStream é maior ou igual a 1

            bool containsText = ms.Length >= 1;

            // Extrair imagens do documento PDF de entrada
            extractor.ExtractImage();

            // Chamando o método HasNextImage no loop while. Quando as imagens terminarem, o loop será encerrado
            bool containsImage = extractor.HasNextImage();

            // Agora descubra se este PDF é apenas texto ou apenas imagem

            if (containsText && !containsImage)
                Console.WriteLine("PDF contém apenas texto");
            else if (!containsText && containsImage)
                Console.WriteLine("PDF contém apenas imagem");
            else if (containsText && containsImage)
                Console.WriteLine("PDF contém tanto texto quanto imagem");
            else if (!containsText && !containsImage)
                Console.WriteLine("PDF não contém nem texto nem imagem");
        }

    }
```