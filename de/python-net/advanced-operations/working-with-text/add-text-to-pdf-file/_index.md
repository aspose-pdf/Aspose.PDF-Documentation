---
title: Text zu PDF in Python hinzufügen
linktitle: Text zu PDF hinzufügen
type: docs
weight: 10
url: /de/python-net/add-text-to-pdf-file/
description: Erfahren Sie, wie Sie Text, HTML-Fragmente, Listen, Links und benutzerdefinierte Schriften zu PDF-Dokumenten in Python hinzufügen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fügen Sie Text, Links, HTML und Schriftarten zu PDF-Dateien mit Python hinzu.
Abstract: Dieser Artikel erklärt, wie man Text in PDF-Dokumenten mit Aspose.PDF for Python via .NET hinzufügt und formatiert. Er behandelt Kerntechniken wie das Positionieren von Text, das Anwenden von Schrift- und Stileinstellungen, das Einfügen von Links und Listen sowie die Verwendung von HTML, LaTeX und benutzerdefinierten Schriften in Python-Workflows.
---

Dieser Leitfaden erklärt, wie man Textinhalte zu PDF-Dokumenten mit Aspose.PDF for Python via .NET hinzufügt. Sie lernen grundlegende Techniken zur Texteinfügung – vom Platzieren eines einfachen Textfragmentes an einer bestimmten Position bis hin zur Formatierung (Schriftart, Größe, Farbe, Stil), dem Umgang mit Rechts‑nach‑Links (RTL)-Sprachen, dem Einbetten von Hyperlinks und der Arbeit mit Absatzlayout, Listen und Transparenzeffekten. Der Artikel behandelt zudem fortgeschrittene Szenarien wie die Verwendung von HTML‑ oder LaTeX‑Fragmenten, benutzerdefinierten Schriften und Textformatierungsoptionen wie Zeilenabstand und Zeichenabstand.

Ob Sie einfache Anmerkungen oder komplexe typografische Layouts erstellen, diese Ressource liefert Ihnen die grundlegenden Bausteine für die Arbeit mit Text in PDFs mithilfe von Aspose.PDF.

## Grundlegende Texteinfügung

Aspose.PDF for Python via .NET bietet eine leistungsstarke und flexible API zur Handhabung von Text in PDF-Dateien.
Egal, ob Sie einfache statische Beschriftungen, reich formatierte Inhalte, mehrsprachigen Text oder interaktive Hyperlinks benötigen, das Toolkit ermöglicht Ihnen all das mit prägnantem Python-Code.

### Text hinzufügen – einfacher Fall

Aspose.PDF for Python via .NET zeigt, wie man ein einfaches TextFragment an einer bestimmten Position auf einer Seite hinzufügt. Sie lernen, wie man ein neues PDF-Dokument erstellt, eine Seite hinzufügt, Text an angegebenen Koordinaten einfügt und die resultierende Datei speichert.

