---
title: PDF 문서 비교
linktitle: PDF 비교 
type: docs
weight: 180
url: /ko/net/compare-pdf-documents/
description: 24.7 릴리스부터 PDF 문서의 내용을 주석 표시와 나란히 출력으로 비교할 수 있습니다
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aspose.PDF for .NET을 사용한 PDF 문서 비교

PDF 문서를 작업할 때 두 문서의 내용을 비교하여 차이점을 식별할 필요가 있는 경우가 있습니다. Aspose.PDF for .NET 라이브러리는 이를 위한 강력한 도구 세트를 제공합니다. 이 글에서는 몇 가지 간단한 코드 스니펫을 사용하여 PDF 문서를 비교하는 방법을 탐구합니다.

Aspose.PDF의 비교 기능을 사용하면 두 PDF 문서를 페이지별로 비교할 수 있습니다. 특정 페이지 또는 전체 문서를 비교할 수 있습니다. 결과 비교 문서는 차이점을 강조 표시하여 두 파일 간의 변경 사항을 쉽게 식별할 수 있도록 합니다.

### 특정 페이지 비교

첫 번째 코드 스니펫은 두 PDF 문서의 첫 페이지를 비교하는 방법을 보여줍니다.
첫 번째 코드 스니펫은 두 PDF 문서의 첫 페이지를 비교하는 방법을 보여줍니다.

단계:

1. 문서 초기화.
코드는 각각의 파일 경로(documentPath1 및 documentPath2)를 사용하여 두 PDF 문서를 초기화하는 것으로 시작됩니다. 경로는 현재 비어 있는 문자열로 지정되어 있지만, 실제로는 실제 파일 경로로 교체해야 합니다.
2. 비교 과정.
- 페이지 선택 - 비교는 각 문서의 첫 페이지('Pages[1]')로 제한됩니다.
- 비교 옵션:

'AdditionalChangeMarks = true' - 이 옵션은 추가 변경 표시기가 표시되도록 합니다. 이러한 표시기는 현재 비교 중인 페이지에 없더라도 다른 페이지에 존재할 수 있는 차이점을 강조 표시합니다.

'ComparisonMode = ComparisonMode.IgnoreSpaces' - 이 모드는 비교자에게 텍스트의 공백을 무시하고 단어 내의 변경 사항에만 초점을 맞추도록 지시합니다.
```cs
    string documentPath1 = "";
    string documentPath2= "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

### 전체 문서 비교

두 번째 코드 스니펫은 두 PDF 문서의 전체 내용을 비교하는 범위를 확장합니다.

단계:

1. 문서 초기화.
첫 번째 예제와 마찬가지로, 두 PDF 문서는 파일 경로로 초기화됩니다.
2. 비교 과정.
- 전체 문서 비교 - 첫 번째 스니펫과 달리, 이 코드는 두 문서의 전체 내용을 비교합니다.
- 비교 옵션 - 첫 번째 스니펫과 동일한 옵션을 사용하여 공백을 무시하고 추가 변경 마커가 표시됩니다.

3.
```cs
    string documentPath1 = "";
    string documentPath2 = "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1, document2, resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

이 코드 스니펫으로 생성된 비교 결과는 Adobe Acrobat과 같은 뷰어에서 열 수 있는 PDF 문서입니다. Adobe Acrobat에서 양면 보기를 사용하면 변경 사항을 나란히 볼 수 있습니다:

- 삭제된 내용 - 왼쪽 페이지에 표시됩니다.
- 삽입된 내용 - 오른쪽 페이지에 표시됩니다.

'AdditionalChangeMarks'를 'true'로 설정하면 현재 페이지에 표시되지 않은 다른 페이지의 변경 사항에 대한 마커도 볼 수 있습니다.

**Aspose.PDF for .NET**은 특정 페이지 또는 전체 문서를 비교할 때 강력한 도구를 제공합니다.
**Aspose.PDF for .NET**은 특정 페이지 또는 전체 문서를 비교할 필요가 있을 때 강력한 PDF 문서 비교 도구를 제공합니다.
