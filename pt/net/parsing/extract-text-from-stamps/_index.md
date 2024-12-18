---
title: Extrair Texto de Carimbos usando C#
type: docs
weight: 60
url: /pt/net/extract-text-from-stamps/
description: Aprenda como usar a funcionalidade especial do Aspose.PDF para .NET - extração de texto de anotações de carimbo
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair Texto de Anotações de Carimbo

Aspose.PDF para NET permite que você extraia texto de anotações de carimbo. Para extrair texto de Anotações de Carimbo em um PDF, os seguintes passos podem ser usados.

1. Criar um objeto da classe `Document`
1. Obter a `Annotation` desejada da lista de anotações de uma página
1. Definir um novo objeto da classe `TextAbsorber`
1. Usar o método visit do TextAbsorber para obter o Texto

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

```csharp
public static void ExtractText()
{
   Document document = new Document(_dataDir + "ExtractStampText.pdf");
   Annotation item = document.Pages[1].Annotations[1];
   if (item is StampAnnotation annot) {
         TextAbsorber ta = new TextAbsorber();
         XForm ap = annot.Appearance["N"];
         ta.Visit(ap);
         Console.WriteLine(ta.Text);
   }
}
```

