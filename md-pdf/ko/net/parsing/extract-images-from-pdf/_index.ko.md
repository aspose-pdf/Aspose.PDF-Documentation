---
title: PDF에서 이미지 추출 C#
linktitle: PDF에서 이미지 추출
type: docs
weight: 20
url: /net/extract-images-from-the-pdf-file/
description: Aspose.PDF for .NET을 사용하여 PDF에서 이미지 일부를 추출하는 방법
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

각 페이지의 [Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources) 컬렉션의 [Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images) 컬렉션에 이미지가 저장됩니다. 특정 페이지를 선택한 다음, 이미지 컬렉션에서 이미지의 특정 인덱스를 사용하여 이미지를 가져옵니다.

이미지의 인덱스는 [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage) 객체를 반환합니다. 이 객체는 추출한 이미지를 저장하는 데 사용할 수 있는 Save 메서드를 제공합니다. 다음 코드 스니펫은 PDF 파일에서 이미지를 추출하는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 함께 작동합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인할 수 있습니다.
```
```
// 완전한 예제와 데이터 파일은 다음을 참조하세요 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// 문서 열기
Document pdfDocument = new Document(dataDir+ "ExtractImages.pdf");

// 특정 이미지 추출
XImage xImage = pdfDocument.Pages[1].Resources.Images[1];

FileStream outputImage = new FileStream(dataDir + "output.jpg", FileMode.Create);

// 출력 이미지 저장
xImage.Save(outputImage, ImageFormat.Jpeg);
outputImage.Close();

dataDir = dataDir + "ExtractImages_out.pdf";

// 업데이트된 PDF 파일 저장
pdfDocument.Save(dataDir);
```
