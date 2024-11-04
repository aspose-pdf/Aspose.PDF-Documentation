---
title: Inserir páginas PDF
type: docs
weight: 50
url: /net/insert-pdf-pages/
description: Esta seção explica como inserir páginas PDF com Aspose.PDF Facades usando a classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Inserir Páginas PDF Entre Dois Números Usando Caminhos de Arquivo

Um intervalo específico de páginas pode ser inserido de um PDF em outro usando o método [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Para fazer isso, você precisa de um arquivo PDF de entrada no qual deseja inserir as páginas, um arquivo de origem do qual as páginas precisam ser retiradas para inserção, um local onde as páginas devem ser inseridas e um intervalo de páginas do arquivo de origem que devem ser inseridas no arquivo PDF de entrada. Este intervalo é especificado com parâmetros de página inicial e página final. Finalmente, o arquivo PDF de saída é salvo com o intervalo especificado de páginas inseridas no arquivo de entrada. O trecho de código a seguir mostra como inserir páginas PDF entre dois números usando fluxos de arquivos.

## Inserir Array de Páginas PDF Usando Caminhos de Arquivo

Se você deseja inserir algumas páginas especificadas em outro arquivo PDF, então você pode usar uma sobrecarga do método [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) que requer um array de inteiros das páginas. Neste array, você pode especificar quais páginas específicas deseja inserir no arquivo PDF de entrada. Para fazer isso, você precisa de um arquivo PDF de entrada no qual deseja inserir as páginas, um arquivo de origem do qual as páginas precisam ser retiradas para inserção, um local onde as páginas serão inseridas e um array de inteiros das páginas do arquivo de origem que devem ser inseridas no arquivo PDF de entrada. Este array contém uma lista de páginas específicas que você está interessado em inserir no arquivo PDF de entrada. Finalmente, o arquivo PDF de saída é salvo com o array especificado de páginas inserido no arquivo de entrada.
O trecho de código a seguir mostra como inserir um array de páginas PDF usando caminhos de arquivos.

## Inserir Páginas PDF entre Dois Números Usando Streams

Se você deseja inserir o intervalo de páginas usando streams, você só precisa usar a sobrecarga apropriada do método [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Para fazer isso, você precisa de um fluxo de entrada de PDF no qual deseja inserir as páginas, um fluxo de porta do qual as páginas precisam ser retiradas para inserção, um local onde as páginas devem ser inseridas e um intervalo de páginas do fluxo de porta que precisam ser inseridas no fluxo de entrada de PDF. Este intervalo é especificado com parâmetros de página inicial e página final. Finalmente, o fluxo de saída de PDF é salvo com o intervalo especificado de páginas inseridas no fluxo de entrada. O trecho de código a seguir mostra como inserir páginas de PDF entre dois números usando fluxos.

## Inserir Array de Páginas PDF Usando Streams

Você também pode inserir um array de páginas em outro arquivo PDF usando fluxos com a ajuda da sobrecarga apropriada do método Insert, que requer um array de inteiros de páginas. No array, você pode especificar quais páginas em particular deseja inserir no fluxo de entrada do PDF. Para fazer isso, você precisa de um fluxo de entrada de PDF no qual deseja inserir as páginas, um fluxo de porta do qual as páginas precisam ser retiradas para inserção, um local onde as páginas devem ser inseridas e um array de inteiros das páginas do fluxo de porta que devem ser inseridas no arquivo PDF de entrada. Este array contém uma lista de páginas específicas que você está interessado em inserir no fluxo de entrada do PDF. Finalmente, o fluxo de saída do PDF é salvo com o array especificado de páginas inseridas no arquivo de entrada. O trecho de código a seguir mostra como inserir um array de páginas PDF usando fluxos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesUsingStreams-InsertPagesUsingStreams.cs" >}}