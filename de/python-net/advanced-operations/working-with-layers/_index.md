---
title: Arbeiten mit PDF-Ebenen mit Python
linktitle: Arbeiten mit PDF-Ebenen
type: docs
weight: 50
url: /de/python-net/working-with-pdf-layers/
description: Erfahren Sie, wie Sie PDF‑Ebenen in Python hinzufügen, sperren, extrahieren, flachlegen und zusammenführen können.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verwalten Sie PDF‑Ebenen mit Python
Abstract: Dieser Artikel erklärt, wie man mit PDF‑Ebenen (Optional Content Groups) mithilfe von Aspose.PDF for Python via .NET arbeitet. Erfahren Sie, wie man Ebenen hinzufügt, die Sichtbarkeit von Ebenen sperrt, Ebeneninhalte extrahiert, geschichtete Inhalte abflacht und Ebenen zu einer zusammenführt.
---

PDF‑Ebenen, die auch als Optional Content Groups (OCGs) bezeichnet werden, ermöglichen es Ihnen, Inhalte in separate visuelle Gruppen zu organisieren, die in kompatiblen PDF‑Betrachtern ein- oder ausgeblendet werden können. In Aspose.PDF basieren Layer‑Operationen auf dem [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) API.

Mit Aspose.PDF for Python via .NET können Sie:

- Fügen Sie einer Seite mehrere Ebenen hinzu.
- Ebenen sperren und entsperren, um das Sichtbarkeitsverhalten zu steuern.
- Extrahieren Sie Ebenen in separate Dateien oder Streams.
- Den geschichteten Inhalt auf der Seite flachlegen.
- Mehrere Ebenen zu einer Ebene zusammenführen.

## Ebenen zu einem PDF hinzufügen

Dieses Beispiel erstellt ein PDF mit drei Ebenen. Es verwendet ein [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), fügt ein [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), und fügt hinzu [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) Objekte zu dieser Seite.

