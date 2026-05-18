---
title: PDF-Dateien in Python optimieren
linktitle: PDF optimieren
type: docs
weight: 30
url: /de/python-net/optimize-pdf/
description: Erfahren Sie, wie Sie PDF-Dateigröße in Python mit Aspose.PDF optimieren, komprimieren und reduzieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF‑Seiten mit Python komprimieren
Abstract: Dieser Artikel bietet eine umfassende Anleitung zur Optimierung von PDF‑Dateien, um deren Größe zu reduzieren und die Leistung auf verschiedenen Plattformen wie Webseiten, E‑Mails und Speichersystemen zu verbessern. Die Optimierungstechniken umfassen die Reduzierung der Bildgrößen, das Entfernen nicht verwendeter Ressourcen und das Entbetten von Schriftarten. Es werden spezifische Methoden zur Optimierung von PDFs für das Web und zur Verringerung der Gesamtdateigröße diskutiert, wobei die `Optimize`‑ und `OptimizeResources`‑Methoden in Aspose.PDF for Python verwendet werden. Die Anpassung von Optimierungsstrategien ist über `OptimizationOptions` möglich, was gezielte Aktionen wie das Komprimieren von Bildern, das Entfernen nicht verwendeter Objekte und Streams, das Verknüpfen doppelter Streams und das Entbetten von Schriftarten erlaubt. Weitere Strategien umfassen das Flatten von Anmerkungen, das Entfernen von Formularfeldern und die Umwandlung von PDF‑Dateien von RGB zu Graustufen, um die Größe weiter zu verringern. Der Artikel hebt zudem die Verwendung der FlateDecode‑Kompression zur Bildoptimierung hervor und sorgt damit für eine effektive PDF‑Dateiverwaltung bei gleichzeitigem Erhalt von Qualität und Funktionalität.
---

Ein PDF-Dokument kann manchmal zusätzliche Daten enthalten. Die Reduzierung der Größe einer PDF-Datei hilft Ihnen, die Netzwerkübertragung und den Speicher zu optimieren. Das ist besonders praktisch für die Veröffentlichung auf Webseiten, das Teilen in sozialen Netzwerken, das Versenden per E‑Mail oder das Archivieren im Speicher. Wir können mehrere Techniken einsetzen, um PDFs zu optimieren:

Verwenden Sie diese Seite, wenn Sie die PDF-Größe für die Webübertragung, das Teilen per E‑Mail, Speicherersparnisse oder druckfreundliche Ausgaben reduzieren müssen, ohne das Document von Grund auf neu zu erstellen.

- Optimieren Sie den Seiteninhalt für das Online-Browsing
- Alle Bilder verkleinern oder komprimieren
- Wiederverwendung von Seiteninhalten aktivieren
- Doppelte Streams zusammenführen
- Einbettung von Schriftarten aufheben
- Unbenutzte Objekte entfernen
- Flachlegen von Formularfeldern entfernen
- Annotationen entfernen oder flachlegen

{{% alert color="primary" %}}

 Eine ausführliche Erklärung der Optimierungsmethoden finden Sie auf der Seite "Optimization Methods Overview".

{{% /alert %}}

## PDF Document für das Web optimieren

Optimierung, oder Linearisation für das Web, bezeichnet den Prozess, eine PDF-Datei für die Online-Durchsicht mit einem Webbrowser geeignet zu machen. Um eine Datei für die Webanzeige zu optimieren:

