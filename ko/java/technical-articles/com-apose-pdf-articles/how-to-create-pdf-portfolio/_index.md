---
title: PDF 포트폴리오 생성 방법
type: docs
weight: 10
url: /ko/java/how-to-create-pdf-portfolio/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

PDF 포트폴리오는 다양한 소스(예: PDF, Word, Excel, JPEG 파일)의 콘텐츠를 하나의 통합된 컨테이너로 결합할 수 있게 해줍니다. 원본 파일은 개별 정체성을 유지하지만 PDF 포트폴리오 파일로 조합됩니다. 사용자는 각 구성 요소 파일을 다른 구성 요소 파일과 독립적으로 열고, 읽고, 편집하고, 서식을 지정할 수 있습니다.

Aspose.PDF for Java는 Document 클래스를 사용하여 PDF 포트폴리오 문서를 생성할 수 있습니다. 개별 파일을 FileSpecification 객체에 로드하고 add(...) 메서드를 사용하여 Document.Collection 객체에 추가합니다. 파일이 추가되면 Document 클래스의 save(..) 메서드를 사용하여 포트폴리오 문서를 생성합니다.

{{% /alert %}}

## 코드 샘플

다음 예제는 Microsoft XPS 파일, Word 문서, PDF 및 이미지 파일을 사용하여 PDF 포트폴리오를 생성합니다.

**Aspose.PDF로 생성된 PDF 포트폴리오**

![todo:image_alt_text](how-to-create-pdf-portfolio_1.png)

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "CreatePDFPortfolio.java" >}}