---
title: Definir Informações do Arquivo PDF
type: docs
weight: 40
url: /net/set-pdf-file-information/
description: Esta seção explica como definir Informações do Arquivo PDF com Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

A classe [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) permite definir informações específicas de arquivo de um arquivo PDF. Você precisa criar um objeto da classe [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) e, em seguida, definir diferentes propriedades específicas de arquivo como Autor, Título, Palavra-chave e Criador etc. Finalmente, salve o arquivo PDF atualizado usando o método [SaveNewInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) do objeto [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo).

O trecho de código a seguir mostra como definir informações do arquivo PDF.

```csharp
 public static void SetPdfInfo()
        {
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf")
            {
                // Definir informações do PDF
                Author = "Aspose",
                Title = "Hello World!",
                Keywords = "Peace and Development",
                Creator = "Aspose"
            };
            // Salvar arquivo atualizado
            fileInfo.SaveNewInfo(_dataDir + "SetFileInfo_out.pdf");
        }
```

## Definir Informações de Meta

O método [SetMetaInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) permite adicionar qualquer informação. Em nosso exemplo, adicionamos um campo. Confira o próximo trecho de código:

```csharp
 public static void SetMetaInfo()
        {
            // Criar instância do objeto PdfFileInfo
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "sample.pdf");

            // Definir novo atributo de cliente como meta info
            fInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

            // Salvar arquivo atualizado
            fInfo.SaveNewInfo(_dataDir + "SetMetaInfo_out.pdf");
```