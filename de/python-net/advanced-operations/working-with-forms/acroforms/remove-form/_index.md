---
title: Formulare aus PDF in Python löschen
linktitle: Formulare löschen
type: docs
weight: 70
url: /de/python-net/remove-form/
description: Entfernen Sie Formularobjekte von PDF-Seiten, indem Sie Aspose.PDF for Python via .NET verwenden, einschließlich vollständiger Bereinigung und gezielter Löschung.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Formulare aus PDF mit Aspose.PDF for Python via .NET entfernen
Abstract: Dieser Artikel stellt zwei Ansätze zum Entfernen von Formularelementen aus PDF-Dokumenten vor, indem Aspose.PDF for Python via .NET verwendet wird. Die erste Methode löscht alle Formularobjekte von einer ausgewählten Seite, während die zweite Methode nur passende Typewriter-Formularressourcen entfernt. Diese Beispiele unterstützen die Formularbereinigung, die Vorlagenvorbereitung und Workflows zur Dokumentnormalisierung.
---

## Alle Formulare von einer Seite entfernen

Dieser Code entfernt alle Form-Objekte von der angegebenen Seite `page_num` und speichert das aktualisierte Dokument.

1. Laden Sie das PDF-Dokument.
1. Seitenressourcen zugreifen.
1. Formobjekte löschen.
1. Speichern Sie das aktualisierte Dokument.

```python
import aspose.pdf as ap

def remove_all_forms(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(output_file_name)
```

## Entferne einen bestimmten Form-Typ

Im nächsten Beispiel wird über die Form-Objekte einer angegebenen PDF-Seite iteriert, typewriter-Formularannotationen identifiziert, diese gelöscht und anschließend das aktualisierte PDF mithilfe von Aspose.PDF for Python via .NET gespeichert.

1. Laden Sie das PDF-Dokument.
1. Greife auf Seiten-Formen zu.
1. Iteriere über Form-Objekte.
1. Prüfe auf typewriter-Formen.
1. Lösche das übereinstimmende Formular.
1. Speichern Sie das aktualisierte Dokument.

```python
import aspose.pdf as ap

def remove_specified_form(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(output_file_name)
```

## Verwandte Themen

- [AcroForm erstellen](/pdf/de/python-net/create-form/)
- [AcroForm ausfüllen](/pdf/de/python-net/fill-form/)
- [AcroForm ändern](/pdf/de/python-net/modifying-form/)
- [Formulare posten](/pdf/de/python-net/posting-form/)
