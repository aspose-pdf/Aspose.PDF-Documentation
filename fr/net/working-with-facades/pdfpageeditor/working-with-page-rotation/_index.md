---
title: Travailler avec la Rotation de Page
type: docs
weight: 10
url: fr/net/working-with-page-rotation/
description: Cette section explique comment travailler avec la Rotation de Page en utilisant la classe PdfPageEditor.
lastmod: "2021-07-07"
draft: false
---

{{% alert color="primary" %}}

La classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) offre la possibilité de faire pivoter une page.

{{% /alert %}}

## Faire pivoter une page en utilisant PageRotations

Pour faire pivoter les pages dans un document, nous pouvons utiliser [PageRotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations).
`PageRotations` contient le numéro de la page et le degré de rotation, la clé représente le numéro de la page, la valeur de la clé représente la rotation en degrés.

```csharp
public static void RotatePages1()
{
    var editor = new PdfPageEditor();
    editor.BindPdf(_dataDir + "sample.pdf");

    editor.PageRotations = new System.Collections.Generic.Dictionary<int, int> { { 1, 90 }, { 2, 180 }, { 3,270 } };

    editor.Save(_dataDir + "sample-rotate-a.pdf");
}
```

## Faire pivoter la page en utilisant la Rotation

Nous pouvons également utiliser la propriété [Rotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/rotation). La rotation doit être de 0, 90, 180 ou 270

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