1. Neu erstellen [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Objekt.
1. Verwenden `document.pages.add()` ein neues leeres erstellen [Seite](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Erstelle ein [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) mit dem Textinhalt.
1. Stellen Sie die Textposition mit dem [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/) Klasse. Wenn Sie angeben `Position`, der Text wird in Ihrem Dokument von links nach rechts angeordnet und nach unten verschoben.
1. Passen Sie das Erscheinungsbild des Textes an. Sie können Schriftgröße, Farbe, Schriftstil und mehr über die [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. Anhänge das `TextFragment` zur Absatzsammlung der Seite mit `page.paragraphs.add(text_fragment)`.
1. Speichern Sie das Dokument.

Das folgende Code‑Snippet zeigt Ihnen, wie Sie Text in einer bestehenden PDF‑Datei hinzufügen:

```python
import math
import sys
import os
import aspose.pdf as ap

# region Basic text insertion
def add_text_simple_case(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

Dieses Codebeispiel verwendet ein TextFragment. Sie können auch Text zu einer PDF-Seite hinzufügen, indem Sie ein TextParagraph verwenden.
Der **[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** ist ein einzelnes Textstück. Es stellt eine Textzeichenfolge dar, die unabhängig platziert, gestaltet und positioniert werden kann. Es ist ideal, wenn Sie kleinen, einfachen Textinhalt hinzufügen müssen.

Der **[Textabsatz](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** ist eine Gruppe von TextFragments. Es kann mehrere Textzeilen hinzufügen. TextParagraph ist ein Container oder eine Sammlung von einem oder mehreren TextFragment-Objekten. Es ist ideal, wenn Sie mehrere Fragmente gruppieren müssen — zum Beispiel, um einen Textblock mit mehreren Zeilen, Wörtern oder formatierten Elementen zu erstellen.
Ein TextParagraph verwaltet zudem die Textausrichtung, den Zeilenabstand und das automatische Layout auf der Seite. Die Verwendung der roten Linie ist nur mit TextParagraph möglich.

Weitere Informationen zur Arbeit mit Text finden Sie unter [Textformatierung im PDF](/pdf/de/python-net/text-formatting-inside-pdf/) und [Suche und hole Text aus PDF](/pdf/de/python-net/search-and-get-text-from-pdf/).

### Text mit TextParagraph hinzufügen

Aspose.PDF for Python via .NET kann einen Absatz Text hinzufügen, indem es verwendet [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) und [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) mit Umbruchoptionen.

1. Neu erstellen [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) und ein Leerzeichen [Seite](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) Verwenden `document.pages.add()`.
1. Lese Text aus einer Datei oder verwende Standardtext.
1. Erstelle ein [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) um Inhalte auf Absatzebene mit Layout- und Umbruchsteuerung hinzuzufügen.
1. Erstelle ein [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) und setzen Sie den Umbruchmodus (das Beispiel verwendet `DISCRETIONARY_HYPHENATION`).
1. Erstelle ein [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/), wende Stile an und füge das Fragment dem Absatz hinzu.
1. Fügen Sie den Absatz zur Seite hinzu, indem Sie die `TextBuilder`.
1. Speichern Sie das Dokument.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraph(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.first_line_indent = 20
    paragraph.rectangle = ap.Rectangle(80, 800, 400, 200, True)
    # paragraph.formatting_options.wrap_mode = TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.DISCRETIONARY_HYPHENATION
    )

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)

    document.save(output_file_name)
```

![Text mit TextParagraph hinzufügen](text_paragraph.png)

### Absätze mit Einzügen in PDF hinzufügen

Das folgende Code‑Snippet zeigt, wie man ein neues PDF‑Dokument erstellt und zwei Textabsätze mit unterschiedlichen Einrückungsstilen hinzufügt:

- Der erste Absatz demonstriert einen Erstzeileneinzug (nur die erste Zeile ist eingerückt).

- Der zweite Absatz demonstriert einen nachfolgenden Zeileneinzug (alle Zeilen nach der ersten sind eingerückt).

Es verwendet die Klassen 'TextParagraph', 'TextBuilder' und 'TextFragment' von Aspose.PDF, um das Layout und die Formatierung präzise zu steuern.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraphs_indents(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    builder = ap.text.TextBuilder(page)
    paragraph1 = ap.text.TextParagraph()
    paragraph1.first_line_indent = 20
    paragraph1.rectangle = ap.Rectangle(80, 800, 300, 50, True)
    paragraph1.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph1.append_line(fragment)
    builder.append_paragraph(paragraph1)

    paragraph2 = ap.text.TextParagraph()
    paragraph2.subsequent_lines_indent = 20
    paragraph2.rectangle = ap.Rectangle(320, 800, 500, 50, True)
    paragraph2.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph2.append_line(fragment)
    builder.append_paragraph(paragraph2)
    document.save(output_file_name)
```

### Neue Textzeile in PDF hinzufügen

Aspose.PDF for Python via .NET ermöglicht das Einfügen von mehrzeiligem Text in ein PDF-Dokument mithilfe der Klassen TextFragment, TextParagraph und TextBuilder.

1. Erstelle ein neues Dokument.
1. Definieren Sie ein TextFragment, das ein Zeilenumbruchzeichen enthält.
1. Textstil festlegen.
1. Fügen Sie das Fragment zu einem Absatz hinzu.
1. Positionieren Sie den Absatz.
1. Absatz auf der Seite rendern.
1. Speichern Sie das Dokument.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_new_line(output_file):
    """Add a new line of text to a PDF document."""
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initialize new TextFragment with text containing required newline markers
    text_fragment = ap.text.TextFragment("Applicant Name: " + os.linesep + " Joe Smoe")

    # Set text fragment properties if necessary
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Create TextParagraph object
    par = ap.text.TextParagraph()

    # Add new TextFragment to paragraph
    par.append_line(text_fragment)

    # Set paragraph position
    par.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)

    # Add the TextParagraph using TextBuilder
    text_builder.append_paragraph(par)

    # Save PDF document
    document.save(output_file)
```

### Bestimmen von Zeilenumbrüchen und Protokollieren von Benachrichtigungen in einem PDF

Es zeigt, wie man ein PDF‑Dokument erstellt, das mehrere Textfragmente enthält, und das Aspose.PDF‑Benachrichtigungs‑Logging aktiviert, um Layout‑Ereignisse — wie Zeilenumbrüche und Textumbruch — während der Renderung zu überwachen.

1. Erstellen Sie ein neues PDF-Dokument.
1. Benachrichtigungsprotokollierung aktivieren.
1. Verwenden Sie document.pages.add(), um die erste Seite zu erstellen.
1. Fügen Sie mehrere Textfragmente hinzu.
1. Verwenden Sie page.paragraphs.add(text), um jedes Textfragment zu rendern.
1. Speichern Sie das Dokument.

```python
import math
import sys
import os
import aspose.pdf as ap

def determine_line_break(output_file):
    """Create a PDF document with multiple text fragments and log notifications."""
    # Create PDF document
    document = ap.Document()

    # Enable notification logging
    document.enable_notification_logging = True

    page = document.pages.add()

    for i in range(4):
        text = ap.text.TextFragment(
            "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
            "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
            "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
            "culpa qui officia deserunt mollit anim id est laborum."
        )
        text.text_state.font_size = 20
        page.paragraphs.add(text)

    # Save PDF document
    document.save(output_file)

    notifications = document.pages[1].get_notifications()
    print(notifications)
```

### Textbreite dynamisch im PDF messen

Dynamisches Messen der Breite von Zeichen und Zeichenketten in einer bestimmten Schriftart mithilfe von Aspose.PDF for Python via .NET. Es verwendet die 'Font.measure_string()'- und 'TextState.measure_string()'-Methoden, um zu überprüfen, dass die gemessenen Zeichenkettenbreiten konsistent und genau sind.

1. Verwenden Sie 'FontRepository.find_font()', um das Arial Font-Objekt aus dem Repository abzurufen.
1. Erstellen Sie ein TextState-Objekt, um Schrifteigenschaften zu verwalten.
1. Einzelne Zeichen messen.
1. Vergleichen Sie die Ergebnisse beider Methoden für alle Zeichen zwischen 'A' und 'z'.
1. Stellen Sie sicher, dass beide Messansätze die gleichen Ergebnisse liefern.

```python
import math
import sys
import os
import aspose.pdf as ap

def get_text_width_dynamically(output_file):
    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if math.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Unexpected font string measure!")

    if math.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Unexpected font string measure!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        if math.fabs(fn_measure - ts_measure) > 0.001:
            print("Font and state string measuring doesn't match!")

        c_code += 1
```

### Text mit Hyperlinks hinzufügen

Fügen Sie anklickbare Hyperlinks zu Text in einem PDF mithilfe von Aspose.PDF for Python via .NET hinzu. Unsere Bibliothek demonstriert, wie man mehrere Textsegmente innerhalb eines einzelnen TextFragment hinzufügt und einem bestimmten Segment einen Hyperlink zuweist sowie Textsegmente einzeln formatiert (z. B. Farbe, kursive Schrift).

1. Erstellen Sie ein neues Dokument und eine Seite mit 'Document()', und 'document.pages.add()', um eine leere Seite hinzuzufügen.
1. Erstelle ein TextFragment.
1. Füge mehrere TextSegment-Objekte hinzu. Jeder Abschnitt kann eigenen Inhalt und eigene Formatierung haben. Zum Beispiel Klartext oder Hyperlink-Text.
1. Wenden Sie einen Hyperlink auf einen Abschnitt an. Erstellen Sie ein WebHyperlink-Objekt mit der gewünschten URL.
1. Stilisiere das Segment. Passe Farbe, Schriftstil, Größe usw. mit text_state an.
1. Fügen Sie das Fragment der Seite mit 'page.paragraphs.add()' hinzu.
1. Speichern Sie das PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_hyperlink(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Sample Text Fragment")

    segment = ap.text.TextSegment(" ... Text Segment 1...")
    fragment.segments.append(segment)

    segment = ap.text.TextSegment("Link to Aspose")
    fragment.segments.append(segment)
    segment.hyperlink = ap.WebHyperlink("https://products.aspose.com/pdf")
    segment.text_state.foreground_color = ap.Color.blue
    segment.text_state.font_style = ap.text.FontStyles.ITALIC

    segment = ap.text.TextSegment("TextSegment without hyperlink")
    fragment.segments.append(segment)

    page.paragraphs.add(fragment)
    document.save(output_file_name)
```

![Textfragment, das in einem PDF angezeigt wird und gemischten Inhalt zeigt, mit Sample Text Fragment, gefolgt von Text Segment 1, dann ein blau verlinkter Text mit der Aufschrift Link zu Aspose (verlinkt zu https://products.aspose.com/pdf), und endet mit TextSegment ohne Hyperlink in regulärer schwarzer Textformatierung](hyperlink_text.png)

### Rechts-nach-Links-Text (RTL) zum PDF-Dokument hinzufügen

RTL (von Rechts nach Links) ist eine Eigenschaft, die die Schreibrichtung des Textes angibt, wobei der Text von rechts nach links geschrieben wird.
Aspose.PDF for Python via .NET. demonstriert, wie man Rechts-nach-Links (RTL)-Text, wie Arabisch oder Hebräisch, zu einem PDF-Dokument hinzufügt.

1. Erstellen Sie ein neues Dokument und eine Seite mit 'Document()', und 'document.pages.add()', um eine leere Seite hinzuzufügen.
1. Erstelle ein TextFragment mit RTL-Inhalt. Füge deinen Arabisch-, Hebräisch- oder anderen RTL-Sprachtext als Fragmentinhalt ein.
Schriftart und Stil festlegen. Wählen Sie eine Schriftart, die das RTL‑Skript unterstützt (z. B. Tahoma, Arial Unicode MS). Setzen Sie font_size und foreground_color nach Bedarf.
1. Setze die horizontale Ausrichtung auf rechts, indem du 'text_fragment.horizontal_alignment' verwendest.
1. Fügen Sie das TextFragment zur Seite hinzu.
1. Speichern Sie das PDF-Dokument.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_rtl_text(output_file_name):
    document = ap.Document()
    page = document.pages.add()
    # Styled text fragment
    text_fragment = ap.text.TextFragment(
        "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية."
    )
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Tahoma")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.RIGHT

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Rechts-nach-Links-Text](rtl_text.png)

## Textformatierung

### Text mit Schriftstil hinzufügen

Dies ist ein weiter fortgeschrittenes Beispiel, das Textformatierung, Font‑Anpassung und gemischte Textformate (unter Verwendung von tiefgestellten Textsegmenten) demonstriert. Aspose.PDF erklärt, wie man Font‑Eigenschaften wie Font‑Familie, Größe, Farbe, Fett, Kursiv und Unterstrichen auf ein TextFragment anwendet.
Zusätzlich zeigt dieses Code‑Snippet, wie mehrere Textsegmente innerhalb eines einzelnen Fragments verwendet werden können, um komplexe Textelemente zu erstellen — zum Beispiel durch Einfügen von tief- oder hochgestellten Zeichen, die häufig in Formeln oder wissenschaftlichen Notationen benötigt werden.

1. Erstellen Sie ein neues Dokument und eine Seite mit 'Document()', und 'document.pages.add()', um eine leere Seite hinzuzufügen.
1. Erstellen Sie ein TextFragment für einfach formatierten Text.
1. Definieren Sie den Textinhalt.
1. Setze die Position mit den Position(x, y)-Koordinaten.
1. Wenden Sie die Formatierung über die 'text_state property' an – font, font_size, foreground_color, font_style, underline.
1. Erstellen Sie einen komplexen Ausdruck mit mehreren TextSegment-Objekten. Jeder TextSegment stellt einen Textabschnitt dar, der einen eigenen Stil haben kann. Dies ermöglicht es Ihnen, Ausdrücke zu erstellen, wie zum Beispiel mathematische oder chemische Formeln.
1. Definieren Sie mehrere TextState-Objekte. Eines für den Haupttext (text_state_letters). Ein weiteres für hoch- oder tiefgestellten Text (text_state_index).
1. Kombinieren Sie Textsegmente. Fügen Sie jedes Segment zu einem 'TextFragment' mit 'segments.append()' hinzu.
1. Fügen Sie beide Textobjekte zur Seite hinzu. Verwenden Sie 'page.paragraphs.add()', um sie im Dokument zu platzieren.
1. Speichern Sie das endgültige Dokument.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_font_styling(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    # Initialize an empty TextFragment to build a formula using segments
    formula = ap.text.TextFragment()
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_fragment.text_state.underline = True
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.LEFT

    text_state_letters = ap.text.TextState()
    text_state_letters.font = ap.text.FontRepository.find_font("Arial")
    text_state_letters.font_size = 14
    text_state_letters.foreground_color = ap.Color.blue
    text_state_letters.font_style = ap.text.FontStyles.BOLD

    text_state_index = ap.text.TextState()
    text_state_index.font = ap.text.FontRepository.find_font("Arial")
    text_state_index.font_size = 14
    text_state_index.foreground_color = ap.Color.dark_red
    # text_state_index.superscript = True
    text_state_index.subscript = True

    position = ap.text.Position(100, 500)

    # Helper function to add segments
    def add_segment(text, state):
        seg = ap.text.TextSegment(text)
        seg.text_state = state
        seg.position = position
        formula.segments.append(seg)

    add_segment("S = a", text_state_letters)
    add_segment("2n", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+1", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+2", text_state_index)
    formula.horizontal_alignment = ap.HorizontalAlignment.LEFT

    page.paragraphs.add(text_fragment)
    page.paragraphs.add(formula)
    document.save(output_file_name)
```

![Textfragment angezeigt in blauer, kursiver Arial-Schrift, das den Text Hello, Aspose! enthält, gefolgt von einer mathematischen Formel, die S = a tiefgestellt 2n + a tiefgestellt 2n+1 + a tiefgestellt 2n+2 zeigt, mit blauer Haupttext‑ und roter Tiefgestellt‑Formatierung](styled_text.png)

## Text transparent hinzufügen

Fügen Sie einem PDF-Dokument mit Aspose.PDF für Python halbtransparente Formen und Text hinzu.
Es erstellt ein farbiges Rechteck mit teilweiser Transparenz und legt ein TextFragment mit einer transparenten Vordergrundfarbe darüber.

1. Initialisieren Sie ein Document-Objekt und fügen Sie eine leere Seite zum Zeichnen von Inhalten hinzu.
1. Verwenden Sie 'ap.drawing.Graph', um eine Leinwand zu erstellen, die es Ihnen ermöglicht, Formen zu zeichnen.
1. Fügen Sie ein Rechteck mit halbtransparenter Füllung hinzu.
1. Verschiebung der Canvas-Position verhindern.
1. Fügen Sie das Canvas zur Seite hinzu. Fügen Sie die grafischen Formen in die Absatzsammlung der Seite ein.
1. Erstelle ein transparentes Textfragment.
1. Fügen Sie das Textfragment in die Absatzsammlung der Seite ein.
1. Speichern Sie das PDF-Dokument.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_transparent(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create Graph object
    canvas = ap.drawing.Graph(100.0, 400.0)

    # Create rectangle with semi-transparent fill
    rect = ap.drawing.Rectangle(100, 100, 400, 400)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 0xC5, 0xB5, 0xFF)
    canvas.shapes.add(rect)

    # Prevent position shift
    canvas.is_change_position = False
    page.paragraphs.add(canvas)

    # Create transparent text
    text = ap.text.TextFragment(
        "This is the transparent text. "
        "This is the transparent text. "
        "This is the transparent text."
    )
    text.text_state.foreground_color = ap.Color.from_argb(30, 0, 255, 0)
    page.paragraphs.add(text)

    document.save(output_file_name)
```

### Unsichtbaren Text zu PDF hinzufügen

Dieses Beispiel zeigt, wie man ein PDF-Dokument erstellt, das sowohl sichtbaren als auch unsichtbaren Text enthält. Unsichtbarer Text bleibt Teil der Dokumentstruktur, ist jedoch nicht sichtbar, was ihn nützlich macht für das Einbetten von Metadaten, Barrierefreiheits-Tags oder durchsuchbarem Inhalt, ohne das Layout zu beeinflussen.

1. Erstelle PDF Document und Page.
1. Erstellen Sie ein TextFragment mit wiederholtem sichtbarem Inhalt.
1. Fügen Sie ein zweites TextFragment hinzu und markieren Sie es als unsichtbar.
1. Speichern Sie das Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_invisible(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. This is the visible text. This is the visible text."
    )
    page.paragraphs.add(text1)

    # Create transparent text
    text2 = ap.text.TextFragment(
        "This is the invisible text. "
        "This is the invisible text. "
        "This is the invisible text."
    )
    text2.text_state.invisible = True
    page.paragraphs.add(text2)

    document.save(output_file_name)
```

### Text mit Rahmenstil in PDF hinzufügen

Aspose.PDF library zeigt, wie man ein PDF-Dokument erstellt, das ein formatiertes Textfragment mit sichtbarem Rand enthält. Die Methode wendet Hintergrund‑ und Vordergrundfarben, Schrifteinstellungen und einen Strich (Rand) um das Textrechteck an, um die visuelle Betonung zu verstärken.

1. Erstelle ein PDF-Dokument und eine Seite.
1. Textfragment erstellen und positionieren. Ein Textfragment mit der Nachricht hinzufügen und seine Position festlegen.
1. Textformatierung anwenden. Schriftart auf Times New Roman, Größe 12 setzen. Einen hellgrauen Hintergrund und rote Vordergrundfarbe (Text) anwenden.
1. Randgestaltung konfigurieren.
1. Text zur Seite hinzufügen. Verwenden Sie TextBuilder, um den formatierten Text an die Seite anzuhängen.
1. Speichern Sie das Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_border(output_file_name):
    # Create PDF document
    document = ap.Document()
    # Get particular page
    page = document.pages.add()
    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample text with border.")
    text_fragment.position = ap.text.Position(10, 700)

    # Set text properties
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    # Set StrokingColor property for drawing border (stroking) around text rectangle.
    # Note: This only affects the border if draw_text_rectangle_border is set to True.
    text_fragment.text_state.stroking_color = ap.Color.dark_red
    # Enable drawing of the text rectangle border
    text_fragment.text_state.draw_text_rectangle_border = True

    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

### Durchgestrichenen Text zu einem PDF hinzufügen

Fügen Sie einem Textfragment in einem PDF-Dokument Strikeout‑ (Durchstreichung) Formatierung hinzu. Durchgestrichener Text ist nützlich, um Löschungen, Überarbeitungen oder Hervorhebungen in annotierten Dokumenten anzuzeigen.

1. Erstellen Sie ein neues Dokument und eine Seite mit 'Document()', und 'document.pages.add()', um eine leere Seite hinzuzufügen.
1. Erstelle und style Textfragment.
1. Farbe und Durchstreichungsformatierung anwenden. Setzen Sie den Hintergrund auf hellgrau, die Textfarbe auf rot und aktivieren Sie die Durchstreichung.
1. Positionieren Sie den Text.
1. Verwenden Sie 'TextBuilder', um den formatierten Text an die Seite anzuhängen.
1. Speichern Sie das Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_strikeout_text(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample strikeout text.")
    # Set text properties
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    text_fragment.text_state.strike_out = True
    text_fragment.text_state.font_style = ap.text.FontStyles.BOLD
    text_fragment.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

## Erweiterte Farbeffekte

### Anwenden eines axialen Farbverlaufs auf Text in einem PDF

Aspose.PDF for Python via .NET demonstriert, wie man einen linearen Gradienteneffekt auf Text in einem PDF-Dokument anwendet. Der axiale Gradient verläuft sanft von Rot zu Blau über den gesamten Text hinweg und erzeugt eine visuell auffällige Überschrift. Diese Technik ist ideal für stilisierte Titel, Markenbildung oder dekorative Elemente in PDF-Dokument-Layouts.

1. Initialisieren Sie ein neues Dokument und fügen Sie eine leere Seite hinzu.
1. Erstelle und formatiere Textfragment. Füge Titel hinzu, setze Position, Schriftart und Größe.
1. Wenden Sie Axial Gradient Shading mit ‘GradientAxialShading’ an. Setzen Sie die Vordergrundfarbe mithilfe von GradientAxialShading von Rot nach Blau.
1. Unterstreichungsstil hinzufügen.
1. Fügen Sie das formatierte Textfragment in die Seite ein.
1. Speichern Sie das Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_axial_shading_to_text(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

### Anwenden eines radialen Farbverlaufs auf Text in einem PDF

Ein radialer Farbverlauf erzeugt einen kreisförmigen Farbwechsel, der vom Zentrum des Textes nach außen strahlt und eine visuell dynamische Stiloption für Titel, Überschriften oder dekorative Elemente bietet.

1. Initialisieren Sie ein neues Dokument und fügen Sie eine leere Seite hinzu.
1. Erstelle und formatiere Textfragment. Füge Titel hinzu, setze Position, Schriftart und Größe.
1. Wenden Sie einen radialen Verlauf mit 'GradientRadialShading' an. Setzen Sie die Vordergrundfarbe mithilfe von GradientRadialShading von Rot zu Blau.
1. Unterstreichungsstil hinzufügen.
1. Fügen Sie das formatierte Textfragment in die Seite ein.
1. Speichern Sie das Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_radial_shading_to_text(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    # Apply radial gradient shading (red to blue)
    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientRadialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Radialen Farbverlauf anwenden](gradient_radial_shading.png)

## HTML- und LaTeX-Fragmente

### HTML-Text zum PDF-Dokument hinzufügen

Die Aspose.PDF for Python via .NET Bibliothek ermöglicht es Ihnen, HTML-formatierten Inhalt in ein PDF-Dokument einzufügen, indem Sie die HtmlFragment-Klasse verwenden. Durch die Verwendung von HTML-Tags können Sie stilisierten, strukturierten oder formelähnlichen Text direkt in ein PDF rendern.

1. Erstellen Sie ein neues Dokument und eine Seite mit 'Document()', und 'document.pages.add()', um eine leere Seite hinzuzufügen.
1. Erstellen Sie eine Instanz der HtmlFragment-Klasse und übergeben Sie Ihre HTML-Zeichenkette als Parameter.
1. Fügen Sie das Fragment mit 'page.paragraphs.add()' zur Seite hinzu, um den HTML‑Inhalt einzufügen.
1. Speichern Sie das PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_html_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![HTML Text zu einem PDF Document hinzufügen](html_fragment.png)

### Ein stilisiertes HTML-Fragment mit verschiedenen Formatierungen zu einem PDF-Dokument hinzufügen

Wir können ein HTML-Fragment definieren und den Textstil direkt mit HTML-Tags festlegen. Stilisierten HTML-Inhalt in ein PDF-Dokument einbetten. Dieses Code‑Snippet erstellt eine neue PDF-Datei, fügt eine Seite hinzu, fügt ein HTML-Fragment mit verschiedenen Formatierungselementen (Überschriften, Absätze, Links und Inline-Stile) ein und speichert das Ergebnis an dem angegebenen Pfad.

1. Initialisiert ein neues Document-Objekt, das das PDF repräsentiert.
1. Fügt dem Dokument eine leere Seite hinzu, auf der der HTML-Inhalt platziert wird.
1. HTML-Inhalt vorbereiten. Der HTML-String enthält eine h1‑Überschrift, einen grün gefärbten Absatz mit fett, kursiv und unterstrichenem Text sowie einen Hyperlink zu einer Webseite mit vergrößerter Schriftgröße.
1. HTML-Fragment erstellen. Wickeln Sie die HTML-Zeichenkette in ein HtmlFragment-Objekt ein.
1. HTML in Seite einfügen. Fügt das HTML-Fragment zur Absatzsammlung der Seite hinzu und rendert das HTML als nativen PDF-Inhalt.
1. Speichern Sie das Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment(output_file_name):
    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    page.paragraphs.add(html_fragment)
    document.save(output_file_name)
```

![HTML-Inhalt zu einem PDF-Dokument hinzufügen](html_content.png)

### HTML-Fragment mit überschriebenem Textzustand hinzufügen

Wie wir im vorherigen Beispiel gesehen haben, ist es möglich, Stile direkt im HTML-Code festzulegen. Das hat seine Vorteile, aber auch einige Nachteile. Angenommen, wir arbeiten mit dem HTML eines Kunden und möchten das Erscheinungsbild unserer Ausgabe vereinheitlichen.
In diesem Fall können wir das Styling des Kunden überschreiben, indem wir unseren eigenen TextState verwenden, wie im folgenden Beispiel gezeigt.

1. Erstellen Sie ein neues Dokument und eine Seite mit 'Document()', und 'document.pages.add()', um eine leere Seite hinzuzufügen.
1. HTML-Inhalt vorbereiten. Der HTML-String enthält eine h1-Überschrift mit Verdana-Schrift, einen grün gefärbten Absatz mit fett, kursiv und unterstrichenem Text sowie einen Hyperlink zu einer Website mit größerer Schriftgröße.
1. HTML-Fragment erstellen. Wickeln Sie die HTML-Zeichenkette in ein HtmlFragment-Objekt ein.
1. Überschreibe die Textformatierung. Erstelle ein TextState-Objekt und setze die Schriftart, Schriftgröße und Textfarbe.
1. Fügen Sie das HTML‑Fragment zur Absatzsammlung der Seite hinzu.
1. Speichern Sie das Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment_override_text_state(output_file_name):
    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    html_fragment.text_state = ap.text.TextState()
    html_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    html_fragment.text_state.font_size = 14
    html_fragment.text_state.foreground_color = ap.Color.red

    page.paragraphs.add(html_fragment)
    document.save(output_file_name)
```

![HTML-Fragment-Überschreibungs-Textstatus hinzufügen](html_override.png)

### LaTeX-Text zum PDF-Dokument hinzufügen

Fügen Sie LaTeX-formatierte mathematische Ausdrücke zu einem PDF-Dokument hinzu, indem Sie die TeXFragment-Klasse in Aspose.PDF for Python via .NET verwenden.
LaTeX ist ein leistungsstarkes Satzsystem, das weit verbreitet für die Erstellung wissenschaftlicher und mathematischer Dokumente verwendet wird. Durch die Verwendung von TeXFragment können Sie LaTeX‑Mathematiknotationen und -Symbole direkt auf einer PDF‑Seite rendern.

1. Erstellen Sie ein neues Dokument und eine Seite mit 'Document()', und 'document.pages.add()', um eine leere Seite hinzuzufügen.
1. Verwenden Sie die TeXFragment-Klasse, um LaTeX-Syntax direkt zu rendern.
1. Fügen Sie den LaTeX-Inhalt dem PDF-Layout mit 'page.paragraphs.add()' hinzu.
1. Speichern Sie das PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_latex_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Komplexer mathematischer Ausdruck, der in einem PDF angezeigt wird und die LaTeX-Formel mit Overbrace-Notation über (a+b)⁶, Underbrace-Notation unter dem gesamten Ausdruck (a+b)⁶·(c+d)⁷, gekennzeichnet als Beispieltext, und gleich 42 besitzt. Die Formel demonstriert fortgeschrittenes mathematisches Satzlayout mit korrektem Abstand und Klammergestaltung, wie sie typischerweise bei LaTeX-Darstellungen vorkommen.](latex_fragment.png)

## Benutzerdefinierte Schriftarten

### Verwenden Sie eine benutzerdefinierte Font aus einer Datei

Dieses Beispiel ermöglicht es Ihnen, Text zu einer PDF-Datei hinzuzufügen, indem Sie eine benutzerdefinierte OpenType-Schriftart in Aspose.PDF for Python via .NET verwenden. Es zeigt, wie man ein neues PDF-Dokument erstellt, Text präzise auf der Seite positioniert und benutzerdefinierte Formatierungen wie Schriftart, Größe, Farbe und Kursivstil anwendet.

1. Erstelle ein neues PDF-Dokument und füge eine Seite hinzu.
1. Definieren Sie den Textinhalt, den Sie dem PDF hinzufügen möchten.
1. Setzen Sie die Position des Textes.
1. Fügen Sie das TextFragment zur Seite hinzu.
1. Speichern Sie das PDF-Dokument.

Diese Funktion funktioniert nicht nur mit OTF, sondern auch mit TTF-Schriften.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_file(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(output_file_name)
```

![Textfragment, das in einem PDF-Dokument angezeigt wird und „Hello, Aspose!“ in blauer, kursiver BriosoPro-Schrift darstellt, und die Integration benutzerdefinierter OpenType-Schriften sowie Stilfähigkeiten innerhalb der PDF-Textformatierung demonstriert.](custom_font.png)

### Verwenden Sie eine benutzerdefinierte Font aus einem Stream

Dieses Code‑Snippet demonstriert, wie man Text zu einem PDF‑Dokument hinzufügt, indem man mit Aspose.PDF for Python via .NET eine benutzerdefinierte eingebettete OpenType (OTF)-Schrift verwendet. Es zeigt, wie man eine Schriftdatei als Stream öffnet, sie in das PDF einbettet, um die Verfügbarkeit der Schrift auf verschiedenen Systemen sicherzustellen, und Textformatierungen wie Schriftgröße, Farbe und Kursivstil anwendet. Dieser Ansatz ist ideal, um visuell konsistente PDFs zu erstellen, die die Typografie bewahren, selbst wenn sie geteilt oder auf Geräten ohne die installierte Schrift angezeigt werden.

1. Laden Sie die Font-Datei als Binärstrom.
1. Öffnen und betten Sie die Schriftart mit 'FontRepository.open_font' ein.
1. Erstelle ein neues PDF-Dokument und füge eine Seite hinzu.
1. Fügen Sie ein gestyltes Textfragment hinzu mit:
    - Eingebettete benutzerdefinierte Schriftart.
    - Kursiver Stil und blaue Farbe.
    - Spezifische Schriftgröße und Position.
1. Speichern Sie das endgültige Dokument an einem angegebenen Ausgabepfad.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_stream(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
    with open(font_path, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.OTF)
        font.is_embedded = True

        document = ap.Document()
        page = document.pages.add()

        fragment = ap.text.TextFragment("Hello, Aspose!")
        fragment.position = ap.text.Position(100, 600)
        fragment.text_state.font = font
        fragment.text_state.font_size = 14
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.font_style = ap.text.FontStyles.ITALIC

        page.paragraphs.add(fragment)
        document.save(output_file_name)
```

Das Einbetten von Schriftarten sorgt für eine konsistente Darstellung über verschiedene Plattformen hinweg und macht diesen Ansatz ideal für Branding, Designtreue und mehrsprachige Unterstützung.

## Verwandte Textthemen

- [Arbeiten Sie mit Text in PDF mit Python](/pdf/de/python-net/working-with-text/)
- [PDF-Text formatieren in Python](/pdf/de/python-net/text-formatting-inside-pdf/)
- [Text in PDF über Python ersetzen](/pdf/de/python-net/replace-text-in-pdf/)
- [PDF-Text in Python suchen und extrahieren](/pdf/de/python-net/search-and-get-text-from-pdf/)