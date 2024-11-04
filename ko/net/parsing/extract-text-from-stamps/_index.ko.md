---
title: 도장에서 텍스트 추출하기 C#
type: docs
weight: 60
url: /net/extract-text-from-stamps/
description: Aspose.PDF for .NET의 특별 기능 사용 방법 배우기 - 도장 주석에서 텍스트 추출
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 도장 주석에서 텍스트 추출하기

Aspose.PDF for NET는 도장 주석에서 텍스트를 추출할 수 있습니다. PDF에서 도장 주석의 텍스트를 추출하기 위해 다음 단계를 사용할 수 있습니다.

1. `Document` 클래스 객체 생성
1. 페이지의 주석 목록에서 원하는 `Annotation` 가져오기
1. `TextAbsorber` 클래스의 새 객체 정의
1. TextAbsorber의 visit 메서드를 사용하여 텍스트 가져오기

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 함께 작동합니다.

```csharp
public static void ExtractText()
{
   Document document = new Document(_dataDir + "ExtractStampText.pdf");
   Annotation item = document.Pages[1].Annotations[1];
   if (item is StampAnnotation annot) {
         TextAbsorber ta = new TextAbsorber();
         XForm ap = annot.Appearance["N"];
         ta.Visit(ap);
         Console.WriteLine(ta.Text);
   }
}
```

