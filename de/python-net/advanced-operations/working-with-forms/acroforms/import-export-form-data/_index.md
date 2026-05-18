---
title: Formulardaten importieren und exportieren
linktitle: Formulardaten importieren und exportieren
type: docs
weight: 80
url: /de/python-net/import-export-form-data/
description: Importieren und Exportieren von AcroForm-Felddaten in XML-, FFD-, XFDF- und JSON-Formaten mit Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Import- und Exporttechniken mit Aspose.PDF for Python via .NET.
Abstract: Diese Zusammenstellung präsentiert eine umfassende Sammlung von Import‑ und Exporttechniken für Formulardaten unter Verwendung von Aspose.PDF for Python via .NET. Sie deckt Workflows zur Integration von PDF‑Formularen mit externen Datenformaten einschließlich XML, FDF, XFDF und JSON ab. Benutzer können die massenhafte Formularausfüllung automatisieren, indem sie strukturierte Daten in interaktive Felder importieren, oder Feldwerte für Analyse, Backup oder Integration mit anderen Systemen extrahieren. Die Beispiele zeigen, wie PDF‑Formulare gebunden, Daten zwischen Formaten übertragen und aktualisierte Dokumente gespeichert werden, wodurch eine skalierbare und konsistente Dokumentverarbeitung über verschiedene Anwendungen hinweg ermöglicht wird.
---

Diese Seite zeigt gängige Arbeitsabläufe zum Importieren und Exportieren von AcroForm-Daten mit Aspose.PDF for Python via .NET. Alle Vorgänge verwenden die [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) Fassade.

## Formularfelddaten aus XML importieren

Verwenden Sie diesen Ansatz, um ein PDF-Formular mit externen XML-Daten zu füllen.

1. Erstelle ein `Form` Objekt.
1. Binden Sie das Eingabe-PDF.
1. Öffnen Sie die XML-Datendatei.
1. XML-Daten in das Formular importieren.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xml(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xml(f)

    form.save(output_file_name)
```

## Formulardaten in XML exportieren

Diese Methode exportiert Formularfeldwerte aus einem PDF-Dokument nach XML.

1. Erstelle ein `Form` Objekt.
1. Binden Sie das Eingabe-PDF.
1. Öffnen Sie die XML‑Ausgabedatei.
1. Formulardaten nach XML exportieren.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xml(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)
    with FileIO(output_file_name, "w") as f:
        form.export_xml(f)
```

## Formularfelddaten aus FDF importieren

Der `import_data_from_fdf` Methode importiert Formulardaten aus einer FDF (Forms Data Format)-Datei in ein PDF-Formular.

1. Erstelle ein `Form` Objekt.
1. Binden Sie das Eingabe-PDF.
1. Importieren Sie die Formulardaten mit `import_fdf()`.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_fdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_fdf(f)
        form.save(output_file_name)
```

## Formularfelddaten nach FDF exportieren

Dieses Beispiel exportiert Formulardaten aus einem PDF-Dokument in eine FDF-Datei.

1. Erstelle ein `Form` Objekt.
1. Binden Sie das PDF-Dokument.
1. Formulardaten exportieren mit `export_fdf()`.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_fdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_fdf(f)
```

## Importieren von FormField-Daten aus XFDF

Verwenden Sie diese Methode, um Formularfelddaten aus einer XFDF (XML Forms Data Format)-Datei in ein PDF-Formular zu importieren.

1. Erstelle ein `Form` Objekt.
1. Binden Sie das Eingabe-PDF.
1. Formulardaten aus einer XFDF-Datei importieren.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xfdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xfdf(f)
        form.save(output_file_name)
```

## Formulardaten in XFDF exportieren

Dieser Code exportiert Formulardaten aus einem PDF-Dokument in eine XFDF-Datei.

1. Erstelle ein `Form` Objekt.
1. Binden Sie das Eingabe-PDF.
1. Formulardaten nach XFDF exportieren.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xfdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_xfdf(f)
```

## Daten aus einem anderen PDF importieren

Dieses Beispiel überträgt Formulardaten von einer Quell-PDF zu einer Ziel-PDF, indem es XFDF in einen In-Memory-Stream exportiert und diesen in die Ziel-Form importiert.

1. Erstelle Quelle und Ziel `Form` Objekte.
1. Binden Sie die Quell- und Ziel-PDFs.
1. Formulardaten aus der Quell-PDF exportieren.
1. Formulardaten in das Ziel-PDF importieren.
1. Speichern Sie das aktualisierte Ziel-PDF.

```python
from io import StringIO
import aspose.pdf as ap

def import_data_from_another_pdf(source_pdf_name, destination_pdf_name, output_file_name):
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    form_source.bind_pdf(source_pdf_name)
    form_dest.bind_pdf(destination_pdf_name)

    with StringIO() as xfdf_stream:
        form_source.export_xfdf(xfdf_stream)
        xfdf_stream.seek(0)
        form_dest.import_xfdf(xfdf_stream)

    form_dest.save(output_file_name)
```

## Formularfelder in JSON extrahieren

Diese Methode exportiert Formularfelder in eine JSON-Datei durch Verwendung `export_json()`.

1. Erstelle ein `Form` Objekt.
1. Öffnen Sie die JSON-Ausgabedatei.
1. Formularfelder exportieren mittels `export_json()`.

```python
from io import FileIO
import aspose.pdf as ap

def extract_form_fields_to_json(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    with FileIO(output_file_name, "w") as json_file:
        form.export_json(json_file, True)
```

## Formularfelder in JSON-Dokument extrahieren

Dieses Beispiel erstellt ein benutzerdefiniertes JSON-Dokument aus den Namen und Werten von Formularfeldern.

1. Erstellen Sie ein Form-Objekt aus der Eingabedatei.
1. Initialisieren Sie ein leeres Wörterbuch, um FormField-Daten zu speichern.
1. Iterieren Sie über alle Formularfelder und extrahieren Sie deren Werte.
1. Serialisieren Sie das Formulardaten‑Wörterbuch in einen JSON‑String mit einer 4‑Leerzeichen‑Einrückung.
1. Schreiben Sie die JSON‑Zeichenkette in die Ausgabedatei mit UTF‑8‑Kodierung.

```python
import json
import aspose.pdf as ap

def extract_form_fields_to_json_doc(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    form_data = {}
    for field_name in form.field_names:
        form_data[field_name] = form.get_field(field_name)

    json_string = json.dumps(form_data, indent=4)

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Verwandte Themen (Facade-Ansatz)

- [XML-Daten importieren](/pdf/de/python-net/import-xml-data/)
- [FDF-Daten importieren](/pdf/de/python-net/import-fdf-data/)
- [XFDF-Daten importieren](/pdf/de/python-net/import-xfdf-data/)
- [JSON-Daten importieren](/pdf/de/python-net/import-json-data/)
- [Export nach XML](/pdf/de/python-net/export-to-xml/)
- [Exportieren nach FDF](/pdf/de/python-net/export-to-fdf/)
- [Exportieren nach XFDF](/pdf/de/python-net/export-to-xfdf/)
- [Exportieren nach JSON](/pdf/de/python-net/export-to-json/)
