---
title: Editando páginas individuais de um PDF
type: docs
weight: 20
url: pt/net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/
description: Esta seção explica como editar páginas individuais de um PDF usando a classe PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

O namespace Aspose.Pdf.Facades no [Aspose.PDF para .NET](/pdf/net/) permite manipular páginas individuais em um arquivo PDF. Este recurso ajuda a trabalhar com a exibição da página, alinhamento e transição, etc. A classe PdfpageEditor ajuda a alcançar essa funcionalidade. Neste artigo, examinaremos as propriedades e métodos fornecidos por esta classe e o funcionamento desses métodos também.

{{% /alert %}}

## Explicação

A classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) é diferente da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) e da classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Primeiro, precisamos entender a diferença e, então, seremos capazes de entender melhor a classe PdfPageEditor. A classe PdfFileEditor permite que você manipule todas as páginas em um arquivo, como adicionar, excluir ou concatenar páginas, etc., enquanto a classe PdfContentEditor ajuda você a manipular o conteúdo de uma página, ou seja, texto e outros objetos, etc. Por outro lado, a classe PdfPageEditor trabalha apenas com a própria página individual, como girar, ampliar e alinhar uma página, etc.

Podemos dividir os recursos fornecidos por esta classe em três categorias principais, ou seja, Transição, Alinhamento e Exibição. Vamos discutir essas categorias abaixo:

### Transição

Esta classe contém duas propriedades relacionadas à transição, ou seja. [TransitionType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitiontype) e [TransitionDuration](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitionduration). TransitionType especifica o estilo de transição a ser usado ao mover para esta página a partir de outra página durante uma apresentação. TransitionDuration especifica a duração de exibição para as páginas.

### Alignment

A classe PdfPageEditor suporta alinhamentos tanto horizontais quanto verticais. It provides two properties to serve the purpose i.e. [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/alignment) and [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/VerticalAlignment). Alignment property is used to align the contents horizontally. Alignment property takes a value of AlignmentType, which contains three options i.e. Center, Left, and Right. VerticalAlignment property takes a value of VerticalAlignmentType, which contains three options i.e. Bottom, Center, and Top.

### Exibição

Na categoria de exibição, podemos incluir propriedades como TamanhoDaPágina, Rotação, Zoom e DuraçãoDeExibição. PageSize property especifica o tamanho da página individual no arquivo. Esta propriedade aceita um objeto PageSize como entrada, que encapsula tamanhos de página predefinidos como A0, A1, A2, A3, A4, A5, A6, B5, Carta, Ledger e P11x17. A propriedade Rotation é usada para definir a rotação de uma página individual. Ela pode receber os valores 0, 90, 180 ou 270. A propriedade Zoom define o coeficiente de zoom para a página e aceita um valor de ponto flutuante como entrada. Esta classe também fornece um método para obter o tamanho e a rotação da página individual no arquivo.

Você pode encontrar exemplos dos métodos mencionados acima no trecho de código fornecido abaixo:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-EditPdfPages-EditPdfPages.cs" >}}

## Conclusão

{{% alert color="primary" %}}
Neste artigo, examinamos mais de perto a classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). We have elaborated the properties and methods provided by this class. It makes the manipulation of individual pages in a class a very easy and simple task.  
Elaboramos as propriedades e métodos fornecidos por esta classe. Isso torna a manipulação de páginas individuais em uma classe uma tarefa muito fácil e simples.  
{{% /alert %}}