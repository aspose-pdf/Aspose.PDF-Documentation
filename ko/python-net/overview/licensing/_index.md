---
title: PDF 라이선스 추가
linktitle: 라이선스 및 제한
type: docs
weight: 50
url: /ko/python-net/licensing/
description: 파이썬용 Aspose.PDF 는 고객들에게 클래식 라이선스를 받도록 초대합니다.또한 제한된 라이선스를 사용하여 제품을 더 잘 탐색할 수 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 라이선스
Abstract: 이 문서에서는 Python용 Aspose.PDF 제한 및 라이선스 옵션에 대해 설명합니다.이 글에서는 평가 버전에서는 전체 기능 테스트가 가능하지만 생성된 PDF에는 저작권 정보와 함께 “평가 전용”이라는 워터마크가 추가된다는 점을 강조하고 있습니다.이러한 제한 없이 테스트하려는 사용자는 30일 임시 라이선스를 이용할 수 있습니다.이 문서에서는 파일 또는 스트림에서 클래식 라이선스를 로드하여 클래식 라이선스를 구현하는 방법에 대해 자세히 설명합니다. 라이선스 파일을 Aspose.PDF.dll 파일과 동일한 디렉터리에 배치하고 `Aspose.Pdf.License` 클래스를 사용하여 라이선스를 설정하는 것이 좋습니다.라이선스 프로세스를 설명하기 위한 코드 스니펫이 제공됩니다.
---

## 평가 버전의 제한

우리는 고객이 구매 전에 구성 요소를 철저히 테스트하여 평가 버전을 평상시처럼 사용할 수 있기를 바랍니다.

- **평가 워터마크를 사용하여 만든 PDF.** Python용 Aspose.PDF 평가 버전은 전체 제품 기능을 제공하지만 생성된 PDF 문서의 모든 페이지에는 “평가 전용”으로 워터마크가 표시됩니다.Aspose.PDF 버전으로 작성되었습니다.저작권 2002-2020 Aspose Pty Ltd”가 맨 위에 있습니다.

>평가 버전 제한 없이 Aspose.PDF 를 테스트하려는 경우 30일 임시 라이선스를 요청할 수도 있습니다.을 참조하십시오. [임시 라이선스는 어떻게 받을 수 있나요?](https://purchase.aspose.com/temporary-license)

## 클래식 라이선스

라이센스는 파일 또는 스트림 객체에서 로드할 수 있습니다.라이선스를 설정하는 가장 쉬운 방법은 아래 예와 같이 라이선스 파일을 ASpose.pdf.dll 파일과 같은 폴더에 넣고 경로 없이 파일 이름을 지정하는 것입니다.

Python용 Aspose.PDF 와 함께 다른 Python용 Aspose 구성 요소를 사용하는 경우 License의 네임스페이스를 다음과 같이 지정하십시오. [Aspose.Pdf. 라이선스 클래스]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```
