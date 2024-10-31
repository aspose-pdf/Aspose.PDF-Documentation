---
title: 파이썬을 사용한 양식 작업
linktitle: PDF 문서의 양식
type: docs
weight: 60
url: /python-java/forms/
lastmod: "2023-05-19"
description: 이 섹션은 파이썬 API를 사용하여 PDF 문서에서 양식을 작업하는 것과 관련된 기사를 포함합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

양식은 정보를 수집하고 저장하기 위한 목적으로 사용자들이 선택하거나 정보를 작성할 수 있는 영역을 가진 파일입니다.

AcroForms는 양식 필드를 포함하는 PDF 파일입니다. 사용자는 수동으로 또는 자동화된 프로세스를 통해 이 필드에 데이터를 입력할 수 있으며, 양식의 작성자가 입력할 수도 있습니다. 내부적으로 AcroForms는 PDF 문서에 적용된 주석이나 필드입니다.

이 섹션에서는 Aspose.PDF를 사용하여 프로그래밍 방식으로 PDF 문서를 완성하는 빠르고 간단한 방법을 설명합니다. 또한, Java용 Aspose.PDF를 사용하여 기존 PDF에서 AcroForms가 있는 필드를 발견하고 매핑하는 방법에 대해서도 논의합니다.

**Java를 통한 우리 Aspose.PDF for Python** 라이브러리를 사용하면 PDF 문서의 양식을 성공적으로, 빠르고 쉽게 작업할 수 있습니다.

- **AcroForms** - 양식을 생성하고, 양식 필드를 채우고, 양식에서 데이터를 추출하고, Java 라이브러리를 사용하여 PDF의 필드를 수정합니다.
- **XFA Forms** - XFA 필드를 채우고, XFA를 변환하고, XFA 필드 속성을 가져옵니다.

## 다음 기능들이 제공됩니다:

- fdf 내보내기/가져오기
- xfdf 내보내기/가져오기
- xml 내보내기/가져오기
- XfaData 내보내기/설정
- 필드 채우기
- 필드 평탄화
- 유효한 라디오 버튼 값 결정
- 필드 이름, 플래그, 유형, 값 가져오기
- 필드 이름 변경

```python

from asposepdf import Api, Forms


# 라이센스 초기화
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

DIR_INPUT = baseDir+"testdata/forms/"
DIR_OUTPUT = baseDir+"testout/"

# 필드 채우기 예제

input_pdf1 = DIR_INPUT + "Testing.pdf"
output_pdf = DIR_OUTPUT + "test5_1.pdf"

form = Forms.Form(sourceFileName=input_pdf1)
print(form.getFieldType("form1[0].Page1[0].fldBarCode1[0]"))
form.fillField("form1[0].Page1[0].fldBarCode1[0]", "54321")

form.save(output_pdf)
```