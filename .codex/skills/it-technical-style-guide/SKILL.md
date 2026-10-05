---
name: it-technical-style-guide
description: Use this skill when writing, translating, reviewing, or editing Italian programming documentation. It normalizes headings, step-by-step instructions, figure captions, terminology, API identifiers, UI labels, punctuation, and technical formatting to consistent technical Italian.
---

# Italian Technical Documentation Style

## Goal

Normalize Italian programming documentation to a clear, concise, consistent style suitable for developers.

Use standard contemporary Italian.

For procedural instructions, address the reader consistently using the **second-person plural imperative (`voi`)** as the default documentation convention.

## Priority

When rules conflict, apply them in this order:

1. Project-specific localization instructions.
2. Approved terminology glossary.
3. Product and API terminology.
4. This style guide.
5. General Italian writing conventions.

Never change API identifiers, commands, paths, filenames, macros, or actual UI labels merely to satisfy a linguistic rule.

---

## 1. Identify the structural role first

Before rewriting text, determine whether it is:

- a task heading;
- a conceptual heading;
- a procedural step;
- a figure caption;
- a note or warning;
- explanatory prose;
- a UI label;
- an API or code identifier.

Do not apply transformations mechanically without determining the text's structural role.

---

## 2. General writing style

Use concise, direct technical Italian.

Prefer active constructions and short sentences.

Good:

- Questo metodo salva il documento PDF.
- L'esempio seguente converte un file PDF in formato DOCX.
- La classe `Document` rappresenta un documento PDF.

Avoid unnecessary introductory expressions.

Avoid:

- È importante notare che...
- Si noti che...
- Come possiamo vedere...
- Occorre sottolineare che...

when the same information can be stated directly.

Prefer:

- Questo metodo richiede una password.

instead of:

- È importante notare che questo metodo richiede una password.

---

## 3. Headings

Use sentence-style capitalization.

Good:

- Convertire un PDF in DOCX
- Creare un documento PDF
- Estrarre il testo da un PDF
- Configurare le opzioni di conversione
- Opzioni di conversione

Bad:

- Convertire Un PDF In DOCX
- Creare Un Documento PDF
- Estrarre Il Testo Da Un PDF

Capitalize proper names, products, technologies, and identifiers according to their official spelling.

Do not normally put a period at the end of a heading.

Good:

- Creare un documento PDF

Bad:

- Creare un documento PDF.

---

## 4. Task headings

Use the infinitive for headings describing tasks or operations.

Good:

- Creare un documento PDF
- Aggiungere una pagina
- Convertire un PDF in DOCX
- Estrarre immagini
- Configurare le opzioni
- Salvare il documento

Avoid mixing grammatical structures among sibling headings.

Bad:

- Creazione di un documento
- Aggiungere una pagina
- Come configurare i font
- Salvataggio del documento

Prefer:

- Creare un documento
- Aggiungere una pagina
- Configurare i font
- Salvare il documento

---

## 5. Conceptual headings

Use concise noun phrases for conceptual and reference sections.

Good:

- Prerequisiti
- Opzioni di conversione
- Formati supportati
- Limitazioni note
- Gestione dei font
- Struttura del documento
- Riferimento API

Do not convert a conceptual heading to an infinitive merely because the section discusses an operation.

---

## 6. Step-by-step instructions

Use direct imperative instructions consistently.

Default to the **second-person plural**.

Good:

- Create un oggetto `Document`.
- Aprite il file PDF.
- Aggiungete una pagina al documento.
- Configurate le opzioni di conversione.
- Salvate il documento.

Avoid infinitives as ordinary procedural instructions.

Bad:

- Creare un oggetto `Document`.
- Aprire il file PDF.
- Aggiungere una pagina.
- Configurare le opzioni.
- Salvare il documento.

Avoid unnecessarily impersonal constructions.

Avoid:

- È necessario creare un oggetto `Document`.
- Si deve creare un oggetto `Document`.

Prefer:

- Create un oggetto `Document`.

If the project explicitly uses formal singular **Lei** instructions, preserve that convention consistently instead of mixing `Lei` and `voi`.

---

## 7. Common instruction normalization

Using the default `voi` convention:

