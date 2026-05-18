---
title: PDF-Text in Python formatieren
linktitle: Textformatierung in PDF
type: docs
weight: 70
url: /de/python-net/text-formatting-inside-pdf/
description: Erfahren Sie, wie Sie Text in PDF-Dokumenten in Python mit Abständen, Rahmen, Einzügen und Stiloptionen formatieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Text in PDF-Dateien mit Python formatieren und gestalten
Abstract: Dieser Artikel erklärt, wie Sie Text in PDF-Dokumenten mit Aspose.PDF for Python via .NET formatieren. Erfahren Sie, wie Sie Abstände, Einzüge, Rahmen, Unterstreichungen, Durchstreichungen und weitere Textstile in Python steuern.
---

## Zeilen- und Zeichenabstand

### Zeilenabstand verwenden

#### Text mit benutzerdefiniertem Zeilenabstand in Python formatieren - einfacher Fall

Aspose.PDF for Python bietet einen unkomplizierten Ansatz, um Textlayout und Lesbarkeit über Anpassungen des Zeilenabstands zu steuern.

Unser Codebeispiel zeigt, wie Sie den Zeilenabstand in einem PDF-Dokument steuern. Es liest Text aus einer Datei ein oder verwendet eine Fallback-Nachricht, wendet eine benutzerdefinierte Schriftgröße und einen angepassten Zeilenabstand an und fügt den formatierten Text einer neuen Seite in einem PDF hinzu.

1. Erstellen Sie ein neues PDF-Dokument.
1. Laden Sie den Quelltext.
1. Initialisieren Sie ein `TextFragment`-Objekt und weisen Sie ihm den geladenen Text zu.
1. Legen Sie Schrift- und Abstandsoptionen für den Text fest. Diese Werte bestimmen, wie dicht oder locker die Textzeilen erscheinen:
   - Schriftgröße: 12 Punkt
   - Zeilenabstand: 16 Punkt
1. Fügen Sie das formatierte Textfragment der `paragraphs`-Sammlung der Seite hinzu.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_simple_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Text mit benutzerdefiniertem Zeilenabstand in Python formatieren - spezifischer Fall

Sehen wir uns an, wie Sie verschiedene Modi für den Zeilenabstand in einem PDF-Dokument mit einer benutzerdefinierten TrueType-Schriftart (TTF) anwenden.
Das Beispiel lädt Text aus einer Datei, bettet eine bestimmte Schriftart ein und rendert denselben Text zweimal auf einer PDF-Seite, wobei jeweils ein anderer Modus für den Zeilenabstand verwendet wird:

- Modus `FONT_SIZE`: Der Zeilenabstand entspricht der Schriftgröße.
- Modus `FULL_SIZE`: Der Zeilenabstand berücksichtigt die vollständige Höhe der Schrift einschließlich Ober- und Unterlängen.

Das Beispiel zeigt, wie sich das Verhalten des Zeilenabstands abhängig vom gewählten Modus unterscheiden kann.

1. Erstellen Sie ein neues PDF-Dokument.
1. Geben Sie die Pfade zur benutzerdefinierten Schriftdatei und zur Quelldatei mit dem Text an.
1. Laden Sie den Textinhalt.
1. Öffnen Sie die benutzerdefinierte Schriftart.
1. Erstellen und konfigurieren Sie das erste `TextFragment` für den Modus `FONT_SIZE`. Setzen Sie `line_spacing` auf `TextFormattingOptions.LineSpacingMode.FONT_SIZE`, damit der Zeilenabstand der Schriftgröße entspricht.
1. Erstellen und konfigurieren Sie das zweite `TextFragment` für den Modus `FULL_SIZE`. Setzen Sie `line_spacing` auf `TextFormattingOptions.LineSpacingMode.FULL_SIZE`, damit die volle Schrifthöhe verwendet wird.
1. Fügen Sie beide Textfragmente derselben PDF-Seite hinzu.
1. Speichern Sie das fertige Dokument unter dem angegebenen Ausgabepfad.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_specific_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    font_file = path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

    with open(font_file, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.TTF)

        fragment1 = ap.text.TextFragment(text)
        fragment1.text_state.font = font
        fragment1.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment1.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FONT_SIZE
        )
        page.paragraphs.add(fragment1)

        fragment2 = ap.text.TextFragment(text)
        fragment2.text_state.font = font
        fragment2.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment2.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE
        )
        page.paragraphs.add(fragment2)

    document.save(outfile)
