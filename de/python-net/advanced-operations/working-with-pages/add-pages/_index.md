---
title: PDF-Seiten in Python hinzufügen
linktitle: Seiten hinzufügen
type: docs
weight: 10
url: /de/python-net/add-pages/
description: Erfahren Sie, wie Sie Seiten zu PDF-Dokumenten in Python hinzufügen oder einfügen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Seiten mit Python hinzufügen oder einfügen
Abstract: Dieser Artikel erklärt, wie man Seiten zu PDF-Dateien mit Aspose.PDF for Python via .NET hinzufügt. Erfahren Sie, wie Sie leere Seiten an bestimmten Positionen einfügen, Seiten am Ende eines Dokuments anhängen und eine Seite aus einem anderen PDF mithilfe der Document- und PageCollection-APIs importieren.
---

Aspose.PDF for Python via .NET bietet flexible Seiten‑Ebene‑Operationen für PDF‑Dokumente. Sie können Seiten verwalten über [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) und Seiten zu einem [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) an bestimmten Positionen oder am Ende der Datei.

Verwenden Sie diese Seite, wenn Sie neue leere Seiten in ein vorhandenes PDF einfügen oder Seiten am Ende eines Dokuments während Generierungs‑Workflows anhängen müssen.

## Seiten zu einer PDF‑Datei hinzufügen oder einfügen

Aspose.PDF for Python via .NET unterstützt sowohl das Einfügen von Seiten an einem bestimmten Index als auch das Anhängen von Seiten am Ende eines PDFs.

### Leere Seite in einer PDF-Datei einfügen

Um eine leere Seite in einer PDF-Datei einzufügen:

1. Öffnen Sie ein vorhandenes [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) unter Verwendung geeigneter Methoden.
1. Fügen Sie an einem bestimmten Index eine neue leere Seite ein, indem Sie die [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `insert()` Methode.
1. Speichern Sie das modifizierte [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) zum gewünschten Ausgabepfad.

Fügen Sie einer bestehenden PDF-Datei an einer angegebenen Position eine leere Seite ein:

```python
import aspose.pdf as ap

def insert_empty_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### Fügen Sie einer PDF-Datei am Ende eine leere Seite hinzu

Manchmal möchten Sie sicherstellen, dass ein Dokument auf einer leeren Seite endet. Dieses Thema erklärt, wie man am Ende des PDF-Dokuments eine leere Seite einfügt.

Um am Ende einer PDF-Datei eine leere Seite einzufügen:

1. Öffnen Sie ein vorhandenes [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) unter Verwendung geeigneter Methoden.
1. Fügen Sie eine neue leere Seite am Ende des Dokuments mit dem hinzu [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `add()` Methode.
1. Speichere das Aktualisierte [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Das folgende Code‑Snippet zeigt Ihnen, wie Sie eine leere Seite am Ende einer PDF‑Datei einfügen.

```python
import aspose.pdf as ap

def add_empty_page_to_end(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.add()
    document.save(output_file_name)
```

### Fügen Sie eine Seite aus einem anderen PDF-Dokument hinzu

Mit Aspose.PDF for Python via .NET können Sie ein neues [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), fügen Sie eine Anfangsseite hinzu und importieren dann eine Seite aus einem anderen PDF in diese.

1. Neu erstellen [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Fügen Sie eine neue leere Seite hinzu [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) und schreiben Sie etwas Text darauf mithilfe von [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. Ein weiteres vorhandenes öffnen [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Kopiere ein [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) aus diesem Dokument.
1. Füge die kopierte Seite in Ihr Hauptdokument ein, indem Sie [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Speichern Sie die kombinierte Datei.

```python
import aspose.pdf as ap

def add_page_from_another_document(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    document.save(output_file_name)
```

## Verwandte Seitenthemen

- [Arbeiten Sie mit PDF-Seiten in Python](/pdf/de/python-net/working-with-pages/)
- [PDF‑Seiten in Python verschieben](/pdf/de/python-net/move-pages/)
- [PDF‑Seiten in Python löschen](/pdf/de/python-net/delete-pages/)
- [PDF-Seiten in Python extrahieren](/pdf/de/python-net/extract-pages/)
