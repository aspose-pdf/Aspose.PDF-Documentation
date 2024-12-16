---
title: Substituir Texto em Arquivo PDF
type: docs
weight: 40
url: /pt/java/replace-text/
description: Esta seção explica como substituir texto com Aspose.PDF Facades - um conjunto de ferramentas para operações populares com PDF.
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Substituir Texto em um Arquivo PDF Existente (facades)

Para substituir texto em um arquivo PDF existente, você precisa criar um objeto da classe [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor), e vincular um arquivo PDF de entrada usando o método bindPdf. Depois disso, você precisa chamar o método [replaceText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-).
Você precisa salvar o arquivo PDF atualizado usando o método save da classe [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor). O trecho de código a seguir mostra como substituir texto em um arquivo PDF existente.

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

        // salvar o arquivo de saída
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```


Confira como fica no documento original:

![Substituir Texto](replace_text1.png)

E confira o resultado após substituir o texto:

![Resultado da substituição de Texto](replace_text2.png)

No segundo exemplo, você verá como, além de substituir o texto, também pode aumentar ou diminuir o tamanho da fonte:

```java
public static void ReplaceText02(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        editor.replaceText("Value", "Label", 12);

        // salvar o arquivo de saída
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```

Para possibilidades mais avançadas de trabalhar com nosso texto, usaremos o método [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState). Com este método, podemos deixar o texto em negrito, itálico, colorido, e assim por diante.

```java
public static void ReplaceText03(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        TextState textState = new TextState();
        textState.setFontSize(12);
        editor.replaceText("Value", "Label", textState);

        // salvar o arquivo de saída
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    

```


Caso você precise substituir todo o texto especificado no documento, use o seguinte trecho de código. Ou seja, a substituição do texto ocorrerá sempre que o texto especificado para substituição for encontrado, e também contará o número de tais substituições.

```java
    public static void ReplaceText04()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("Value", "Label")) count++;

        System.out.println(count+" ocorrências foram substituídas.");

        // salvar o arquivo de saída
        editor.save(_dataDir + "PdfContentEditorDemo04.pdf");
    }
```

![Substituir todo o Texto](replace_text3.png)

O seguinte trecho de código mostra como fazer todas as substituições de texto, mas em uma página específica do seu documento.

```java
    public static void ReplaceText05()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("9999", 2, "ABCDE")) count++;
        System.out.println(count+" ocorrências foram substituídas.");

        // salvar o arquivo de saída
        editor.save(_dataDir + "PdfContentEditorDemo05.pdf");
    }
```


No próximo trecho de código, mostraremos como substituir, por exemplo, um determinado número pelas letras que precisamos.

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

        // salvar o arquivo de saída
        editor.save(_dataDir + "PdfContentEditorDemo06.pdf");
    }

}
```