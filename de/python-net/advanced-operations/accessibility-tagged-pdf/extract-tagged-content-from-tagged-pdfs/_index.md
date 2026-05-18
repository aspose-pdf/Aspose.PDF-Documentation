---
title: Getaggte Inhalte aus PDFs in Python extrahieren
linktitle: Getaggte Inhalte extrahieren
type: docs
weight: 20
url: /de/python-net/extract-tagged-content-from-tagged-pdfs/
description: Erfahren Sie, wie Sie getaggte PDF-Inhalte in Python mit Aspose.PDF for Python via .NET extrahieren, einschließlich Zugriff auf getaggte Inhalte, Root-Struktur und untergeordnete Struktur-Elemente.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

In diesem Artikel erfahren Sie, wie Sie getaggte Inhalte aus PDF-Dokumenten mit Python extrahieren.

Verwenden Sie diese Beispiele, wenn Sie ein tagged PDF untersuchen, den logischen Strukturbaum lesen oder validieren müssen, dass Structure Elements korrekt erstellt wurden für Barrierefreiheits‑Workflows.

## Abrufen von Tagged PDF-Inhalt

Um den Inhalt eines PDF Document mit Tagged Text zu erhalten, bietet Aspose.PDF [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) Eigenschaft von [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse.

Erstellen Sie ein fortschrittliches, voll getaggtes PDF-Dokument mit einem strukturierten und hierarchischen Inhaltsverzeichnis (TOC):

1. Erstelle ein neues Document-Objekt.
1. Greifen Sie auf die tagged_content-Eigenschaft zu.
1. Setzen Sie den Dokumenttitel mithilfe von 'set_title()'.
1. Setzen Sie die Dokumentsprache mithilfe von 'set_language()'.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

# region Extract Tagged Content from PDF
def get_tagged_content(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Work with Tagged PDF content
        # Set Title and Language for Document
        tagged_content.set_title("Simple Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Abrufen der Root-Struktur

Tagged PDFs enthalten einen logischen Strukturbaum, der die semantische Struktur des Dokuments definiert. Der StructTreeRoot stellt die Wurzel dieses logischen Baums dar, während das RootElement eine Schnittstelle bietet, um mit dem obersten Strukturelement des Dokuments zu interagieren.

Das folgende Code‑Snippet zeigt, wie die Root‑Struktur eines Tagged‑PDF‑Dokuments abgerufen wird:

1. Erstellen Sie ein neues Tagged PDF-Dokument.
1. Greifen Sie auf getaggte Inhalte zu und setzen Sie Metadaten.
1. Greifen Sie auf StructTreeRoot und RootElement zu.
1. Speichern Sie das Tagged PDF.

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def get_root_structure(outfile):

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Properties StructTreeRootElement and RootElement are used for access to
        # StructTreeRoot object of pdf document and to root structure element (Document structure element).
        struct_tree_root_element = tagged_content.struct_tree_root_element
        root_element = tagged_content.root_element

        print(f"StructTreeRootElement: {struct_tree_root_element}")
        print(f"RootElement: {root_element}")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Zugriff auf Kindelemente

Tagged PDFs enthalten einen logischen Strukturbaum, der die semantische Hierarchie des Dokuments definiert (Überschriften, Absätze, Formulare, Listen usw.). Der Zugriff auf und die Änderung dieser Strukturelemente ermöglicht es Ihnen:

- Metadaten wie Titel, Sprache, actual_text und barrierefreiheitsbezogene Eigenschaften prüfen
- Eigenschaften aktualisieren, um die Barrierefreiheit oder Lokalisierung zu verbessern
- Programmgesteuert die logische Dokumentenstruktur für PDF/UA-Konformität anpassen

 Das folgende Code‑Snippet zeigt, wie man auf Kind‑Elemente eines Tagged PDF‑Dokuments zugreift:

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def access_child_elements(infile, outfile):

    # Open PDF Document
    with ap.Document(infile) as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Access to root element(s)
        element_list = tagged_content.struct_tree_root_element.child_elements

        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = cast(ap.logicalstructure.StructureElement, element)
                # Get properties
                print(
                    "StructureElement properties - "
                    f"title: {structure_element.title}, "
                    f"language: {structure_element.language}, "
                    f"actual_text: {structure_element.actual_text}, "
                    f"expansion_text: {structure_element.expansion_text}, "
                    f"alternative_text: {structure_element.alternative_text}"
                )

        # Access to child elements of first element in root element
        element_list = tagged_content.root_element.child_elements[1].child_elements
        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = element

                # Set properties
                structure_element.title = "title"
                structure_element.language = "fr-FR"
                structure_element.actual_text = "actual text"
                structure_element.expansion_text = "exp"
                structure_element.alternative_text = "alt"

        # Save Tagged PDF Document
        document.save(outfile)
```

## Verwandte Tagged PDF-Themen

- [Tagged PDF erstellen](/pdf/de/python-net/create-tagged-pdf/) um barrierefreie getaggte Dokumente zu erstellen, bevor ihre Struktur inspiziert wird.
- [Einstellen der Structure Elements-Eigenschaften](/pdf/de/python-net/setting-structure-elements-properties/) um semantische Eigenschaften nach dem Extrahieren von Strukturelementen zu aktualisieren.
- [Arbeiten mit Tabelle in Tagged PDFs](/pdf/de/python-net/working-with-table-in-tagged-pdfs/) für Barrierefreiheits‑Workflows mit gekennzeichneten Tabellen.