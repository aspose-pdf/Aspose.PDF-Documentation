---
title: PDF-Kopfzeilen und Fußzeilen in Python hinzufügen
linktitle: Kopfzeile und Fußzeile zu PDF hinzufügen
type: docs
weight: 50
url: /de/python-net/add-headers-and-footers-of-pdf-file/
description: Erfahren Sie, wie Sie Kopf- und Fußzeilen zu PDF-Dateien in Python mit Text, Bildern und strukturierten Inhalten hinzufügen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fügen Sie PDF-Dateien mit Python Kopf- und Fußzeilen hinzu.
Abstract: Dieser Artikel zeigt, wie man Kopf- und Fußzeilen zu PDF-Dokumenten mit Aspose.PDF for Python via .NET hinzufügt. Er behandelt Text, Seitennummerierung, HTML, Bild, Tabelle und LaTeX-basierte Kopf- und Fußzeileninhalte.
---

Verwenden Sie diese Seite, um konsistente Kopf- und Fußzeileninhalte über PDF-Seiten hinweg hinzuzufügen, mit **Aspose.PDF for Python via .NET**.

Sie können Kopfzeilen und Fußzeilen erstellen mit [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), und [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) Objekte, dann wende sie durch an [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) auf jeder Seite.

## Hinzufügen von Kopf- und Fußzeilen als Textfragmente

Fügen Sie einfachen Text als Kopf- und Fußzeilen zu allen Seiten eines PDFs hinzu. Es erstellt [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) Objekte, Einfügungen [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) Elemente in sie, setzt [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) für die korrekte Positionierung und fügt sie jeder Seite im Dokument hinzu. Das Ergebnis ist ein PDF, bei dem jede Seite konsistenten Kopf- und Fußzeilentext anzeigt.

Das folgende Code‑Snippet zeigt, wie man Kopf‑ und Fußzeilen als Textfragmente in einem PDF mit Python hinzufügt:

1. Erstelle Textfragmente für die Kopf- und Fußzeile.
1. Erstellen Sie HeaderFooter-Objekte und fügen Sie die Textfragmente zu ihnen hinzu.
1. Definieren Sie die Rand-Einstellungen, um die Platzierung von Kopfzeile und Fußzeile zu steuern.
1. Laden Sie das PDF-Dokument aus der Eingabedatei.
1. Durchlaufen Sie alle Seiten im Dokument.
1. Weisen Sie die Kopf- und Fußzeile jeder Seite zu.
1. Speichern Sie das modifizierte PDF in die Ausgabedatei.

```python
import aspose.pdf as ap

def add_header_and_footer_as_text(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Diese Methode ist nützlich, um konsistente Titel, Seitenindikatoren oder rechtliche Hinweise oben und unten auf jeder Seite hinzuzufügen. Sie können sie auch erweitern, um Bilder oder dynamische Inhalte, wie Seitenzahlen, einzuschließen.

## Kopf- und Fußzeilen für die Seitennummerierung hinzufügen

Fügen Sie einer PDF-Datei automatische Seitenzahlen zu den Kopf‑ und Fußzeilen hinzu, indem Sie Aspose.PDF for Python verwenden. Mit den integrierten Variablen $p (aktuelle Seitenzahl) und $P (Gesamtzahl der Seiten) fügt das Skript dynamisch Seitenzahlen auf jeder Seite ein. Die Kopfzeilen zeigen das Format 'Seite X von Y' an, während die Fußzeilen 'Seite X / Y' anzeigen. Der [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) stellt sicher, dass die korrekte Platzierung auf jeder Seite erfolgt.

1. Erstellen Sie ein TextFragment für die Kopfzeile, das "Page $p from $P" verwendet, um die aktuelle und die gesamte Seitenzahl anzuzeigen.
1. Erstelle ein HeaderFooter-Objekt und füge den Header-Text hinzu.
1. Erstellen Sie ein TextFragment für die Fußzeile mit "Page $p / $P" für einen alternativen Nummerierungsstil.
1. Erstellen Sie ein Footer-Objekt und fügen Sie den Fußzeilentext hinzu.
1. Definieren Sie die Rand-Einstellungen (links = 50, oben = 20) und wenden Sie sie sowohl auf die Kopfzeile als auch auf die Fußzeile an.
1. Öffnen Sie das PDF‑Dokument aus der Eingabedatei.
1. Durchlaufen Sie alle Seiten und weisen Sie jeder Seite Header und Footer zu.
1. Speichern Sie das aktualisierte PDF im Ausgabepfad.

```python
import aspose.pdf as ap