```

![PDF-Dokument mit Text und benutzerdefiniertem Zeilenabstand, das 16-Punkt-Abstände zwischen den Zeilen zur Verbesserung von Lesbarkeit und Textlayout zeigt](line_spacing.png)

### Zeichenabstand verwenden

#### Zeichenabstand in PDF-Text mit der Klasse TextFragment steuern

Der Zeichenabstand bestimmt den Abstand zwischen einzelnen Zeichen in einer Textzeile. Das ist nützlich, um das Erscheinungsbild von Text fein abzustimmen oder bestimmte typografische Effekte zu erzielen.

1. Initialisieren Sie ein neues `Document`-Objekt und fügen Sie eine leere Seite hinzu, auf der der Text platziert wird.
1. Definieren Sie einen Fragmentgenerator. Implementieren Sie dazu eine Hilfsfunktion `make_fragment(spacing)`:
   - Erstellen Sie ein `TextFragment` mit Beispieltext.
   - Legen Sie die Schriftart fest.
1. Fügen Sie Textfragmente mit unterschiedlichen Abstandswerten hinzu.
1. Speichern Sie das `Document`.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_fragment(outfile):
    document = ap.Document()
    page = document.pages.add()

    def make_fragment(spacing):
        fragment = ap.text.TextFragment("Sample Text with character spacing")
        fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment.text_state.font_size = 14
        fragment.text_state.character_spacing = spacing
        return fragment

    page.paragraphs.add(make_fragment(2.0))
    page.paragraphs.add(make_fragment(1.0))
    page.paragraphs.add(make_fragment(0.75))

    document.save(outfile)
```

![PDF-Dokument mit drei Zeilen desselben Textes und unterschiedlich engem Zeichenabstand von oben nach unten, das die visuelle Wirkung verschiedener Werte für den Zeichenabstand bei der Formatierung von PDF-Text zeigt](character_spacing_simple.png)

#### Zeichenabstand in PDF-Text mit TextParagraph und TextBuilder steuern

Aspose.PDF ermöglicht es, beim Hinzufügen von Text zu einem PDF-Dokument mit `TextParagraph` und `TextBuilder` benutzerdefinierte Zeichenabstände anzuwenden.
Dabei wird ein bestimmter Bereich auf der Seite definiert, ein Zeilenumbruch konfiguriert und ein Textfragment mit angepasstem Abstand zwischen den Zeichen gerendert.

`TextParagraph` ist ideal, wenn Sie eine präzise Kontrolle über die Platzierung und das Layout von Text benötigen, zum Beispiel beim Aufbau strukturierter oder mehrspaltiger Textblöcke.

1. Erstellen Sie ein neues PDF-Dokument.
1. Initialisieren Sie eine `TextBuilder`-Instanz für die Seite.
1. Erstellen und konfigurieren Sie einen `TextParagraph`.
   - Setzen Sie den Zeilenumbruchmodus auf `TextFormattingOptions.WordWrapMode.BY_WORDS`.
1. Erstellen Sie ein `TextFragment` mit benutzerdefiniertem Zeichenabstand.
   - Erstellen Sie ein neues `TextFragment` und setzen Sie seinen Text, zum Beispiel `"Sample Text with character spacing"`.
   - Geben Sie Schriftattribute wie Arial und Schriftgröße 14 pt an.
   - Wenden Sie `character_spacing = 2.0` an, um den Abstand zwischen den Zeichen zu vergrößern.
1. Fügen Sie das `TextFragment` dem `TextParagraph` hinzu.
1. Fügen Sie den `TextParagraph` der Seite hinzu.
1. Speichern Sie das PDF-Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_paragraph(outfile):
    document = ap.Document()
    page = document.pages.add()

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(100, 700, 500, 750, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    fragment = ap.text.TextFragment("Sample Text with character spacing")
    fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment.text_state.font_size = 14
    fragment.text_state.character_spacing = 2.0

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)
    document.save(outfile)