1. Öffnen Sie das Eingabedokument in einem [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Objekt.
1. Verwenden Sie das [Optimieren](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode.
1. Speichern Sie das optimierte Dokument mit der [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode.

Der folgende Codeabschnitt zeigt, wie man ein PDF-Dokument für das Web optimiert.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def optimize_pdf(infile, outfile):
    document = ap.Document(infile)
    document.optimize()
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## PDF Größe reduzieren

Der [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode ermöglicht es Ihnen, die Dokumentgröße zu reduzieren, indem unnötige Informationen entfernt werden. Standardmäßig funktioniert diese Methode wie folgt:

- Ressourcen, die nicht auf den Dokumentseiten verwendet werden, werden entfernt
- Gleiche Ressourcen werden zu einem Objekt zusammengefasst.
- Unbenutzte Objekte werden gelöscht

Das untenstehende Snippet ist ein Beispiel. Beachten Sie jedoch, dass diese Methode das Schrumpfen des Dokuments nicht garantieren kann.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def reduce_size_pdf(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## Optimierungsstrategiemanagement

Wir können die Optimierungsstrategie ebenfalls anpassen. Derzeit ist die [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode verwendet 5 Techniken. Diese Techniken können mit der OptimizeResources()-Methode angewendet werden mit dem [Optimierungsoptionen](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) Parameter.

### Verkleinern oder Komprimieren aller Bilder

Wir haben zwei Möglichkeiten, mit Bildern zu arbeiten: die Bildqualität reduzieren und/oder ihre Auflösung ändern. Auf jeden Fall, [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) sollte angewendet werden. Im folgenden Beispiel verkleinern wir Bilder, indem wir die ImageQuality auf 50 reduzieren.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def shrinking_or_compressing_all_images(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Entfernen ungenutzter Objekte

Ein PDF-Dokument enthält manchmal PDF-Objekte, die von keinem anderen Objekt im Dokument referenziert werden. Das kann beispielsweise passieren, wenn eine Seite aus dem Dokumenten‑Seitenbaum entfernt wird, das Seitenobjekt selbst jedoch nicht entfernt wird. Das Entfernen dieser Objekte macht das Dokument nicht ungültig, sondern verkleinert es lediglich.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_objects(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedObjects option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Entfernen nicht verwendeter Streams

Manchmal enthält das Dokument ungenutzte Ressourcen‑Streams. Diese Streams sind nicht „unused objects“, weil sie von einem Seiten‑Ressourcen‑Dictionary referenziert werden. Daher werden sie nicht mit einer „remove unused objects“-Methode entfernt. Aber diese Streams werden nie in den Seiteninhalten verwendet. Das kann vorkommen, wenn ein Bild von der Seite entfernt wurde, aber nicht aus den Seitenressourcen. Auch tritt diese Situation häufig auf, wenn Seiten aus dem Dokument extrahiert werden und Dokumentseiten „common“ Ressourcen haben, das heißt, dasselbe Resources‑Objekt. Die Seiteninhalte werden analysiert, um zu bestimmen, ob ein Ressourcen‑Stream verwendet wird oder nicht. Ungebrauchte Streams werden entfernt. Das verringert manchmal die Dokumentgröße. Die Verwendung dieser Technik ist dem vorherigen Schritt ähnlich:

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Verknüpfung doppelter Streams

Einige Dokumente können mehrere identische Ressourcen-Streams enthalten (wie zum Beispiel Bilder). Das kann vorkommen, beispielsweise wenn ein Dokument mit sich selbst verkettet wird. Das Ausgabedokument enthält dann zwei unabhängige Kopien desselben Ressourcen-Streams. Wir analysieren alle Ressourcen-Streams und vergleichen sie. Wenn Streams dupliziert sind, werden sie zusammengeführt, das heißt, es bleibt nur eine Kopie übrig. Die Verweise werden entsprechend angepasst und die Kopien des Objekts werden entfernt. In einigen Fällen hilft das, die Dokumentgröße zu verringern.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def linking_duplicate_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set link_duplicate_streams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplicate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Schriftarten entbetten

Wenn das Dokument eingebettete Schriftarten verwendet, bedeutet das, dass alle Schriftartdaten im Dokument gespeichert sind. Der Vorteil ist, dass das Dokument unabhängig davon, ob die Schriftart auf dem Rechner des Benutzers installiert ist, angezeigt werden kann. Allerdings vergrößert das Einbetten von Schriftarten das Dokument. Die Methode zum Entfernen eingebetteter Schriftarten entfernt alle eingebetteten Schriftarten. Damit verringert sich die Dateigröße, aber das Dokument selbst kann unlesbar werden, wenn die korrekte Schriftart nicht installiert ist.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def unembed_fonts(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set unembed_fonts option
    optimize_options = ap.optimization.OptimizationOptions()
    optimize_options.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimize_options)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Die Optimierungsressourcen wenden diese Methoden auf das Dokument an. Wenn eine dieser Methoden angewendet wird, wird die Dokumentgröße höchstwahrscheinlich sinken. Wenn keine dieser Methoden angewendet wird, ändert sich die Dokumentgröße nicht, was offensichtlich ist.

## Weitere Möglichkeiten, die PDF-Dokumentgröße zu reduzieren

### Entfernen oder Flachlegen von Anmerkungen

Anmerkungen können gelöscht werden, wenn sie nicht erforderlich sind. Wenn sie benötigt werden, aber keine zusätzliche Bearbeitung erfordern, können sie flachgelegt werden. Beide Techniken reduzieren die Dateigröße.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_annotations(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(outfile)
```

### Entfernen von Formularfeldern

Wenn das PDF-Dokument AcroForms enthält, können wir versuchen, die Dateigröße zu reduzieren, indem wir Formularfelder flachlegen.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_forms(infile, outfile):
    # Load source PDF form
    doc = ap.Document(infile)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Ein PDF vom RGB-Farbraum in Graustufen konvertieren

Eine PDF-Datei besteht aus Text, Bild, Anhang, Annotationen, Diagrammen und anderen Objekten. Möglicherweise stoßen Sie auf die Anforderung, ein PDF vom RGB-Farbraum in Graustufen zu konvertieren, damit der Druck dieser PDF-Dateien schneller erfolgt. Außerdem wird bei der Konvertierung in Graustufen die Dateigröße reduziert, kann jedoch ebenso zu einer Verschlechterung der Dokumentqualität führen. Diese Funktion wird derzeit vom Pre‑Flight‑Tool von Adobe Acrobat unterstützt, aber im Bereich der Office‑Automation ist Aspose.PDF die ultimative Lösung, um solche Vorteile bei der Dokumentenmanipulation zu bieten. Um diese Anforderung zu erfüllen, kann das folgende Code‑Snippet verwendet werden.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def сonvert_PDF_from_RGB_colorspace_to_grayscale(infile, outfile):
    document = ap.Document(infile)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(outfile)
```

### FlateDecode‑Komprimierung

Aspose.PDF for Python via .NET bietet Unterstützung für die FlateDecode-Kompression für die PDF-Optimierungsfunktionalität. Der folgende Codeausschnitt unten zeigt, wie man die Option in der Optimierung verwendet, um Bilder mit **FlateDecode**-Kompression zu speichern:

```python
import aspose.pdf as ap
from os import path, stat
import sys


def using_flatedecode_compression(infile, outfile):

    # Open Document
    doc = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = (
        ap.optimization.ImageEncoding.FLATE
    )
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(outfile)
```

## Verwandte Dokumentthemen

- [Arbeiten mit PDF-Dokumenten in Python](/pdf/de/python-net/working-with-documents/)
- [PDF-Dateien in Python zusammenführen](/pdf/de/python-net/merge-pdf-documents/)
- [PDF-Dateien in Python teilen](/pdf/de/python-net/split-document/)
- [PDF‑Dokumente in Python manipulieren](/pdf/de/python-net/manipulate-pdf-document/)

