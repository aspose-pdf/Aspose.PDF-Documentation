---
title: Reemplazar Texto - Fachadas
type: docs
weight: 40
url: es/net/replace-text-facades/
description: Esta sección explica cómo trabajar con Texto - Fachadas usando la Clase PdfContentEditor.
lastmod: "2021-06-24"
draft: false
---

## Reemplazar Texto en un Archivo PDF Existente

Para reemplazar texto en un archivo PDF existente, necesita crear un objeto de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) y enlazar un archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Después de eso, necesitas llamar al método [ReplaceText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index). Necesitas guardar el archivo PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). El siguiente fragmento de código te muestra cómo reemplazar texto en un archivo PDF existente.

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

Revisa cómo se ve en el documento original:

![Replace Text](replace_text1.png)

Y verifica el resultado después de reemplazar el texto:

![Result of replacing Text](replace_text2.png)

En el segundo ejemplo, verás cómo, además de reemplazar el texto, también puedes aumentar o disminuir el tamaño de la fuente:
```csharp
public static void ReplaceText02()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        editor.ReplaceText("Value", "Label", 12);

        // guardar el archivo de salida
        editor.Save(_dataDir + "PdfContentEditorDemo02.pdf");
    }
```

Para posibilidades más avanzadas de trabajar con nuestro texto, utilizaremos el método [TextState](https://reference.aspose.com/pdf/net/aspose.pdf.text/textstate). Con este método, podemos hacer que el texto sea negrita, cursiva, coloreado, y así sucesivamente.

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

        // guardar el archivo de salida
        editor.Save(_dataDir + "PdfContentEditorDemo03.pdf");
    }
```

En caso de que necesites reemplazar todo el texto especificado en el documento, utiliza el siguiente fragmento de código. Es decir, la sustitución del texto se llevará a cabo dondequiera que se encuentre el texto especificado para la sustitución, y también contará el número de tales sustituciones.

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

![Reemplazar todo el texto](replace_text3.png)

El siguiente fragmento de código muestra cómo realizar todas las sustituciones de texto pero en una página específica de su documento.

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
En el siguiente fragmento de código, mostraremos cómo reemplazar, por ejemplo, un número dado con las letras que necesitamos.

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
        // guardar el archivo de salida
        editor.Save(_dataDir + "PdfContentEditorDemo06.pdf");
    }
```