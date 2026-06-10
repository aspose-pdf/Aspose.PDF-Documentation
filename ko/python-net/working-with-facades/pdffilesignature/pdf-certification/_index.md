---
title: PDF 인증
type: docs
weight: 30
url: /ko/python-net/pdf-certification/
description: 문서 수정 권한이 다른 PDF 파일 서명과 DocMDP 서명을 사용하여 Python에서 PDF 문서를 인증하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 DocMDP 권한으로 PDF 문서 인증하기
Abstract: 이 문서에서는 PDFFileSignature 파사드를 사용하여.NET을 통해 파이썬용 Aspose.PDF PDF 문서를 인증하는 방법을 설명합니다.DOCMDP 서명을 만들고, 양식 작성 권한으로 인증을 적용하고, 변경 없는 인증 수준으로 문서를 잠그는 방법을 보여줍니다.
---

.NET을 통한 Python용 Aspose.PDF 를 사용하면 다음과 같이 문서 수준 서명을 적용하여 PDF 문서를 인증할 수 있습니다. [PDF 파일 서명](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/).인증은 문서가 인증된 후 허용되는 변경 사항이 있을 경우 이를 정의한다는 점에서 표준 승인 서명과 다릅니다.

이 문서에서는 두 가지 일반적인 인증 워크플로를 보여줍니다.

1. PDF를 인증하고 인증 후 양식 작성을 허용합니다.
1. PDF를 인증하고 추가 변경을 방지하세요.

## 양식 작성을 위한 PDF 인증

문서를 인증된 상태로 유지해야 하지만 사용자가 여전히 대화형 양식을 작성하거나 파일에 계속 서명해야 하는 경우 이 방법을 사용하십시오. `FILLING_IN_FORMS` 권한 수준은 인증을 유효하게 유지하면서 이러한 통제된 변경을 허용합니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def certify_pdf_with_mdp_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.FILLING_IN_FORMS,
            reason="Certified for form filling and signing",
        )
        pdf_signature.certify(
            1,
            "Certified for form filling and signing",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## 변경이 허용되지 않는 문서 수준 인증 적용

인증 후에도 인증된 문서가 변경되지 않은 상태로 남아 있어야 하는 경우 이 모드를 사용하십시오. `NO_CHANGES` 권한 수준은 나중에 수정하면 인증 상태가 무효화되는 최종 PDF에 적합합니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_document_level_certification(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.NO_CHANGES,
            reason="Certified with no further changes allowed",
        )
        pdf_signature.certify(
            1,
            "Certified with no further changes allowed",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
