---
title: PDF에 이미지 또는 텍스트가 포함되어 있는지 확인
linktitle: 텍스트 및 이미지 존재 확인
type: docs
weight: 40
url: ko/net/find-whether-pdf-file-contains-images-or-text-only/
description: 이 주제는 PdfExtractor 클래스를 사용하여 PDF 파일에 이미지 또는 텍스트만 포함되어 있는지 찾는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 배경

PDF 파일은 텍스트와 이미지를 모두 포함할 수 있습니다. 때때로 사용자는 PDF 파일에 텍스트만 포함되어 있는지 아니면 이미지만 포함되어 있는지를 확인해야 할 수도 있습니다. 또한, 둘 다 포함되어 있는지 또는 아무것도 포함되어 있지 않은지도 확인할 수 있습니다.

{{% alert color="primary" %}}

다음 코드 스니펫은 이 요구 사항을 충족하는 방법을 보여줍니다.

{{% /alert %}}

```csharp
 public static void CheckIfPdfContainsTextOrImages()
{
    // 문서에서 추출한 텍스트를 저장할 MemoryStream 객체를 인스턴스화합니다.
    MemoryStream ms = new MemoryStream();
    // PdfExtractor 객체를 인스턴스화합니다.
    PdfExtractor extractor = new PdfExtractor();

    // 입력 PDF 문서를 추출기에 바인딩합니다.
    extractor.BindPdf(_dataDir + "FilledForm.pdf");
    // 입력 PDF 문서에서 텍스트를 추출합니다.
    extractor.ExtractText();
    // 추출한 텍스트를 텍스트 파일에 저장합니다.
    extractor.GetText(ms);
    // MemoryStream 길이가 1 이상인지 확인합니다.

    bool containsText = ms.Length >= 1;

    // 입력 PDF 문서에서 이미지를 추출합니다.
    extractor.ExtractImage();

    // while 루프에서 HasNextImage 메서드를 호출합니다. 이미지가 끝나면 루프가 종료됩니다.
    bool containsImage = extractor.HasNextImage();

    // 이제 이 PDF가 텍스트만 또는 이미지만 포함되어 있는지 확인합니다.

    if (containsText && !containsImage)
        Console.WriteLine("PDF에는 텍스트만 포함되어 있습니다.");
    else if (!containsText && containsImage)
        Console.WriteLine("PDF에는 이미지만 포함되어 있습니다.");
    else if (containsText && containsImage)
        Console.WriteLine("PDF에는 텍스트와 이미지가 모두 포함되어 있습니다.");
    else if (!containsText && !containsImage)
        Console.WriteLine("PDF에는 텍스트와 이미지가 모두 포함되어 있지 않습니다.");
}
```