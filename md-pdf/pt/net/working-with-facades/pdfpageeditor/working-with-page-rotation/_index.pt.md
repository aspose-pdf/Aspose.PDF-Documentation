---
title: Trabalhando com Rotação de Página
type: docs
weight: 10
url: /net/working-with-page-rotation/
description: Esta seção explica como trabalhar com Rotação de Página usando a Classe PdfPageEditor.
lastmod: "2021-07-07"
draft: false
---

{{% alert color="primary" %}}

A classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) fornece a funcionalidade para rotacionar uma página.

{{% /alert %}}

## Rotacionar página usando PageRotations

Para rotacionar páginas no documento, podemos usar [PageRotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations).
`PageRotations` contém o número da página e o grau de rotação, a chave representa o número da página, o valor da chave representa a rotação em graus.

```csharp
public static void RotatePages1()
{
    var editor = new PdfPageEditor();
    editor.BindPdf(_dataDir + "sample.pdf");

    editor.PageRotations = new System.Collections.Generic.Dictionary<int, int> { { 1, 90 }, { 2, 180 }, { 3,270 } };

    editor.Save(_dataDir + "sample-rotate-a.pdf");
}
```

## Rotacionar página usando Rotação

Também podemos usar a propriedade [Rotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/rotation). A rotação deve ser 0, 90, 180 ou 270

```csharp
public static void RotatePages2()
{
    var editor = new PdfPageEditor();
    editor.BindPdf(_dataDir + "sample.pdf");

    editor.ProcessPages = new int[] { 1, 3 };
    editor.Rotation = 90;

    editor.Save(_dataDir + "sample-rotate-a.pdf");
}
```