1. Neu erstellen [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) und füge ein [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Erstelle und füge die rote Ebene hinzu.
1. Erstelle und füge die grüne Ebene hinzu.
1. Erstelle und füge die blaue Ebene hinzu.
1. Speichern Sie das PDF-Dokument.

Das resultierende PDF wird drei separate Ebenen enthalten: eine rote Linie, eine grüne Linie und eine blaue Linie. Jede kann in PDF-Readern, die schichteten Inhalt unterstützen, ein- oder ausgeschaltet werden.

```python
import aspose.pdf as ap

def add_layers(outfile: str) -> None:
    document = ap.Document()
    page = document.pages.add()

    # Red layer
    layer = ap.Layer("oc1", "Red Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(1, 0, 0))
    layer.contents.append(ap.operators.MoveTo(500, 700))
    layer.contents.append(ap.operators.LineTo(400, 700))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Green layer
    layer = ap.Layer("oc2", "Green Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 1, 0))
    layer.contents.append(ap.operators.MoveTo(500, 750))
    layer.contents.append(ap.operators.LineTo(400, 750))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Blue layer
    layer = ap.Layer("oc3", "Blue Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 0, 1))
    layer.contents.append(ap.operators.MoveTo(500, 800))
    layer.contents.append(ap.operators.LineTo(400, 800))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    document.save(outfile)
    print(f"Layers added successfully. File saved at {outfile}")
```

## PDF-Ebene sperren

Dieses Beispiel öffnet ein PDF, sperrt eine bestimmte Ebene auf der ersten Seite und speichert die aktualisierte Datei.

Das Sperren einer Ebene verhindert, dass Benutzer in unterstützten PDF‑Betrachtern den Sichtbarkeitsstatus dieser Ebene ändern. Ebenen werden von einer Seite aus zugegriffen und über die Ebenensammlung der Seite verwaltet.

Verfügbare Methoden und Eigenschaft:

- [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) sperrt die Ebene.
- [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) entsperrt die Ebene.
- [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties) gibt den aktuellen Sperrzustand zurück.

1. Öffnen Sie das PDF-Dokument.
1. Greifen Sie auf die erste Seite des PDF zu.
1. Prüfen Sie, ob die Seite Ebenen hat.
1. Rufe die erste Ebene ab und sperre sie.
1. Speichere das aktualisierte PDF.

Wenn das PDF Ebenen enthält, wird die erste Ebene gesperrt, sodass ihr Sichtbarkeitsstatus vom Benutzer nicht geändert werden kann. Wenn keine Ebenen gefunden werden, wird stattdessen eine Meldung ausgegeben.

```python
import aspose.pdf as ap

def lock_layer(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) > 0:
        layer = page.layers[0]
        layer.lock()
        document.save(outfile)
        print(f"Layer locked successfully. File saved at {outfile}")
    else:
        print("No layers found in the document.")
```

## PDF-Layer-Elemente extrahieren

Dieses Beispiel verwendet die Aspose.PDF for Python via .NET-Bibliothek, um einzelne Ebenen der ersten Seite eines PDF-Dokuments zu extrahieren und jede Ebene als separate PDF-Datei zu speichern, indem es [`Layer.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

Um ein neues PDF aus einer Ebene zu erstellen, kann der folgende Codeausschnitt verwendet werden:

1. PDF laden [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Zugriff auf Ebenen auf Seite 1 bis [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Prüfen Sie, ob Ebenen existieren.
1. Durchlaufe die Ebenen und speichere jede.

```python
import aspose.pdf as ap

def extract_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    index = 1
    for layer in layers:
        output_file = outfile.replace(".pdf", f"{index}.pdf")
        layer.save(output_file)
        print(f"Layer {index} saved to {output_file}")
        index += 1
```

Es ist möglich, PDF‑Ebenen‑Elemente zu extrahieren und sie in einen neuen PDF‑Dateistream zu speichern:

```python
from io import FileIO
import aspose.pdf as ap

def extract_layers_stream(infile: str, outfile: str) -> None:
    document = ap.Document(infile)

    if len(document.pages[1].layers) == 0:
        print("No layers found in the document.")
        return

    layer = document.pages[1].layers[0]

    with FileIO(outfile, "wb") as output_layer:
        layer.save(output_layer)
    print(f"Layer extracted to stream: {outfile}")
```

## Ein geschichtetes PDF flachlegen

Dieses Skript verwendet Aspose.PDF for Python via .NET, um alle Ebenen auf der ersten Seite eines PDF-Dokuments flachzulegen. Das Flachlegen fasst den visuellen Inhalt jeder Ebene zu einer einheitlichen Ebene zusammen, wodurch das Drucken, Teilen oder Archivieren erleichtert wird, ohne die visuelle Treue oder ebenspezifische Daten zu verlieren. Der Vorgang wird ausgeführt mit [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

1. Laden Sie das PDF-Dokument.
1. Zugriff auf Ebenen auf Seite 1.
1. Prüfen Sie, ob Ebenen existieren.
1. Jede Ebene zusammenfassen mit `layer.flatten(True)`.
1. Speichern Sie das geänderte Dokument.

```python
import aspose.pdf as ap

def flatten_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    for layer in layers:
        layer.flatten(True)

    document.save(outfile)
    print(f"Layers flattened successfully. File saved at {outfile}")
```

## Alle Ebenen in einem PDF zu einer zusammenführen

Dieser Codeausschnitt verwendet Aspose.PDF, um alle Ebenen auf der ersten Seite eines PDFs zu einer einheitlichen Ebene mit einem benutzerdefinierten Namen zusammenzuführen, indem er verwendet [`Page.merge_layers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods).

1. Laden Sie das PDF-Dokument.
1. Greifen Sie auf Seite 1 zu und rufen Sie deren Ebenen ab.
1. Prüfen Sie, ob Ebenen existieren.
1. Definieren Sie einen neuen Ebenennamen.
1. Führen Sie die Ebenen zu einer zusammen.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap

def merge_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) == 0:
        print("No layers found in the document.")
        return

    new_layer_name = "LayerNew"
    page.merge_layers(new_layer_name)
    document.save(outfile)
    print(f"Layers merged successfully. File saved at {outfile}")
```

## Verwandte Ebenen-Themen

- [Arbeiten Sie mit PDF-Seiten in Python](/pdf/de/python-net/working-with-pages/)
- [Tabellen in PDF mit Python bearbeiten](/pdf/de/python-net/working-with-tables/)
- [PDF‑Seiten in Python hinzufügen](/pdf/de/python-net/add-pages/)
