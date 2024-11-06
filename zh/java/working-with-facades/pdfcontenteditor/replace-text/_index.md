---

title: 在PDF文件中替换文本  
type: docs  
weight: 40  
url: zh/java/replace-text/  
description: 本节说明如何使用Aspose.PDF Facades替换文本——一个用于PDF常见操作的工具集。  
lastmod: "2021-06-24"  
sitemap:  
    changefreq: "monthly"  
    priority: 0.7  
---

## 在现有PDF文件中替换文本 (facades)

为了在现有的PDF文件中替换文本，您需要创建一个[pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)类的对象，并使用bindPdf方法绑定一个输入PDF文件。之后，您需要调用[replaceText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-)方法。  
您需要使用[pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)类的save方法保存更新后的PDF文件。以下代码片段向您展示如何在现有PDF文件中替换文本。

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

        // 保存输出文件
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```


检查它在原始文档中的样子：

![Replace Text](replace_text1.png)

并检查替换文本后的结果：

![Result of replacing Text](replace_text2.png)

在第二个示例中，您将看到除了替换文本之外，还可以增加或减少字体大小：

```java
public static void ReplaceText02(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        editor.replaceText("Value", "Label", 12);

        // 保存输出文件
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```

对于处理文本的更多高级功能，我们将使用[TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState)方法。使用此方法，我们可以使文本加粗、斜体、着色等。

```java
public static void ReplaceText03(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        TextState textState = new TextState();
        textState.setFontSize(12);
        editor.replaceText("Value", "Label", textState);

        // 保存输出文件
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```


在需要替换文档中所有指定文本的情况下，请使用以下代码片段。也就是说，文本的替换将发生在遇到指定替换文本的任何地方，并且还将计算这种替换的次数。

```java
    public static void ReplaceText04()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("Value", "Label")) count++;

        System.out.println(count+" 次出现已被替换。");

        // 保存输出文件
        editor.save(_dataDir + "PdfContentEditorDemo04.pdf");
    }
```

![替换所有文本](replace_text3.png)

以下代码片段显示了如何进行所有文本替换，但在文档的特定页面上。

```java
    public static void ReplaceText05()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("9999", 2, "ABCDE")) count++;
        System.out.println(count+" 次出现已被替换。");

        // 保存输出文件
        editor.save(_dataDir + "PdfContentEditorDemo05.pdf");
    }
```


在下一个代码片段中，我们将展示如何将给定的数字替换为我们需要的字母。

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

        // 保存输出文件
        editor.save(_dataDir + "PdfContentEditorDemo06.pdf");
    }

}
```