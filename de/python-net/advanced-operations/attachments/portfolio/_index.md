---
title: PDF-Portfolios in Python erstellen
linktitle: Portfolio
type: docs
weight: 20
url: /de/python-net/portfolio/
description: Erfahren Sie, wie Sie PDF-Portfolios in Python mit Aspose.PDF for Python via .NET erstellen und verwalten.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Portfolios mit eingebetteten Dateien in Python erstellen und bearbeiten
Abstract: Dieser Artikel erklärt, wie man PDF-Portfolios mit Aspose.PDF for Python via .NET erstellt und verwaltet. Erfahren Sie, wie Sie mehrere Dateitypen zu einem einzigen PDF-Portfolio bündeln, Dateien zu einer Document collection hinzufügen und Portfolio-Elemente programmgesteuert mit Python entfernen.
---

Die Erstellung eines PDF-Portfolios ermöglicht die Konsolidierung und Archivierung verschiedener Dateitypen in einem einzigen, konsistenten Dokument. Ein solches Dokument kann Textdateien, Bilder, Tabellenkalkulationen, Präsentationen und weiteres Material enthalten und sicherstellen, dass alle relevanten Materialien an einem Ort gespeichert und organisiert sind.

Das PDF-Portfolio hilft, Ihre Präsentation in hochwertiger Weise zu zeigen, wo immer Sie es verwenden. Im Allgemeinen ist das Erstellen eines PDF-Portfolios eine sehr aktuelle und moderne Aufgabe.

Verwenden Sie ein PDF-Portfolio, wenn Sie eine Sammlung verwandter Dateien zusammen verteilen möchten, wobei jede Datei in ihrem ursprünglichen Format innerhalb eines einzigen PDF-Containers bleibt.

## Wie man ein PDF-Portfolio erstellt

Aspose.PDF for Python via .NET ermöglicht das Erstellen von PDF-Portfolio-Dokumenten mit der [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Fügen Sie eine Datei in ein document.collection Objekt ein, nachdem Sie es mit der [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) class. Wenn die Dateien hinzugefügt wurden, verwenden Sie die Document class’ [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode zum Speichern des Portfoliodokuments.

Das folgende Beispiel verwendet eine Microsoft Excel‑Datei, ein Word‑Dokument und eine Bilddatei, um ein PDF‑Portfolio zu erstellen.

Der untenstehende Code ergibt das folgende Portfolio.

### Ein PDF‑Portfolio erstellt mit Aspose.PDF for Python

![Ein PDF‑Portfolio erstellt mit Aspose.PDF for Python](working-with-pdf-portfolio_1.jpg)

```python
import aspose.pdf as ap

def create_pdf_portfolio(input_files, outfile):
    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_files[0])
    word = ap.FileSpecification(input_files[1])
    image = ap.FileSpecification(input_files[2])

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(outfile)
```

## Dateien aus PDF-Portfolio entfernen

Um Dateien aus einem PDF-Portfolio zu löschen/entfernen, versuchen Sie, die folgenden Codezeilen zu verwenden.

```python
import aspose.pdf as ap

def remove_files_from_pdf_portfolio(infile, outfile):
    # Open document
    document = ap.Document(infile)
    document.collection.delete()

    # Save updated file
    document.save(outfile)
```

## Verwandte Anhangsthemen

- [Arbeiten mit PDF-Anhängen in Python](/pdf/de/python-net/attachments/)
- [Anhänge zu PDF in Python hinzufügen](/pdf/de/python-net/add-attachment-to-pdf-document/)
- [Anhänge aus PDF in Python entfernen](/pdf/de/python-net/removing-attachment-from-an-existing-pdf/)

