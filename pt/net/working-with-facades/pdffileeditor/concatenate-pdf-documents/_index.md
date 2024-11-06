---
title: Concatenar documentos PDF em C#
linktitle: Concatenar documentos PDF
type: docs
weight: 20
url: pt/net/concatenate-pdf-documents/
description: Esta seção explica como concatenar documentos PDF com Aspose.PDF Facades usando a classe PdfFileEditor.
aliases:
    - /pdf/net/concatenate-multiple-pdf-files-using-memorystreams/
    - /pdf/net/concatenate-pdf-files-and-create-table-of-contents/
    - /pdf/net/concatenate-pdf-forms-and-keep-fields-names-unique/
    - /pdf/net/concatenating-all-pdf-files-in-particular-folder/
    - /pdf/net/how-to-concatenate-pdf-files-in-different-ways/
    - /pdf/net/append-pdf-files/
lastmod: "2021-06-05"
---

## **Visão Geral**

Este artigo explica como mesclar, combinar ou concatenar diferentes arquivos PDF em um único PDF usando C#. Ele cobre tópicos como:

- [C# Mesclar Arquivos PDF](#concatenate-pdf-files-using-file-paths)
- [C# Combinar Arquivos PDF](#concatenate-pdf-files-using-file-paths)

- [C# Mesclar Múltiplos Arquivos PDF em um PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Combinar Múltiplos arquivos PDF em um único PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Unir todos os arquivos PDF em uma pasta](#concatenating-all-pdf-files-in-particular-folder)
- [C# Combinar todos os arquivos PDF em uma pasta](#concatenating-all-pdf-files-in-particular-folder)
- [C# Unir arquivos PDF usando caminhos de arquivos](#concatenate-pdf-files-using-file-paths)
- [C# Combinar arquivos PDF usando streams](#concatenate-array-of-pdf-files-using-streams)
- [C# Concatenar todos os arquivos PDF na pasta](#concatenate-pdf-files-in-folder)

## Concatenar arquivos PDF usando caminhos de arquivos

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) é a classe no [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) que permite concatenar múltiplos arquivos PDF. Você pode não apenas concatenar arquivos usando FileStreams, mas também usando MemoryStreams. Neste artigo, o processo de concatenação dos arquivos usando MemoryStreams será explicado e, em seguida, mostrado usando o trecho de código.

O método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) pode ser usado para concatenar dois arquivos PDF. O método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) permite que você passe três parâmetros: primeiro PDF de entrada, segundo PDF de entrada e PDF de saída. O PDF de saída final contém ambos os arquivos PDF de entrada.

O trecho de código C# a seguir mostra como concatenar arquivos PDF usando caminhos de arquivo.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-ConcatenateUsingPath.cs" >}}

Em alguns casos, quando há muitos contornos, os usuários podem desativá-los configurando CopyOutlines para false e melhorar o desempenho da concatenação.
{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-CopyOutline.cs" >}}

## Concatenar vários arquivos PDF usando MemoryStreams

O método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) leva os arquivos PDF de origem e o arquivo PDF de destino como parâmetros. Esses parâmetros podem ser caminhos para os arquivos PDF no disco ou podem ser MemoryStreams. Agora, para este exemplo, primeiro criaremos dois fluxos de arquivos para ler os arquivos PDF do disco. Em seguida, converteremos esses arquivos em arrays de bytes. Esses arrays de bytes dos arquivos PDF serão convertidos em MemoryStreams. Uma vez que obtemos os MemoryStreams dos arquivos PDF, seremos capazes de passá-los para o método de concatenação e mesclar em um único arquivo de saída.

O snippet de código C# a seguir mostra como concatenar vários arquivos PDF usando MemoryStreams:

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenateMultiplePDFUsingMemoryStream-ConcatenateMultiplePDFUsingMemoryStream.cs" >}}

## Concatenar Array de Arquivos PDF Usando Caminhos de Arquivo

Se você deseja concatenar vários arquivos PDF, pode usar a sobrecarga do método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index), que permite passar um array de arquivos PDF. O resultado final é salvo como um arquivo mesclado criado a partir de todos os arquivos no array. O seguinte trecho de código C# mostra como concatenar um array de arquivos PDF usando caminhos de arquivo.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfFilesWithPath-ConcatenateArrayOfFilesWithPath.cs" >}}

## Concatenar Array de Arquivos PDF Usando Streams

Concatenar um array de arquivos PDF não se limita apenas a arquivos que residem no disco. Você também pode concatenar um array de arquivos PDF a partir de fluxos. Se você quiser concatenar vários arquivos PDF, pode usar a sobrecarga apropriada do método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). Primeiro, você precisa criar um array de fluxos de entrada e um fluxo para o PDF de saída e, em seguida, chamar o método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). A saída será salva no fluxo de saída. O seguinte trecho de código C# mostra como concatenar um array de arquivos PDF usando fluxos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfPdfUsingStreams-ConcatenateArrayOfPdfUsingStreams.cs" >}}

## Concatenando todos os arquivos Pdf em uma pasta específica

Você pode até mesmo ler todos os arquivos Pdf em uma pasta específica em tempo de execução e concatená-los, sem nem mesmo saber os nomes dos arquivos. Forneça simplesmente o caminho do diretório, que contém os documentos PDF, que você gostaria de concatenar.

Por favor, tente usar o seguinte trecho de código C# para alcançar essa funcionalidade.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatingAllPdfFiles-ConcatenatingAllPdfFiles.cs" >}}

## Concatenar Formulários PDF e manter nomes de campos únicos

A classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) no [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) oferece a capacidade de concatenar os arquivos PDF. Agora, se os arquivos Pdf que devem ser concatenados tiverem campos de formulário com nomes de campo semelhantes, o Aspose.PDF fornece o recurso para manter os campos no arquivo Pdf resultante como únicos e também é possível especificar o sufixo para tornar os nomes dos campos únicos. A propriedade [KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) de [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) como verdadeira fará com que os nomes dos campos sejam únicos quando os formulários Pdf forem concatenados. Além disso, a propriedade [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) de PdfFileEditor pode ser usada para especificar o formato definido pelo usuário do sufixo que é adicionado ao nome do campo para torná-lo único quando os formulários são concatenados. Esta string deve conter a substring `%NUM%`, que será substituída por números no arquivo resultante.

