---
title: Aspose.PDF for Java 9.7.1의 공용 API 변경 사항
type: docs
weight: 80
url: /ko/java/public-api-changes-in-aspose-pdf-for-java-9-7-1/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

이 페이지는 [Aspose.PDF for Java 9.7.1](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry600386.aspx)에서 도입된 공용 API 변경 사항을 나열합니다. 여기에는 새로운 공용 메서드와 사용되지 않는 메서드뿐만 아니라 Aspose.PDF for Java에서 기존 코드를 영향을 줄 수 있는 내부 동작의 변경 사항도 설명되어 있습니다. 회귀로 볼 수 있고 기존 동작을 수정하는 동작은 특히 중요하며 여기에서 문서화됩니다.

{{% /alert %}}

XML 데이터를 PDF 양식에 가져오기를 지원하기 위해 **com.aspose.facades.Form** 클래스에 **importXml(String inputXml)**라는 메서드가 추가되었습니다.

다음 메서드는 **com.aspose.pdf.generator.legacyxmlmodel.Heading** 클래스에서 변경되었습니다.

- isAutoSequence(boolean)이 setAutoSequence(boolean)로 변경되었습니다.

- isInList(boolean)이 setInList(boolean)로 변경되었습니다.

## 새로운 기능 구현

- [EPUB을 PDF로 변환](http://www.aspose.com/docs/display/pdfjava/Convert+EPUB+File+to+PDF+Format).
- [검색할 수 없는 PDF를 검색 가능한 PDF 문서로 변환](http://www.aspose.com/docs/display/pdfjava/Converting+non+searchable+PDF+to+searchable+PDF+document)