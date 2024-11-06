---
title: Comparar documentos PDF
linktitle: Comparar PDF
type: docs
weight: 180
url: pt/net/compare-pdf-documents/
description: Desde o lançamento 24.7 é possível comparar o conteúdo de documentos PDF com marcas de anotação e saída lado a lado
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Comparando Documentos PDF com Aspose.PDF para .NET

Ao trabalhar com documentos PDF, há momentos em que você precisa comparar o conteúdo de dois documentos para identificar diferenças. A biblioteca Aspose.PDF para .NET oferece um conjunto de ferramentas poderoso para esse propósito. Neste artigo, exploraremos como comparar documentos PDF usando alguns trechos de código simples.

A funcionalidade de comparação em Aspose.PDF permite comparar dois documentos PDF página por página. Você pode escolher comparar páginas específicas ou documentos inteiros. O documento de comparação resultante destaca as diferenças, facilitando a identificação de mudanças entre os dois arquivos.

### Comparando Páginas Específicas

O primeiro trecho de código demonstra como comparar as primeiras páginas de dois documentos PDF.

O primeiro trecho de código demonstra como comparar as primeiras páginas de dois documentos PDF.

Passos:

1. Inicialização do Documento.
O código começa inicializando dois documentos PDF usando seus respectivos caminhos de arquivo (documentPath1 e documentPath2). Os caminhos são especificados como strings vazias por enquanto, mas na prática, você substituiria esses caminhos pelos caminhos de arquivo reais.
2. Processo de Comparação.
- Seleção de Página - a comparação é limitada à primeira página de cada documento ('Pages[1]').
- Opções de Comparação:

'Marcas de Alteração Adicionais = verdadeiro' - essa opção garante que marcadores de alteração adicionais sejam exibidos. Esses marcadores destacam diferenças que podem estar presentes em outras páginas, mesmo que não estejam na página atual sendo comparada.

'Modo de Comparação = ModoDeComparação.IgnorarEspaços' - este modo instrui o comparador a ignorar espaços no texto, focando apenas nas alterações dentro das palavras.

3.
```
```cs
    string documentPath1 = "";
    string documentPath2= "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

### Comparando Documentos Inteiros

O segundo trecho de código expande o escopo para comparar o conteúdo inteiro de dois documentos PDF.

Passos:

1. Inicialização do Documento.
Assim como no primeiro exemplo, dois documentos PDF são inicializados com seus caminhos de arquivo.
2. Processo de Comparação.
- Comparação de Documento Inteiro - ao contrário do primeiro trecho, este código compara o conteúdo inteiro dos dois documentos.
- Opções de Comparação - as opções são as mesmas do primeiro trecho, garantindo que espaços sejam ignorados e marcadores de alterações adicionais sejam exibidos.

3.
```cs
    string documentPath1 = "";
    string documentPath2 = "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1, document2, resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

Os resultados da comparação gerados por esses trechos de código são documentos PDF que você pode abrir em um visualizador como o Adobe Acrobat. Se você usar a visualização de duas páginas no Adobe Acrobat, você verá as alterações lado a lado:

- Deleções - estas são indicadas na página esquerda.
- Inserções - estas são indicadas na página direita.

Ao definir 'AdditionalChangeMarks' como 'true', você também pode ver marcadores para alterações que podem ocorrer em outras páginas, mesmo que essas alterações não estejam na página atual sendo visualizada.

**Aspose.PDF for .NET** oferece ferramentas robustas para comparar documentos PDF, seja para comparar páginas específicas ou documentos inteiros.
**Aspose.PDF para .NET** oferece ferramentas robustas para comparar documentos PDF, seja para comparar páginas específicas ou documentos inteiros.
