---
title: PDF 파일에서 주석을 XFDF로 변환 (facades)
type: docs
weight: 40
url: /ko/java/flatten-annotation/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일에서 주석을 XFDF로 내보내는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

평탄화 과정은 주석이 문서에서 제거될 때, 그 시각적 표현은 그대로 유지되는 것을 의미합니다. 평탄화된 주석은 여전히 보이지만 사용자가나 앱에서 더 이상 편집할 수 없습니다. 예를 들어, 문서에 주석을 영구적으로 적용하거나, 주석을 표시할 수 없는 뷰어에게 주석을 보이도록 할 때 사용할 수 있습니다. 만약 명시되지 않으면, 내보내기는 모든 주석을 원래 상태로 유지합니다.

이 옵션이 선택되면, 주석은 내보낸 PDF에 PDF 표준 주석으로 포함됩니다.

다음 코드 스니펫에서 사용된 [flatteningAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#flatteningAnnotations--) 메서드를 확인하십시오.

```java
public static void Flattening() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf"); // PDF 파일을 바인딩합니다.
        FlattenSettings flattenSettings = new FlattenSettings();
        flattenSettings.setApplyRedactions(true); // 수정 사항을 적용합니다.
        flattenSettings.setCallEvents(false); // 이벤트 호출을 설정합니다.
        flattenSettings.setHideButtons(true); // 버튼을 숨깁니다.
        flattenSettings.setUpdateAppearances(true); // 외관을 업데이트합니다.
        annotationEditor.flatteningAnnotations(flattenSettings);
        annotationEditor.save(_dataDir + "FlattenAnnotation.pdf"); // PDF 파일을 저장합니다.
    }
```