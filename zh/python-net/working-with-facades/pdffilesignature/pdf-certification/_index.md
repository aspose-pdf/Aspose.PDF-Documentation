---
title: PDF 认证
type: docs
weight: 30
url: /zh/python-net/pdf-certification/
description: 了解如何在 Python 中使用 PdfFileSignature 和 DocMDPSignature 通过不同的文档修改权限对 PDF 文档进行认证。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用 DocMDP 权限对 PDF 文档进行认证
Abstract: 本文说明了如何使用 Aspose.PDF for Python via .NET 通过 PdfFileSignature 门面对 PDF 文档进行认证。它展示了如何创建 DocMDPSignature、使用填写表单权限进行认证，以及使用无更改认证级别锁定文档。
---

Aspose.PDF for Python via .NET 允许您通过应用文档级签名来认证 PDF 文档， [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/)。认证不同于标准批准签名，因为它定义了在文档已被认证后，是否允许进行哪些更改。

本文演示了两种常见的认证工作流：

1. 对 PDF 进行认证，并在认证后允许填写表单。
1. 对 PDF 进行认证，并阻止任何进一步的更改。

## 对 PDF 进行表单填写认证

当文档应保持已认证状态，但用户仍需完成交互式表单或继续对文件进行签名时，请使用此方法。该 `FILLING_IN_FORMS` 权限级别允许这些受控更改，同时保持认证有效。

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

## 应用文档级别的认证，且不允许更改

使用此模式，当经认证的文档在认证后必须保持不变时。The `NO_CHANGES` 权限级别适用于已完成的 PDF，在以后进行任何修改时应使认证状态失效。

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
