---
title: 파이썬으로 PDF 파일 보안 및 서명
linktitle: PDF 보안 및 로그인
type: docs
weight: 210
url: /ko/python-net/securing-and-signing/
description: 디지털 서명, 스마트 카드 및 문서 권한을 포함하여 Python에서 PDF 파일에 서명, 암호화, 암호 해독 및 보안을 설정하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 문서에 서명, 암호화, 암호 해독 및 보호
Abstract: 이 단원에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서를 보호하고 서명하는 방법을 설명합니다.Python에서 디지털 서명을 적용하고, 스마트 카드 및 인증서를 사용하고, 서명 정보를 추출하고, PDF 암호화, 암호 및 액세스 권한을 관리하는 방법을 알아봅니다.
---

이 단원에서는 Python 라이브러리를 사용하여 PDF 문서에 디지털 서명을 안전하게 적용하는 방법을 설명합니다.전자 서명과 디지털 서명이라는 용어는 때때로 같은 의미로 사용되지만 동일하지는 않습니다.디지털 서명은 다음을 통해 뒷받침됩니다. [인증 기관](https://en.wikipedia.org/wiki/Certificate_authority)문서가 변조되지 않도록 보호하는 신뢰할 수 있는 봉인을 제공합니다.반대로 전자 서명은 일반적으로 동일한 수준의 보안 검증 없이 문서에 서명하려는 사람의 의사를 나타내는 데 사용됩니다.

Python 워크플로에서 PDF 콘텐츠를 보호하고, 문서 권한을 제어하고, 신뢰를 확인하거나, 인증서 기반 서명을 적용해야 할 때 이 가이드를 사용하십시오.

## 보안 및 서명 작업 포함

Aspose.PDF 는 디지털 서명을 지원합니다.

- RSA 시그니처 알고리즘과 SHA-1 다이제스트가 포함된 PKCS1
- RSA 시그니처 알고리즘과 SHA-1 다이제스트가 포함된 PKCS7
- DSA, RSA 및 ECDSA 시그니처 알고리즘을 사용하여 PKCS7 을 분리했습니다.지원되는 다이제스트 알고리즘은 시그니처 알고리즘에 따라 달라집니다.
- 타임스탬프 서명

분리된 PKCS7 다이제스트 알고리즘:

- DSA - 샤-1.
- RSA - 샤-1, 샤-256, 샤-384, 샤-512.
- ECDSA - 샤-256, 샤-384, 샤-512, 샤3-256, 샤3-384, 샤3-512.

SHA-1 다이제스트 알고리즘의 디지털 서명은 안전하지 않으므로 사용하지 않는 것이 좋습니다.

- [PDF 파일에 디지털 서명](/pdf/ko/python-net/digitally-sign-pdf-file/)
- [권한 설정, PDF 파일 암호화 및 암호 해독](/pdf/ko/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [이미지 및 서명 정보 추출](/pdf/ko/python-net/extract-image-and-signature-information/)
- [스마트 카드에서 PDF 문서에 서명](/pdf/ko/python-net/sign-pdf-document-from-smart-card/)
