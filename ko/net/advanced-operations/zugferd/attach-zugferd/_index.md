---
title: PDF/3-A 준수 PDF 생성 및 ZUGFeRD 청구서 첨부 in C#
linktitle: PDF에 ZUGFeRD 첨부
type: docs
weight: 10
url: /ko/net/attach-zugferd/
description: Aspose.PDF for .NET에서 ZUGFeRD가 포함된 PDF 문서를 생성하는 방법을 알아봅니다.
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF에 ZUGFeRD 첨부

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

PDF에 ZUGFeRD를 첨부하기 위해 다음 단계를 따르는 것이 좋습니다:

* 입력 및 출력 PDF 파일이 위치한 폴더를 가리키는 경로 변수를 정의합니다.
* 경로에서 기존 PDF 파일(예: "ZUGFeRD-test.pdf")을 로드하여 문서 객체를 생성합니다.
* "factur-x.xml"이라는 다른 파일의 경로와 설명을 제공하여 [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) 객체를 생성합니다. 이 파일에는 ZUGFeRD 표준을 준수하는 청구서 메타데이터가 포함되어 있습니다.
* 파일 사양 객체에 설명, MIME 유형, AF 관계 등의 속성을 추가합니다.
* 파일 사양 객체에 설명, MIME 유형 및 AF 관계와 같은 속성을 추가합니다.
* 파일 사양 객체를 문서의 내장 파일 컬렉션에 추가합니다. 파일 이름은 ZUGFeRD 표준으로 지정해야 합니다. 예를 들어, "factur-x.xml".
* 문서를 PDF/A-3U 형식으로 변환합니다. PDF/A-3U는 전자 문서의 장기 보존을 보장하는 PDF의 하위 집합입니다. PDF/A-3U는 PDF 문서에 모든 형식의 파일을 포함할 수 있습니다.
* 변환된 문서를 새 PDF 파일로 저장합니다 (예: "ZUGFeRD-res.pdf").

```cs
var path = @"C:\Samples\ZUGFeRD\";

var document = new Aspose.Pdf.Document(Path.Combine(path,"ZUGFeRD-test.pdf"));
// 첨부 파일로 추가될 새 파일 설정
var description = "ZUGFeRD 표준에 따른 인보이스 메타데이터";
var fileSpecification = new Aspose.Pdf.FileSpecification(Path.Combine(path, "factur-x.xml"), description)
{
    Description = "Zugferd",
    MIMEType = "text/xml",
    AFRelationship = Aspose.Pdf.AFRelationship.Alternative
};
// 문서의 첨부 파일 컬렉션에 첨부 파일 추가
document.EmbeddedFiles.Add(fileSpecification);
document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.PDF_A_3U, Aspose.Pdf.ConvertErrorAction.Delete);
document.Save(Path.Combine(path, "ZUGFeRD-res.pdf"));
```
변환 메소드는 스트림, PDF 형식, 변환 오류 액션을 매개변수로 받습니다. 스트림 매개변수는 변환 로그를 저장하는 데 사용할 수 있습니다. 변환 오류 액션 매개변수는 변환 중에 오류가 발생했을 때 수행할 작업을 지정합니다. 이 경우 "삭제"로 설정되어 있어, PDF/A-3U 형식에 부합하지 않는 요소는 문서에서 삭제됩니다.
