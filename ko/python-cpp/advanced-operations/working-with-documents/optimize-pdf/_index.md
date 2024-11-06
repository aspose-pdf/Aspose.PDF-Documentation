---
title: Python에서 PDF 크기 최적화, 압축 또는 줄이기
linktitle: PDF 최적화
type: docs
weight: 30
url: ko/python-cpp/optimize-pdf/
keywords: "optimize pdf Python"
description: PDF 파일 최적화, 모든 이미지 축소, PDF 크기 줄이기, 폰트 임베드 제거, 사용되지 않는 객체 제거를 Python으로 합니다.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDF 문서는 때때로 추가 데이터를 포함할 수 있습니다. PDF 파일의 크기를 줄이면 네트워크 전송 및 저장을 최적화하는 데 도움이 됩니다. 이는 특히 웹 페이지에 게시하거나, 소셜 네트워크에서 공유하거나, 이메일로 전송하거나, 저장소에 보관할 때 유용합니다. PDF를 최적화하기 위해 몇 가지 기법을 사용할 수 있습니다:

- 온라인 브라우징을 위한 페이지 콘텐츠 최적화
- 모든 이미지 축소 또는 압축
- 페이지 콘텐츠 재사용 활성화
- 중복 스트림 병합
- 폰트 임베드 제거
- 사용되지 않는 객체 제거
- 평탄화된 양식 필드 제거
- 주석 제거 또는 평탄화

{{% alert color="primary" %}}

최적화 방법에 대한 자세한 설명은 최적화 방법 개요 페이지에서 찾을 수 있습니다.

{{% /alert %}}

## 웹을 위한 PDF 문서 최적화

웹을 위한 최적화 또는 선형화는 PDF 파일을 웹 브라우저를 사용하여 온라인으로 탐색할 수 있도록 만드는 프로세스를 의미합니다. 파일을 웹 디스플레이에 맞게 최적화하려면 다음을 수행하십시오:

다음 코드 스니핏은 웹을 위해 PDF 문서를 최적화하는 방법을 보여줍니다.

```python

    import AsposePDFPythonWrappers as ap

    # 문서 디렉터리의 경로입니다.
    dataDir = "..."

    # 문서 열기
    document = ap.Document(dataDir + "OptimizeDocument.pdf")

    # 웹을 위해 최적화
    document.optimize()

    dataDir = dataDir + "OptimizeDocument_out.pdf"

    # 출력 문서 저장
    document.Save(dataDir)
```