---
title: PDF-Dokumente in Python vergleichen
linktitle: PDF vergleichen
type: docs
weight: 130
url: /de/python-net/compare-pdf-documents/
description: Erfahren Sie, wie Sie PDF-Dokumente in Python mit nebeneinanderliegenden und grafischen Unterschiedsausgaben mit Aspose.PDF for Python via .NET vergleichen können.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Vergleichen Sie PDF-Seiten und vollständige Dokumente mit visuellen Unterschiedsausgaben in Python
Abstract: Dieser Artikel erklärt, wie man PDF-Dokumente in Aspose.PDF for Python via .NET vergleicht. Lernen Sie, wie man bestimmte Seiten oder ganze PDF-Dateien mit nebeneinander stehender Ausgabe vergleicht und wie man grafische Vergleichsmethoden verwendet, um bildbasierte oder PDF-basierte Unterschiedsberichte zu erstellen.
---

## Möglichkeiten zum Vergleich von PDF-Dokumenten

Beim Arbeiten mit PDF-Dokumenten gibt es Zeiten, in denen Sie den Inhalt zweier Dokumente vergleichen müssen, um Unterschiede zu erkennen. Die Aspose.PDF for Python via .NET Bibliothek stellt dafür ein leistungsstarkes Werkzeugset bereit. In diesem Artikel werden wir untersuchen, wie man PDF-Dokumente mithilfe einiger einfacher Code‑Snippets vergleicht.

Verwenden Sie den Nebeneinander-Vergleich, wenn Sie eine PDF-Ausgabe benötigen, die Text- und Layoutänderungen über Seiten hinweg hervorhebt. Verwenden Sie den grafischen Vergleich, wenn Sie eine bildbasierte Unterschiedserkennung für visuelle Prüfungs‑Workflows, Regressionstests oder PDF-Vergleichsberichte benötigen.

Die Vergleichsfunktionalität in Aspose.PDF ermöglicht es Ihnen, zwei PDF‑Dokumente Seite für Seite zu vergleichen. Sie können wählen, ob Sie bestimmte Seiten oder ganze Dokumente vergleichen möchten. Das resultierende Vergleichsdokument hebt Unterschiede hervor und erleichtert die Identifizierung von Änderungen zwischen den beiden Dateien.

Hier ist eine Liste möglicher Methoden, um PDF‑Dokumente mit Aspose.PDF for Python via .NET zu vergleichen:

1. **Vergleich bestimmter Seiten** - Vergleichen Sie die ersten Seiten zweier PDF‑Dokumente.
1. **Vergleich ganzer Dokumente** - Vergleichen Sie den gesamten Inhalt von zwei PDF‑Dokumenten.
1. **PDF-Dokumente grafisch vergleichen**:

- Vergleichen Sie PDF mit der Methode 'comparer.get_difference' - einzelne Bilder, in denen Änderungen markiert sind.
- Vergleichen Sie PDF mit der Methode 'comparer.compare_documents_to_pdf' - PDF‑Dokument mit Bildern, in denen Änderungen markiert sind.

## Vergleich spezifischer Seiten

Der erste Codeabschnitt demonstriert, wie man die ersten Seiten zweier PDF-Dokumente mit der Klasse SideBySidePdfComparer vergleicht.

1. Dokumentinitialisierung.
1. Erstellen Sie eine Funktion, um den Vergleich durchzuführen.
1. Vergleichsprozess:

- document1.pages[1] und document2.pages[1]: - diese geben die erste Seite jedes Dokuments für den Vergleich an. Hinweis: Die Seitennummerierung beginnt in Aspose.PDF bei 1.
- SideBySideComparisonOptions - diese Klasse ermöglicht die Anpassung des Vergleichsverhaltens.
- additional_change_marks = True - aktiviert die Anzeige zusätzlicher Änderungsmarkierungen, die Unterschiede hervorheben, die möglicherweise auf anderen Seiten vorhanden sind, selbst wenn sie nicht auf der aktuell verglichenen Seite liegen.
- comparison_mode = ComparisonMode.IgnoreSpaces - legt den Vergleichsmodus fest, um Leerzeichen im Text zu ignorieren, wobei nur Änderungen innerhalb von Wörtern berücksichtigt werden.

1. Das Ergebnis des Vergleichs wird als neue PDF-Datei mit dem Namen ComparingSpecificPages_out.pdf im angegebenen data_dir gespeichert.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_specific_pages(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1.pages[1], document_2.pages[1], outfile, options
    )
```

## Vergleich ganzer Dokumente

Das zweite Code‑Snippet erweitert den Umfang, um den gesamten Inhalt von zwei PDF‑Dokumenten zu vergleichen.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_entire_documents(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1, document_2, outfile, options
    )
```

Der bereitgestellte Code demonstriert den Vergleich von zwei PDF-Dokumenten mithilfe von Aspose.PDF for Python via .NET. Er verwendet die Klasse SideBySidePdfComparer, um einen seitenweisen Vergleich durchzuführen und ein neues PDF zu erzeugen, das die Unterschiede nebeneinander anzeigt. Der Vergleich ist mit SideBySideComparisonOptions konfiguriert, wobei additional_change_marks auf True gesetzt ist, um Änderungen nicht nur auf der aktuellen Seite, sondern auch auf anderen Seiten hervorzuheben, und comparison_mode auf IgnoreSpaces gesetzt ist, um sich auf bedeutungsvolle Inhaltsunterschiede zu konzentrieren, indem Leerzeichenvariationen ignoriert werden.

## Vergleichen mit GraphicalPdfComparer

