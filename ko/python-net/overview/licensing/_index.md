---
title: Aspose PDF 라이선스
linktitle: 라이선싱 및 제한 사항
type: docs
weight: 50
url: /ko/python-net/licensing/
description: Aspose. PDF for Python은 고객에게 Classic 라이선스를 얻도록 권장합니다. 제품을 더 잘 탐색하기 위해 제한된 라이선스도 사용할 수 있습니다.
lastmod: "2022-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 평가판 버전의 제한 사항

고객이 구매 전에 당사의 구성 요소를 철저히 테스트할 수 있도록 평가판 버전은 정상적으로 사용할 수 있도록 허용합니다.

- **평가판 워터마크가 있는 PDF 생성.** Aspose.PDF for Python의 평가판 버전은 전체 제품 기능을 제공하지만, 생성된 PDF 문서의 모든 페이지는 "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd"라는 워터마크가 상단에 표시됩니다.

> 평가판 버전의 제한 없이 Aspose.PDF를 테스트하려면 30일 임시 라이선스를 요청할 수도 있습니다.
 [임시 라이센스 받는 방법](https://purchase.aspose.com/temporary-license)을 참조하십시오.

## 클래식 라이센스

라이센스는 파일 또는 스트림 객체에서 로드될 수 있습니다. 라이센스를 설정하는 가장 쉬운 방법은 라이센스 파일을 Aspose.PDF.dll 파일과 동일한 폴더에 놓고, 아래 예제에서와 같이 경로 없이 파일 이름만 지정하는 것입니다.

Aspose.PDF for Python과 함께 다른 Aspose for Python 구성 요소를 사용하는 경우, [Aspose.Pdf.License 클래스]()와 같이 라이센스를 위한 네임스페이스를 지정하십시오.

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```