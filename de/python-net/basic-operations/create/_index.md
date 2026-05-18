---
title: PDF-Dokument programmgesteuert erstellen
linktitle: PDF erstellen
type: docs
weight: 10
url: /de/python-net/create-document/
description: Diese Seite beschreibt, wie man ein PDF-Dokument von Grund auf mit der Aspose.PDF for Python via .NET Bibliothek erstellt.
TechArticle: true
AlternativeHeadline: Generieren von PDF-Dateien mit Aspose.PDF für Python
Abstract: In der Softwareentwicklung ist das programmgesteuerte Erzeugen von PDF-Dateien eine häufige Anforderung, insbesondere beim Erstellen von Berichten und anderen Dokumenten. Das Schreiben von individuellem Code für diese Aufgabe kann ineffizient und zeitaufwändig sein. Stattdessen können Entwickler **Aspose.PDF for Python via .NET** nutzen, eine robuste Lösung zum Erstellen von PDF-Dateien mit Python. Der Vorgang beinhaltet das Erzeugen eines `Document`-Objekts, das Hinzufügen eines `Page`-Objekts zur `Pages`-Sammlung des Dokuments, das Einfügen eines `TextFragment` in die `paragraphs`-Sammlung der Seite und anschließend das Speichern des Dokuments. Ein Beispiel‑Python‑Code‑Snippet demonstriert diese Schritte und zeigt, wie einfach PDF-Dateien mit Aspose.PDF generiert werden können.
---

Für Entwickler gibt es viele Szenarien, in denen es notwendig wird, PDF-Dateien programmatisch zu erzeugen. Möglicherweise müssen Sie PDF-Berichte und andere PDF-Dateien in Ihrer Software programmatisch generieren. Es ist ziemlich langwierig und ineffizient, eigenen Code und Funktionen von Grund auf neu zu schreiben. Um mit Python eine PDF-Datei zu erstellen, gibt es eine bessere Lösung – **Aspose.PDF for Python via .NET**.

## So erstellen Sie eine PDF-Datei mit Python

Um eine PDF-Datei mit Python zu erstellen, können die folgenden Schritte verwendet werden.

1. Erzeugen Sie ein Objekt von [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse
1. Hinzufügen [Seite](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) Objekt zu dem [Seiten](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) Sammlung des Document-Objekts
1. Hinzufügen [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) zu [Absätze](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) Sammlung der Seite
1. Speichern Sie das resultierende PDF Document

```python
import aspose.pdf as ap

# Initialize document object
document = ap.Document()
# Add page
page = document.pages.add()
# Add text to new page
page.paragraphs.add(ap.text.TextFragment("Hello World!"))
# Define output file path
output_pdf = "output.pdf"
# Save updated PDF
output_pdf = "output.pdf"
document.save(output_pdf)
```