Bei der Zusammenarbeit an Dokumenten, insbesondere in professionellen Umgebungen, entstehen häufig mehrere Versionen derselben Datei.
Der bereitgestellte Code demonstriert, wie man bestimmte Seiten von zwei PDF-Dokumenten visuell vergleicht, indem man Aspose.PDF for Python via .NET verwendet. Durch die Verwendung des `GraphicalPdfComparer` Klasse, hebt Unterschiede zwischen den ersten Seiten der beiden PDFs hervor und erzeugt entsprechende Bilder, um diese Unterschiede darzustellen.

Sie können die folgenden Eigenschaften der Klasse festlegen:

- Resolution - Auflösung in DPI‑Einheiten für Ausgabebilder sowie für während des Vergleichs erzeugte Bilder.
- Color - die Farbe der Änderungsmarkierungen.
- Schwelle - Schwelle in Prozent ändern. Der Standardwert ist null. Das Festlegen eines Werts, der von null abweicht, ermöglicht es Ihnen, grafische Änderungen zu ignorieren, die für Sie unbedeutend sind.

Mit Aspose.PDF for Python via .NET ist es möglich, Dokumente und Seiten zu vergleichen und das Vergleichsergebnis in ein PDF-Dokument oder eine Bilddatei auszugeben.

Der `GraphicalPdfComparer` Die Klasse hat eine Methode, die es Ihnen ermöglicht, Seitenbildunterschiede in einer für die weitere Verarbeitung geeigneten Form zu erhalten: `get_difference(document1.pages[1], document2.pages[1])`.

Diese Methode gibt ein Objekt des `images_difference` Typ, der ein Bild der ersten zu vergleichenden Seite und ein Array von Unterschieden enthält.

Der `images_difference` Objekt ermöglicht es Ihnen, ein anderes Bild zu erzeugen und ein Bild der zweiten Seite zu erhalten, das durch Anwenden eines Arrays von Unterschieden auf das Originalbild verglichen wird. Um dies zu tun, verwenden Sie das `difference_to_image` und `get_destination_image` Methoden.

### PDF vergleichen mit der Get Difference-Methode

Der bereitgestellte Code definiert eine Methode `get_difference` die zwei PDF-Dokumente vergleicht und visuelle Darstellungen der Unterschiede zwischen ihnen erzeugt.

Diese Methode vergleicht die ersten Seiten von zwei PDF-Dateien und erzeugt zwei PNG‑Bilder:

- Ein Bild hebt die Unterschiede zwischen den Seiten in Rot hervor.
- Das andere Bild ist eine visuelle Darstellung der Ziel (zweiten) PDF‑Seite.

Dieser Prozess kann nützlich sein, um Änderungen oder Unterschiede zwischen zwei Versionen eines Dokuments visuell zu vergleichen.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_get_difference_method(infile1, infile2, outfile1, outfile2):
    # Open PDF documents
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)

    # Create comparer
    comparer = ap.comparison.GraphicalPdfComparer()

    # Compare specific pages
    images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

    # Get image showing differences in red over a white background
    diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
    diff_img.save(outfile1)

    # Get the second image representing the destination page
    dest_img = images_difference.get_destination_image()
    dest_img.save(outfile2)
```

### PDF vergleichen mit der CompareDocumentsToPdf-Methode

Der bereitgestellte Codeausschnitt verwendet die `compare_documents_to_pdf` Methode, die zwei Dokumente vergleicht und einen PDF-Bericht über die Vergleichsergebnisse erstellt.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_compare_documents_to_pdf_method(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Create comparer and set options
    pdf_comparer = ap.comparison.GraphicalPdfComparer()
    pdf_comparer.threshold = 3.0
    pdf_comparer.color = ap.Color.blue
    pdf_comparer.resolution = ap.devices.Resolution(300)

    # Compare and output to a PDF file
    pdf_comparer.compare_documents_to_pdf(document_1, document_2, outfile)
```

Dieses Beispiel demonstriert, wie man einen grafischen Vergleich von zwei gesamten PDF-Dokumenten mit Aspose.PDF for Python via .NET durchführt. Durch die Nutzung des `GraphicalPdfComparer` Klasse, erzeugt sie eine neue PDF-Datei, die die Unterschiede zwischen den Dokumenten visuell hervorhebt.

- Die Schwellenwert‑Eigenschaft ist auf 3,0 eingestellt, was bedeutet, dass kleinere Unterschiede unter diesem Prozentsatz bei der Vergleichsprüfung ignoriert werden und sich auf bedeutendere Änderungen konzentriert wird.
- Unterschiede werden in Blau markiert, indem die Farbeigenschaft auf ap.Color.blue gesetzt wird, was eine klare visuelle Unterscheidung ermöglicht.
- Der Vergleich wird bei einer Auflösung von 300 DPI durchgeführt, indem die Auflösungseigenschaft gesetzt wird, wodurch ein detailliertes und klares Ergebnis gewährleistet wird.

Der `compare_documents_to_pdf` Die Methode vergleicht alle Seiten beider Dokumente und gibt das Ergebnis in einer neuen PDF-Datei, compareDocumentsToPdf_out.pdf, aus, wobei die Unterschiede visuell hervorgehoben werden.

## Verwandte Themen

- [Erweiterte PDF-Operationen in Python](/pdf/de/python-net/advanced-operations/)
- [Arbeiten Sie mit PDF-Dokumenten in Python](/pdf/de/python-net/working-with-documents/)
- [Arbeiten mit PDF-Seiten in Python](/pdf/de/python-net/working-with-pages/)
- [Arbeiten mit PDF-Text in Python](/pdf/de/python-net/working-with-text/)
