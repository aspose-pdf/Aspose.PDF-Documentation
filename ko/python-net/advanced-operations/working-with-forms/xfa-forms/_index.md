---
title: XFA 양식 사용
linktitle: XFA 양식
type: docs
weight: 20
url: /ko/python-net/xfa-forms/
description: .NET API를 통한 파이썬용 Aspose.PDF 기능을 사용하면 PDF 문서에서 XFA 및 XFA 아크로폼 필드를 사용할 수 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## XFA를 아크로폼으로 변환

{{% alert color="primary" %}}

온라인 체험하기
다음 링크에서 Aspose.PDF 변환의 품질을 확인하고 온라인으로 결과를 볼 수 있습니다. [products.aspose.app/pdf/xfa/아크로폼](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

다음 코드 스니펫은 동적 XFA (XML 양식 아키텍처) 양식을 표준 AcroForm으로 변환하는 방법을 보여줍니다.

**주요 단계는 다음과 같습니다.**

1. 입력 PDF 문서를 로드합니다.
1. 양식 유형을 스탠다드로 변경합니다.
1. 변환된 PDF를 새 파일에 저장

이러한 변환을 통해 다양한 PDF 리더 및 응용 프로그램에서 호환성과 일관된 양식 처리를 개선할 수 있습니다.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_dynamic_xfa_to_acroform(infile: str, outfile: str):
    """Convert dynamic XFA form to standard AcroForm."""
    with ap.Document(infile) as document:
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```

## 무시 니즈 렌더링 사용

이 예제에서는 파이썬용 Aspose.PDF 를 사용하여 동적 XFA 양식을 표준 AcroForm으로 변환하는 방법을 보여줍니다.코드는 입력 PDF에 XFA 양식이 포함되어 있는지 확인하고 필요한 경우 렌더링을 재정의합니다.그런 다음 양식 유형을 STANDARD로 설정하고 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_xfa_form_with_ignore_needs_rendering(infile: str, outfile: str):
    """Convert XFA form ignoring needs rendering flag."""
    with ap.Document(infile) as document:
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```
