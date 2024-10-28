---
title: Excluir páginas de PDF
type: docs
weight: 70
url: /net/delete-pdf-pages/
description: Esta seção explica como excluir páginas de PDF com Aspose.PDF Facades usando a classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

Se você deseja excluir um número de páginas do arquivo PDF que está no disco, então você pode usar a sobrecarga do método [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) que leva os seguintes três parâmetros: caminho do arquivo de entrada, array de números de páginas a serem excluídas e caminho do arquivo PDF de saída. O segundo parâmetro é um array de inteiros representando todas as páginas que precisam ser excluídas. As páginas especificadas são removidas do arquivo de entrada e o resultado é salvo como arquivo de saída. O seguinte trecho de código mostra como excluir páginas de PDF usando caminhos de arquivo.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingFilePath-DeletePagesUsingFilePath.cs" >}}


## Excluir Páginas de PDF Usando Fluxos

O método [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) também fornece uma sobrecarga que permite excluir as páginas do arquivo PDF de entrada, enquanto ambos os arquivos de entrada e saída estão nos fluxos. Esta sobrecarga leva os seguintes três parâmetros: fluxo de entrada, array de inteiros das páginas do PDF a serem excluídas e fluxo de saída. O trecho de código a seguir mostra como excluir páginas de um PDF usando fluxos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingStream-DeletePagesUsingStream.cs" >}}