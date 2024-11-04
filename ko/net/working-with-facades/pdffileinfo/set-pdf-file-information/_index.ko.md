---
title: PDF 파일 정보 설정
type: docs
weight: 40
url: /net/set-pdf-file-information/
description: 이 섹션은 Aspose.PDF Facades를 사용하여 PDF 파일 정보를 설정하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

[PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) 클래스는 PDF 파일의 파일별 정보를 설정할 수 있게 해줍니다. [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) 클래스의 객체를 생성한 후, Author, Title, Keyword, Creator 등과 같은 다양한 파일별 속성을 설정합니다. 마지막으로, [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) 객체의 [SaveNewInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) 메소드를 사용하여 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일 정보를 설정하는 방법을 보여줍니다.

```csharp
 public static void SetPdfInfo()
        {
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf")
            {
                // Set PDF information
                Author = "Aspose",
                Title = "Hello World!",
                Keywords = "Peace and Development",
                Creator = "Aspose"
            };
            // Save updated file
            fileInfo.SaveNewInfo(_dataDir + "SetFileInfo_out.pdf");
        }
```

## Set Meta Info

[SetMetaInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) 메서드는 정보를 추가할 수 있게 해줍니다. 우리의 예제에서는 필드를 추가했습니다. 다음 코드 스니펫을 확인하세요:

```csharp
 public static void SetMetaInfo()
        {
            // PdfFileInfo 객체의 인스턴스 생성
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "sample.pdf");

            // 신규 고객 속성을 메타 정보로 설정
            fInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

            // 업데이트된 파일 저장
            fInfo.SaveNewInfo(_dataDir + "SetMetaInfo_out.pdf");
```