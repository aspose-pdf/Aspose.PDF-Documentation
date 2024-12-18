---
title: PDF 파일에서 텍스트 교체
type: docs
weight: 40
url: /ko/java/replace-text/
description: 이 섹션은 PDF와 관련된 인기 있는 작업을 위한 도구 세트인 Aspose.PDF Facades를 사용하여 텍스트를 교체하는 방법을 설명합니다.
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 기존 PDF 파일에서 텍스트 교체하기 (facades)

기존 PDF 파일에서 텍스트를 교체하기 위해서는 [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 클래스의 객체를 생성하고, bindPdf 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, [replaceText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-) 메서드를 호출해야 합니다. 업데이트된 PDF 파일은 [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 클래스의 save 메서드를 사용하여 저장해야 합니다. 다음 코드 스니펫은 기존 PDF 파일에서 텍스트를 교체하는 방법을 보여줍니다.

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

        // 출력 파일 저장
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```


원본 문서에서 어떻게 보이는지 확인하세요:

![Replace Text](replace_text1.png)

텍스트를 교체한 후 결과를 확인하세요:

![Result of replacing Text](replace_text2.png)

두 번째 예에서는 텍스트를 교체하는 것 외에도 글꼴 크기를 증가시키거나 감소시킬 수 있는 방법을 볼 수 있습니다:

```java
public static void ReplaceText02(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        editor.replaceText("Value", "Label", 12);

        // 출력 파일 저장
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```

텍스트 작업을 위한 더 고급의 가능성을 위해, 우리는 [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) 메소드를 사용할 것입니다. 이 메소드를 사용하여 텍스트를 굵게, 기울임꼴, 색상 변경 등을 할 수 있습니다.

```java
public static void ReplaceText03(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        TextState textState = new TextState();
        textState.setFontSize(12);
        editor.replaceText("Value", "Label", textState);

        // 출력 파일 저장
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    

```


문서의 지정된 모든 텍스트를 교체해야 하는 경우, 다음 코드 스니펫을 사용하십시오. 즉, 교체할 텍스트가 발견되는 곳마다 텍스트가 교체될 것이며, 이러한 교체의 수를 세게 됩니다.

```java
    public static void ReplaceText04()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("Value", "Label")) count++;

        System.out.println(count+" occurrences have been replaced.");

        // 출력 파일 저장
        editor.save(_dataDir + "PdfContentEditorDemo04.pdf");
    }
```

![모든 텍스트 교체](replace_text3.png)

다음 코드 스니펫은 문서의 특정 페이지에서 모든 텍스트 교체를 수행하는 방법을 보여줍니다.

```java
    public static void ReplaceText05()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("9999", 2, "ABCDE")) count++;
        System.out.println(count+" occurrences have been replaced.");

        // 출력 파일 저장
        editor.save(_dataDir + "PdfContentEditorDemo05.pdf");
    }
```


다음 코드 스니펫에서는 주어진 숫자를 필요한 문자로 교체하는 방법을 보여드립니다.

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

        // 출력 파일 저장
        editor.save(_dataDir + "PdfContentEditorDemo06.pdf");
    }

}
```