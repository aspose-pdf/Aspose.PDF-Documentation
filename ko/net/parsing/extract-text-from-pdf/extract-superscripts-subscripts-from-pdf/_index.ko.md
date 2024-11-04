---
title: PDF에서 상첨자 및 하첨자 텍스트 추출
linktitle: 상첨자 및 하첨자 추출
type: docs
weight: 30
url: /net/extract-superscripts-subscripts-from-pdf/
description: 이 문서는 C#에서 Aspose.PDF를 사용하여 PDF에서 상첨자 및 하첨자 텍스트를 추출하는 다양한 방법을 설명합니다.
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 상첨자 및 하첨자 텍스트 추출

PDF 문서에서 텍스트를 추출하는 것은 일반적인 일입니다. 그러나 이러한 텍스트에서 추출할 때, 기술 문서와 기사에서 일반적인 **상첨자와 하첨자**가 표시되지 않을 수 있습니다. 하첨자 또는 상첨자는 텍스트의 정규 라인 아래나 위에 배치되는 문자, 숫자 또는 글자입니다. 일반적으로 나머지 텍스트보다 작습니다.

**하첨자와 상첨자**는 주로 공식, 수학적 표현, 화학 화합물의 사양에 사용됩니다.
**아래첨자와 윗첨자**는 대부분 수식, 수학적 표현, 화학 화합물의 사양에서 사용됩니다.
최근 릴리스 중 하나에서 **Aspose.PDF for .NET** 라이브러리는 PDF에서 아래첨자와 윗첨자 텍스트를 추출하는 기능을 추가했습니다.

**TextFragmentAbsorber** 클래스를 사용하면 찾은 텍스트로 무엇이든 할 수 있습니다. 즉, 전체 텍스트를 그대로 사용할 수 있습니다. 다음 코드 스니펫을 시도해 보세요:

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            writer.WriteLine(absorber.Text);
        }
```

또는 **TextFragments**를 개별적으로 사용하고 그것들로 다양한 조작을 수행할 수 있습니다. 예를 들어, 좌표나 크기에 따라 정렬합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.
다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                writer.Write(textFragment.Text);
            }
        }
```
