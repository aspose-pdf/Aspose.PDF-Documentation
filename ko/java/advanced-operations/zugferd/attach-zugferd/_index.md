---
title: PDF/3-A 준수 PDF 만들기 및 ZUGFeRD 송장 Java에 첨부하기
linktitle: PDF에 ZUGFeRD 첨부
type: docs
weight: 10
url: /ko/java/attach-zugferd/
description: Aspose.PDF for Java에서 ZUGFeRD가 포함된 PDF 문서를 생성하는 방법을 학습하세요
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF에 ZUGFeRD 첨부

PDF에 ZUGFeRD를 첨부하기 위해 다음 단계를 권장합니다:

* 입력 및 출력 PDF 파일이 위치한 폴더를 가리키는 경로 변수를 정의합니다.
* 처리될 PDF 파일의 경로를 저장하는 문자열 변수 경로를 정의합니다. `Paths.get` 메소드를 사용하여 전체 경로의 부분을 결합합니다.
* 경로 변수에서 생성된 Document 객체가 문이 끝난 후 자동으로 닫히도록 보장하는 try-with-resources 문을 만듭니다. Document 객체는 수정 및 저장될 PDF 문서를 나타냅니다.

* ZUGFeRD 표준에 부합하는 송장 메타데이터를 포함하는 다른 파일의 경로와 설명을 제공하여 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) 객체를 생성합니다.
 * 파일 사양 객체에 설명, MIME 유형 및 AFrelationship과 같은 속성을 추가합니다. AFrelationship은 포함된 파일이 PDF 문서와 어떻게 관련되어 있는지를 나타냅니다. 이 경우 "대체"로 설정되어 있으며, 포함된 파일이 PDF 콘텐츠의 대체 표현임을 의미합니다.
* 문서의 포함된 파일 컬렉션에 파일 사양 객체를 추가합니다. 파일 이름은 "factor-x.xml"과 같이 ZUGFeRD 표준에 맞게 지정해야 합니다.
* 전자 문서의 장기 보존을 보장하는 PDF의 하위 집합인 PDF/A-3U 형식으로 문서를 변환합니다. PDF/A-3U는 PDF 문서에 모든 형식의 파일을 포함할 수 있습니다.
* 변환된 문서를 새 PDF 파일로 저장합니다 (예: "ZUGFeRD-res.pdf").
* try-with-resources 문을 닫고 Document 객체를 해제합니다.

```java
String _dataDir = "/home/aspose/pdf-examples/Samples/";
String path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-test.pdf").toString();
try (Document document = new Document(path)) {
    String description = "ZUGFeRD 표준에 맞는 송장 메타데이터";
    path = Paths.get(_dataDir, "ZUGFeRD", "factur-x.xml").toString();
    FileSpecification fileSpecification = new FileSpecification(path.toString(), description);
    fileSpecification.setMIMEType("text/xml");
    fileSpecification.setAFRelationship(com.aspose.pdf.AFRelationship.Alternative);

    // 문서의 첨부 파일 컬렉션에 첨부 파일 추가
    document.getEmbeddedFiles().add(fileSpecification);
    path = Paths.get(_dataDir, "ZUGFeRD", "log.xml").toString();
    document.convert(path, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
    path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-res.pdf").toString();
    document.save(path);
}
```