```

## Listen erstellen

Bei der Arbeit mit PDF-Dateien müssen Sie möglicherweise strukturierte Informationen wie Listen darstellen, egal ob mit Aufzählungszeichen, nummeriert oder mit HTML oder LaTeX formatiert.
Aspose.PDF for Python via .NET bietet mehrere flexible Möglichkeiten, Listen direkt in Ihren PDF-Dokumenten zu erstellen und zu formatieren, sodass Sie die volle Kontrolle über Layout, Schriftart und Stil haben.

Dieser Artikel zeigt mehrere Ansätze zum Erstellen von Listen in PDFs, von einfacher Textformatierung bis hin zu erweitertem HTML- und LaTeX-Rendering. Jede Methode eignet sich für einen bestimmten Anwendungsfall, je nachdem, ob Sie eine präzise programmgesteuerte Kontrolle oder komfortables Styling auf Markup-Basis bevorzugen.

Nach diesem Artikel wissen Sie, wie Sie:

- benutzerdefinierte Aufzählungs- und nummerierte Listen mit `TextParagraph` und `TextBuilder` erstellen.
- HTML-Fragmente (`HtmlFragment`) verwenden, um `<ul>`- und `<ol>`-Listen einfach in PDFs zu rendern.
- LaTeX-Fragmente (`TeXFragment`) für mathematische oder wissenschaftliche Listenformatierung einsetzen.
- Zeilenumbruch, Schriftstile und Layoutpositionierung innerhalb einer Seite steuern.
- den Unterschied zwischen manueller Listenerstellung und markupbasierten Ansätzen verstehen.

### Nummerierte Liste erstellen

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for item in items:
        fragment = ap.text.TextFragment("вЂў " + item)
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### Aufzählungsliste erstellen

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for i, item in enumerate(items):
        fragment = ap.text.TextFragment(f"{i + 1}. {item}")
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### Nummerierte Liste als HTML-Version erstellen

Erstellen Sie eine nummerierte Liste in einem PDF-Dokument mit HTML-Fragmenten. Dazu wird eine Python-Liste aus Zeichenfolgen in ein HTML-Element `<ol>` umgewandelt und als `HtmlFragment` in eine PDF-Seite eingefügt.

Mit HTML-Fragmenten können Sie HTML-basierte Formatierungen wie nummerierte Listen, Fett, Kursivschrift und mehr direkt in Ihrem PDF verwenden.

1. Erstellen Sie ein neues PDF-Dokument und fügen Sie eine Seite hinzu.
1. Bereiten Sie die Listenelemente vor.
1. Wandeln Sie die Liste in eine geordnete HTML-Liste um.
   - Verwenden Sie das Tag `<ol>` für eine nummerierte Liste.
   - Umhüllen Sie jedes Element mit `li`-Tags mithilfe einer List Comprehension.
1. Wandeln Sie die HTML-Zeichenfolge in ein `HtmlFragment`-Objekt um, das der PDF-Seite hinzugefügt werden kann.
1. Fügen Sie das `HtmlFragment` der `paragraphs`-Sammlung der Seite hinzu.
1. Speichern Sie das PDF-Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_html_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ol>" + "".join([f"<li>{item}</li>" for item in items]) + "</ol>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Nummerierte Liste in einem PDF-Dokument mit vier automatisch nummerierten Elementen und korrekter Reihenfolge, Einrückung und Abständen, die HTML-basiertes Rendering einer geordneten Liste im PDF zeigt](numbered_list_html.png)

### Aufzählungsliste als HTML-Version erstellen

Unsere Bibliothek zeigt, wie Sie mit HTML-Fragmenten eine Liste mit Aufzählungszeichen in einem PDF-Dokument erstellen. Dazu wird eine Python-Liste von Zeichenfolgen in ein HTML-Element `<ul>` umgewandelt und als `HtmlFragment` in eine PDF-Seite eingefügt. Mit HTML-Fragmenten können Sie HTML-Formatierungen wie Listen, Fettschrift oder Kursivschrift direkt im PDF nutzen.

1. Erstellen Sie ein neues PDF-Dokument und fügen Sie eine Seite hinzu.
1. Bereiten Sie die Listenelemente vor.
1. Wandeln Sie die Liste in eine ungeordnete HTML-Liste um.
   - Verwenden Sie das Tag `<ul>` für eine ungeordnete Liste mit Aufzählungszeichen.
   - Umhüllen Sie jedes Element mit `li`-Tags mithilfe einer List Comprehension.
1. Erstellen Sie ein `HtmlFragment`. Wandeln Sie die HTML-Zeichenfolge in ein `HtmlFragment`-Objekt um, das der PDF-Seite hinzugefügt werden kann.
1. Fügen Sie das `HtmlFragment` der `paragraphs`-Sammlung der Seite hinzu.
1. Speichern Sie das PDF-Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_html_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Aufzählungsliste in einem PDF-Dokument mit vier Elementen, jeweils mit einem Aufzählungszeichen sowie korrekter Einrückung und Abständen, die HTML-formatiertes Listen-Rendering im PDF zeigt](bullet_list_html.png)

### Aufzählungsliste als LaTeX-Version erstellen

Erstellen Sie eine Liste mit Aufzählungszeichen in einem PDF mit LaTeX-Fragmenten (`TeXFragment`). Dabei wird eine Python-Liste von Zeichenfolgen in eine LaTeX-Umgebung `itemize` umgewandelt und in eine PDF-Seite eingefügt. LaTeX-Fragmente sind ideal, wenn Sie mathematische Formeln, Symbole oder strukturierte Listen mit präziser Formatierung rendern möchten.

1. Erstellen Sie ein neues PDF-Dokument und fügen Sie eine Seite hinzu.
1. Definieren Sie eine Python-Liste von Zeichenfolgen, die zu Aufzählungspunkten in der LaTeX-Umgebung `itemize` werden.
1. Wandeln Sie die Liste in eine LaTeX-Umgebung `itemize` um:
   - Umhüllen Sie die Elemente mit `\begin{itemize}` und `\end{itemize}`.
   - Jedes Element wird mit `\item` über eine List Comprehension versehen.
1. Wandeln Sie die LaTeX-Zeichenfolge in ein `TeXFragment`-Objekt um, das im PDF gerendert werden kann.
1. Fügen Sie das LaTeX-Fragment der Seite hinzu.
1. Speichern Sie das PDF-Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_latex_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{itemize}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{itemize}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Aufzählungsliste im PDF mit LaTeX-gerendertem Layout und sauberem Satz, korrekten Aufzählungszeichen, konsistenten Abständen und Zeilenumbrüchen](bullet_list_latex.png)

### Nummerierte Liste als LaTeX-Version erstellen

Erstellen Sie eine nummerierte Liste in einem PDF mit LaTeX-Fragmenten (`TeXFragment`). Dabei wird eine Python-Liste von Zeichenfolgen in eine LaTeX-Umgebung `enumerate` umgewandelt und in eine PDF-Seite eingefügt. LaTeX-Fragmente sind ideal, wenn Sie präzise Formatierung, strukturierte Listen oder mathematische Notation in PDFs benötigen.

1. Erstellen Sie ein neues PDF-Dokument und fügen Sie eine Seite hinzu.
1. Definieren Sie eine Python-Liste von Zeichenfolgen, die in der LaTeX-Umgebung `enumerate` zu nummerierten Einträgen werden.
1. Wandeln Sie die Liste in eine LaTeX-Umgebung `enumerate` um.
1. Wandeln Sie die LaTeX-Zeichenfolge in ein `TeXFragment`-Objekt um, das im PDF gerendert werden kann.
1. Fügen Sie das LaTeX-Fragment der Seite hinzu.
1. Speichern Sie das PDF-Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_latex_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{enumerate}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{enumerate}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Nummerierte Liste im PDF mit LaTeX-gerendertem Layout und den Einträgen 1 bis 4 sowie dem einleitenden Text Lists are easy to create](numbered_list_latex.png)

## Fußnoten und Endnoten

### Fußnoten hinzufügen

Fußnoten werden verwendet, um im Textkörper eines Dokuments auf Anmerkungen zu verweisen, indem fortlaufende hochgestellte Zahlen neben den relevanten Text gesetzt werden. Diese Zahlen verweisen auf ausführliche Anmerkungen, die normalerweise eingerückt am unteren Rand derselben Seite stehen und zusätzlichen Kontext, Zitate oder Kommentare liefern.

Fügen Sie mit Aspose.PDF for Python via .NET eine Fußnote zu einem Textfragment in einem PDF-Dokument hinzu. Fußnoten sind nützlich, um ergänzende Informationen, Zitate oder Erläuterungen bereitzustellen, ohne den Hauptinhalt zu überladen. Diese Methode stellt sicher, dass Fußnoten visuell und strukturell in das PDF-Layout integriert werden.

1. Erstellen Sie ein neues Dokument.
1. Erstellen Sie ein `TextFragment` mit dem Hauptinhalt.
1. Fügen Sie Inline-Text hinzu. Erstellen Sie ein weiteres `TextFragment`, das im selben Absatz fortgeführt wird.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    inline_text = ap.text.TextFragment(
        " This is another text after footnote in the same paragraph."
    )
    inline_text.is_in_line_paragraph = True
    inline_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    inline_text.text_state.font_size = 14
    page.paragraphs.add(inline_text)

    document.save(outfile)
```