def using_header_and_footer_for_page_numbering(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Kopf- und Fußzeilen als HTML-Fragmente hinzufügen

Wenden Sie HTML-formatierte Kopf- und Fußzeilen auf jeder Seite eines PDF-Dokuments mit Aspose.PDF for Python an. Durch die Verwendung [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), das Skript ermöglicht Rich-Text-Formatierungen—wie fett und kursiv—im Header und Footer anzuzeigen. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) wird für die korrekte Platzierung angewendet, und dieselben formatierten Elemente werden jeder Seite im Dokument hinzugefügt.

Das folgende Code‑Snippet zeigt, wie man Kopf‑ und Fußzeilen als HTML‑Fragmente zu einem PDF mit Python hinzufügt:

1. Erstellen Sie ein HTML-Header‑Snippet mit HtmlFragment—einschließlich stilisiertem Text wie '<strong>' für fett.
1. Erstellen Sie ein HeaderFooter-Objekt und fügen Sie ihm die HTML‑Kopfzeile hinzu.
1. Erstellen Sie ein HTML-Fußzeilen‑Snippet mit '<i>' für kursive Schrift.
1. Erstellen Sie ein Footer-Objekt und fügen Sie das Footer-HTML hinzu.
1. Konfigurieren Sie die Ränder (links = 50, oben = 20) und weisen Sie sie sowohl Header als auch Footer zu.
1. Laden Sie das PDF-Dokument mit 'ap.Document()'.
1. Durchlaufe alle Seiten und weise jeder die Kopf‑ und Fußzeile zu.
1. Speichern Sie das modifizierte PDF im angegebenen Ausgabepfad.

```python
import aspose.pdf as ap

def add_header_and_footer_as_html(input_file, output_file):
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Die Verwendung von HtmlFragment ermöglicht eine reichhaltige Formatierung mit Inline‑Stilen oder HTML‑Markup und bietet Ihnen mehr Designflexibilität im Vergleich zu einfachem Text.

## Kopf- und Fußzeilen als Bilder hinzufügen

Fügen Sie jedem PDF-Dokument bildbasierte Kopf- und Fußzeilen hinzu, indem Sie Aspose.PDF for Python verwenden. Für die Kopf- und Fußzeile jeder Seite wird dieselbe Bilddatei verwendet. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) Positioniert die Bilder, und das Bild wird automatisch angepasst, um in den Header/Footer‑Bereich zu passen.

Der folgende Codeabschnitt demonstriert, wie man Kopf- und Fußzeilen als Bilder zu einem PDF mit Python hinzufügt:

1. Laden Sie das Bild in ein ‘ap.Image’-Objekt und bereiten Sie es für die Verwendung als Kopfzeile vor.
1. Erstellen Sie ein HeaderFooter-Objekt und hängen Sie das Header-Bild daran an.
1. Laden Sie das gleiche Bild erneut zur Verwendung als Fußzeile.
1. Erstellen Sie ein Footer-Objekt und fügen Sie das Footer-Bild hinzu.
1. Laden Sie das Eingabe-PDF-Dokument mit 'ap.Document()'.
1. Durchlaufen Sie alle Seiten des Dokuments.
1. Wenden Sie Ränder (links = 50) an, um sowohl Header als auch Footer zu positionieren.
1. Weisen Sie die Kopf- und Fußzeile jeder Seite im PDF zu.
1. Speichern Sie das aktualisierte PDF in der angegebenen Ausgabedatei.

Diese Technik ist ideal für das Branding von Dokumenten mit Logos oder Wasserzeichen im Kopf‑/Fußzeilenbereich.

```python
import aspose.pdf as ap

def add_header_and_footer_as_image(input_file, image_file, output_file):
    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Kopf- und Fußzeilen als Tabelle hinzufügen

