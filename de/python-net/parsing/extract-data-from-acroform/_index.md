---
title: Daten aus AcroForm mit Python extrahieren
linktitle: Daten aus AcroForm extrahieren
type: docs
weight: 50
url: /de/python-net/extract-data-from-acroform/
description: Aspose.PDF macht es einfach, Formulardaten aus PDF-Dateien zu extrahieren. Erfahren Sie, wie Sie Daten aus AcroForms extrahieren und in JSON, XML oder FDF format speichern.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Daten aus AcroForm mit Python extrahiert
Abstract: Der Artikel bietet eine umfassende Anleitung zur Verwendung von Aspose.PDF for Python, um FormField in PDF-Dokumenten zu verwalten. Er beschreibt verschiedene Methoden zum Extrahieren, Manipulieren und Exportieren von Formulardaten aus PDFs. Der Artikel beginnt mit einer Demonstration, wie FormField‑Werte extrahiert und in einem Dictionary gespeichert werden, wobei die Daten anschließend im JSON‑Format ausgegeben werden. Weiterhin wird gezeigt, wie Formulardaten direkt in JSON‑Dateien exportiert werden können, was die Datenserialisierung verbessert. Zusätzlich behandelt der Artikel den Export von Formulardaten in andere Formate wie XML, FDF (Forms Data Format) und XFDF, die für den Datenaustausch und die strukturierte Datenspeicherung nützlich sind. Jeder Abschnitt enthält Python‑Code‑Snippets, die das Verständnis und die Implementierung erleichtern. Insgesamt dient der Artikel als praktische Ressource für Entwickler, die die PDF‑Formularverarbeitung in ihre Python‑Anwendungen integrieren möchten.
---

## Formularfelder aus PDF-Dokument extrahieren

[Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) von dem `aspose.pdf.facades` Namespace bietet eine einfache Möglichkeit, AcroForm-Felddaten zu lesen, ohne das komplette Dokumentenobjektmodell zu öffnen. Iterieren Sie über `form.field_names` um jeden im Formular vorhandenen Feldnamen zu erhalten, rufen Sie dann `form.get_field(name)` um seinen aktuellen Wert abzurufen.

1. Konstruiere ein `Form` Objekt, indem Sie den Eingabedateipfad übergeben.
1. Durchlaufen `form.field_names` um alle Feldnamen aufzulisten.
1. Anruf `form.get_field(name)` Für jeden Namen das Ergebnis in einem Wörterbuch speichern.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = self.dataDir + infile
    form = apdf.facades.Form(path_infile)

    form_values = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_values[formField] = form.get_field(formField)

    print(form_values)
```

## Formularfeldwert anhand des Titels abrufen

Wenn Sie den genauen Feldnamen (title) kennen, der im PDF-Formular definiert ist, können Sie dessen Wert direkt abrufen mit `form.get_field(name)` ohne die gesamte Feldsammlung zu durchlaufen. Dies ist der schnellste Ansatz, wenn nur bestimmte Felder benötigt werden.

1. Konstruiere ein [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) Objekt mit dem Eingabedateipfad.
1. Anruf `form.get_field("FieldName")` Verwenden Sie den genauen Feldtitel, wie er im PDF angezeigt wird.
1. Verwenden Sie den zurückgegebenen Zeichenfolgenwert nach Bedarf in Ihrer Anwendung.

```python

    import aspose.pdf as apdf

    form = apdf.facades.Form(path_infile)

    # Retrieve a single field value by its name
    value = form.get_field("FirstName")
    print(value)
```

## Formularfelder aus PDF-Dokument in JSON extrahieren

Es gibt zwei Möglichkeiten, AcroForm-Daten nach JSON zu exportieren. Die erste verwendet die eingebaute `export_json` Methode auf [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form), die alle Felddaten direkt in einen Dateistream in einem einzigen Aufruf serialisiert.

1. Konstruiere ein `Form` Objekt mit dem Eingabedateipfad.
1. Öffnen Sie die Ausgabedatei als Binärstrom mit `FileIO`.
1. Anruf `form.export_json(stream, True)` die JSON-Ausgabe schreiben.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

Der zweite Ansatz erstellt ein Python-Wörterbuch aus `field_names` und `get_field`, dann serialisiert es mit `json.dumps`. Verwenden Sie dies, wenn Sie die Daten vor dem Schreiben transformieren oder filtern müssen.

1. Durchlaufen `form.field_names` und ein Wörterbuch mit Feldwerten füllen.
1. Serialisieren Sie das Wörterbuch mit `json.dumps(form_data, indent=4)`.
1. Schreiben Sie die resultierende JSON-Zeichenkette in die Ausgabedatei.

```python

    import aspose.pdf as apdf
    from os import path
    import json

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Daten aus einer PDF-Datei in XML extrahieren

XML-Export ist nützlich, um PDF-Formulardaten in Systeme zu integrieren, die strukturierte XML-Feeds oder Schemas verarbeiten. Der [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) Klasse liefert `export_xml` um die Konvertierung in einem Schritt zu erledigen.

1. Erstelle ein `Form` Instanz und binden Sie das PDF mit `form.bind_pdf(path)`.
1. Öffnen Sie die Ausgabedatei als Binärstrom.
1. Anruf `form.export_xml(stream)` alle Felddaten als XML schreiben.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export data to XML file
    with FileIO(path_outfile, "w") as f:
        form.export_xml(f)
```

## Exportieren von Daten nach FDF aus einer PDF-Datei

FDF (Forms Data Format) ist das standardmäßige Austauschformat für AcroForm-Daten und wird von PDF-Viewern und Verarbeitungstools weit verbreitet unterstützt. Verwenden `export_fdf` auf dem [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) Klasse zur Erstellung einer eigenständigen FDF-Datei, die zurück in das ursprüngliche PDF oder ein anderes kompatibles Formular importiert werden kann.

1. Erstelle ein `Form` Instanz und binde das Quell-PDF mit `form.bind_pdf(path)`.
1. Öffnen Sie die Ausgabedatei als Binärstrom.
1. Anruf `form.export_fdf(stream)` um die FDF-Daten zu schreiben.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## Daten zu XFDF aus einer PDF-Datei exportieren

XFDF (XML Forms Data Format) ist der XML‑basierte Nachfolger von FDF und besser geeignet für den Einsatz in Webdiensten und modernen Datenpipelines. Wie FDF kann eine XFDF‑Datei zurück in ein kompatibles PDF‑Formular importiert werden. Verwenden `export_xfdf` auf dem [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) Klasse zur Erzeugung der Ausgabe.

1. Erstelle ein `Form` Instanz und binde das Quell-PDF mit `form.bind_pdf(path)`.
1. Öffnen Sie die Ausgabedatei als Binärstrom.
1. Anruf `form.export_xfdf(stream)` die XFDF-Daten zu schreiben.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```
