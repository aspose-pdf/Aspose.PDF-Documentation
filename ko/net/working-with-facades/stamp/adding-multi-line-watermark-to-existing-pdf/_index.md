---
title: 여러 줄 워터마크 추가
type: docs
weight: 10
url: ko/net/adding-multi-line-watermark-to-existing-pdf/
description: 이 섹션에서는 FormattedText 클래스를 사용하여 기존 PDF에 여러 줄 워터마크를 추가하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

많은 사용자가 여러 줄 텍스트로 PDF 문서에 스탬프를 찍고 싶어합니다. 그들은 보통 `\n` 및 `<br>`을 사용하려고 하지만 이러한 유형의 문자는 Aspose.Pdf.Facades 네임스페이스에서 지원되지 않습니다. 따라서 이를 가능하게 하기 위해 Aspose.Pdf.Facades 네임스페이스의 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 클래스에 [AddNewLineText()](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index)라는 다른 메서드를 추가했습니다.

{{% /alert %}}

## 구현

기존 PDF에 여러 줄 워터마크를 추가하기 위해 다음 코드 조각을 참조하십시오.

```csharp

// 스탬프 객체 인스턴스화
Stamp logoStamp = new Stamp();

// FormattedText 클래스의 객체 인스턴스화
FormattedText formatText = new FormattedText("Hello World!",
System.Drawing.Color.FromArgb(180, 0, 0), FontStyle.TimesItalic, EncodingType.Winansi, false, 50);

// 스탬프에 다른 줄 추가
formatText.AddNewLineText("Good Luck");
// PDF에 로고 바인딩
logoStamp.BindLogo(formatText);
```
```