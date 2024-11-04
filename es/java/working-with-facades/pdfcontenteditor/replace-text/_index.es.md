---
title: Reemplazar Texto en un Archivo PDF
type: docs
weight: 40
url: /java/replace-text/
description: Esta sección explica cómo reemplazar texto con Aspose.PDF Facades - un conjunto de herramientas para operaciones populares con PDF.
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Reemplazar Texto en un Archivo PDF Existente (facades)

Para reemplazar texto en un archivo PDF existente, necesitas crear un objeto de la clase [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor), y vincular un archivo PDF de entrada usando el método bindPdf. Después de eso, necesitas llamar al método [replaceText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-).
Necesitas guardar el archivo PDF actualizado usando el método save de la clase [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor). El siguiente fragmento de código te muestra cómo reemplazar texto en un archivo PDF existente.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.TextState;
import com.aspose.pdf.facades.PdfContentEditor;
import com.aspose.pdf.facades.ReplaceTextStrategy;

public class PdfContentEditorText {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void ReplaceText01(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        editor.replaceText("Value", "Label");

        // guardar el archivo de salida
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```


Revisa cómo se ve en el documento original:

![Replace Text](replace_text1.png)

Y revisa el resultado después de reemplazar el texto:

![Result of replacing Text](replace_text2.png)

En el segundo ejemplo, verás cómo, además de reemplazar el texto, también puedes aumentar o disminuir el tamaño de la fuente:

```java
public static void ReplaceText02(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        editor.replaceText("Value", "Label", 12);

        // guarda el archivo de salida
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```

Para más posibilidades avanzadas de trabajar con nuestro texto, usaremos el método [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState). Con este método, podemos hacer el texto en negrita, cursiva, coloreado, etc.

```java
public static void ReplaceText03(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        TextState textState = new TextState();
        textState.setFontSize(12);
        editor.replaceText("Value", "Label", textState);

        // guarda el archivo de salida
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    

```


En caso de que necesite reemplazar todo el texto especificado en el documento, use el siguiente fragmento de código. Es decir, el reemplazo del texto se llevará a cabo dondequiera que se encuentre el texto especificado para el reemplazo, y también contará el número de tales reemplazos.

```java
    public static void ReplaceText04()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("Value", "Label")) count++;

        System.out.println(count+" ocurrencias han sido reemplazadas.");

        // guardar el archivo de salida
        editor.save(_dataDir + "PdfContentEditorDemo04.pdf");
    }
```

![Reemplazar todo el texto](replace_text3.png)

El siguiente fragmento de código muestra cómo hacer todos los reemplazos de texto pero en una página específica de su documento.

```java
    public static void ReplaceText05()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("9999", 2, "ABCDE")) count++;
        System.out.println(count+" ocurrencias han sido reemplazadas.");

        // guardar el archivo de salida
        editor.save(_dataDir + "PdfContentEditorDemo05.pdf");
    }
```


En el siguiente fragmento de código, mostraremos cómo reemplazar, por ejemplo, un número dado con las letras que necesitamos.

```java
    public static void ReplaceText06()
    {
        PdfContentEditor editor = new PdfContentEditor();
        ReplaceTextStrategy replaceTextStrategy = new ReplaceTextStrategy();
        replaceTextStrategy.setRegularExpressionUsed(true);
        replaceTextStrategy.setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.setReplaceTextStrategy(replaceTextStrategy);
        
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.replaceText("\\d{4}", "ABCDE");

        // guardar el archivo de salida
        editor.save(_dataDir + "PdfContentEditorDemo06.pdf");
    }

}
```