---
title: PDF에서 XFDF로 주석 평탄화
type: docs
weight: 40
url: /ko/net/flatten-annotation/
description: 이 섹션은 Aspose.PDF Facades를 사용하여 PDF 파일에서 XFDF로 주석을 내보내는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

평탄화 프로세스는 주석이 문서에서 제거될 때 그 시각적 표현이 그대로 유지되는 것을 의미합니다. 평탄화된 주석은 여전히 ​​보이지만 사용자나 앱에서 더 이상 편집할 수 없습니다. 예를 들어, 문서에 주석을 영구적으로 적용하거나 주석을 표시할 수 없는 뷰어에게 주석을 표시하는 데 사용할 수 있습니다. 명시적으로 지정하지 않으면 내보내기는 모든 주석을 있는 그대로 유지합니다.

이 옵션이 선택되면 내보낸 PDF에 PDF 표준 주석으로 주석이 포함됩니다.

다음 코드 조각에서 사용된 [flatteningAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations) 메서드를 확인하세요.

```csharp
public static void Flattening()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            FlattenSettings flattenSettings = new FlattenSettings
            {
                ApplyRedactions = true,
                CallEvents = false,
                HideButtons = true,
                UpdateAppearances = true
            };
            annotationEditor.FlatteningAnnotations(flattenSettings);
            annotationEditor.Save(_dataDir + "FlattenAnnotation.pdf");
        }
```