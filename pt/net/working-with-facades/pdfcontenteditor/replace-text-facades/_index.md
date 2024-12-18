---
title: Substituir Texto - Facades
type: docs
weight: 40
url: /pt/net/replace-text-facades/
description: Esta seção explica como trabalhar com Texto - Facades usando a Classe PdfContentEditor.
lastmod: "2021-06-24"
draft: false
---

## Substituir Texto em um Arquivo PDF Existente

Para substituir texto em um arquivo PDF existente, você precisa criar um objeto da classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) e vincular um arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Após isso, você precisa chamar o método [ReplaceText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index). Você precisa salvar o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) da classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). O trecho de código a seguir mostra como substituir texto em um arquivo PDF existente.

```csharp
public static void ReplaceText01()
{
    PdfContentEditor editor = new PdfContentEditor();
    editor.BindPdf(_dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label");

    // save the output file
    editor.Save(_dataDir + "PdfContentEditorDemo01.pdf");
    }
```

Veja como fica no documento original:

![Replace Text](replace_text1.png)

E veja o resultado após substituir o texto:

![Result of replacing Text](replace_text2.png)

No segundo exemplo, você verá como, além de substituir o texto, você também pode aumentar ou diminuir o tamanho da fonte:
```csharp
public static void ReplaceText02()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        editor.ReplaceText("Value", "Label", 12);

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo02.pdf");
    }
```

Para possibilidades mais avançadas de trabalhar com nosso texto, usaremos o método [TextState](https://reference.aspose.com/pdf/net/aspose.pdf.text/textstate). Com este método, podemos tornar o texto em negrito, itálico, colorido, e assim por diante.

```csharp
    public static void ReplaceText03()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        TextState textState = new TextState
        {
            ForegroundColor = Color.Red,
            FontSize = 12,
        };
        editor.ReplaceText("Value", "Label", textState);

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo03.pdf");
    }
```

Caso você precise substituir todo o texto especificado no documento, use o seguinte trecho de código. Isso é, a substituição do texto ocorrerá sempre que o texto especificado para substituição for encontrado, e também contará o número de tais substituições.

```csharp
public static void ReplaceText04()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.ReplaceText("Value", "Label")) count++;

        Console.WriteLine($"{count} occurrences have been replaced.");

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo04.pdf");
    }
```

![Substituir todo o Texto](replace_text3.png)

O trecho de código a seguir mostra como fazer todas as substituições de texto, mas em uma página específica do seu documento.

```csharp
public static void ReplaceText05()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.ReplaceText("9999", 2, "ABCDE")) count++;
        Console.WriteLine($"{count} occurrences have been replaced.");

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo05.pdf");
    }
```
No próximo trecho de código, mostraremos como substituir, por exemplo, um determinado número pelas letras que precisamos.

```csharp
   public static void ReplaceText06()
    {
        PdfContentEditor editor = new PdfContentEditor
        {
            ReplaceTextStrategy = new ReplaceTextStrategy
            {
                IsRegularExpressionUsed = true,
                ReplaceScope = ReplaceTextStrategy.Scope.ReplaceAll
            }
        };
        editor.BindPdf(_dataDir + "sample.pdf");
        editor.ReplaceText("\\d{4}", "ABCDE");
        // salvar o arquivo de saída
        editor.Save(_dataDir + "PdfContentEditorDemo06.pdf");
    }
```