| Infinitive | Instruction |
|---|---|
| accedere | Accedete |
| aggiungere | Aggiungete |
| aprire | Aprite |
| chiamare | Chiamate |
| configurare | Configurate |
| convertire | Convertite |
| copiare | Copiate |
| creare | Create |
| definire | Definite |
| eliminare | Eliminate |
| eseguire | Eseguite |
| esportare | Esportate |
| estrarre | Estraete |
| importare | Importate |
| installare | Installate |
| ottenere | Ottenete |
| salvare | Salvate |
| selezionare | Selezionate |
| specificare | Specificate |
| usare | Usate |
| verificare | Verificate |

Follow the approved glossary if another verb is established.

Do not alternate unnecessarily among:

- usare;
- utilizzare;
- impiegare.

For concise developer documentation, prefer **usare** unless project terminology specifies otherwise.

---

## 8. Numbered procedures

Use numbered lists when actions must be performed in sequence.

Good:

1. Create un oggetto `Document`.
2. Aggiungete una pagina al documento.
3. Create un oggetto `TextFragment`.
4. Aggiungete il testo alla pagina.
5. Salvate il documento PDF.

Each step should normally represent one primary action.

Avoid combining an entire procedure into one step.

Bad:

1. Create il documento, aggiungete una pagina, configurate il font, aggiungete il testo e salvate il file.

Split meaningful stages into separate steps.

Closely related operations may remain together when separating them would make the procedure unnecessarily fragmented.

---

## 9. Step punctuation

Write procedural steps as complete sentences.

Start each step with a capital letter and end it with appropriate punctuation.

Good:

1. Aprite il documento PDF.
2. Selezionate la pagina da elaborare.
3. Estraete il testo dalla pagina.

Bad:

1. aprire il documento
2. selezione della pagina
3. estrarre il testo

---

## 10. Context before action

When useful, establish where an action occurs.

Good:

- Nel menu **File**, selezionate **Salva con nome**.
- In `PdfSaveOptions`, impostate la proprietà `Compliance`.
- In Visual Studio, aprite **Gestione pacchetti NuGet**.

Use the exact UI terminology of the documented product.

---

## 11. Explanations are not steps

Do not turn explanatory information into numbered steps unless the reader must perform an action.

Preferred:

1. Create un oggetto `Document`.

   Questo oggetto rappresenta il documento PDF da elaborare.

The numbered sentence describes the action.

The following paragraph explains the object or result.

---

## 12. Figure captions

Use the following default pattern:

`Figura N. Descrizione`

Examples:

- Figura 1. Struttura del documento PDF
- Figura 2. Opzioni di conversione
- Figura 3. Risultato della conversione
- Figura 4. Configurazione del progetto

Use sentence-style capitalization.

Keep captions concise and descriptive.

Avoid:

- Figure 3: Conversion Result
- Figura 3. Risultato Della Conversione
- Figura 3. Screenshot
- Figura 3. Esempio

Describe what the figure communicates.

---

## 13. Figure references

In running text, use:

- Consultate la figura 2.
- La figura 3 mostra il risultato della conversione.
- La configurazione del progetto è illustrata nella figura 4.

Use lowercase `figura` in ordinary running text unless the publishing system specifies another convention.

---

## 14. API identifiers

Never translate:

- class names;
- method names;
- property names;
- namespaces;
- enum members;
- source-code variables;
- package names;
- command-line options;
- file extensions.

Good:

- Create un oggetto `Document`.
- Chiamate il metodo `save()`.
- Impostate la proprietà `page_info`.

Bad:

- Create un oggetto `Documento`.
- Chiamate il metodo `salva()`.

Use code formatting for identifiers.

---

## 15. Grammar around identifiers

Apply normal Italian grammar around technical identifiers.

Good:

- Create un'istanza di `Document`.
- Usate il metodo `save()`.
- Impostate la proprietà `Compliance`.
- Accedete alla raccolta `pages`.

Do not modify identifiers to make them conform to Italian morphology.

---

## 16. Files, paths, and commands

Format literal filenames, paths, commands, and extensions as code.

Good:

- Aprite `input.pdf`.
- Salvate il risultato come `output.pdf`.
- Eseguite `dotnet build`.
- Aprite la directory `C:\Samples\PDF`.

Do not translate literal values.

---

## 17. UI labels

Preserve the exact text displayed by the documented product.

If the Italian UI displays:

**Salva con nome**

write:

