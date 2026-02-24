---
title: 기존 PDF에서 표 제거
linktitle: 표 제거
type: docs
weight: 50
url: /ko/python-net/removing-tables/
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 표를 삭제하는 방법
Abstract: 이 문서는 Aspose.PDF for Python via .NET의 기능을 논의하며, 특히 PDF 문서 내에서 표를 조작하는 데 중점을 둡니다. 이 라이브러리는 새 PDF 파일과 기존 PDF 파일 모두에 표를 삽입하거나 만들 수 있으며, 기존 PDF에서 표를 조작하거나 제거할 수도 있습니다. 이 문서는 PDF에서 표를 식별하고 상호 작용하는 데 핵심적인 `TableAbsorber` 클래스를 소개합니다. 표 제거를 가능하게 하는 새로운 메서드 `remove()`가 추가되었습니다. 문서에는 두 개의 코드 스니펫이 제공됩니다 - 하나는 PDF에서 단일 표를 제거하는 방법을 보여주고, 다른 하나는 여러 표를 제거하는 방법을 설명합니다. 이러한 예제들은 PDF 문서에서 표 제거를 수행하기 위해 `TableAbsorber` 클래스를 실제로 활용하는 방법을 강조합니다.
---

## PDF 문서에서 표 제거

Aspose.PDF for Python을 사용하면 PDF에서 표를 제거할 수 있습니다. 기존 PDF를 열고, TableAbsorber를 사용하여 첫 페이지의 첫 번째 표를 감지한 다음, [remove_one_table](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) 메서드를 사용하여 해당 표를 삭제합니다. 그런 다음 업데이트된 PDF를 새 파일에 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(path_outfile)
```

## PDF 문서에서 모든 표 제거

우리 라이브러리를 사용하면 PDF의 특정 페이지에서 모든 표를 제거할 수 있습니다. 코드는 기존 PDF를 열고, TableAbsorber를 사용하여 두 번째 페이지의 모든 표를 감지한 다음, 감지된 표들을 순회하면서 각각을 제거하고, 수정된 PDF를 새 파일에 저장합니다. 페이지에서 표를 대량으로 제거하면서 PDF의 다른 콘텐츠는 그대로 유지해야 할 때 유용합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit second page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(path_outfile)
```


