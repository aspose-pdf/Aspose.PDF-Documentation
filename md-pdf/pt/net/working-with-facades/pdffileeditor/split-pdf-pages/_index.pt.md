---
title: Dividir páginas de PDF
type: docs
weight: 60
url: /net/split-pdf-pages/
description: Esta seção explica como dividir páginas de PDF com Aspose.PDF Facades usando a classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Dividir Páginas de PDF a partir da Primeira Usando Caminhos de Arquivo

O método [SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) permite que você divida o arquivo PDF começando na primeira página e terminando no número de página especificado. Se você deseja manipular os arquivos PDF do disco, pode passar os caminhos dos arquivos PDF de entrada e saída para este método. O trecho de código a seguir mostra como dividir páginas de PDF a partir da primeira usando caminhos de arquivo.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingPaths-SplitPagesUsingPaths.cs" >}}

## Dividir Páginas de PDF a partir da Primeira Usando Fluxos de Arquivo

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) método da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) permite que você divida o arquivo PDF começando da primeira página e terminando no número de página especificado. Se você quiser manipular os arquivos PDF a partir de fluxos, pode passar os fluxos de entrada e saída do PDF para este método. O seguinte trecho de código mostra como dividir páginas de PDF a partir do primeiro usando fluxos de arquivos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingStreams-SplitPagesUsingStreams.cs" >}}

## Dividir Páginas PDF em Lotes Usando Caminhos de Arquivo

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) método da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) permite que você divida o arquivo PDF em vários conjuntos de páginas. Neste exemplo, precisamos de dois conjuntos de páginas (1, 2) e (5, 6). Se você quiser acessar o arquivo PDF do disco, é necessário passar o PDF de entrada como caminho de arquivo. Este método retorna um array de MemoryStream. Você pode percorrer este array e salvar os conjuntos individuais de páginas como arquivos separados. O trecho de código a seguir mostra como dividir páginas de PDF em massa usando caminhos de arquivos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingPaths-SplitPagesToBulkUsingPaths.cs" >}}

## Dividir Páginas de PDF em Massa Usando Streams

O método [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite dividir o arquivo PDF em múltiplos conjuntos de páginas. No exemplo, precisamos de dois conjuntos de páginas (1, 2) e (5, 6). Você pode passar um fluxo para este método em vez de acessar o arquivo do disco. Este método retorna um array de MemoryStream. Você pode percorrer este array e salvar os conjuntos individuais de páginas como arquivos separados. O trecho de código a seguir mostra como dividir páginas de PDF em massa usando fluxos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingStreams-SplitPagesToBulkUsingStreams.cs" >}}

## Dividir Páginas de PDF Até o Fim Usando Caminhos de Arquivo

O método [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você divida o PDF a partir do número de página especificado até o final do arquivo PDF e o salve como um novo PDF. Para fazer isso, usando caminhos de arquivo, você precisa passar os caminhos de arquivo de entrada e saída e o número da página de onde a divisão precisa ser iniciada. O PDF de saída será salvo no disco. O trecho de código a seguir mostra como dividir páginas de PDF até o final usando caminhos de arquivo.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingPaths-SplitPagesToEndUsingPaths.cs" >}}

## Dividir Páginas de PDF até o Final Usando Streams

O método [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você divida o PDF a partir do número da página especificada até o final do arquivo PDF e o salve como um novo PDF. Para fazer isso, usando streams, você precisa passar streams de entrada e saída e o número da página de onde a divisão deve começar. O PDF de saída será salvo no stream de saída. O trecho de código a seguir mostra como dividir páginas de PDF até o final usando streams.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingStreams-SplitPagesToEndUsingStreams.cs" >}}

## Dividir PDF em Páginas Individuais Usando Caminhos de Arquivo

{{% alert color="primary" %}}

Você pode tentar dividir o documento PDF e visualizar os resultados online neste link:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

Para dividir o arquivo PDF em páginas individuais, você precisa passar o PDF como caminho de arquivo para o método [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Este método retornará um array de MemoryStream contendo páginas individuais do arquivo PDF. Você pode percorrer esse array de MemoryStream e salvar páginas individuais como arquivos PDF individuais no disco. O trecho de código a seguir mostra como dividir um PDF em páginas individuais usando caminhos de arquivos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingPaths-SplitToIndividualPagesUsingPaths.cs" >}}

## Dividir PDF em Páginas Individuais Usando Streams

Para dividir o arquivo PDF em páginas individuais, você precisa passar o PDF como stream para o método [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Este método retornará um array de MemoryStream contendo páginas individuais do arquivo PDF. Você pode percorrer este array de MemoryStream e salvar páginas individuais como arquivos PDF individuais no disco, ou você pode manter essas páginas individuais no fluxo de memória para uso posterior em sua aplicação. O trecho de código a seguir mostra como dividir um PDF em páginas individuais usando fluxos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingStreams-SplitToIndividualPagesUsingStreams.cs" >}}