Fügen Sie allen Seiten eines PDF-Dokuments strukturierte, tabellenbasierte Kopf‑ und Fußzeilen mit Aspose.PDF für Python hinzu. [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) Objekte bieten eine bessere Layoutkontrolle, Ausrichtung und konsistente Formatierung für komplexe Kopf- und Fußzeilen. Der Kopfzeilentext ist zentriert, während der Fußzeilentext linksbündig ist, beide in Arial 12pt Schrift. Die Spaltenbreiten werden dynamisch basierend auf den Seitenabmessungen berechnet, um eine korrekte Platzierung sicherzustellen.

Dieses Codebeispiel fügt jeder Seite eines PDF Document mit Aspose.PDF for Python via .NET Kopf‑ und Fußzeilen (unter Verwendung von Tabellen) hinzu.

1. Definieren Sie Textstile mit [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) für Kopf- und Fußzeile (Schriftart, Größe, Ausrichtung).
1. Erstellen [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) Objekte für die Kopf- und Fußzeile.
1. Header erstellen [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) mit einer einzelnen Zeile und einer Zelle, die den Header-Text enthält.
1. Erstelle die Fußzeile [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) mit einer einzigen Zeile und Zelle, die den Fußzeilentext enthält.
1. Fügen Sie die Tabellen zu den entsprechenden hinzu [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) Objekte.
1. Fußzeile festlegen [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) für die korrekte horizontale Positionierung.
1. Öffnen Sie das [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) unter Verwendung geeigneter Methoden.
1. Iterieren Sie über alle Seiten und weisen Sie jeder Seite die tabellenbasierte Kopf‑ und Fußzeile zu.
1. Speichern Sie das modifizierte [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) zur Ausgabedatei.

```python
import aspose.pdf as ap

def add_header_and_footer_as_table(input_file, output_file):
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Kopf- und Fußzeilen als LaTeX hinzufügen

Fügen Sie allen Seiten eines PDF-Dokuments mithilfe von Aspose.PDF for Python Kopf‑ und Fußzeilen mit LaTeX‑formatiertem Inhalt hinzu. LaTeX ermöglicht die Darstellung mathematischer Symbole, Daten, Copyright‑Zeichen und anderer fortgeschrittener Formatierungen. Die Kopfzeile enthält ein dynamisches Datum, während die Fußzeile ein Copyright‑Symbol zusammen mit der aktuellen Seitennummer und der Gesamtseitenzahl anzeigt.

Der folgende Codeabschnitt zeigt, wie man verwendet [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) in Kopf- und Fußzeilen für ein PDF mit Aspose.PDF for Python via .NET.

1. Öffnen Sie das [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) unter Verwendung geeigneter Methoden.
1. Bestimmen Sie die Gesamtseitenzahl zur Verwendung in dynamischen Fußzeilen.
1. Durchlaufen Sie alle Seiten des Dokuments.
1. Erstelle ein [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) Objekt für die Kopfzeile.
1. Erstelle ein [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) für den Header-Text, der LaTeX-Befehle enthält (z. B., `\\today\\`).
1. Erstelle ein [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) Objekt für die Fußzeile.
1. Erstelle ein [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) für den Fußzeilentext einschließlich LaTeX‑Symbolen und Seitenzahlen.
1. Füge das [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) zum entsprechenden Kopf-/Fußzeilen-Objekt.
1. Binden Sie die Kopfzeile und Fußzeile an die aktuelle Seite.
1. Speichern Sie das modifizierte [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) zur Ausgabedatei.

```python
import aspose.pdf as ap

def add_header_and_footer_as_latex(input_file, output_file):
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTeX Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = (
                f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            )
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Verwandte Seitenthemen

- [Arbeiten Sie mit PDF-Seiten in Python](/pdf/de/python-net/working-with-pages/)
- [Seitenzahlen zum PDF in Python hinzufügen](/pdf/de/python-net/add-page-number/)
- [PDF-Seiten in Python stempeln](/pdf/de/python-net/stamping/)
- [PDF-Dokumente in Python formatieren](/pdf/de/python-net/formatting-pdf-document/)