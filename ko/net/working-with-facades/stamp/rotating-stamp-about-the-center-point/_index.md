---
title: 중심점을 기준으로 도장을 회전시키기
type: docs
weight: 10
url: ko/net/rotating-stamp-about-the-center-point/
description: 이 섹션에서는 Stamp 클래스를 사용하여 중심점을 기준으로 도장을 회전시키는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)는 [Aspose.PDF for .NET](/pdf/net/)에서 기존 PDF 파일에 도장을 추가할 수 있게 합니다. 때때로, 사용자는 도장을 회전시킬 필요가 있습니다. 이 기사에서는 도장을 중심점을 기준으로 회전시키는 방법을 살펴보겠습니다.

{{% /alert %}}

## 구현 세부사항

[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스는 PDF 파일에 워터마크를 추가할 수 있게 합니다. 이미지를 스탬프로 추가하려면 [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1) 메서드를 사용할 수 있습니다. [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) 메서드는 추가된 스탬프의 원점을 설정할 수 있게 해줍니다. 이 원점은 스탬프의 좌하단 좌표입니다. 또한 [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize) 메서드를 사용하여 이미지의 크기를 설정할 수 있습니다.

이제 스탬프의 중심을 기준으로 스탬프를 회전시키는 방법을 봅니다. [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스는 Rotation이라는 속성을 제공합니다. 이 속성은 스탬프 콘텐츠의 회전을 0에서 360까지 설정하거나 가져옵니다. 우리는 0에서 360까지의 회전 값을 지정할 수 있습니다. 회전 값을 지정함으로써 스탬프를 중심점에 대해 회전시킬 수 있습니다. 만약 Stamp가 Stamp 타입의 객체라면 회전 값은 aStamp.Rotation = 90으로 지정할 수 있습니다. 이 경우 스탬프는 스탬프 콘텐츠의 중심을 기준으로 90도 회전됩니다. 다음 코드 스니펫은 스탬프를 중심점에 대해 회전시키는 방법을 보여줍니다:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-RotatingStamp-RotatingStamp.cs" >}}