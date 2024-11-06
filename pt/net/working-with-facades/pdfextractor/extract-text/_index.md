---
title: Extrair Texto de Arquivo PDF
type: docs
weight: 30
url: pt/net/extract-text/
description: Esta seção explica como extrair texto de um pdf usando a classe PdfExtractor.
lastmod: "2021-06-05"
---

Neste artigo, vamos analisar os detalhes de extração de texto de um arquivo PDF. Todos esses recursos de extração são fornecidos em um só lugar, na classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor). Veremos como usar esses recursos em nosso código.

A classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) fornece três tipos de capacidades de extração. Essas três categorias são Texto, Imagens e Anexos. Para realizar a extração em cada uma dessas três categorias, o PdfExtractor fornece vários métodos que trabalham juntos para fornecer o resultado final.

Por exemplo, para extrair texto você pode usar três métodos, ou seja, [ExtractText, GetText, HasNextPageText e GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index). Agora, para começar a extrair texto, antes de mais nada, você precisa chamar o método [ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index); isso irá extrair o texto do arquivo PDF e armazená-lo na memória. Depois disso, o método [GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) pegará esse texto extraído e o salvará no disco em um local especificado em um arquivo. [HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) ajuda você a percorrer cada página e verificar se a próxima página tem algum texto ou não. Se contiver algum texto, então [GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) ajudará você a salvar o texto de uma página individual no arquivo.

```csharp
public static void ExtractText()
{
    bool WholeText = true;
    // Criar um objeto da classe PdfExtractor
    PdfExtractor pdfExtractor = new PdfExtractor();

    // Vincular o PDF de entrada
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // ExtrairTexto
    pdfExtractor.ExtractText();

    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // Extrair o texto em arquivos separados
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```
Para Extrair o Modo de Extração de Texto, use o seguinte código:

```csharp
public static void ExtractTextExtractonMode()
{
    bool WholeText = true;
    // Crie um objeto da classe PdfExtractor
    PdfExtractor pdfExtractor = new PdfExtractor();

    // Vincule o PDF de entrada
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // ExtrairTexto
    // pdfExtractor.ExtractTextMode = 0; //modo puro
    pdfExtractor.ExtractTextMode = 1; //modo bruto
    pdfExtractor.ExtractText();


    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // Extraia o texto em arquivos separados
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```