- Selezionate **Salva con nome**.

If the actual product displays:

**Save As**

write:

- Selezionate **Save As**.

Do not invent localized UI labels.

---

## 18. Technical terminology

Prefer established Italian technical terminology when a natural term exists.

Examples:

- file
- directory
- codice sorgente
- database
- configurazione
- interfaccia utente
- libreria
- metodo
- proprietà
- parametro
- applicazione

Do not force translations of terms that are conventionally used in English in Italian developer documentation.

Preserve technologies, formats, product names, and API terminology:

- .NET
- Python
- Java
- REST API
- JSON
- NuGet
- GitHub

Avoid unnecessary hybrid constructions.

Avoid:

- Fate il save del documento.

Prefer:

- Salvate il documento.

But preserve actual API identifiers:

- Chiamate il metodo `save()`.

---

## 19. Anglicisms

Italian programming documentation naturally contains established English technical terminology.

Do not translate a widely established technical term merely to eliminate English.

Examples that may remain unchanged depending on project terminology:

- file
- database
- framework
- runtime
- build
- package
- server
- client

However, avoid unnecessary English verbs embedded in Italian sentences.

Avoid:

- Fate il download del file, if the project prefers a standard Italian equivalent.

Prefer the project's approved terminology consistently.

Do not modify commands or UI labels.

---

## 20. Terminology consistency

Use one preferred term for one concept.

Do not randomly alternate between:

- directory / cartella;
- usare / utilizzare;
- eliminare / cancellare;
- selezionare / scegliere;
- applicazione / app.

Different terms are acceptable when they represent genuinely different concepts.

The approved project glossary takes precedence.

---

## 21. Notes and warnings

Use consistent labels.

Recommended:

- **Nota:** supplementary information.
- **Suggerimento:** optional advice.
- **Importante:** information necessary for successful completion.
- **Avviso:** potential risk, destructive operation, security issue, or data loss.

If the project uses **Attenzione** for warnings, preserve that convention consistently.

Do not alternate labels without a semantic reason.

---

## 22. Parallel structure

Keep sibling headings grammatically parallel.

Good:

- Creare un documento
- Aggiungere una pagina
- Configurare i font
- Salvare il documento

Bad:

- Creare un documento
- Aggiunta di una pagina
- Come configurare i font
- Salvataggio del documento

Keep procedural steps parallel:

- Create...
- Aggiungete...
- Configurate...
- Salvate...

---

## 23. Normalization examples

### Heading

Before:

`Creare Un Documento PDF.`

After:

`Creare un documento PDF`

### Instruction

Before:

`Creare un oggetto Document.`

After:

`Create un oggetto `Document`.`

### Impersonal instruction

Before:

`È necessario salvare il documento.`

After:

`Salvate il documento.`

### Figure

Before:

`Figure 2: Conversion Result`

After:

`Figura 2. Risultato della conversione`

### API identifier

Before:

`Chiamate il metodo salva().`

After:

`Chiamate il metodo `save()`.`

Only perform the last transformation when `save()` is the actual API identifier.

---

## 24. Review checklist

Before completing an Italian technical-documentation task, verify:

- [ ] Task headings use infinitives.
- [ ] Conceptual headings use appropriate noun phrases.
- [ ] Headings use sentence-style capitalization.
- [ ] Headings do not end with unnecessary periods.
- [ ] Procedural steps consistently use the project's chosen form, `voi` by default.
- [ ] `voi`, `Lei`, and impersonal constructions are not mixed arbitrarily.
- [ ] Steps are complete sentences.
- [ ] Numbered steps contain clear actions.
- [ ] Sibling headings and steps use parallel structures.
- [ ] Figure captions follow `Figura N. Descrizione`.
- [ ] Figure captions describe their content.
- [ ] API identifiers have not been translated.
- [ ] Commands, filenames, paths, and macros remain unchanged.
- [ ] UI labels match the actual product UI.
- [ ] Established technical terms are not over-translated.
- [ ] Technical terminology is consistent.
- [ ] The approved glossary takes precedence.

## Core rule

**Use infinitives for task headings, consistent direct imperatives for procedural instructions, and descriptive noun phrases for figure captions.**

Example:

Heading:

> Creare un documento PDF

Step:

> Create un oggetto `Document`.

Figure:

> Figura 1. Struttura del documento PDF