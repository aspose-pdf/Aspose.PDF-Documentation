---
title: PDF-Dokument programmgesteuert speichern
linktitle: PDF speichern
type: docs
weight: 30
url: /de/python-net/save-pdf-document/
description: Erfahren Sie, wie Sie eine PDF-Datei in Python mit der Aspose.PDF for Python via .NET-Bibliothek speichern. Speichern Sie das PDF-Dokument im Dateisystem, in einen Stream und in Webanwendungen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Speichern von PDF-Dokumenten mit der Aspose.PDF-Bibliothek in Python
Abstract: Der Artikel bietet Anleitungen zum Speichern von PDF-Dokumenten mithilfe der Aspose.PDF-Bibliothek in Python. Er beschreibt drei Hauptmethoden zum Speichern von PDFs – im Dateisystem, in einen Stream und in spezifischen Formaten wie PDF/A oder PDF/X. Die `save()`-Methode der `Document`-Klasse ist dabei zentral. Um ein PDF im Dateisystem zu speichern, kann ein Dokument erstellt oder manipuliert werden, z. B. durch Hinzufügen einer neuen Seite, und anschließend direkt an einem Pfad gespeichert werden. Beim Speichern in einen Stream erlauben die Überladungen der `Save`-Methode das Schreiben eines Dokuments in ein Stream‑Objekt. Zusätzlich erklärt der Artikel, wie Dokumente im PDF/A- oder PDF/X-Format gespeichert werden können, die Standards für Langzeitarchivierung bzw. Grafikdatenaustausch darstellen. Dieser Vorgang erfordert die Vorbereitung des Dokuments mit der `convert`‑Methode, bevor es gespeichert wird. Die bereitgestellten Python‑Code‑Snippets demonstrieren jeden Ansatz und zeigen die praktische Anwendung dieser Methoden.
---

## PDF-Dokument im Dateisystem speichern

Sie können das erstellte oder bearbeitete PDF-Dokument im Dateisystem speichern, indem Sie [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode von [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse.

```python
import aspose.pdf as ap

def save_document_to_file(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    document.save(outfile)
```

## PDF-Dokument in Stream speichern

Sie können das erstellte oder manipulierte PDF-Dokument auch in einen Stream speichern, indem Sie Überladungen von `Save` Methoden.

```python
import aspose.pdf as ap
import io

def save_document_to_stream(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    with io.FileIO(outfile, 'w') as stream:
        document.save(stream)
```

## PDF/A‑ oder PDF/X‑Format speichern

Sie können ein Dokument ganz einfach in einer bestimmten PDF‑Version speichern, z. B. PDF/A oder PDF/X. In diesem Fall müssen wir die convert-Methode aufrufen, bevor wir das Dokument speichern.

PDF/A ist eine ISO‑standardisierte Version des Portable Document Format (PDF) zur Nutzung bei der Archivierung und langfristigen Aufbewahrung elektronischer Dokumente.
PDF/A unterscheidet sich von PDF dadurch, dass es Funktionen verbietet, die für die langfristige Archivierung nicht geeignet sind, wie zum Beispiel Schriftartenverlinkung (im Gegensatz zur Schriftarteinbettung) und Verschlüsselung. ISO‑Anforderungen an PDF/A‑Viewer umfassen Richtlinien für das Farbmanagement, Unterstützung eingebetteter Schriftarten und eine Benutzeroberfläche zum Lesen eingebetteter Anmerkungen.

PDF/X ist ein Teil der PDF‑ISO‑Norm. Der Zweck von PDF/X besteht darin, den Grafikaustausch zu erleichtern, und es hat daher eine Reihe von druckbezogenen Anforderungen, die nicht für Standard‑PDF‑Dateien gelten.

In beiden Fällen, die [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode wird verwendet, um die Dokumente zu speichern, während die Dokumente mithilfe von [konvertieren](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode.

```python
import aspose.pdf as ap
import io


def save_document_as_standard(infile, outfile, logfile):
    document = ap.Document(infile)
    document.pages.add()
    document.convert(logfile, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