Veja o seguinte trecho de código simples para alcançar essa funcionalidade.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePDFForms-ConcatenatePDFForms.cs" >}}
## Concatenate PDF files and create Table Of Contents

## Concatenate PDF files

Por favor, dê uma olhada no seguinte trecho de código para informações sobre como mesclar os arquivos PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-ConcatenatePdfFilesAndCreateTOC.cs" >}}

### Insert blank page

Uma vez que os arquivos PDF foram mesclados, podemos inserir uma página em branco no início do documento na qual podemos criar o Índice. Para realizar este requisito, podemos carregar o arquivo mesclado no objeto **Document** e precisamos chamar o método Page.Insert(...) para inserir uma página em branco.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-InsertBlankPage.cs" >}}

### Add Text Stamps

Para criar um Índice, precisamos adicionar selos de texto na primeira página usando os objetos [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) e [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp). Classe Stamp fornece o método `BindLogo(...)` para adicionar [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) e também podemos especificar a localização para adicionar essas marcas de texto usando o método `SetOrigin(..)`. Neste artigo, estamos concatenando dois arquivos PDF, então precisamos criar dois objetos de marca de texto apontando para esses documentos individuais.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-AddTextStamps.cs" >}}

### Criar links locais

Agora precisamos adicionar links para as páginas dentro do arquivo concatenado. Para cumprir esse requisito, podemos usar o método `CreateLocalLink(..)` da classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). No trecho de código a seguir, passamos Transparente como 4º argumento para que o retângulo ao redor do link não seja visível.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CreateLocalLinks.cs" >}}
### Código Completo

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CompletedCode.cs" >}}

## Concatenar arquivos PDF na pasta

A classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) no namespace Aspose.Pdf.Facades oferece a capacidade de concatenar o arquivo PDF. Você pode até mesmo ler todos os arquivos Pdf em uma pasta específica em tempo de execução e concatená-los, sem sequer saber os nomes dos arquivos. Basta fornecer o caminho do diretório, que contém os documentos PDF, que você gostaria de concatenar.

Por favor, tente usar o seguinte trecho de código C# para alcançar essa funcionalidade do Aspose.PDF:

```csharp
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

// Recuperar nomes de todos os arquivos Pdf em um Diretório específico
string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

// Obter a data atual do Sistema e definir seu formato
string date = DateTime.Now.ToString("MM-dd-yyyy");
// Obter a hora atual do Sistema e definir seu formato
string hoursSeconds = DateTime.Now.ToString("hh-mm");
// Definir o valor para o documento Pdf Resultante final
string masterFileName = date + "_" + hoursSeconds + "_out.pdf";

// Instanciar objeto PdfFileEditor
Aspose.Pdf.Facades.PdfFileEditor pdfEditor = new PdfFileEditor();

// Chamar o método Concatenate do objeto PdfFileEditor para concatenar todos os arquivos de entrada
// Em um único arquivo de saída
pdfEditor.Concatenate(fileEntries, dataDir + masterFileName);
```