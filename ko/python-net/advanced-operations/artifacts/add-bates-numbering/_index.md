---
title: 파이썬에서 PDF에 베이츠 넘버링 추가
linktitle: 베이츠 넘버링 추가
type: docs
weight: 10
url: /ko/python-net/add-bates-numbering/
description: .NET을 통해 파이썬용 Aspose.PDF 와 함께 Python을 사용하여 PDF 문서에서 베이츠 넘버링을 추가하고 제거하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬을 통해 베이츠 넘버링 추가
Abstract: Bates 넘버링은 법률, 의료 및 비즈니스 문서 워크플로우에서 중요한 기능으로, 세트의 각 페이지가 신뢰할 수 있는 참조를 위해 고유한 순차적 식별자를 받도록 합니다.이 문서에서는 .NET을 통한 Python용 Aspose.PDF 가 유연한 API를 통해 베이츠 넘버링 자동화를 간소화하는 방법을 보여줍니다.개발자는 BatesArtifact 클래스를 사용하여 자릿수, 접두사, 접미사, 정렬 및 여백을 비롯한 넘버링 동작을 구성하고 이를 프로그래밍 방식으로 전체 문서에 적용할 수 있습니다.다이렉트 아티팩트 애플리케이션부터 델리게이트 기반 구성에 이르기까지 정적 제어와 동적 제어를 모두 제공하는 다양한 접근 방식이 제시됩니다.또한 API는 단일 메서드 호출로 베이츠 번호를 완전히 제거할 수 있도록 지원하므로 페이지네이션 아티팩트의 전체 라이프사이클 관리가 가능합니다.명확한 단계별 코드 예제는 Bates 넘버링을 추가, 사용자 지정 및 삭제하는 방법을 보여 주므로 이 가이드는 문서 처리 워크플로를 간소화하려는 개발자에게 유용한 리소스입니다.
---

베이츠 넘버링은 법률, 의료 및 비즈니스 워크플로우에서 문서 세트 내의 페이지에 고유한 순차 식별자를 할당하는 데 널리 사용됩니다..NET을 통한 Python용 Aspose.PDF 프로그램은 이 프로세스를 자동화하는 간단하고 유연한 API를 제공하므로 표준화된 베이츠 번호를 모든 PDF에 프로그래밍 방식으로 적용할 수 있습니다.

를 사용하여 [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) 클래스에서 개발자는 시작 번호, 자릿수, 접두사 및 접미사, 정렬 및 여백을 포함하여 번호 지정 동작을 완전히 사용자 지정할 수 있습니다.구성이 완료되면 아티팩트를 에 적용할 수 있습니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 를 통해 `add_bates_numbering` 에 대한 메서드 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 또는 목록의 일부로 추가 [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) 사물.또한 Aspose.PDF 는 델리게이트 기반 구성 스타일을 지원하므로 런타임 시 아티팩트 설정을 동적으로 제어할 수 있습니다.

API는 Bates 번호를 생성하는 것 외에도 다음을 사용하여 Bates 번호를 쉽게 제거할 수 있는 방법을 제공합니다. `delete_bates_numbering`문서 처리 워크플로우에 완벽한 유연성을 제공합니다.

이 문서에서는 Aspose.PDF for Python을 사용하여.NET을 통해 PDF에서 Bates 넘버링을 추가하고 제거하는 여러 방법을 아티팩트 구성, 적용 및 제거에 대한 명확한 예와 함께 보여줍니다.

## 베이츠 넘버링 아티팩트 추가

이 예제에서는 .NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 Bates 넘버링을 프로그래밍 방식으로 추가하는 방법을 보여줍니다.를 구성하여 [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) 원하는 설정을 사용하여 문서 페이지에 적용하면 각 페이지에 표준화된 식별자를 추가하는 프로세스를 자동화할 수 있습니다.

Bates 넘버링 아티팩트를 a에 추가하려면 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), 전화해 `AddBatesNumbering(BatesNArtifact)` 의 확장 메서드 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), 합격 [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) 매개 변수로서의 인스턴스:

```python
import sys
from os import path
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact
```

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## 페이징 아티팩트를 사용하여 Bates 넘버링 추가

파이썬용 Aspose.PDF 파일의 페이지네이션 아티팩트 컬렉션을 사용하여 PDF에 베이츠 넘버링을 추가합니다.

1. PDF 문서를 로드합니다.
1. 필요한 경우 넘버링을 적용하기 전에 추가 페이지를 삽입합니다.
1. 베이츠 아티팩트를 만드세요.
1. 아티팩트 속성을 구성합니다.
1. 아티팩트를 페이지 매김 컬렉션에 추가합니다.
1. 페이지에 페이지 매김을 적용합니다.
1. 업데이트된 문서를 저장합니다.

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## 베이츠 넘버링 삭제

에서 Bates 넘버링을 제거하려면 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), 사용 `delete_bates_numbering()` 에 대한 메서드 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python
import sys
from os import path
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## 관련 아티팩트 주제

- [파이썬에서 PDF 아티팩트로 작업하기](/pdf/ko/python-net/artifacts/)
- [파이썬에서 PDF에 워터마크 추가](/pdf/ko/python-net/add-watermarks/)
- [파이썬에서 PDF 배경 추가](/pdf/ko/python-net/add-backgrounds/)
- [PDF 파일의 아티팩트 유형 수 계산](/pdf/ko/python-net/counting-artifacts/)