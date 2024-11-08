---
title: Python에서 이미지 PDF로 변환
linktitle: 이미지 파일을 PDF로 변환
type: docs
weight: 10
url: /ko/python-cpp/convert-image-to-pdf/
lastmod: "2024-04-22"
description: 이 주제는 Aspose.PDF for Python via C++ 라이브러리를 사용하여 이미지를 PDF로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

우리 라이브러리는 가장 인기 있는 이미지 형식인 JPEG을 변환하는 코드 스니펫을 보여줍니다. Aspose.PDF for Python via C++를 사용하여 JPG 이미지를 PDF로 매우 쉽게 변환할 수 있습니다. 다음 단계를 따르세요:

## 이미지 PDF로 변환

Aspose.PDF for C++를 사용하여 JPG 이미지를 PDF로 매우 쉽게 변환할 수 있습니다. 다음 단계를 따르세요:

1. PIL 라이브러리를 사용하여 입력 이미지 파일을 엽니다.
1. 이미지의 너비와 높이를 가져옵니다.
1. AsposePDFPythonWrappers 라이브러리를 사용하여 새로운 Document 인스턴스를 생성합니다.
1. 이미지의 고정 높이와 너비를 설정합니다.
1. 문서에 새로운 페이지를 추가합니다.
1. 페이지에 이미지를 추가합니다.
1. 'document.save' 메서드를 사용하여 출력 PDF를 저장합니다.

아래 코드 스니펫은 Python을 통해 C++를 사용하여 JPG 이미지를 PDF로 변환하는 방법을 보여줍니다:

```python
import AsposePDFPythonWrappers as apw
import os
import os.path
from PIL import Image

# 데이터 파일의 디렉토리 경로 설정
dataDir = os.path.join(os.getcwd(), "samples")

# 입력 파일 경로 설정
input_file = os.path.join(dataDir, "sample.jpg")

# 출력 파일 경로 설정
output_file = os.path.join(dataDir, "results", "jpg-to-pdf.pdf")

# PIL 라이브러리를 사용하여 입력 이미지 파일 열기
pil_img = Image.open(input_file)

# 이미지의 너비와 높이 가져오기
width, height = pil_img.size

# AsposePDFPythonWrappers 라이브러리를 사용하여 새로운 Document 인스턴스 생성
document = apw.Document()

# AsposePDFPythonWrappers 라이브러리를 사용하여 새로운 Image 인스턴스 생성
image = apw.Image()

# 이미지의 파일 경로 설정
image.file = input_file

# 이미지의 고정 높이와 너비 설정
image.fix_height = height
image.fix_width = width

# 문서에 새 페이지 추가
page = document.pages.add()

# 페이지에 이미지 추가
page.paragraphs.add(image)

# 문서를 출력 파일 경로로 저장
document.save(output_file)
```