---
title: 텍스트 교체 - Facades
type: docs
weight: 40
url: /net/replace-text-facades/
description: 이 섹션은 PdfContentEditor 클래스를 사용하여 텍스트 - Facades를 작업하는 방법을 설명합니다.
lastmod: "2021-06-24"
draft: false
---

## 기존 PDF 파일에서 텍스트 교체

기존 PDF 파일에서 텍스트를 교체하려면 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그런 다음 [ReplaceText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index) 메서드를 호출해야 합니다. [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 기존 PDF 파일의 텍스트를 교체하는 방법을 보여줍니다.

```csharp
public static void ReplaceText01()
{
    PdfContentEditor editor = new PdfContentEditor();
    ditor.BindPdf(_dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label");

    // save the output file
    editor.Save(_dataDir + "PdfContentEditorDemo01.pdf");
    }
```

원본 문서에서 어떻게 보이는지 확인하세요:

![Replace Text](replace_text1.png)

텍스트를 교체한 후 결과를 확인하세요:

![Result of replacing Text](replace_text2.png)

두 번째 예제에서는 텍스트를 교체하는 것 외에도 글꼴 크기를 늘리거나 줄일 수 있는 방법을 볼 수 있습니다:
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

우리의 텍스트를 다루기 위한 더 고급적인 기능을 위해서는 [TextState](https://reference.aspose.com/pdf/net/aspose.pdf.text/textstate) 메서드를 사용할 것입니다. 이 메서드를 사용하면 텍스트를 굵게, 기울임꼴, 색상 적용 등으로 만들 수 있습니다.

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

문서에서 지정된 모든 텍스트를 교체해야 하는 경우, 다음 코드 스니펫을 사용하십시오. 즉, 지정된 텍스트를 교체할 텍스트가 발견되는 모든 곳에서 텍스트 교체가 이루어지고, 그러한 교체의 횟수도 계산됩니다.

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

![모든 텍스트 교체](replace_text3.png)

다음 코드 스니펫은 문서의 특정 페이지에서 모든 텍스트 교체를 수행하는 방법을 보여줍니다.

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
다음 코드 스니펫에서는 예를 들어 주어진 숫자를 우리가 필요한 문자로 교체하는 방법을 보여줍니다.

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
        // 출력 파일 저장
        editor.Save(_dataDir + "PdfContentEditorDemo06.pdf");
    }
```