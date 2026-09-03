---
title: 제출 플래그 설정
linktitle: 제출 플래그 설정
type: docs
weight: 40
url: /java/set-submit-flag/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 PDF 양식 버튼에 제출 플래그를 설정하는 방법에 대한 현재 Java 적용 범위를 검토하세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java FormEditor 예제에서 플래그 구성 제출
Abstract: 현재 Java 샘플 세트는 제출 플래그 구성을 별도의 독립 실행형 예제 메소드로 노출하지 않습니다. 대신 `setSubmitUrl(...)`의 제출 URL 구성과 함께 시연됩니다.
---
Java `FormEditorExamples.setSubmitUrl(...)` 메소드에는 다음이 포함됩니다.


## 
제출 플래그 구성


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
버튼 필드의 제출 URL을 설정합니다.

3. 
필수 형식에 대한 제출 플래그를 설정하십시오.
4. 업데이트된 문서를 저장합니다.


```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```


이 저장소에서 제출 플래그를 구성하기 위한 소스 지원 Java 워크플로로 결합된 예제를 사용하세요.
