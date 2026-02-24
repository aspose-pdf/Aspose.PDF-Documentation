---
title: Python에서 PDF/x를 PDF 형식으로 변환하기
linktitle: PDF/x를 PDF 형식으로 변환하기
type: docs
weight: 120
url: /ko/python-net/convert-pdf_x-to-pdf/
lastmod: "2025-09-27"
description: 이 주제에서는 Aspose.PDF for Python via .NET를 사용하여 PDF/x를 PDF 형식으로 변환하는 방법을 보여줍니다.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: PDF/x를 PDF 형식으로 변환하는 방법
Abstract: 이 문서는 Aspose.PDF for Python을 사용하여 PDF/UA 및 PDF/A를 PDF 파일로 변환하는 포괄적인 가이드를 제공합니다.
---

**PDF/x를 PDF 형식으로 변환한다는 것은 PDF/UA 및 PDF/A를 PDF 파일로 변환하는 기능을 의미합니다.**

## PDF/A를 PDF로 변환

1. 'ap.Document'를 사용하여 PDF 문서를 로드합니다.
1. 'remove_pdfa_compliance()'를 호출하여 PDF/A와 관련된 모든 규정 설정 및 메타데이터를 제거합니다.
1. 결과 PDF를 출력 경로에 저장합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## PDF/UA 규정 제거

이 함수는 두 단계 변환 프로세스를 보여줍니다: 먼저 PDF/UA(Universal Accessibility) 규정을 제거하고, 그 다음 결과 PDF를 접근성 및 의미 구조를 위한 자동 태깅이 포함된 PDF/A-1B 형식으로 변환합니다.

1. 'ap.Document()'를 사용하여 PDF 문서를 로드합니다.
1. 'document.remove_pdfa_compliance()'를 호출하여 PDF/A 제한이나 규정 설정을 제거합니다.
1. 수정된 PDF를 'path_outfile'에 저장합니다.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```
