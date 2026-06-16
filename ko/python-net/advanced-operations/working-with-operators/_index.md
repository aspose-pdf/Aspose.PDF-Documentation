---
title: 파이썬에서 PDF 연산자로 작업하기
linktitle: 오퍼레이터와 함께 작업하기
type: docs
weight: 90
url: /ko/python-net/working-with-operators/
description: 정확한 콘텐츠 스트림 조작 및 그래픽 제어를 위해 Python에서 저수준 PDF 연산자를 사용하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 콘텐츠 스트림 제어를 위한 저수준 PDF 연산자 사용
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 저수준 PDF 연산자를 사용하는 방법을 설명합니다.Python 워크플로에서 콘텐츠 스트림을 직접 조작하고, 연산자 클래스를 사용하여 그래픽을 정확하게 배치하고, PDF 페이지에서 그려진 개체를 제거하는 방법을 알아봅니다.
---

## PDF 연산자 및 사용법 소개

연산자는 페이지에 그래픽 모양 페인팅과 같이 수행할 작업을 지정하는 PDF 키워드입니다.연산자 키워드는 첫 솔리더스 문자 (2Fh) 가 없다는 점에서 이름이 지정된 객체와 구별됩니다.연산자는 콘텐츠 스트림 내에서만 의미가 있습니다.

콘텐츠 스트림은 페이지에 그릴 그래픽 요소를 설명하는 지침으로 구성된 데이터를 포함하는 PDF 스트림 객체입니다.PDF 연산자에 대한 자세한 내용은 에서 확인할 수 있습니다. [PDF 사양](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

정확한 좌표에 그래픽을 배치하거나, 그래픽 상태 변경 사항을 래핑하거나, 페이지에서 특정 그리기 연산자를 제거하는 등 Python에서 PDF 콘텐츠 스트림을 직접 제어해야 하는 경우 이 페이지를 사용하십시오.

## 연산자 클래스가 포함된 이미지 추가

상위 레이아웃 추상화에 의존하지 않고 PDF 페이지 스트림에 이미지 내용을 매우 정확하게 배치해야 하는 경우 저수준 연산자 클래스를 사용하십시오.

이 방법을 사용하면 저수준 그래픽 연산자로 내용 스트림을 직접 조작하여 PDF 내 이미지 배치를 세밀하게 제어할 수 있습니다.다음과 같이 이미지를 정밀하게 배치하고 변환해야 하는 경우에 특히 유용합니다.

- 특정 위치에 워터마크 또는 로고 추가
- 이미지를 기존 콘텐츠에 정확히 정렬하여 오버레이합니다.
- 상위 추상화로는 달성할 수 없는 사용자 지정 레이아웃을 구현합니다.

개발자는 gSave, ConcatenateMatrix, Do 및 GreStore와 같은 연산자를 사용하여 다른 페이지 콘텐츠에 의도하지 않은 부작용이 발생하지 않고 이미지가 정확하게 렌더링되도록 할 수 있습니다.

- 더 [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) 연산자는 PDF의 현재 그래픽 상태를 저장합니다.
- 더 [행렬 결합하기](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) (행렬 연결) 연산자는 이미지를 PDF 페이지에 배치하는 방법을 정의하는 데 사용됩니다.
- 더 [해야 할 것](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) 운영자가 페이지에 이미지를 그립니다.
- 더 [복원](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) 연산자는 그래픽 상태를 복원합니다.

PDF 파일에 이미지를 추가하려면:

1. PDF 문서 열기
1. 이미지 배치 좌표 정의
1. 대상 페이지 액세스
1. 이미지를 스트림에 로드
1. 현재 그래픽 상태 저장
1. 사각형 및 변환 행렬 만들기
1. 변환 매트릭스 적용
1. 이미지 그리기
1. 이전 그래픽 상태 복원
1. 수정된 PDF 문서 저장

다음 코드 스니펫은 PDF 연산자를 사용하는 방법을 보여줍니다.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_using_pdf_operators(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        page = document.pages[1]

        with open(imagefile, "rb") as image_stream:
            page.resources.images.add(image_stream)

        page.contents.append(ap.operators.GSave())

        rectangle = ap.Rectangle(
            lower_left_x, lower_left_y, upper_right_x, upper_right_y, True
        )
        matrix = ap.Matrix(
            [
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            ]
        )

        page.contents.append(ap.operators.ConcatenateMatrix(matrix))

        x_image = page.resources.images[len(page.resources.images)]

        page.contents.append(ap.operators.Do(x_image.name))

        page.contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## 연산자를 사용하여 페이지에 XForm 그리기

이 예제에서는 XForms와 그래픽 연산자의 강력한 기능을 사용하여 PDF 내에서 그래픽 콘텐츠를 효율적으로 재사용했습니다.이미지를 XForm으로 캡슐화하면 이미지 데이터를 복제하지 않고도 여러 번 그릴 수 있어 파일 크기가 작아지고 성능이 향상됩니다.이 방법은 다음과 같은 경우에 특히 유용합니다.

- 문서에 동일한 이미지나 그래픽이 여러 번 나타나야 합니다.

- 그래픽의 배치 및 변환에 대한 정밀한 제어가 필요합니다.

- 성능 및 크기에 맞게 PDF를 최적화하는 것이 최우선 과제입니다.

GSave 및 greStore를 사용하여 그래픽스 상태를 관리하고 ConcatenateMatrix와 함께 변환 행렬을 사용하여 이 기법을 사용하면 각 그래픽이 정확하고 독립적으로 렌더링됩니다.

```python
import sys
import aspose.pdf as ap
from os import path

def draw_xform_on_page(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        page_contents = document.pages[1].contents

        page_contents.insert(1, ap.operators.GSave())
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GSave())

        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.append(form)

        form.contents.append(ap.operators.GSave())
        form.contents.append(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        with open(imagefile, "rb") as image_stream:
            form.resources.images.add(image_stream)

        x_image = form.resources.images[len(form.resources.images)]
        form.contents.append(ap.operators.Do(x_image.name))
        form.contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 500)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 300)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## 연산자 클래스를 사용하여 그래픽스 객체 제거하기

다음 코드 스니펫은 그래픽을 제거하는 방법을 보여줍니다.참고로 이 방법을 사용하면 PDF 파일에 그래픽의 텍스트 레이블이 포함되어 있는 경우 해당 레이블이 PDF 파일에 그대로 남아 있을 수 있습니다.따라서 그래픽 연산자를 검색하여 이러한 이미지를 삭제하는 다른 방법을 찾아보십시오.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_graphics_objects(infile, outfile):
    with ap.Document(infile) as document:
        page = document.pages[1]
        # Collect operators to remove in single pass
        # Operator codes: S=Stroke, h=ClosePathStroke, f=Fill'
        graphics_operators = {"S", "h", "f"}
        operators_to_remove = [
            op for op in page.contents if str(op) in graphics_operators
        ]

        page.contents.delete(operators_to_remove)
        document.save(outfile)
```

## 관련 주제

- [파이썬에서의 고급 PDF 작업](/pdf/ko/python-net/advanced-operations/)
- [파이썬에서 PDF 페이지 작업하기](/pdf/ko/python-net/working-with-pages/)
- [Python을 사용하여 PDF의 이미지로 작업하기](/pdf/ko/python-net/working-with-images/)
- [파이썬에서 PDF 그래프로 작업하기](/pdf/ko/python-net/working-with-graphs/)
