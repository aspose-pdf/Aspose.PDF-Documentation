---
title: Замена текста в PDF файле
type: docs
weight: 40
url: /ru/java/replace-text/
description: Этот раздел объясняет, как заменить текст с помощью Aspose.PDF Facades - набора инструментов для популярных операций с PDF.
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Замена текста в существующем PDF файле (facades)

Чтобы заменить текст в существующем PDF файле, вам нужно создать объект класса [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) и связать входной PDF файл с помощью метода bindPdf. После этого вам нужно вызвать метод [replaceText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-). Вам нужно сохранить обновленный PDF файл, используя метод save класса [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor). Следующий фрагмент кода показывает, как заменить текст в существующем PDF файле.

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

        // сохранить выходной файл
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```


Проверьте, как это выглядит в оригинальном документе:

![Заменить текст](replace_text1.png)

И проверьте результат после замены текста:

![Результат замены текста](replace_text2.png)

Во втором примере вы увидите, как, помимо замены текста, вы также можете увеличить или уменьшить размер шрифта:

```java
public static void ReplaceText02(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        editor.replaceText("Value", "Label", 12);

        // сохранить выходной файл
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```

Для более продвинутых возможностей работы с нашим текстом мы будем использовать метод [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState). С помощью этого метода мы можем сделать текст жирным, курсивным, цветным и так далее.

```java
public static void ReplaceText03(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        TextState textState = new TextState();
        textState.setFontSize(12);
        editor.replaceText("Value", "Label", textState);

        // сохранить выходной файл
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    

```


В случае, если вам нужно заменить весь указанный текст в документе, используйте следующий фрагмент кода. То есть замена текста произойдет везде, где будет встречаться текст, указанный для замены, и также будет подсчитано количество таких замен.

```java
    public static void ReplaceText04()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("Value", "Label")) count++;

        System.out.println(count+" occurrences have been replaced.");

        // сохранить выходной файл
        editor.save(_dataDir + "PdfContentEditorDemo04.pdf");
    }
```

![Заменить весь текст](replace_text3.png)

Следующий фрагмент кода показывает, как сделать все замены текста, но на определенной странице вашего документа.

```java
    public static void ReplaceText05()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("9999", 2, "ABCDE")) count++;
        System.out.println(count+" occurrences have been replaced.");

        // сохранить выходной файл
        editor.save(_dataDir + "PdfContentEditorDemo05.pdf");
    }
```


In the next code snippet, we will show how to replace, for example, a given number with the letters we need.

В следующем фрагменте кода мы покажем, как заменить, например, заданное число на нужные нам буквы.

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

        // save the output file
        // сохранить выходной файл
        editor.save(_dataDir + "PdfContentEditorDemo06.pdf");
    }

}
```