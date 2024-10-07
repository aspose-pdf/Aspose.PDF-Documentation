---
title: Descobrir se PDF contém imagens ou texto
linktitle: Verificar presença de texto e imagens
type: docs
weight: 40
url: /net/find-whether-pdf-file-contains-images-or-text-only/
description: Este tópico explica como descobrir se um arquivo PDF contém apenas imagens ou texto com a Classe PdfExtractor.
lastmod: "2021-06-05"
draft: false
---

## Background

Um arquivo PDF pode conter tanto texto quanto imagens. Às vezes, um usuário pode precisar descobrir se um arquivo PDF contém apenas texto ou se contém apenas imagens. Também podemos descobrir se contém ambos ou nenhum.

{{% alert color="primary" %}}

O seguinte trecho de código mostra como atender a esse requisito.

{{% /alert %}}

```csharp
 public static void CheckIfPdfContainsTextOrImages()
{
    // Instanciar um objeto memoryStream para armazenar o texto extraído do Documento
    MemoryStream ms = new MemoryStream();
    // Instanciar objeto PdfExtractor
    PdfExtractor extractor = new PdfExtractor();

    // Vincular o documento PDF de entrada ao extractor
    extractor.BindPdf(_dataDir + "FilledForm.pdf");
    // Extrair texto do documento PDF de entrada
    extractor.ExtractText();
    // Salvar o texto extraído em um arquivo de texto
    extractor.GetText(ms);
    // Verificar se o comprimento do MemoryStream é maior ou igual a 1

    bool containsText = ms.Length >= 1;

    // Extrair imagens do documento PDF de entrada
    extractor.ExtractImage();

    // Chamando o método HasNextImage no loop while. Quando as imagens terminarem, o loop será encerrado
    bool containsImage = extractor.HasNextImage();

    // Agora descubra se este PDF é apenas texto ou apenas imagem

    if (containsText && !containsImage)
        Console.WriteLine("PDF contém apenas texto");
    else if (!containsText && containsImage)
        Console.WriteLine("PDF contém apenas imagem");
    else if (containsText && containsImage)
        Console.WriteLine("PDF contém tanto texto quanto imagem");
    else if (!containsText && !containsImage)
        Console.WriteLine("PDF não contém nem texto nem imagem");
}
```