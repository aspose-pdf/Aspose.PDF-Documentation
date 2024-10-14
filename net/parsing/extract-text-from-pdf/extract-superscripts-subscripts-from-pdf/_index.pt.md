---
title: Extrair Textos SuperScripts e SubScripts de PDF
linktitle: Extrair SuperScripts e SubScripts
type: docs
weight: 30
url: /net/extract-superscripts-subscripts-from-pdf/
description: Este artigo descreve várias maneiras de extrair textos SuperScripts e SubScripts de PDF usando Aspose.PDF em C#.
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Textos SuperScripts e SubScripts

Extrair texto de um documento PDF é algo comum. No entanto, nesse texto, quando extraído, os **SuperScripts e SubScripts** contidos neles, que são típicos para documentos técnicos e artigos, podem não ser exibidos. Um SubScript ou SuperScript é um caractere, número ou letra colocado abaixo ou acima de uma linha regular de texto. Ele geralmente é menor que o resto do texto.

**SubScripts e SuperScripts** são mais frequentemente usados em fórmulas, expressões matemáticas e especificações de compostos químicos.
**SubScripts e SuperScripts** são mais frequentemente usados em fórmulas, expressões matemáticas e especificações de compostos químicos.
Em um dos últimos lançamentos, a biblioteca **Aspose.PDF for .NET** adicionou suporte para a extração de textos SuperScripts e SubScripts de PDF.

Use a classe **TextFragmentAbsorber** e você já pode fazer qualquer coisa com o texto encontrado, ou seja, você pode simplesmente usar todo o texto. Experimente o próximo trecho de código:

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            writer.WriteLine(absorber.Text);
        }
```

Ou use **TextFragments** separadamente e faça todo tipo de manipulações com eles, por exemplo, ordenar por coordenadas ou por tamanho.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                writer.Write(textFragment.Text);
            }
        }
```
