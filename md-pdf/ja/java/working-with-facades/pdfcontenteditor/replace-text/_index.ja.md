---
title: PDFファイル内のテキストを置換
type: docs
weight: 40
url: /java/replace-text/
description: このセクションでは、PDFで人気の操作を行うためのツールセットであるAspose.PDF Facadesを使用してテキストを置換する方法を説明します。
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 既存のPDFファイル内のテキストを置換する（ファサード）

既存のPDFファイル内のテキストを置換するには、[pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)クラスのオブジェクトを作成し、bindPdfメソッドを使用して入力PDFファイルをバインドする必要があります。その後、[replaceText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-)メソッドを呼び出す必要があります。
[pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)クラスのsaveメソッドを使用して、更新されたPDFファイルを保存する必要があります。以下のコードスニペットは、既存のPDFファイル内のテキストを置換する方法を示しています。

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

        // 出力ファイルを保存
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```


元のドキュメントでどのように見えるか確認してください：

![Replace Text](replace_text1.png)

テキストを置き換えた後の結果を確認してください：

![Result of replacing Text](replace_text2.png)

2番目の例では、テキストを置き換えることに加えて、フォントサイズを増減する方法も確認できます：

```java
public static void ReplaceText02(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        editor.replaceText("Value", "Label", 12);

        // 出力ファイルを保存
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```

テキストを扱うためのより高度な可能性のために、[TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState)メソッドを使用します。このメソッドを使用すると、テキストを太字、斜体、色付きなどにすることができます。

```java
public static void ReplaceText03(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        TextState textState = new TextState();
        textState.setFontSize(12);
        editor.replaceText("Value", "Label", textState);

        // 出力ファイルを保存
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    

```


ドキュメント内のすべての指定されたテキストを置換する必要がある場合は、次のコードスニペットを使用してください。つまり、置換のために指定されたテキストが見つかるたびにテキストの置換が行われ、またそのような置換の回数もカウントされます。

```java
    public static void ReplaceText04()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("Value", "Label")) count++;

        System.out.println(count+" 回の置換が行われました。");

        // 出力ファイルを保存します
        editor.save(_dataDir + "PdfContentEditorDemo04.pdf");
    }
```

![すべてのテキストを置換](replace_text3.png)

次のコードスニペットは、ドキュメントの特定のページでテキスト置換を行う方法を示しています。

```java
    public static void ReplaceText05()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("9999", 2, "ABCDE")) count++;
        System.out.println(count+" 回の置換が行われました。");

        // 出力ファイルを保存します
        editor.save(_dataDir + "PdfContentEditorDemo05.pdf");
    }
```


次のコードスニペットでは、例えば、指定された数字を必要な文字に置き換える方法を示します。

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

        // 出力ファイルを保存
        editor.save(_dataDir + "PdfContentEditorDemo06.pdf");
    }

}
```