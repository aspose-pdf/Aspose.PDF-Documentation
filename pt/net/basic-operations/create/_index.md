---
title: Criar documento PDF programaticamente
linktitle: Criar PDF
type: docs
weight: 10
url: pt/net/create-document/
description: Esta página descreve como criar um documento PDF do zero com a biblioteca Aspose.PDF.
---

Aspose.PDF para API .NET permite que você crie e leia arquivos PDF usando C# e VB.NET. A API pode ser usada em uma variedade de aplicações .NET, incluindo WinForms, ASP.NET, e várias outras. Neste artigo, vamos mostrar como usar a Aspose.PDF para API .NET para gerar e ler arquivos PDF em aplicações .NET facilmente.

## Como Criar um Arquivo PDF usando C#

Para criar um arquivo PDF usando C#, os seguintes passos podem ser utilizados.

1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Adicionar um objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) à coleção [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) do objeto Document
1.
1. Salve o documento PDF resultante

O próximo trecho de código também funciona com a nova interface gráfica [Aspose.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// Inicializa o objeto documento
Document document = new Document();
// Adiciona página
Page page = document.Pages.Add();
// Adiciona texto à nova página
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// Salva o PDF atualizado
document.Save(dataDir + "HelloWorld_out.pdf")
```

Neste caso, criamos um documento PDF de uma página com tamanho de página A4, orientação retrato. Nossa página conterá um "Hello, World" na parte superior esquerda da página.
