---
title: Aspose PDF 라이선스
linktitle: 라이선스 및 제한 사항
type: docs
weight: 50
url: /ko/python-net/licensing/
description: Aspose.PDF for Python은 고객에게 클래식 라이선스를 받도록 권장합니다. 또한 제한된 라이선스를 사용하여 제품을 더 잘 탐색할 수 있습니다.
lastmod: "2025-02-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python의 라이선스
Abstract: 이 문서는 Aspose.PDF for Python의 제한 사항 및 라이선스 옵션에 대해 설명합니다. 평가 버전은 전체 기능 테스트를 허용하지만 생성된 PDF에 "Evaluation Only"와 저작권 정보가 포함된 워터마크를 추가한다는 점을 강조합니다. 이러한 제한 없이 테스트하고자 하는 사용자를 위해 30일 임시 라이선스를 제공됩니다. 또한 클래식 라이선스를 파일 또는 스트림에서 로드하여 구현하는 방법을 설명하고, 라이선스 파일을 Aspose.PDF.dll 파일과 같은 디렉터리에 배치하고 `Aspose.Pdf.License` 클래스를 사용하여 라이선스를 설정할 것을 권장합니다. 라이선스 프로세스를 보여주는 코드 스니펫이 제공됩니다.
---

## 평가 버전의 제한 사항

고객이 구매 전에 당사의 구성 요소를 충분히 테스트할 수 있도록 평가 버전은 일반적으로 사용하듯이 사용할 수 있게 합니다.

- **평가 워터마크가 포함된 PDF**. Aspose.PDF for Python의 평가 버전은 전체 제품 기능을 제공하지만 생성된 PDF 문서의 모든 페이지 상단에 "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" 라는 워터마크가 표시됩니다.

>평가 버전의 제한 없이 Aspose.PDF를 테스트하고 싶다면 30일 임시 라이선스를 요청할 수 있습니다. 자세한 내용은 [임시 라이선스 얻는 방법?](https://purchase.aspose.com/temporary-license) 를 참조하십시오.

## 클래식 라이선스

라이선스는 파일이나 스트림 객체에서 로드할 수 있습니다. 라이선스를 설정하는 가장 쉬운 방법은 아래 예시와 같이 라이선스 파일을 Aspose.PDF.dll 파일과 같은 폴더에 두고 경로 없이 파일 이름만 지정하는 것입니다.

Aspose.PDF for Python과 함께 다른 Aspose for Python 구성 요소를 사용하는 경우, [Aspose.Pdf.License 클래스]()와 같이 라이선스의 네임스페이스를 지정해 주세요.

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```

