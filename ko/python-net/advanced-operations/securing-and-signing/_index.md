---
title: Python에서 PDF 보안 및 서명
linktitle: PDF 보안 및 서명
type: docs
weight: 210
url: /ko/python-net/securing-and-signing/
description: 이 섹션에서는 Python을 사용하여 PDF 문서를 서명하고 보호하는 기능에 대해 설명합니다.
lastmod: "2025-06-23"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF 문서 서명
Abstract: 이 섹션은 Aspose.PDF for Python via .NET 문서에서 PDF 문서를 프로그래밍 방식으로 보호하고 서명하는 방법에 대한 포괄적인 가이드를 제공합니다. 여기에는 비밀번호 보호, 암호화 알고리즘, 디지털 서명 적용 및 검증, 인증서 처리, 문서 권한 등 필수 주제가 포함됩니다. 개발자는 민감한 콘텐츠를 보호하고 문서 무결성을 보장하며 규제 기준을 준수하기 위해 다양한 보안 수준을 구현하는 방법을 배웁니다. 예제와 API 참조를 통해 보안 기능을 Python 애플리케이션에 빠르게 통합할 수 있어 PDF 워크플로를 안심하고 보호할 수 있습니다.
---

이 섹션에서는 Python 라이브러리를 사용하여 PDF 문서에 디지털 서명을 안전하게 적용하는 방법을 설명합니다. 전자 서명과 디지털 서라는 용어가 때때로 혼용되지만 동일하지 않습니다. 디지털 서명은 [인증 기관](https://en.wikipedia.org/wiki/Certificate_authority)으로부터 지원받아 문서를 변조로부터 보호하는 신뢰할 수 있는 봉인을 제공합니다. 반면 전자 서명은 일반적으로 문서에 서명하려는 사람의 의도를 표시하기 위해 사용되며 동일한 수준의 보안 검증을 제공하지 않습니다.

Aspose.PDF는 디지털 서명을 지원합니다:

- RSA 서명 알고리즘 및 SHA-1 다이제스트를 사용하는 PKCS1.
- RSA 서명 알고리즘 및 SHA-1 다이제스트를 사용하는 PKCS7.
- DSA, RSA 및 ECDSA 서명 알고리즘을 사용하는 PKCS7 디태치드. 지원되는 다이제스트 알고리즘은 서명 알고리즘에 따라 다릅니다.
- 타임스탬프 서명.

PKCS7 디태치드용 다이제스트 알고리즘:

- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

보안 취약성 때문에 SHA-1 다이제스트 알고리즘을 사용하는 디지털 서명은 피하는 것이 권장됩니다.

- [PDF 파일 디지털 서명](/pdf/python-net/digitally-sign-pdf-file/)
- [PDF 파일 권한 설정, 암호화 및 복호화](/pdf/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [이미지 및 서명 정보 추출](/pdf/python-net/extract-image-and-signature-information/)
- [스마트 카드로 PDF 문서 서명](/pdf/python-net/sign-pdf-document-from-smart-card/)
