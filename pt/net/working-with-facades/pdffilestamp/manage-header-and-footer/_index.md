---
title: Gerenciar Cabeçalho e Rodapé
type: docs
weight: 40
url: /pt/net/manage-header-and-footer/
description: Esta seção explica como gerenciar Cabeçalho e Rodapé com Aspose.PDF Facades usando a Classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Adicionar Cabeçalho em um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) permite adicionar cabeçalho em um arquivo PDF. In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class.

Para adicionar um cabeçalho, você primeiro precisa criar um objeto da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Você pode formatar o texto do cabeçalho usando a classe [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Assim que estiver pronto para adicionar o cabeçalho no arquivo, você precisa chamar o método [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Você também precisa especificar pelo menos a margem superior no método [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). O trecho de código a seguir mostra como adicionar um cabeçalho em um arquivo PDF.

```csharp
 public static void AddHeader()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create formatted text for page number
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Yellow,
                System.Drawing.Color.Black,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Add header
            fileStamp.AddHeader(formattedText, 10);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddHeader_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## Adicionar Rodapé em um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) permite que você adicione um rodapé em um arquivo PDF. In order to add footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class.

Para adicionar um rodapé, você primeiro precisa criar um objeto da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Você pode formatar o texto do rodapé usando a classe [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Quando estiver pronto para adicionar o rodapé no arquivo, você precisa chamar o método [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Você também precisa especificar pelo menos a margem inferior no método [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). O trecho de código a seguir mostra como adicionar um rodapé em um arquivo PDF.

```csharp
 public static void AddFooter()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create formatted text for page number
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Blue,
                System.Drawing.Color.Gray,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Add footer
            fileStamp.AddFooter(formattedText, 10);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddFooter_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## Adicionar Imagem no Cabeçalho de um Arquivo PDF Existente

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) permite que você adicione uma imagem no cabeçalho de um arquivo PDF.  Para adicionar uma imagem no cabeçalho, você primeiro precisa criar um objeto da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Depois disso, você precisa chamar o método [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Você pode passar a imagem para o método [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). O trecho de código a seguir mostra como adicionar uma imagem no cabeçalho do arquivo PDF.

```csharp
public static void AddImageHeader()
        {
            // Criar objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir Documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Adicionar Cabeçalho
                fileStamp.AddHeader(fs, 10);

                // Salvar arquivo PDF atualizado
                fileStamp.Save(_dataDir + "AddImage-Header_out.pdf");
                // Fechar fileStamp
                fileStamp.Close();
            }
        }
```
## Adicionar Imagem no Rodapé de um Arquivo PDF Existente

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) permite adicionar imagem no rodapé de um arquivo PDF. Para adicionar uma imagem no rodapé, você primeiro precisa criar um objeto da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Depois disso, você precisa chamar o método [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Você pode passar a imagem para o método [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). O seguinte trecho de código mostra como adicionar uma imagem no rodapé de um arquivo PDF.

```csharp
public static void AddImageFooter()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Add footer
                fileStamp.AddFooter(fs, 10);

                // Save updated PDF file
                fileStamp.Save(_dataDir + "AddImage-Footer_out.pdf");

                // Close fileStamp
                fileStamp.Close();
            }
        }
```