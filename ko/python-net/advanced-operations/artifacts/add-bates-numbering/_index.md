---
title: Python을 통한 .NET에서 베이츠 번호 매기기 아티팩트 추가
linktitle: 베이츠 번호 매기기 추가
type: docs
weight: 10
url: /ko/python-net/add-bates-numbering/
description: Aspose.PDF for Python via .NET은 PDF에 베이츠 번호 매기기를 추가할 수 있게 해줍니다.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 통해 베이츠 번호 매기기 추가
Abstract: 베이츠 번호 매기기는 법률, 의료 및 비즈니스 문서 워크플로우에서 중요한 기능으로, 세트 내 각 페이지에 고유하고 순차적인 식별자를 부여하여 신뢰할 수 있는 참조를 보장합니다. 이 문서는 Aspose.PDF for Python via .NET이 유연한 API를 통해 베이츠 번호 매기기 자동화를 어떻게 간소화하는지 보여줍니다. BatesNArtifact 클래스를 사용하면 개발자는 자리수, 접두사, 접미사, 정렬 및 여백 등을 포함한 번호 매기기 동작을 구성하고 전체 문서에 프로그램matically 적용할 수 있습니다. 직접 아티팩트 적용부터 위임자 기반 구성에 이르는 다양한 접근 방식을 제시하여 정적 및 동적 제어를 모두 제공합니다. 또한, API는 단일 메서드 호출로 베이츠 번호를 완전히 제거하는 기능을 지원해 페이지 매김 아티팩트의 전체 수명 주기 관리를 가능하게 합니다. 명확한 단계별 코드 예제가 베이츠 번호를 추가, 맞춤 설정 및 삭제하는 방법을 설명하여 문서 처리 워크플로우를 간소화하려는 개발자에게 실용적인 리소스를 제공합니다.
---

베이츠 번호 매기기는 법률, 의료 및 비즈니스 워크플로우에서 널리 사용되며, 문서 세트 내 페이지에 고유하고 순차적인 식별자를 부여합니다. Aspose.PDF for Python via .NET은 이 프로세스를 자동화하기 위한 간단하고 유연한 API를 제공하여 모든 PDF에 표준화된 베이츠 번호를 프로그래밍 방식으로 적용할 수 있게 합니다.

`[`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/)` 클래스를 사용하면 개발자는 시작 번호, 자리수, 접두사와 접미사, 정렬 및 여백 등을 포함한 번호 매기기 동작을 완전히 사용자 정의할 수 있습니다. 구성 후에는 해당 아티팩트를 `Document`에 적용할 수 있으며, 이는 `PageCollection`의 `add_bates_numbering` 메서드를 통해 수행하거나 `PaginationArtifact` 객체 목록의 일부로 추가할 수 있습니다. Aspose.PDF는 위임자 기반 구성 방식을 지원하여 런타임에 아티팩트 설정을 동적으로 제어할 수 있습니다.

베이츠 번호를 생성하는 것 외에도, API는 `delete_bates_numbering`을 사용하여 이를 쉽게 제거할 수 있는 방법을 제공하며, 문서 처리 워크플로우에서 완전한 유연성을 제공합니다.

이 문서는 Aspose.PDF for Python via .NET을 사용하여 PDF에서 베이츠 번호 매기기를 추가하고 제거하는 다양한 방법을 보여주며, 아티팩트 구성, 적용 및 제거에 대한 명확한 예제를 제공합니다.

## 베이츠 번호 매기기 아티팩트 추가

이 예제는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에 프로그래밍 방식으로 베이츠 번호 매기기를 추가하는 방법을 보여줍니다. 원하는 설정으로 [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/)을 구성하고 이를 문서 페이지에 적용함으로써 각 페이지에 표준화된 식별자를 추가하는 프로세스를 자동화할 수 있습니다.

`[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)`에 베이츠 번호 매기기 아티팩트를 추가하려면, [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)의 `AddBatesNumbering(BatesNArtifact)` 확장 메서드를 호출하고, 매개변수로 [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) 인스턴스를 전달합니다:

```python

import aspose.pdf as ap

def add_bates_numbering(path_outfile):
    # Create a new or empty PDF document
    with ap.Document() as document:

        # Add 10 blank pages
        for _ in range(10):
            document.pages.add()

        # Create Bates numbering artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,  # 0 = apply until last page
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add Bates numbering to all pages
        document.pages.add_bates_numbering(bates)

        # Save the resulting PDF
        document.save(path_outfile)
```

또는, [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) 객체의 컬렉션을 전달할 수 있습니다:

```python

import aspose.pdf as ap

def add_bates_numbering_collection(path_outfile):
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Create Bates artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add as a pagination artifact list
        document.pages.add_pagination([bates])

        # Save document
        document.save(path_outfile)
```

액션 위임자를 사용하여 베이츠 번호 매기기 아티팩트를 추가합니다:

```python

import aspose.pdf as ap

def add_bates_numbering_delegate(path_outfile):
    def configure_bates(b):
        """Configure Bates numbering artifact with desired settings."""
        b.start_page = 1
        b.end_page = 0
        b.subset = ap.Subset.ALL
        b.number_of_digits = 6
        b.start_number = 1
        b.prefix = ""
        b.suffix = ""
        b.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
        b.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
        b.right_margin = 72
        b.left_margin = 72
        b.top_margin = 36
        b.bottom_margin = 36
        b.text_state.font_size = 10
    
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Use delegate function to configure Bates artifact
        document.pages.add_bates_numbering(configure_bates)

        # Save output PDF
        document.save(path_outfile)
```

## 베이츠 번호 매기기 삭제

`[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)`에서 베이츠 번호 매기기를 제거하려면, [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)의 `delete_bates_numbering()` 메서드를 사용합니다:

```python

import aspose.pdf as ap

def delete_bates_numbering(path_infile, path_outfile):
    with ap.Document(path_infile) as document:

        # Remove Bates numbering from all pages
        document.pages.delete_bates_numbering()

        # Save updated document
        document.save(path_outfile)
```
