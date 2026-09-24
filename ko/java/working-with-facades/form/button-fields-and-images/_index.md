---
title: 버튼 필드 및 이미지
linktitle: 버튼 필드 및 이미지
type: docs
weight: 40
url: /java/button-fields-and-images/
description: Java용 Aspose.PDF의 Form Facade를 사용하여 PDF 양식의 버튼 필드에 이미지 모양을 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java의 PDF 버튼 필드에 이미지 모양 추가
Abstract: 이 기사에서는 Java용 Aspose.PDF의 Form Facade를 사용하여 PDF 양식을 바인딩하고, 이미지를 스트림으로 로드하고, 이미지 버튼 필드를 채우고, 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
`FormExamples.addImageAppearanceToButtonField(...)`의 Java 예제는 이미지 스트림으로 버튼 필드 모양을 업데이트하는 방법을 보여줍니다.



작업 흐름은 간단합니다.


- 
입력 PDF를 `form.bindPdf(...)`으로 바인딩

- 
`Files.newInputStream(...)`으로 이미지 파일을 엽니다.

- 
버튼 필드에 대해 `form.fillImageField(...)`으로 전화하세요.
- 업데이트된 PDF를 저장하세요

```java
public static void addImageAppearanceToButtonField(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        form.bindPdf(inputFile.toString());
        form.fillImageField("Image1_af_image", imageStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