### Fußnote mit benutzerdefiniertem Stil im PDF hinzufügen

1. Initialisieren Sie ein neues PDF-Dokument und fügen Sie eine leere Seite hinzu.
1. Erstellen Sie das Haupt-Textfragment.
1. Erstellen und formatieren Sie die Fußnote mit Schriftart, Größe, Farbe und Stil.
1. Fügen Sie das formatierte Textfragment mit Fußnote in die Seite ein.
1. Fügen Sie ein weiteres Textfragment ohne Fußnote hinzu.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text_style(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text_state = ap.text.TextState()
    note.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    note.text_state.font_size = 10
    note.text_state.foreground_color = ap.Color.red
    note.text_state.font_style = ap.text.FontStyles.ITALIC
    text_fragment.foot_note = note

    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    document.save(outfile)
```

### Fußnoten mit benutzerdefinierten Symbolen im PDF hinzufügen

Fügen Sie Fußnoten zu Textfragmenten in einem PDF-Dokument hinzu und passen Sie dabei das Symbol für den Fußnotenmarker an.

1. Erstellen Sie ein PDF-Dokument und eine Seite.
1. Fügen Sie das erste Textfragment mit benutzerdefiniertem Fußnotensymbol hinzu.
1. Fügen Sie ein weiteres Textfragment hinzu, das den Absatz ohne Fußnote fortsetzt.
1. Fügen Sie ein zweites Textfragment mit Standardfußnote hinzu.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text = "*"
    text_fragment.foot_note = note
    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

### Fußnoten mit benutzerdefiniertem Linienstil im PDF hinzufügen

Passen Sie die visuelle Darstellung von Fußnotenlinien in einem PDF-Dokument mit der Python-Bibliothek an. Angepasste Fußnotenlinien verbessern die visuelle Klarheit und sorgen für stilistische Konsistenz in Dokumenten wie Berichten, wissenschaftlichen Arbeiten oder kommentierten Publikationen.

1. Erstellen Sie ein neues PDF-Dokument und fügen Sie eine Seite hinzu.
1. Definieren Sie einen benutzerdefinierten Linienstil für Fußnotenverbindungen mit Farbe, Breite und Strichmuster.
1. Fügen Sie mehrere Textfragmente mit Fußnoten hinzu.
1. Speichern Sie das fertige Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_custom_line_style(outfile):
    document = ap.Document()
    page = document.pages.add()

    # Define custom line style
    graph_info = ap.GraphInfo()
    graph_info.line_width = 2
    graph_info.color = ap.Color.red
    graph_info.dash_array = [3]
    graph_info.dash_phase = 1
    page.note_line_style = graph_info

    # First text fragment with footnote
    text1 = ap.text.TextFragment("This is a sample text with a footnote.")
    text1.foot_note = ap.Note("foot note for text 1")
    page.paragraphs.add(text1)

    # Second text fragment with footnote
    text2 = ap.text.TextFragment("This is yet another sample text with a footnote.")
    text2.foot_note = ap.Note("foot note for text 2")
    page.paragraphs.add(text2)

    document.save(outfile)
```

### Fußnoten mit Bild und Tabelle im PDF hinzufügen

Wie können Sie Fußnoten in einem PDF-Dokument anreichern, indem Sie Bilder, formatierten Text und Tabellen mit Aspose.PDF for Python via .NET einbetten?

1. Erstellen Sie ein neues PDF-Dokument und fügen Sie eine Seite hinzu.
1. Fügen Sie ein Textfragment mit angehängter Fußnote hinzu.
1. Betten Sie ein Bild, formatierten Text und eine Tabelle in die Fußnote ein.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_image_and_table(outfile):
    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = path.join(DATA_DIR, "logo.jpg")
    image_note.fix_height = 20
    image_note.fix_width = 20
    note.paragraphs.add(image_note)

    # Add text
    text_note = ap.text.TextFragment("This is the footnote content.")
    text_note.text_state.font_size = 20
    text_note.is_in_line_paragraph = True
    note.paragraphs.add(text_note)

    # Add table
    table = ap.Table()
    table.rows.add().cells.add("Cell 1,1")
    table.rows.add().cells.add("Cell 1,2")
    note.paragraphs.add(table)

    text.foot_note = note

    document.save(outfile)
```

### Endnoten zu PDF-Dokumenten hinzufügen

Eine Endnote ist eine Form des Verweises, die Leser zu einem Bereich am Ende eines Dokuments führt, in dem sich der vollständige Verweis auf ein Zitat, eine paraphrasierte Idee oder zusammengefasste Inhalte befindet. Bei der Verwendung von Endnoten wird direkt nach dem referenzierten Material eine hochgestellte Zahl gesetzt, die den Leser zur entsprechenden Anmerkung am Ende des Dokuments führt.

Dieses Codebeispiel zeigt, wie Sie einem Textfragment in einem PDF-Dokument eine Endnote hinzufügen. Im Gegensatz zu Fußnoten, die in der Nähe des referenzierten Textes erscheinen, werden Endnoten normalerweise am Ende eines Dokuments oder Abschnitts platziert. Die Methode simuliert außerdem ein längeres Dokument, um zu zeigen, wie sich Endnoten in umfangreicheren Inhalten verhalten.

1. Erstellen Sie ein PDF-Dokument und eine Seite.
1. Fügen Sie ein Textfragment mit Endnote hinzu.
1. Laden Sie externen Textinhalt.
1. Simulieren Sie ein langes Dokument. Fügen Sie den geladenen Text mehrfach hinzu, um umfangreicheren Inhalt zu simulieren.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### Endnoten mit benutzerdefiniertem Markertext im PDF hinzufügen

Fügen Sie einem Textfragment in einem PDF-Dokument eine Endnote mit einem benutzerdefinierten Markersymbol wie `"***"` hinzu. Endnoten werden normalerweise am Ende eines Dokuments oder Abschnitts platziert und sind nützlich, um zusätzlichen Kontext, Zitate oder Kommentare bereitzustellen.

1. Erstellen Sie ein PDF-Dokument und eine Seite.
1. Fügen Sie ein formatiertes Textfragment mit einer Endnote hinzu.
1. Passen Sie den Markertext der Endnote an.
1. Laden Sie externe Inhalte aus einer `.txt`-Datei.
1. Simulieren Sie längeren Inhalt, um die Platzierung der Endnote zu veranschaulichen.
1. Speichern Sie das PDF-Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote_custom_text(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## Layout und Seitensteuerung

### Eine Tabelle erzwingen, auf einer neuen PDF-Seite zu beginnen

Fügen Sie Inhalte so ein, dass sie in einem PDF-Dokument mit Aspose.PDF for Python via .NET auf einer neuen Seite beginnen.
Durch Setzen der Eigenschaft `is_in_new_page` können Sie Seitenlayout und Dokumentstruktur präzise steuern, sodass bestimmte Abschnitte wie Tabellen, Berichte oder Zusammenfassungen immer auf einer neuen Seite beginnen. Das ist ideal für Dokumentformatierung, druckfertige Berichte oder klar strukturierte Ausgaben.

1. Erstellen und konfigurieren Sie eine Tabelle.
1. Fügen Sie Daten zur Tabelle hinzu.
1. Erzwingen Sie eine neue Seite für die Tabelle. Dadurch beginnt die Tabelle am oberen Rand einer neuen Seite, auch wenn auf der aktuellen Seite bereits Inhalt vorhanden ist.
1. Fügen Sie die Tabelle der Seite hinzu. Verwenden Sie `page.paragraphs.add()`, um die Tabelle in das PDF-Layout einzubinden.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def force_new_page(output_file_name):
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()
    table.column_widths = "150 150 150"
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)

    # Add rows with sample data
    for i in range(5):
        row = table.rows.add()
        row.cells.add(f"Row {i + 1} - Col 1")
        row.cells.add(f"Row {i + 1} - Col 2")
        row.cells.add(f"Row {i + 1} - Col 3")

    # --- Key part: force table to start on a new PDF page ---
    table.is_in_new_page = True

    # Add table to page
    page.paragraphs.add(table)

    # Save the PDF
    document.save(output_file_name)
```

### Die Eigenschaft für Inline-Absätze in einem PDF verwenden

Unsere Bibliothek ermöglicht es Ihnen, die Eigenschaft `is_in_line_paragraph` zu verwenden, um den Inline-Fluss zwischen Text und Bildern innerhalb eines PDFs zu steuern.
Normalerweise beginnt jedes neue Element wie ein Textfragment oder Bild in einer neuen Zeile oder einem neuen Absatz.
Wenn Sie `is_in_line_paragraph = True` setzen, können Elemente in derselben Zeile oder im selben Absatz erscheinen. So lassen sich fließende Inline-Layouts erstellen, zum Beispiel für Logos, Symbole oder kleine Icons innerhalb eines Satzes.

Das erste Textfragment, das Bild und das zweite Textfragment erscheinen in derselben Zeile und bilden einen durchgehenden Inline-Absatz.
Das dritte Textfragment beginnt einen neuen Absatz und zeigt damit das Standardverhalten beim Zeilenumbruch.

1. Erstellen Sie ein neues PDF-Dokument.
1. Fügen Sie das erste Textfragment hinzu.
1. Fügen Sie ein Inline-Bild ein.
1. Ergänzen Sie weiteren Inline-Text.
1. Fügen Sie einen neuen Absatz hinzu.
1. Speichern Sie das PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def using_inline_paragraph_property(output_file_name):
    # Create a PDF document
    document = ap.Document()
    page = document.pages.add()

    # --- First text fragment (normal paragraph) ---
    fragment1 = ap.text.TextFragment("This is the first part of the paragraph. ")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment1.text_state.font_size = 14
    page.paragraphs.add(fragment1)

    # --- Inline image (continues same paragraph flow) ---
    image = ap.Image()
    image.is_in_line_paragraph = True  # Makes image inline with previous paragraph
    image.file = path.join(DATA_DIR, "logo.jpg")
    image.fix_height = 30
    image.fix_width = 30
    page.paragraphs.add(image)

    # --- Second inline text fragment (keeps same paragraph flow) ---
    fragment2 = ap.text.TextFragment("This is the second part of the same paragraph.")
    fragment2.is_in_line_paragraph = True
    fragment2.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment2.text_state.font_size = 14
    page.paragraphs.add(fragment2)

    # --- Third fragment (starts new paragraph automatically) ---
    fragment3 = ap.text.TextFragment("This is a new paragraph.")
    fragment3.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment3.text_state.font_size = 14
    page.paragraphs.add(fragment3)

    # Save PDF
    document.save(output_file_name)
```

### Ein mehrspaltiges PDF erstellen

Erstellen Sie ein mehrspaltiges, zeitungsähnliches Layout in einem PDF mit Aspose.PDF for Python via .NET.
Das Beispiel zeigt, wie Sie Text, HTML-Formatierung und Grafiken in einer `FloatingBox` kombinieren und damit eine erweiterte Layoutsteuerung ähnlich wie bei Magazinen oder Newslettern erreichen.

1. Initialisieren Sie das PDF-Dokument.
1. Fügen Sie oben eine horizontale Trennlinie hinzu.
1. Fügen Sie eine formatierte HTML-Überschrift hinzu.
1. Erstellen Sie die `FloatingBox` zur Layoutsteuerung.
1. Konfigurieren Sie das mehrspaltige Layout.
1. Fügen Sie Autoreninformationen hinzu.
1. Zeichnen Sie eine weitere horizontale Linie im Inneren.
1. Fügen Sie den Artikeltext hinzu.
1. Speichern Sie das fertige PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_multi_column_pdf(output_file_name):
    # Create PDF document
    document = ap.Document()

    # Set margins
    document.page_info.margin.left = 40
    document.page_info.margin.right = 40

    page = document.pages.add()

    #
    # Draw horizontal line at the top
    #
    graph1 = ap.drawing.Graph(500.0, 2.0)
    page.paragraphs.add(graph1)

    pos_arr = [1.0, 2.0, 500.0, 2.0]
    line1 = ap.drawing.Line(pos_arr)
    graph1.shapes.add(line1)

    #
    # Add HTML heading text
    #
    html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>"
    heading_text = ap.HtmlFragment(html)
    page.paragraphs.add(heading_text)

    #
    # Floating box: enables multi-column layout
    #
    box = ap.FloatingBox()

    box.column_info.column_count = 2  # Two columns
    box.column_info.column_spacing = "5"  # Space between columns
    box.column_info.column_widths = "105 105"  # Width of each column

    #
    # Add title text to the FloatingBox
    #
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)

    text1.text_state.font_size = 10
    text1.text_state.font_style = ap.text.FontStyles.ITALIC

    #
    # Add another horizontal line inside the box
    #
    graph2 = ap.drawing.Graph(50.0, 10.0)

    pos_arr2 = [1.0, 10.0, 100.0, 10.0]
    line2 = ap.drawing.Line(pos_arr2)
    graph2.shapes.add(line2)

    box.paragraphs.add(graph2)

    #
    # Add long text content
    #
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            lorem_text = f.read()
    else:
        lorem_text = "Lorem ipsum text not found."
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### Benutzerdefinierte Tabstopps für Textausrichtung im PDF

Erstellen Sie ein tabellenähnliches Textlayout in einem PDF mit benutzerdefinierten Tabstopps, ohne Tabellenstrukturen zu verwenden.
Durch die Definition von Positionen, Ausrichtungen und Füllzeichen für Tabstopps können Sie Text präzise über Spalten hinweg ausrichten. Das ist nützlich für Rechnungen, Berichte oder strukturierte Textdaten.

1. Erstellen Sie ein neues PDF-Dokument.
1. Definieren Sie benutzerdefinierte Tabstopps.
1. Verwenden Sie `#$TAB`-Platzhalter im Text.
1. Fügen Sie den Text dem PDF hinzu.
1. Speichern Sie das PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def custom_tab_stops(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Define tab stops
    tab_stops = ap.text.TabStops()

    tab_stop1 = tab_stops.add(100)
    tab_stop1.alignment_type = ap.text.TabAlignmentType.RIGHT
    tab_stop1.leader_type = ap.text.TabLeaderType.SOLID

    tab_stop2 = tab_stops.add(200)
    tab_stop2.alignment_type = ap.text.TabAlignmentType.CENTER
    tab_stop2.leader_type = ap.text.TabLeaderType.DASH

    tab_stop3 = tab_stops.add(300)
    tab_stop3.alignment_type = ap.text.TabAlignmentType.LEFT
    tab_stop3.leader_type = ap.text.TabLeaderType.DOT

    # Create TextFragments with tab placeholders
    header = ap.text.TextFragment(
        "This is an example of forming table with TAB stops", tab_stops
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tab_stops)
    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tab_stops)

    text2 = ap.text.TextFragment("#$TABdata21 ", tab_stops)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    # Add text fragments to page
    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    # Save PDF document
    document.save(output_file_name)
```

### Verwandte Textthemen

- [Mit Text in PDF mit Python arbeiten](/pdf/de/python-net/working-with-text/)
- [Text zu PDF hinzufügen](/pdf/de/python-net/add-text-to-pdf-file/)
- [Text in PDF mit Python drehen](/pdf/de/python-net/rotate-text-inside-pdf/)
- [Text in PDF mit Python ersetzen](/pdf/de/python-net/replace-text-in-pdf/)
